import jsonlines
import csv
from time import sleep
from tester import TesterBase
from selenium.webdriver.common.by import By
from sympy import tribonacci, fibonacci


class OsTester(TesterBase):
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

            with jsonlines.open(self._output_directory / filename, mode='w') as writer:
                for row in reader:
                    writer.write(row)
        
        self.clear_download_directory()

    def get_overview_details(self):
        details = {}

        for kvpair in self.driver.find_elements_by_css_selector('ul.os-key-values li'):
            title = kvpair.find_element_by_tag_name('strong')
            value = kvpair.find_element_by_tag_name('span')

            details[self.get_innerHtml(title)] = self.get_innerHtml(value)

        return details

    def get_div_table_details(self):
        result = []

        headers = [self.get_innerHtml(h) for h in self.get_elements('div.os-table-head div.col span', By.CSS_SELECTOR)]

        for row in self.get_elements('div[ng-repeat]', By.CSS_SELECTOR):
            details = {}

            for i, cell in enumerate(row.find_elements(By.CSS_SELECTOR, 'div')):
                if i == 0:
                    link = cell.find_element(By.CSS_SELECTOR, 'a')

                    details['href'] = self.get_href(link)
                    details[headers[i]] = self.get_innerHtml(link)
                else:
                    details[headers[i]] = self.get_innerHtml(cell)

            result.append(details)

        return result

    def get_table_details(self):
        result = []

        headers = [self.get_innerHtml(h) for h in self.get_elements('table.os-table thead th span', By.CSS_SELECTOR)]

        for row in self.get_elements('table.os-table tbody tr', By.CSS_SELECTOR):
            details = {}

            for i, cell in enumerate(row.find_elements(By.CSS_SELECTOR, 'td')):
                details[headers[i]] = self.get_innerHtml(cell)

            result.append(details)

        return result

