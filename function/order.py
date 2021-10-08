from selenium_test_helper import CssSelector, XpathSelector


class OrderFunction:
    def object_name(self):
        return 'order'

    def function_page_url(self):
        return 'orders'

    def create_button_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def create_page_loaded_selector(self):
        return CssSelector('span[translate="common.buttons.cancel"]')
