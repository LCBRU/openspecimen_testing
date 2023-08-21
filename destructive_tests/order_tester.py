from lbrc_selenium.selenium import CssSelector, XpathSelector
from open_specimen_tester import OpenSpecimenDestructiveTester


def get_order_tester(helper):
    return OrderTester(helper)


class OrderTester(OpenSpecimenDestructiveTester):
    VERSION_CREATE_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.create"]'),
        '10.0': XpathSelector('//button/span[text()="Create"]'),
    }
    VERSION_CANCEL_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.cancel"]'),
        '10.0': XpathSelector('//button/span[text()="Cancel"]'),
    }
    VERSION_PROTOCOL_VALUE = {
        '5.0': CssSelector('div[placeholder="Distribution Protocol"]'),
        '10.0': CssSelector('div[name="order.distributionProtocol"]'),
    }
    VERSION_PROTOCOL_ITEM = {
        '5.0': XpathSelector('//span[text()="BRAVE DNA"]'),
        '10.0': XpathSelector('//li[text()="BRAVE DNA"]'),
    }
    VERSION_INSTITUTE_VALUE = {
        '5.0': CssSelector('div[placeholder="Receiving Institute"]'),
        '10.0': CssSelector('div[name="order.instituteName"]'),
    }
    VERSION_INSTITUTE_ITEM = {
        '5.0': XpathSelector('//span[text()="Imperial College"]'),
        '10.0': XpathSelector('//li[text()="Imperial College"]'),
    }
    VERSION_FUNCTION_NAMES = {
        '5.0': 'orders',
        '10.0': 'orders/-1',
    }

    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return self.helper.get_version_item(self.VERSION_FUNCTION_NAMES)

    def create_item(self):
        # It seems impossible to create an order and then
        # delete it, so I'm just going to check the first page and
        # not actually create it.
        
        self.goto_function_page()

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CREATE_BTN))
        self.helper.get_element(self.helper.get_version_item(self.VERSION_CANCEL_BTN))

        self.helper.click_element(self.helper.get_version_item(self.VERSION_PROTOCOL_VALUE))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_PROTOCOL_ITEM))

        self.helper.click_element(self.helper.get_version_item(self.VERSION_INSTITUTE_VALUE))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_INSTITUTE_ITEM))

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CANCEL_BTN))

    def validate_item(self):
        pass

    def cleanup_item(self):
        pass
