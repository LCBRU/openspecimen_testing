from selenium.webdriver.common.by import By
from function.query import selectors, outputs
from open_specimen_tester import OpenSpecimenDestructiveTester
from selenium_test_helper import ClickAction, EnsureAction


class QueryTester(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper, selectors(helper.version), outputs(helper.compare_version))

    def create_item(self):
        # Queries seem hard to emulate, so for now I'll just check that
        # the page loads.

        self.goto_function_page()

        ClickAction(helper=self.helper, selector=self.selectors.create_button_selector()).do()
        EnsureAction(helper=self.helper, selector=self.selectors.create_page_loaded_selector()).do()


    def validate_item(self):
        pass


    def cleanup_item(self):
        pass
