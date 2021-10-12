from open_specimen_tester import OpenSpecimenDestructiveTester
from selenium_test_helper import ClickAction, CssSelector, EnsureAction, SelectAction, TypeInTextboxAction, XpathSelector


def get_user_tester(helper):
    return UserTester_v5_0(helper)


class UserTester_v5_0(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return 'users'

    def create_button_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def create_page_loaded_selector(self):
        return CssSelector('span[translate="common.buttons.discard"]')

    def create_page_create_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def item_title_selector(self):
        return XpathSelector('//span[normalize-space(text())="Fred Flintoff"]')

    def create_item(self):
        self.goto_function_page()

        self.helper.click_element_selector(self.create_button_selector())
        self.helper.get_element_selector(self.create_page_loaded_selector())

        self.helper.type_in_textbox_selector(CssSelector('input[name="lastName"]'), 'Flintoff')
        self.helper.type_in_textbox_selector(CssSelector('input[name="firstName"]'), 'Fred')
        self.helper.type_in_textbox_selector(CssSelector('input[name="email"]'), 'fred@ecb.co.uk')
        self.helper.type_in_textbox_selector(CssSelector('input[name="loginName"]'), 'fred.flintoff')

        self.helper.click_element_selector(CssSelector('div[placeholder="Institute"]'))
        self.helper.click_element_selector(XpathSelector('//span[text()="University of Leicester"]'))

        self.helper.click_element_selector(self.create_page_create_selector())
        self.helper.get_element_selector(CssSelector('span[translate="common.buttons.delete"]'))


    def validate_item(self):
        self.goto_function_page()

        self.helper.get_element_selector(self.item_title_selector())


    def cleanup_item(self):
        self.goto_function_page()

        self.helper.click_element_selector(self.item_title_selector())
        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.delete"]'))
        self.helper.click_element_selector(CssSelector('span[translate="common.yes"]'))
