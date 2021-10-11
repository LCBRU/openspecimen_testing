from selenium.webdriver.common.by import By
from function.query import QueryFunction
from open_specimen_tester import OpenSpecimenDestructiveTester
from selenium_test_helper import ClickAction, CssSelector, EnsureAction


class QueryTester(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper, QueryFunction())

    def create_item(self):
        # Queries seem hard to emulate, so for now I'll just check that
        # the page loads.

        self.goto_function_page()

        ClickAction(helper=self.helper, selector=self.function.create_button_selector()).do()
        EnsureAction(helper=self.helper, selector=self.function.create_page_loaded_selector()).do()


    def validate_item(self):
        pass


    def cleanup_item(self):
        pass
