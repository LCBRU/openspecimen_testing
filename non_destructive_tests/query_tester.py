from lbrc_selenium.selenium import CssSelector, TableScrubber, SeleniumHelper
from open_specimen_tester import OpenSpecimenNonDestructiveTester
from time import sleep


class QueryResultsTableScrubber(TableScrubber):
    def __init__(self, helper: SeleniumHelper) -> None:
        super().__init__(
            helper,
            parent_selector=CssSelector('div.os-query-results-grid'),
            header_selector=CssSelector('div.ngHeaderContainer div.ngHeaderCell tooltip-append-to-bod'),
            row_selector=CssSelector('div.ngRow'),
            cell_selector=CssSelector('div.ngCell a, div.ngCell span'))


class QueryTester(OpenSpecimenNonDestructiveTester):
    def url_prefixes(self):
        return {
            '5.0': '#',
        }

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

        details['rows'] = QueryResultsTableScrubber(helper=self.helper).get_details()

        return details
