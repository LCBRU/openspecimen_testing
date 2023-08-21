from open_specimen_tester import OpenSpecimenDestructiveTester
from lbrc_selenium.selenium import CssSelector, XpathSelector


def get_role_tester(helper):
    return RoleTester(helper)


class RoleTester(OpenSpecimenDestructiveTester):
    VERSION_CREATE_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.create"]'),
        '10.0': XpathSelector('//button/span[text()="Create"]'),
    }
    VERSION_CANCEL_BTN = {
        '5.0': CssSelector('button[translate="common.buttons.discard"]'),
        '10.0': XpathSelector('//button[text()="Cancel"]'),
    }
    VERSION_NAME_VALUE = {
        '5.0': CssSelector('input[ng-model="role.name"]'),
    }
    VERSION_RESOURCE_VALUE = {
        '5.0': CssSelector('div[placeholder="Resource"]'),
        '10.0': XpathSelector('//div[@ng-model="ac.resourceName"]'),
    }
    VERSION_RESOURCE_ITEM = {
        '5.0': XpathSelector('//span[text()="Orders"]'),
        '6.0': XpathSelector('//span[@class="ng-binding ng-scope" and text()="Orders"]'),
    }

    def url_prefixes(self):
        return {
            '5.0': '#',
        }

    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return 'roles'

    def create_item(self):
        # No option to delete, so never save.

        self.goto_function_page()

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CREATE_BTN))
        self.helper.get_element(self.helper.get_version_item(self.VERSION_CANCEL_BTN))

        self.helper.type_in_textbox(self.helper.get_version_item(self.VERSION_NAME_VALUE), 'Fred')

        self.helper.click_element(self.helper.get_version_item(self.VERSION_RESOURCE_VALUE))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_RESOURCE_ITEM))

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CANCEL_BTN))

    def validate_item(self):
        pass

    def cleanup_item(self):
        pass
