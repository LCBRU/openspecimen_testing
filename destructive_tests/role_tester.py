from open_specimen_tester import OpenSpecimenDestructiveTester
from selenium_test_helper import ClickAction, CssSelector, EnsureAction, SelectAction, TypeInTextboxAction, XpathSelector


def get_role_tester(helper):
    return RoleTester_v5_0(helper)


class RoleTester_v5_0(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return 'roles'

    def create_button_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def create_page_loaded_selector(self):
        return CssSelector('button[translate="common.buttons.discard"]')

    def create_item(self):
        # No option to delete, so never save.

        self.goto_function_page()

        self.helper.click_element_selector(self.create_button_selector())
        self.helper.get_element_selector(self.create_page_loaded_selector())

        self.helper.type_in_textbox_selector(CssSelector('input[ng-model="role.name"]'), 'Fred')

        self.helper.click_element_selector(CssSelector('div[placeholder="Resource"]'))
        self.helper.click_element_selector(XpathSelector('//span[text()="Orders"]'))

        self.helper.click_element_selector(CssSelector('button[translate="common.buttons.discard"]'))

    def validate_item(self):
        pass

    def cleanup_item(self):
        pass
