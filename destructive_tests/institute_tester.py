from lbrc_selenium.selenium import CssSelector, XpathSelector
from open_specimen_tester import OpenSpecimenDestructiveTester


def get_institute_tester(helper):
    return InstituteTester(helper)


class InstituteTester(OpenSpecimenDestructiveTester):
    VERSION_CREATE_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.create"]'),
        '10.0': XpathSelector('//button/span[text()="Create"]'),
    }
    VERSION_PAGE_LOADED = {
        '5.0': CssSelector('span[translate="institute.create_institute"]'),
        '10.0': CssSelector('div[name="institute.name"] input'),
    }
    VERSION_NAME_VALUE = {
        '5.0': CssSelector('input[ng-model="institute.name"]'),
        '10.0': CssSelector('div[name="institute.name"] input'),
    }
    VERSION_MORE_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.more"]'),
        '10.0': CssSelector('h3'),
    }
    VERSION_DELETE_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.delete"]'),
        '10.0': XpathSelector('//button/span[text()="Delete"]'),
    }
    VERSION_YES_BTN = {
        '5.0': CssSelector('span[translate="common.yes"]'),
        '10.0': XpathSelector('//button/span[text()="Yes"]'),
    }
    VERSION_TITLE = {
        '5.0': XpathSelector('//*[normalize-space(text())="Royal Institution"]'),
    }
    VERSION_FUNCTION_NAMES = {
        '5.0': 'institutes',
        '10.0': 'institutes/-1',
    }

    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return self.helper.get_version_item(self.VERSION_FUNCTION_NAMES)

    def create_page_loaded_selector(self):
        return CssSelector('span[translate="institute.create_institute"]')

    def item_title_selector(self):
        return XpathSelector('//span[normalize-space(text())="Royal Institution"]')

    def create_item(self):
        self.goto_function_page()

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CREATE_BTN))
        self.helper.get_element(self.helper.get_version_item(self.VERSION_PAGE_LOADED))

        self.helper.type_in_textbox(self.helper.get_version_item(self.VERSION_NAME_VALUE), 'Royal Institution')

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CREATE_BTN))
        self.helper.get_element(self.helper.get_version_item(self.VERSION_TITLE))

    def validate_item(self):
        self.goto_function_page()

        self.helper.get_element(self.helper.get_version_item(self.VERSION_TITLE))

    def cleanup_item(self):
        self.goto_function_page()

        self.helper.click_element(self.helper.get_version_item(self.VERSION_TITLE))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_MORE_BTN))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_DELETE_BTN))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_YES_BTN))
