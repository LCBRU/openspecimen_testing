from selenium_test_helper import CssSelector, XpathSelector
from open_specimen_tester import OpenSpecimenDestructiveTester


def get_institute_tester(helper):
    return InstituteTester_v5_0(helper)


class InstituteTester_v5_0(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return 'institutes'

    def create_button_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def create_page_loaded_selector(self):
        return CssSelector('span[translate="institute.create_institute"]')

    def create_page_create_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def item_title_selector(self):
        return XpathSelector('//span[normalize-space(text())="Royal Institution"]')

    def create_item(self):
        self.goto_function_page()

        self.helper.click_element_selector(self.create_button_selector())
        self.helper.get_element_selector(self.create_page_loaded_selector())

        self.helper.type_in_textbox_selector(CssSelector('input[ng-model="institute.name"]'), 'Royal Institution')

        self.helper.click_element_selector(self.create_page_create_selector())
        self.helper.get_element_selector(XpathSelector('//h3[normalize-space(text())="Royal Institution"]'))

    def validate_item(self):
        self.goto_function_page()

        self.helper.get_element_selector(self.item_title_selector())

    def cleanup_item(self):
        self.goto_function_page()

        self.helper.click_element_selector(self.item_title_selector())
        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.more"]'))
        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.delete"]'))
        self.helper.click_element_selector(CssSelector('span[translate="common.yes"]'))
