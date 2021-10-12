from open_specimen_tester import OpenSpecimenDestructiveTester
from selenium_test_helper import CssSelector


def get_query_tester(helper):
    return QueryTester_v5_0(helper)


class QueryTester_v5_0(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return 'queries/list'

    def create_button_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def create_page_loaded_selector(self):
        return CssSelector('span[translate="common.buttons.save"]')

    def create_item(self):
        # Queries seem hard to emulate, so for now I'll just check that
        # the page loads.

        self.goto_function_page()

        self.helper.click_element_selector(self.create_button_selector())
        self.helper.get_element_selector(self.create_page_loaded_selector())

    def validate_item(self):
        pass

    def cleanup_item(self):
        pass
