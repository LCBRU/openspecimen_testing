import logging
from re import L
from time import sleep
import jsonlines
from selenium.webdriver.common.by import By
from os_tester import OsTester


class QueryTester(OsTester):
    EXPORT_FILENAME = 'query_export.jsonl'
    DETAILS_FILENAME = 'query_details.jsonl'

    def goto_function_page(self):
        self.get('#/queries/list')

    def goto_query(self, dp):
        self.goto_function_page()
        self.get(dp['href'])
        sleep(15)
        self.get_element('span[translate="common.buttons.actions"]', By.CSS_SELECTOR)

    def get_export(self):
        logging.info('Exporting')

        self.goto_function_page()

        with jsonlines.open(self._output_directory / self.EXPORT_FILENAME, mode='w') as writer:
            for x in self.get_elements('a[ui-sref="query-results({queryId: query.id})"]', By.CSS_SELECTOR):
                details = {
                    'name': self.get_text(x),
                    'href': self.get_href(x),
                }
                writer.write(details)

    def visit_queries(self):
        logging.info('Visiting')

        with jsonlines.open(self._output_directory / self.DETAILS_FILENAME, mode='w') as writer:
            with jsonlines.open(self._output_directory / self.EXPORT_FILENAME) as reader:
                for i, f in enumerate(reader):
                    logging.info(f'Processing Query: {f["name"]}')

                    dets = self.visit_query(f)
                    writer.write(dets)

    def visit_query(self, x):
        details = {}

        self.goto_query(x)

        details['rows'] = self.get_query_result_details()

        return details

    def get_query_result_details(self):
        result = []

        headers = [self.get_innerHtml(h) for h in self.get_elements('div.ngHeaderContainer div.ngHeaderCell tooltip-append-to-bod', By.CSS_SELECTOR)]

        for row in self.get_elements('div.ngRow', By.CSS_SELECTOR):
            details = {}

            for i, cell in enumerate(row.find_elements(By.CSS_SELECTOR, 'div.ngCell a, div.ngCell span')):
                if cell.tag_name == 'a':
                    details[headers[i]] = {
                        'href': self.get_href(cell),
                        'value': self.get_innerHtml(cell),
                    }
                else:
                    details[headers[i]] = self.get_innerHtml(cell)

            result.append(details)

        return result

    def run(self):
        self.get_export()
        self.visit_queries()
