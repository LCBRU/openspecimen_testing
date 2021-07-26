from open_specimen_tester import OpenSpecimenTester
from selenium.webdriver.common.by import By
from time import sleep

class QueryTester(OpenSpecimenTester):
    def object_name(self):
        return 'query'

    def function_page_url(self):
        return 'queries/list'

    def export_link_css_selector(self):
        return 'a[ui-sref="query-results({queryId: query.id})"]'

    def item_page_loaded_css_selector(self):
        return 'span[translate="common.buttons.actions"]'

    def visit_item(self, x):
        details = {}

        details['name'] = x['name']

        self.goto_item_page(x)

        sleep(30)

        details['rows'] = self.get_query_result_details()

        return details

    def get_query_result_details(self):
        result = []

        headers = [self.helper.get_text(h) for h in self.helper.get_elements('div.ngHeaderContainer div.ngHeaderCell tooltip-append-to-bod', By.CSS_SELECTOR)]

        for row in self.helper.get_elements('div.ngRow', By.CSS_SELECTOR):
            details = {}

            for i, cell in enumerate(row.find_elements(By.CSS_SELECTOR, 'div.ngCell a, div.ngCell span')):
                if cell.tag_name == 'a':
                    details[headers[i]] = {
                        'href': self.helper.get_href(cell),
                        'value': self.helper.get_text(cell),
                    }
                else:
                    details[headers[i]] = self.helper.get_text(cell)

            result.append(details)

        return result
