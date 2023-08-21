import logging
from time import sleep
from werkzeug.utils import secure_filename
from lbrc_selenium import ItemsFile
import csv
import jsonlines
from lbrc_selenium.selenium import CssSelector, SeleniumHelper, TagSelector, VersionTranslator, KeyValuePairScrubber, TableScrubber


class OpenSpecimenHelper(SeleniumHelper):
    def save_export(self, filename, in_more=False):
        sleep(1)
        if in_more:
            self.click_element(CssSelector('span[translate="common.buttons.more"]'))
            self.click_element(CssSelector('span[translate="cp.export"]'))
            self.click_element(CssSelector('span[translate="common.buttons.export"]'))
            self.click_element(CssSelector('span[translate="common.yes"]'))
        else:
            self.click_element(CssSelector('span[translate="common.buttons.export"]'))

        sleep(self.download_wait_time)

        self.unzip_download_directory_contents()

        with open(self._download_directory / 'output.csv') as csvfile:
            reader = csv.DictReader(csvfile)

            with jsonlines.open(self.output_directory / filename, mode='w') as writer:
                for row in reader:
                    writer.write(row)
        
        self.clear_download_directory()

    def get_href(self, item):
        href = super().get_href(item)
        if href.count('#') < 1:
            return href
        else:
            return href.split("#")[1]

    def get_overview_details(self, columns=None, version_comparator: VersionTranslator=None):
        if not version_comparator:
            version_comparator = VersionTranslator()

        VERSION_VALUE_SELECTOR = {
            '5.0': CssSelector('span, a'),
            '10.0': CssSelector('span.value, a.value'),
        }
        details = {}

        for kvpair in self.get_elements(CssSelector('ul.os-key-values li')):
            title = self.get_element(TagSelector('strong'), element=kvpair)

            values = self.get_elements(self.get_version_item(VERSION_VALUE_SELECTOR), element=kvpair)
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

        return version_comparator.translate_dictionary(self.compare_version, details)


    def get_div_table_details(self, parent_element_css_selector='', columns=None, version_comparator: VersionTranslator=None):
        VERSION_HEADERS = {
            '5.0': CssSelector(f'{parent_element_css_selector} div.os-table-head div.col span, div.os-table-head div.col'),
            '10.0': CssSelector(f'{parent_element_css_selector} table.os-table thead tr th'),
        }
        VERSION_ROWS = {
            '5.0': CssSelector(f'{parent_element_css_selector} div.os-table-body div.row'),
            '10.0': CssSelector(f'{parent_element_css_selector} table.os-table tbody tr'),
        }
        VERSION_CELLS = {
            '5.0': CssSelector('div.col'),
            '10.0': CssSelector('td'),
        }

        if not version_comparator:
            version_comparator = VersionTranslator()

        result = []

        headers = [self.get_text(h) for h in self.get_elements(self.get_version_item(VERSION_HEADERS))]

        for row in self.get_elements(self.get_version_item(VERSION_ROWS)):
            details = {}

            for i, cell in enumerate(self.get_elements(self.get_version_item(VERSION_CELLS))):
                values = sorted(self.get_elements(CssSelector('span, a'), element=cell), key=lambda x: x.tag_name)

                if len(values) > 0:
                    value = values[0]
                else:
                    value = cell
                
                if i < len(headers):
                    header = headers[i]
                else:
                    header = str(i)

                if columns is None or header in columns:
                    if value.tag_name == 'a':
                        details[header] = {
                            'href': self.get_href(value),
                            'value': self.get_text(value),
                        }
                    else:
                        details[header] = self.get_text(value)

            result.append(version_comparator.translate_dictionary(self.compare_version, details))

        return result

    def get_list_group_details(self, parent_element_css_selector='', columns=None, version_comparator: VersionTranslator=None):
        if not version_comparator:
            version_comparator = VersionTranslator()

        result = []

        header = [self.get_text(h) for h in self.get_elements(CssSelector(f'{parent_element_css_selector} div.list-group .os-section-hdr'))][0]

        for cell in self.get_elements(CssSelector(f'{parent_element_css_selector} div.list-group .os-cpe-item .list-group-item')):
            details = {}

            values = sorted(self.get_elements(CssSelector('span, a'), element=cell), key=lambda x: x.tag_name)

            if len(values) > 0:
                value = values[0]
            else:
                value = cell
            
            if columns is None or header in columns:
                if value.tag_name == 'a':
                    details[header] = {
                        'href': self.get_href(value),
                        'value': self.get_text(value),
                    }
                else:
                    details[header] = self.get_text(value)

            result.append(version_comparator.translate_dictionary(self.compare_version, details))

        return result

    def get_table_details(self, columns=None, has_container=True, version_comparator: VersionTranslator=None):
        if not version_comparator:
            version_comparator = VersionTranslator()

        result = []

        headers = [self.get_text(h) for h in self.get_elements(CssSelector('table.os-table thead .col span:first-of-type'))]

        if not columns:
            columns = headers

        container = '.container' if has_container else ''

        for row in self.get_elements(CssSelector(f'{container} table.os-table tbody tr')):
            details = {}

            for i, cell in enumerate(self.get_elements(CssSelector('td'), element=row)):
                values = sorted(self.get_elements(CssSelector('span, a'), element=cell), key=lambda x: x.tag_name)

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
                result.append(version_comparator.translate_dictionary(self.compare_version, details))

        return result

    def get_form_details(self, version_comparator: VersionTranslator=None):
        if not version_comparator:
            version_comparator = VersionTranslator()

        result = []

        for row in self.get_elements(CssSelector(f'form div.form-group')):
            details = {}

            label = self.get_element(CssSelector('label'), element=row, allow_null=True)

            values = [self.get_value(c) for c in self.get_elements(CssSelector('input, textarea'), element=row)]

            if label and values:
                details[self.get_text(label)] = values

                result.append(details)

        return version_comparator.translate_dictionary(self.compare_version, details)


