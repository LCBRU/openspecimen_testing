from lbrc_selenium.selenium import CssSelector
from open_specimen_tester import OpenSpecimenNonDestructiveTester
from time import sleep

class QueryTester(OpenSpecimenNonDestructiveTester):
    def object_name(self):
        return 'query'

    def function_page_url(self):
        return 'queries/list'

    def export_link_css_selector(self):
        return CssSelector('a[ui-sref="query-results({queryId: query.id})"]')

    def item_page_loaded_css_selector(self):
        return CssSelector('span[translate="common.buttons.actions"]')

    def visit_item(self, x):
        details = {}

        details['name'] = x['name']

        self.goto_item_page(x)

        sleep(30)

        details['rows'] = self.get_query_result_details()

        return details

    def get_query_result_details(self):
        result = []

        headers = [self.helper.get_text(h) for h in self.helper.get_elements(CssSelector('div.ngHeaderContainer div.ngHeaderCell tooltip-append-to-bod'))]

        for row in self.helper.get_elements(CssSelector('div.ngRow')):
            details = {}

            for i, cell in enumerate(self.helper.get_elements(CssSelector('div.ngCell a, div.ngCell span'), element=row)):
                if cell.tag_name == 'a':
                    details[headers[i]] = {
                        'href': self.helper.get_href(cell),
                        'value': self.helper.get_text(cell),
                    }
                else:
                    details[headers[i]] = self.helper.get_text(cell)

            result.append(details)

        return sorted(result, key=lambda r: r.__repr__())
