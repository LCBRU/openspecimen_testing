from selenium_test_helper import CssSelector, XpathSelector


def selectors(version):
    return Selectors_v5_0()


def outputs(version):
    return Outputs_v5_0()


class Outputs_v5_0:
    pass


class Selectors_v5_0:
    def object_name(self):
        return 'participant'

    def function_page_url(self):
        return 'cps'

    def collect_samples_page_loaded_selector(self):
        return XpathSelector('//h3[text()="Collect Primary Specimens"]')

    def create_page_register_selector(self):
        return XpathSelector('//span[text()="Register"]')