class OpenSpecimenTester():
    def __init__(self, helper, selectors=None, outputs=None, sample_all=False):
        self.helper = helper
        self.selectors = selectors
        self.outputs = outputs
        self.sample_all = sample_all

    def object_name(self):
        if self.selectors:
            return self.selectors.object_name()
        else:
            raise NotImplementedError()

    def function_page_url(self):
        if self.selectors:
            return self.selectors.function_page_url()
        else:
            raise NotImplementedError()

    def item_page_loaded_css_selector(self):
        if self.selectors:
            return self.selectors.item_page_loaded_css_selector()
        else:
            raise NotImplementedError()

    def url_prefixes(self):
        return {
            '5.0': '#',
            '10.0': 'ui-app/#',
        }

    def translate_url(self, url):
        prefix = self.helper.get_version_item(self.url_prefixes())
        if url.startswith('/'):
            return f'{prefix}{url}'
        else:
            return f'{prefix}/{url}'
    
    def goto_function_page(self):
        self.helper.get(self.translate_url(self.function_page_url()))
        sleep(self.helper.page_wait_time)

    def goto_item_page(self, o):
        self.goto_function_page()
        href = self.translate_url(o['href'])
        print(href)
        self.helper.get(href)
        sleep(self.helper.page_wait_time)
        sleep(self.helper.page_wait_time)
        self.helper.get_element(self.item_page_loaded_css_selector())

    def goto_item_sub_page(self, o, page_name, selector, original='overview'):
        self.goto_function_page()
        href = self.translate_url(o['href'].replace(original, page_name))
        print(href)
        self.helper.get(href)
        sleep(self.helper.page_wait_time)
        sleep(self.helper.page_wait_time)
        sleep(self.helper.page_wait_time)
        sleep(self.helper.page_wait_time)
        sleep(self.helper.page_wait_time)
        sleep(self.helper.page_wait_time)
        sleep(self.helper.page_wait_time)
        sleep(self.helper.page_wait_time)
        self.helper.get_element(selector)
        
    def goto_item_custom_page(self, url, loaded_css_selector):
        self.goto_function_page()
        url = self.translate_url(url)
        self.helper.get(url)
        sleep(self.helper.page_wait_time)
        self.helper.get_element(loaded_css_selector)
        

