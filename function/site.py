
from selenium_test_helper import CssSelector, XpathSelector


class SiteFunction:
    def object_name(self):
        return 'site'

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
