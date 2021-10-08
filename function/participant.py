from selenium_test_helper import CssSelector, XpathSelector


class ParticipantFunction:
    def object_name(self):
        return 'participant'

    def function_page_url(self):
        return 'cps'

    def collect_samples_page_loaded_selector(self):
        return XpathSelector('//h3[text()="Collect Primary Specimens"]')

    def create_page_register_selector(self):
        return XpathSelector('//span[text()="Register"]')

