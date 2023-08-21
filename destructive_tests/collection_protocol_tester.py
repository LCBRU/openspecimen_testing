from lbrc_selenium.selenium import CssSelector, XpathSelector
from time import sleep
from open_specimen_tester import OpenSpecimenDestructiveTester


def get_collection_protocol_tester(helper):
    if helper.version >= '10.0':
        return CollectionProtocolTester_v10_0(helper)
    elif helper.version >= '6.0':
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

        self.helper.click_element(CssSelector('button[title="Click to add new Collection Protocol"]'))

        sleep(1)

        self.helper.click_element(CssSelector('a > span[translate="common.buttons.create"]'))
        self.helper.get_element(CssSelector('span[translate="cp.create_cp_title"]'))

        self.helper.click_element(CssSelector('input[placeholder="Sites"]'))
        self.helper.click_element(XpathSelector('//span[text()="Glenfield Hospital"]'))

        self.helper.type_in_textbox(CssSelector('input[placeholder="Title"]'), 'Frederick')
        self.helper.type_in_textbox(CssSelector('input[placeholder="Short Title"]'), 'Fred')

        self.helper.click_element(CssSelector('div[placeholder="Principal Investigator"]'))
        self.helper.click_element(XpathSelector('//span[text()="Adlam, Dave"]'))

        self.helper.click_element(CssSelector('span[translate="common.buttons.create"]'))

        self.helper.get_element(XpathSelector('//span[text()="Fred"]'))

    def validate_item(self):
        self.goto_function_page()

        sleep(5)

        self.helper.get_element(XpathSelector('//span[text()="Fred"]'))

    def cleanup_item(self):
        self.goto_function_page()

        sleep(5)

        self.helper.click_element(XpathSelector('//span[text()="Fred"]'))
        self.helper.click_element(CssSelector('span[translate="common.buttons.more"]'))
        self.helper.click_element(CssSelector('span[translate="cp.view_details"]'))

        self.helper.click_element(CssSelector('span[translate="cp.menu_options.delete"]'))
        self.helper.click_element(CssSelector('span[translate="common.yes"]'))


class CollectionProtocolTester_v5_1(CollectionProtocolTester_v5_0):
    def site_field_selector(self):
        return CssSelector('input[ng-model="$select.search"]')

    def create_item(self):
        self.goto_function_page()

        sleep(15)

        self.helper.click_element(CssSelector('span[translate="common.buttons.create"]'))
        self.helper.get_element(CssSelector('span[translate="cp.create_cp_title"]'))

        sleep(5)

        self.helper.click_element(self.site_field_selector())
        self.helper.click_element(XpathSelector('//span[text()="Glenfield Hospital"]'))

        self.helper.type_in_textbox(CssSelector('input[ng-model="cp.title"]'), 'Frederick')
        self.helper.type_in_textbox(CssSelector('input[ng-model="cp.shortTitle"]'), 'Fred')

        self.helper.click_element(CssSelector('div[placeholder="Principal Investigator"] > div > div > span'))
        self.helper.click_element(XpathSelector('//span[text()="Abi Al-Hussaini"]'))

        self.helper.click_element(CssSelector('span[translate="common.buttons.create"]'))

        self.helper.get_element(XpathSelector('//span[text()="Fred"]'))

    def cleanup_item(self):
        self.goto_function_page()

        sleep(5)

        self.helper.click_element(XpathSelector('//span[text()="Fred"]'))
        self.helper.click_element(CssSelector('span[translate="common.buttons.more"]'))
        self.helper.click_element(CssSelector('span[translate="cp.view_details"]'))

        self.helper.click_element(CssSelector('span[translate="cp.menu_options.delete"]'))
        self.helper.type_in_textbox(CssSelector('textarea[ng-model="entityProps.reason"]'), 'Order of magnitude')
        self.helper.click_element(CssSelector('span[translate="common.yes"]'))


class CollectionProtocolTester_v6_0(CollectionProtocolTester_v5_1):
    def site_field_selector(self):
        return CssSelector('div[ng-model="cp.repositoryNames"]')


class CollectionProtocolTester_v10_0(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return 'cps'

    def url_prefixes(self):
        return {
            '5.0': '#',
        }
        
    def create_item(self):
        self.goto_function_page()

        sleep(15)

        self.helper.click_element(CssSelector('button > span[translate="common.buttons.create"]'))
        self.helper.get_element(CssSelector('label[translate="cp.repositories"]'))

        self.helper.click_element(CssSelector('div[name="repositoryNames"]'))
        self.helper.click_element(XpathSelector('//span[text()="Glenfield Hospital"]'))

        self.helper.type_in_textbox(CssSelector('input[name="title"]'), 'Frederick')
        self.helper.type_in_textbox(CssSelector('input[name="shortTitle"]'), 'Fred')

        self.helper.click_element(CssSelector('div[placeholder="Principal Investigator"]'))
        self.helper.click_element(XpathSelector('//span[text()="Dave Adlam"]'))

        self.helper.click_element(CssSelector('span[translate="common.buttons.create"]'))

        sleep(5)

        self.helper.get_element(XpathSelector('//span[text()="Frederick"]'))

    def validate_item(self):
        self.goto_function_page()

        sleep(5)

        self.helper.type_in_textbox(CssSelector('input[placeholder="Title"]'), 'Fred')

        sleep(5)

        self.helper.get_element(CssSelector('a[href^="#/cp-view"]'))

    def cleanup_item(self):
        self.goto_function_page()

        sleep(5)

        self.helper.type_in_textbox(CssSelector('input[placeholder="Title"]'), 'Fred')

        sleep(5)

        self.helper.click_element(XpathSelector('//button[data-title="View CP Details"]'))

        self.helper.click_element(CssSelector('span[translate="cp.menu_options.delete"]'))
        self.helper.type_in_textbox(CssSelector('textarea[ng-model="entityProps.reason"]'), 'Order of magnitude')
        self.helper.click_element(CssSelector('span[translate="common.yes"]'))
