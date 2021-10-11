from selenium_test_helper import CssSelector, XpathSelector


def selectors(version):
    return Selectors_v5_0()


def outputs(version):
    return Outputs_v5_0()


class Outputs_v5_0:
    pass


class Selectors_v5_0:
    def object_name(self):
        return 'institute'

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

