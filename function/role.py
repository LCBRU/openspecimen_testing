from selenium_test_helper import CssSelector, XpathSelector


class RoleFunction:
    def object_name(self):
        return 'role'

    def function_page_url(self):
        return 'roles'

    def create_button_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def create_page_loaded_selector(self):
        return CssSelector('button[translate="common.buttons.discard"]')