class OpenSpecimenNonDestructiveTester(OpenSpecimenTester):
    def export_link_css_selector(self):
        raise NotImplementedError()

    def export_link_name_selector(self):
        return None

    def _export_filename(self):
        return secure_filename(f'{self.object_name()}_export.jsonl')

    def _details_filename(self):
        return secure_filename(f'{self.object_name()}_details.jsonl')

    def get_export(self):
        logging.info('Exporting')

        export_file = ItemsFile(self.helper.output_directory, self._export_filename())

        if not export_file.exists():
            print(f'Export not found {self._export_filename()} - processing')

            self.goto_function_page()
            sleep(self.helper.page_wait_time)

            for x in self.helper.get_elements(self.export_link_css_selector()):
                href = self.helper.get_href(x)

                export_file.add_item(dict(
                    name=self.helper.get_text(x),
                    href=href,
                ))

            export_file.save()
        else:
            print(f'Export found {self._export_filename()} - skipping')


    def visit_items(self):
        logging.info(f'Visiting All {self.object_name()}s')

        export_file = ItemsFile(self.helper.output_directory, self._export_filename())
        details_file = ItemsFile(self.helper.output_directory, self._details_filename(), sorted=False)

        if not details_file.exists():
            print(f'Details not found {self._export_filename()} - processing')

            for o in export_file.get_sample_items():
                logging.info(f'Processing Item: {o["name"]}')

                details_file.add_item(self.visit_item(o))

            details_file.save()
        else:
            print(f'Details found {self._export_filename()} - skipping')

    def visit_item(self, o, version_comparator: VersionTranslator=None):
        details = {}

        self.goto_item_page(o)

        details['overview'] = OSOverviewScrubber(helper=self.helper, version_comparator=version_comparator).get_details()

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


class OSOverviewScrubber(KeyValuePairScrubber):
    def __init__(self, helper: SeleniumHelper, version_comparator: VersionTranslator = None) -> None:
        VERSION_VALUE_SELECTOR = {
            '5.0': CssSelector('span, a'),
            '10.0': CssSelector('span.value, a.value'),
        }
        super().__init__(
            helper,
            parent_selector=CssSelector('ul.os-key-values'),
            value_selector=helper.get_version_item(VERSION_VALUE_SELECTOR),
            version_comparator=version_comparator)


def get_versioned_table_scrubber(helper: SeleniumHelper, version_comparator: VersionTranslator = None) -> TableScrubber:
    VERSION_SCRUBBER = {
        '5.0': OSTableScrubberOld(helper=helper, version_comparator=version_comparator),
        '10.0': OSTableScrubberNew(helper=helper, version_comparator=version_comparator),
    }
    return helper.get_version_item(VERSION_SCRUBBER)


class OSTableScrubberNew(TableScrubber):
    def __init__(self, helper: SeleniumHelper, version_comparator: VersionTranslator = None) -> None:
        super().__init__(
            helper,
            parent_selector=CssSelector('table.os-table'),
            header_selector=CssSelector('thead tr th'),
            row_selector=CssSelector('tbody tr'),
            cell_selector=CssSelector('td'),
            version_comparator=version_comparator)


class OSTableScrubberOld(TableScrubber):
    def __init__(self, helper: SeleniumHelper, version_comparator: VersionTranslator = None) -> None:
        super().__init__(
            helper,
            parent_selector=CssSelector('div.os-table'),
            header_selector=CssSelector('div.os-table-head div.col span, div.os-table-head div.col'),
            row_selector=CssSelector('div.os-table-body div.row'),
            cell_selector=CssSelector('div.col'),
            version_comparator=version_comparator)


class PDataTableScrubberNew(TableScrubber):
    def __init__(self, helper: SeleniumHelper, version_comparator: VersionTranslator = None) -> None:
        super().__init__(
            helper,
            parent_selector=CssSelector('table.p-datatable-table'),
            header_selector=CssSelector('thead tr th'),
            row_selector=CssSelector('tbody tr'),
            cell_selector=CssSelector('td > span:last-of-type'),
            version_comparator=version_comparator)
