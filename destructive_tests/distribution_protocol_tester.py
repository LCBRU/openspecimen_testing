from selenium_test_helper import CssSelector, XpathSelector
from open_specimen_tester import OpenSpecimenDestructiveTester


def get_distribution_protocol_tester(helper):
    if helper.version >= '5.1':
        return DistricutionProtocolTester_v5_1(helper)
    else:
        return DistricutionProtocolTester_v5_0(helper)


class DistricutionProtocolTester_v5_0(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper)

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

    def pi_value_selector(self):
        return XpathSelector('//span[normalize-space(text())="Arnold, Ranjit"]')

    def create_item(self):
        self.goto_function_page()

        self.helper.click_element_selector(self.create_button_selector())
        self.helper.get_element_selector(self.create_page_loaded_selector())

        self.helper.type_in_textbox_selector(CssSelector('input[ng-model="distributionProtocol.title"]'), 'Distro')
        self.helper.type_in_textbox_selector(CssSelector('input[ng-model="distributionProtocol.shortTitle"]'), 'Diso')

        self.helper.click_element_selector(CssSelector('div[placeholder="Receiving Institute"]'))
        self.helper.click_element_selector(XpathSelector('//span[text()="University of Leicester"]'))

        self.helper.click_element_selector(CssSelector('div[placeholder="Principal Investigator"]'))
        self.helper.click_element_selector(self.pi_value_selector())

        self.helper.click_element_selector(CssSelector('div[placeholder="Institute"]'))
        self.helper.click_element_selector(XpathSelector('//span[text()="Kettering General Hospital"]'))

        self.helper.click_element_selector(self.create_page_create_selector())
        self.helper.get_element_selector(self.item_title_selector())

    def validate_item(self):
        self.goto_function_page()

        self.helper.get_element_selector(self.item_title_selector())

    def cleanup_item(self):
        self.goto_function_page()

        self.helper.click_element_selector(self.item_title_selector())
        self.helper.click_element_selector(CssSelector('span[translate="dp.menu_options.delete"]'))
        self.helper.click_element_selector(CssSelector('span[translate="common.yes"]'))


class DistricutionProtocolTester_v5_1(DistricutionProtocolTester_v5_0):
    def pi_value_selector(self):
        return XpathSelector('//span[text()="Abi Al-Hussaini"]')
