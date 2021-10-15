from selenium_test_helper import ClickAction, CssSelector, EnsureAction, XpathSelector
from time import sleep
from open_specimen_tester import OpenSpecimenDestructiveTester


def get_collection_protocol_tester(helper):
    if helper.version >= '6.0':
        return CollectionProtocolTester_v6_0(helper)
    elif helper.version >= '5.1':
        return CollectionProtocolTester_v5_1(helper)
    else:
        return CollectionProtocolTester_v5_0(helper)


class CollectionProtocolTester_v5_0(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return 'cps'

    def create_item(self):
        self.goto_function_page()

        sleep(15)

        self.helper.click_element_selector(CssSelector('button[title="Click to add new Collection Protocol"]'))

        sleep(1)

        self.helper.click_element_selector(CssSelector('a > span[translate="common.buttons.create"]'))
        self.helper.get_element_selector(CssSelector('span[translate="cp.create_cp_title"]'))

        self.helper.click_element_selector(CssSelector('input[placeholder="Sites"]'))
        self.helper.click_element_selector(XpathSelector('//span[text()="Glenfield Hospital"]'))

        self.helper.type_in_textbox_selector(CssSelector('input[placeholder="Title"]'), 'Frederick')
        self.helper.type_in_textbox_selector(CssSelector('input[placeholder="Short Title"]'), 'Fred')

        self.helper.click_element_selector(CssSelector('div[placeholder="Principal Investigator"]'))
        self.helper.click_element_selector(XpathSelector('//span[text()="Adlam, Dave"]'))

        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.create"]'))

        self.helper.get_element_selector(XpathSelector('//span[text()="Fred"]'))

    def validate_item(self):
        self.goto_function_page()

        sleep(5)

        self.helper.get_element_selector(XpathSelector('//span[text()="Fred"]'))

    def cleanup_item(self):
        self.goto_function_page()

        sleep(5)

        self.helper.click_element_selector(XpathSelector('//span[text()="Fred"]'))
        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.more"]'))
        self.helper.click_element_selector(CssSelector('span[translate="cp.view_details"]'))

        self.helper.click_element_selector(CssSelector('span[translate="cp.menu_options.delete"]'))
        self.helper.click_element_selector(CssSelector('span[translate="common.yes"]'))


class CollectionProtocolTester_v5_1(CollectionProtocolTester_v5_0):
    def site_field_selector(self):
        return CssSelector('input[ng-model="$select.search"]')

    def create_item(self):
        self.goto_function_page()

        sleep(15)

        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.create"]'))
        self.helper.get_element_selector(CssSelector('span[translate="cp.create_cp_title"]'))

        sleep(5)

        self.helper.click_element_selector(self.site_field_selector())
        self.helper.click_element_selector(XpathSelector('//span[text()="Glenfield Hospital"]'))

        self.helper.type_in_textbox_selector(CssSelector('input[ng-model="cp.title"]'), 'Frederick')
        self.helper.type_in_textbox_selector(CssSelector('input[ng-model="cp.shortTitle"]'), 'Fred')

        self.helper.click_element_selector(CssSelector('div[placeholder="Principal Investigator"] > div > div > span'))
        self.helper.click_element_selector(XpathSelector('//span[text()="Abi Al-Hussaini"]'))

        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.create"]'))

        self.helper.get_element_selector(XpathSelector('//span[text()="Fred"]'))

    def cleanup_item(self):
        self.goto_function_page()

        sleep(5)

        self.helper.click_element_selector(XpathSelector('//span[text()="Fred"]'))
        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.more"]'))
        self.helper.click_element_selector(CssSelector('span[translate="cp.view_details"]'))

        self.helper.click_element_selector(CssSelector('span[translate="cp.menu_options.delete"]'))
        self.helper.type_in_textbox_selector(CssSelector('textarea[ng-model="entityProps.reason"]'), 'Order of magnitude')
        self.helper.click_element_selector(CssSelector('span[translate="common.yes"]'))


class CollectionProtocolTester_v6_0(CollectionProtocolTester_v5_1):
    def site_field_selector(self):
        return CssSelector('div[ng-model="cp.repositoryNames"]')
