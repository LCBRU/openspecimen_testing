from lbrc_selenium.selenium import CssSelector, XpathSelector
from open_specimen_tester import OpenSpecimenDestructiveTester
from time import sleep

def get_distribution_protocol_tester(helper):
    return DistricutionProtocolTester(helper)


class DistricutionProtocolTester(OpenSpecimenDestructiveTester):
    VERSION_CREATE_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.create"]'),
        '10.0': XpathSelector('//button/span[text()="Create"]'),
    }
    VERSION_TITLE_VALUE = {
        '5.0': CssSelector('input[ng-model="distributionProtocol.title"]'),
        '10.0': CssSelector('div[name="dp.title"] input'),
    }
    VERSION_SHORTTITLE_VALUE = {
        '5.0': CssSelector('input[ng-model="distributionProtocol.shortTitle"]'),
        '10.0': CssSelector('div[name="dp.shortTitle"] input'),
    }
    VERSION_RECEIVING_INST_VALUE = {
        '5.0': CssSelector('div[placeholder="Receiving Institute"]'),
        '10.0': CssSelector('div[name="dp.instituteName"]'),
    }
    VERSION_RECEIVING_INST_ITEM = {
        '5.0': XpathSelector('//span[text()="University of Leicester"]'),
        '10.0': XpathSelector('//li[text()="University of Leicester"]'),
    }
    VERSION_PI_VALUE = {
        '5.0': CssSelector('div[placeholder="Principal Investigator"]'),
        '10.0': CssSelector('span[name="dp.principalInvestigator"] div'),
    }
    VERSION_PI_ITEM = {
        '5.0': XpathSelector('//span[normalize-space(text())="Arnold, Ranjit"]'),
        '5.1': XpathSelector('//span[text()="Abi Al-Hussaini"]'),
        '10.0': XpathSelector('//li[text()="Abi Al-Hussaini"]'),
    }
    VERSION_INSTITUTE_VALUE = {
        '5.0': CssSelector('div[placeholder="Institute"]'),
        '10.0': CssSelector('div[name="institute"]'),
    }
    VERSION_INSTITUTE_ITEM = {
        '5.0': XpathSelector('//span[text()="University of Leicester"]'),
        '10.0': XpathSelector('//li[text()="University of Leicester"]'),
    }
    VERSION_DISP_SITE_VALUE = {
        '5.0': CssSelector('div[placeholder="Institute"]'),
        '10.0': CssSelector('span[name="sites"] div'),
    }
    VERSION_DISP_SITE_ITEM = {
        '5.0': XpathSelector('//span[text()="Glenfield Hospital"]'),
        '10.0': XpathSelector('//span[text()="Glenfield Hospital"]'),
    }
    VERSION_CREATE_CDP_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.create"]'),
        '10.0': XpathSelector('//button/span[text()="Create"]'),
    }
    VERSION_ITEM_TITLE = {
        '5.0': XpathSelector('//span[normalize-space(text())="Diso"]'),
    }
    VERSION_DELETE_BTN = {
        '5.0': CssSelector('span[translate="dp.menu_options.delete"]'),
        '10.0': XpathSelector('//button/span[text()="Delete"]'),
    }
    VERSION_YES_BTN = {
        '5.0': CssSelector('span[translate="common.yes"]'),
        '10.0': XpathSelector('//button/span[text()="Yes"]'),
    }
    VERSION_FUNCTION_NAMES = {
        '5.0': 'dps',
        '10.0': 'dps/-1',
    }

    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return self.helper.get_version_item(self.VERSION_FUNCTION_NAMES)

    def create_item(self):
        self.goto_function_page()

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CREATE_BTN))
        self.helper.get_element(self.helper.get_version_item(self.VERSION_TITLE_VALUE))

        self.helper.type_in_textbox(self.helper.get_version_item(self.VERSION_TITLE_VALUE), 'Distro')
        self.helper.type_in_textbox(self.helper.get_version_item(self.VERSION_SHORTTITLE_VALUE), 'Diso')

        self.helper.click_element(self.helper.get_version_item(self.VERSION_RECEIVING_INST_VALUE))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_RECEIVING_INST_ITEM))
        sleep(5)

        self.helper.click_element(self.helper.get_version_item(self.VERSION_PI_VALUE))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_PI_ITEM))
        sleep(5)

        self.helper.click_element(self.helper.get_version_item(self.VERSION_INSTITUTE_VALUE))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_INSTITUTE_ITEM))
        sleep(5)

        self.helper.click_element(self.helper.get_version_item(self.VERSION_DISP_SITE_VALUE))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_DISP_SITE_ITEM))
        sleep(5)

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CREATE_CDP_BTN))
        self.helper.get_element(self.helper.get_version_item(self.VERSION_ITEM_TITLE))

    def validate_item(self):
        self.goto_function_page()

        self.helper.get_element(self.helper.get_version_item(self.VERSION_ITEM_TITLE))

    def cleanup_item(self):
        self.goto_function_page()

        self.helper.click_element(self.helper.get_version_item(self.VERSION_ITEM_TITLE))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_DELETE_BTN))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_YES_BTN))
