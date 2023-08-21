from time import sleep
from lbrc_selenium.selenium import CssSelector, XpathSelector
from open_specimen_tester import OpenSpecimenDestructiveTester


def get_container_tester(helper):
    return ContainerTester_v5_0(helper)


class ContainerTester_v5_0(OpenSpecimenDestructiveTester):
    VERSION_CREATE_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.create"]'),
        '10.0': XpathSelector('//button/span[text()="Create"]'),
    }
    VERSION_CREATE_SCREEN = {
        '5.0': CssSelector('span[translate="container.create_container"]'),
        '10.0': XpathSelector('//span[text()="Create Container"]'),
    }
    VERSION_TYPE_FIELD = {
        '5.0': CssSelector('div[placeholder="Type"]'),
        '10.0': CssSelector('div[name="container.typeName"]'),
    }
    VERSION_TYPE_VALUE = {
        '5.0': XpathSelector('//span[text()="-20 Box"]'),
        '10.0': XpathSelector('//li[text()="-20 Box"]'),
    }
    VERSION_NAME_FIELD = {
        '5.0': CssSelector('input[placeholder="Name"]'),
        '5.1': CssSelector('input[name="name"]'),
        '10.0': CssSelector('div[name="container.name"] input'),
    }
    VERSION_SITE_FIELD = {
        '5.0': CssSelector('div[placeholder="Site"]'),
        '10.0': CssSelector('span[name="container.siteName"] div'),
    }
    VERSION_SITE_VALUE = {
        '5.0': XpathSelector('//span[text()="Glenfield Hospital"]'),
        '10.0': XpathSelector('//li[text()="Glenfield Hospital"]'),
    }
    VERSION_CREATE_CONTAINER_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.create"]'),
        '10.0': XpathSelector('//button/span[text()="Create"]'),
    }
    VERSION_SEARCH_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.search"]'),
        '10.0': XpathSelector('//button/span[text()="Search"]'),
    }
    VERSION_SEARCH_NAME = {
        '5.0': CssSelector('input[placeholder="Name"]'),
        '10.0': CssSelector('div[placeholder="Name"] input'),
    }
    VERSION_DELETE_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.delete"]'),
        '10.0': XpathSelector('//button/span[text()="Delete"]'),
    }
    VERSION_CONFIRM_INPUT = {
        '10.0': CssSelector('div.p-dialog-content input'),
    }
    VERSION_CONFIRM_BTN = {
        '5.0': CssSelector('button.btn-danger'),
        '10.0': XpathSelector('//button/span[text()="Yes"]'),
    }
    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return 'containers'

    def create_item(self):
        self.goto_function_page()

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CREATE_BTN))
        self.helper.get_element(self.helper.get_version_item(self.VERSION_CREATE_SCREEN))

        self.helper.click_element(self.helper.get_version_item(self.VERSION_TYPE_FIELD))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_TYPE_VALUE))

        self.helper.type_in_textbox(self.helper.get_version_item(self.VERSION_NAME_FIELD), 'Frederick')

        sleep(1)

        self.helper.click_element(self.helper.get_version_item(self.VERSION_SITE_FIELD))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_SITE_VALUE))

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CREATE_CONTAINER_BTN))
        self.helper.get_element(XpathSelector('//span[text()="Frederick"]'))


    def validate_item(self):
        self.goto_function_page()

        self.helper.click_element(self.helper.get_version_item(self.VERSION_SEARCH_BTN))
        self.helper.type_in_textbox(self.helper.get_version_item(self.VERSION_SEARCH_NAME), 'Frederick')
        sleep(1)
        self.helper.get_element(XpathSelector('//span[text()="Frederick"]'))

    def cleanup_item(self):
        self.goto_function_page()

        # self.helper.click_element(self.helper.get_version_item(self.VERSION_SEARCH_BTN))
        # sleep(1)
        # self.helper.type_in_textbox(self.helper.get_version_item(self.VERSION_SEARCH_NAME), 'Frederick')
        sleep(1)
        self.helper.click_element(XpathSelector('//span[text()="Frederick"]'))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_DELETE_BTN))
        self.helper.type_in_textbox(self.helper.get_version_item(self.VERSION_CONFIRM_INPUT), 'DELETE ANYWAY')
        self.helper.click_element(self.helper.get_version_item(self.VERSION_CONFIRM_BTN))
