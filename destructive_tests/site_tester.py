from open_specimen_tester import OpenSpecimenDestructiveTester
from selenium_test_helper import ClickAction, CssSelector, EnsureAction, SelectAction, TypeInTextboxAction, XpathSelector


def get_site_tester(helper):
    return SiteTester_v5_0(helper)


class SiteTester_v5_0(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return 'sites'

    def create_button_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def create_page_loaded_selector(self):
        return CssSelector('button[translate="common.buttons.discard"]')

    def create_page_create_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def item_title_selector(self):
        return XpathSelector('//span[normalize-space(text())="Fred"]')

    def create_item(self):
        self.goto_function_page()

        self.helper.click_element_selector(self.create_button_selector())
        self.helper.get_element_selector(self.create_page_loaded_selector())

        self.helper.click_element_selector(CssSelector('div[placeholder="Institute"]'))
        self.helper.click_element_selector(XpathSelector('//span[text()="University of Leicester"]'))

        self.helper.type_in_textbox_selector(CssSelector('input[name="siteName"]'), 'Fred')

        self.helper.click_element_selector(CssSelector('div[placeholder="Type"]'))
        self.helper.click_element_selector(XpathSelector('//span[text()="Collection Site"]'))

        self.helper.click_element_selector(self.create_page_create_selector())
        self.helper.get_element_selector(XpathSelector('//h3[normalize-space(text())="Fred"]'))

    def validate_item(self):
        self.goto_function_page()

        self.helper.get_element_selector(self.item_title_selector())


    def cleanup_item(self):
        self.goto_function_page()

        self.helper.click_element_selector(self.item_title_selector())
        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.delete"]'))
        self.helper.click_element_selector(CssSelector('span[translate="common.yes"]'))
