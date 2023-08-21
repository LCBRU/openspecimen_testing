from open_specimen_tester import OpenSpecimenDestructiveTester
from lbrc_selenium.selenium import CssSelector, XpathSelector


def get_query_tester(helper):
    return QueryTester_v5_0(helper)


class QueryTester_v5_0(OpenSpecimenDestructiveTester):
    VERSION_CREATE_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.create"]'),
        '10.0': XpathSelector('//button/span[text()="Create"]'),
    }
    VERSION_SAVE_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.save"]'),
        '10.0': XpathSelector('//button/span[text()="Save"]'),
    }
    VERSION_FUNCTION_NAMES = {
        '5.0': 'queries/list',
        '10.0': 'queries/list',
    }

    def url_prefixes(self):
        return {
            '5.0': '#',
        }

    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return self.helper.get_version_item(self.VERSION_FUNCTION_NAMES)

    def create_item(self):
        # Queries seem hard to emulate, so for now I'll just check that
        # the page loads.

        self.goto_function_page()

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CREATE_BTN))
        self.helper.get_element(self.helper.get_version_item(self.VERSION_SAVE_BTN))

    def validate_item(self):
        pass

    def cleanup_item(self):
        pass
