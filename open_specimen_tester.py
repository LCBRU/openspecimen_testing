import logging
import jsonlines
import csv
import collections
from time import sleep
from selenium_test_helper import SeleniumTestHelper
from selenium.webdriver.common.by import By


class OpenSpecimenSeleniumTestHelper(SeleniumTestHelper):
    def login(self):
        self.get('')
        self.type_in_textbox('//input[@ng-model="loginData.loginName"]', By.XPATH, self._username)
        self.type_in_textbox('//input[@ng-model="loginData.password"]', By.XPATH, self._password)
        self.click_element('span[translate="user.sign_in"]', By.CSS_SELECTOR)

    def save_export(self, filename, in_more=False):
        sleep(1)
        if in_more:
            self.click_element('span[translate="common.buttons.more"]', By.CSS_SELECTOR)
            self.click_element('span[translate="cp.export"]', By.CSS_SELECTOR)
            self.click_element('span[translate="common.buttons.export"]', By.CSS_SELECTOR)
            self.click_element('span[translate="common.yes"]', By.CSS_SELECTOR)
        else:
            self.click_element('span[translate="common.buttons.export"]', By.CSS_SELECTOR)

        sleep(self.download_wait_time)

        self.unzip_download_directory_contents()

        with open(self._download_directory / 'output.csv') as csvfile:
            reader = csv.DictReader(csvfile)

            with jsonlines.open(self.output_directory / filename, mode='w') as writer:
                for row in reader:
                    writer.write(row)
        
        self.clear_download_directory()

    def get_overview_details(self, columns=None):
        details = {}

        for kvpair in self.driver.find_elements_by_css_selector('ul.os-key-values li'):
            title = kvpair.find_element_by_tag_name('strong')

            values = kvpair.find_elements(By.CSS_SELECTOR, 'span, a')
            value = [x for x in sorted(values, key=lambda x: x.tag_name)][0]

            header = self.get_text(title)

            if columns is None or header in columns:
                if value.tag_name == 'a':
                    details[header] = {
                        'href': self.get_href(value),
                        'value': self.get_text(value),
                    }
                else:
                    details[header] = self.get_text(value)

        return details

    def get_div_table_details(self, parent_element_css_selector=''):
        result = []

        headers = [self.get_text(h) for h in self.get_elements(f'{parent_element_css_selector} div.os-table-head div.col span, div.os-table-head div.col', By.CSS_SELECTOR)]

        for row in self.get_elements(f'{parent_element_css_selector} div.row', By.CSS_SELECTOR):
            details = {}

            for i, cell in enumerate(row.find_elements(By.CSS_SELECTOR, 'div.col a, div.col')):
                if i < len(headers):
                    header = headers[i]
                else:
                    header = str(i)

                if cell.tag_name == 'a':
                    details[header] = {
                        'href': self.get_href(cell),
                        'value': self.get_text(cell),
                    }
                else:
                    details[header] = self.get_text(cell)

            result.append(details)

        return result

    def get_table_details(self, columns=None):
        result = []

        headers = [self.get_text(h) for h in self.get_elements('table.os-table thead .col span:first-of-type', By.CSS_SELECTOR)]

        if not columns:
            columns = headers

        for row in self.get_elements('.container table.os-table tbody tr', By.CSS_SELECTOR):
            details = {}

            for i, cell in enumerate(row.find_elements(By.CSS_SELECTOR, 'td')):
                values = sorted(cell.find_elements(By.CSS_SELECTOR, 'span, a'), key=lambda x: x.tag_name)

                if len(values) > 0:
                    value = values[0]
                else:
                    value = cell
                
                if i < len(headers):
                    header = headers[i]
                else:
                    header = str(i)

                if header in columns:
                    if value.tag_name == 'a':
                        details[header] = {
                            'href': self.get_href(value),
                            'value': self.get_text(value),
                        }
                    else:
                        val = self.get_text(value)
                        if header or val:
                            details[header] = val

            if len(details) > 0:
                result.append(collections.OrderedDict(sorted(details.items())))

        return result


class OpenSpecimenTester():
    def __init__(self, helper):
        self.helper = helper

    def object_name(self):
        raise NotImplementedError()

    def function_page_url(self):
        raise NotImplementedError()

    def item_page_loaded_css_selector(self):
        raise NotImplementedError()

    def goto_function_page(self):
        self.helper.get(f'#/{self.function_page_url()}')
        sleep(self.helper.page_wait_time)

    def goto_item_page(self, o):
        self.goto_function_page()
        self.helper.get(o['href'])
        self.helper.get_element(self.item_page_loaded_css_selector(), By.CSS_SELECTOR)
        sleep(self.helper.page_wait_time)

    def goto_item_sub_page(self, o, page_name, loaded_css_selector, original='overview'):
        self.goto_function_page()
        self.helper.get(o['href'].replace(original, page_name))
        self.helper.get_element(loaded_css_selector, By.CSS_SELECTOR)
        sleep(self.helper.page_wait_time)
        
    def goto_item_custom_page(self, url, loaded_css_selector):
        self.goto_function_page()
        self.helper.get(url)
        self.helper.get_element(loaded_css_selector, By.CSS_SELECTOR)
        sleep(self.helper.page_wait_time)
        

class OpenSpecimenNonDestructiveTester(OpenSpecimenTester):
    def export_link_css_selector(self):
        raise NotImplementedError()

    def _export_filename(self):
        return f'{self.object_name()}_export.jsonl'

    def _details_filename(self):
        return f'{self.object_name()}_details.jsonl'

    def get_export(self):
        logging.info('Exporting')

        self.goto_function_page()
        sleep(self.helper.page_wait_time)

        existing = []

        with jsonlines.open(self.helper.output_directory / self._export_filename(), mode='w') as writer:
            for x in self.helper.get_elements(self.export_link_css_selector(), By.CSS_SELECTOR):
                href = self.helper.get_href(x)

                if href.count("#") > 1:
                    href = "#".join(href.split("#", 2)[:2])

                details = {
                    'name': self.helper.get_text(x),
                    'href': href,
                }
                if details not in existing:
                    existing.append(details)

            for i in sorted(existing, key=lambda i: i['name']):
                writer.write(i)

    def visit_items(self):
        logging.info(f'Visiting All {self.object_name()}s')

        with jsonlines.open(self.helper.output_directory / self._details_filename(), mode='w') as writer:
            with jsonlines.open(self.helper.output_directory / self._export_filename()) as reader:
                for i, o in enumerate(reader):
                    if self.helper.is_sampling_pick(i):
                        logging.info(f'Processing Item: {o["name"]}')

                        dets = self.visit_item(o)
                        writer.write(dets)
                    else:
                        logging.info(f'Skipping Item: {o["name"]}')

    def visit_item(self, o):
        details = {}

        self.goto_item_page(o)

        details['overview'] = self.helper.get_overview_details()

        return details

    def run(self):
        sleep(self.helper.page_wait_time)
        self.get_export()
        self.visit_items()


class OpenSpecimenDestructiveTester(OpenSpecimenTester):

    def create_item(self):
        raise NotImplementedError()

    def validate_item(self):
        raise NotImplementedError()

    def cleanup_item(self):
        raise NotImplementedError()

    def run(self):
        self.create_item()
        self.validate_item()
        self.cleanup_item()
