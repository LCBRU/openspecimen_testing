from open_specimen_tester import OpenSpecimenDestructiveTester
from selenium_test_helper import ClickAction, CssSelector, EnsureAction, SelectAction, TypeInTextboxAction, XpathSelector


def get_role_tester(helper):
    if helper.version == '6.0':
        return RoleTester_v6_0(helper)
    else:
        return RoleTester_v5_0(helper)


class RoleTester_v5_0(OpenSpecimenDestructiveTester):
    def resource_value_selector(self):
        return XpathSelector('//span[text()="Orders"]')

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
        self.helper.click_element_selector(self.resource_value_selector())

        self.helper.click_element_selector(CssSelector('button[translate="common.buttons.discard"]'))

    def validate_item(self):
        pass

    def cleanup_item(self):
        pass


class RoleTester_v6_0(RoleTester_v5_0):
    def resource_value_selector(self):
        return XpathSelector('//span[@class="ng-binding ng-scope" and text()="Orders"]')

