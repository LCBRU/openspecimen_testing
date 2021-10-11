from selenium_test_helper import CssSelector, XpathSelector


class QueryFunction:
    def object_name(self):
        return 'query'

    def function_page_url(self):
        return 'queries/list'

    def create_button_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def create_page_loaded_selector(self):
        return CssSelector('span[translate="common.buttons.save"]')
