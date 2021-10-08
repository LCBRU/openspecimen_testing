from selenium_test_helper import CssSelector, XpathSelector


class DistricutionProtocolFunction:
    def object_name(self):
        return 'distribution_protocol'

    def function_page_url(self):
        return 'dps'

    def create_button_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def create_page_loaded_selector(self):
        return CssSelector('span[translate="dp.create_dp_title"]')

    def create_page_create_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def item_title_selector(self):
        return XpathSelector('//span[normalize-space(text())="Diso"]')
