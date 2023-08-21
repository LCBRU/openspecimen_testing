from open_specimen_tester import OpenSpecimenDestructiveTester
from lbrc_selenium.selenium import CssSelector, XpathSelector


def get_site_tester(helper):
    return SiteTester_v5_0(helper)


class SiteTester_v5_0(OpenSpecimenDestructiveTester):
    VERSION_CREATE_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.create"]'),
        '10.0': XpathSelector('//button/span[text()="Create"]'),
    }
    VERSION_CANCEL_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.discard"]'),
        '10.0': XpathSelector('//button/span[text()="Cancel"]'),
    }
    VERSION_INSTITUTE_VALUE = {
        '5.0': CssSelector('div[placeholder="Institute"]'),
        '10.0': CssSelector('div[name="site.instituteName"]'),
    }
    VERSION_INSTITUTE_ITEM = {
        '5.0': XpathSelector('//span[text()="University of Leicester"]'),
        '10.0': XpathSelector('//li[text()="University of Leicester"]'),
    }
    VERSION_NAME_VALUE = {
        '5.0': CssSelector('input[name="siteName"]'),
        '10.0': CssSelector('div[name="site.name"] input'),
    }
    VERSION_TYPE_VALUE = {
        '5.0': CssSelector('div[placeholder="Type"]'),
        '10.0': CssSelector('div[name="site.type"]'),
    }
    VERSION_TYPE_ITEM = {
        '5.0': XpathSelector('//span[text()="Collection Site"]'),
        '10.0': XpathSelector('//li[text()="Collection Site"]'),
    }
    VERSION_TITLE = {
        '5.0': XpathSelector('//*[normalize-space(text())="Fred"]'),
    }
    VERSION_DELETE_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.delete"]'),
        '10.0': XpathSelector('//button/span[text()="Delete"]'),
    }
    VERSION_YES_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.yes"]'),
        '10.0': XpathSelector('//button/span[text()="Yes"]'),
    }
    VERSION_FUNCTION_PAGE = {
        '5.0': 'sites',
        '10.0': 'sites/-1',
    }

    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return self.helper.get_version_item(self.VERSION_FUNCTION_PAGE)

    def create_item(self):
        self.goto_function_page()

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CREATE_BTN))
        self.helper.get_element(self.helper.get_version_item(self.VERSION_CANCEL_BTN))

        self.helper.click_element(self.helper.get_version_item(self.VERSION_INSTITUTE_VALUE))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_INSTITUTE_ITEM))

        self.helper.type_in_textbox(self.helper.get_version_item(self.VERSION_NAME_VALUE), 'Fred')

        self.helper.click_element(self.helper.get_version_item(self.VERSION_TYPE_VALUE))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_TYPE_ITEM))

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CREATE_BTN))
        self.helper.get_element(self.helper.get_version_item(self.VERSION_TITLE))

    def validate_item(self):
        self.goto_function_page()

        self.helper.get_element(self.helper.get_version_item(self.VERSION_TITLE))


    def cleanup_item(self):
        self.goto_function_page()

        self.helper.click_element(self.helper.get_version_item(self.VERSION_TITLE))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_DELETE_BTN))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_YES_BTN))
