from selenium_test_helper import ClickAction, CssSelector, EnsureAction, SelectAction, TypeInTextboxAction, XpathSelector
from open_specimen_tester import OpenSpecimenDestructiveTester


def get_order_tester(helper):
    return OrderTester_v5_0(helper)


class OrderTester_v5_0(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return 'orders'

    def create_button_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def create_page_loaded_selector(self):
        return CssSelector('span[translate="common.buttons.cancel"]')

    def create_item(self):
        # It seems impossible to create an order and then
        # delete it, so I'm just going to check the first page and
        # not actually create it.
        
        self.goto_function_page()

        self.helper.click_element_selector(self.create_button_selector())
        self.helper.get_element_selector(self.create_page_loaded_selector())

        self.helper.click_element_selector(CssSelector('div[placeholder="Distribution Protocol"]'))
        self.helper.click_element_selector(XpathSelector('//span[text()="BRAVE DNA"]'))

        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.cancel"]'))

    def validate_item(self):
        pass

    def cleanup_item(self):
        pass
