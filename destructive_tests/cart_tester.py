from time import sleep
from selenium_test_helper import CssSelector, XpathSelector
from open_specimen_tester import OpenSpecimenDestructiveTester


def get_cart_tester(helper):
    if helper.version >= '5.1':
        return CartTester_v5_1(helper)
    else:
        return CartTester_v5_0(helper)


class CartTester_v5_0(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return 'specimen-lists'

    def edit_user_item_selector(self):
        return XpathSelector('//span[text()="Bramley, Richard"]')

    def create_item(self):
        self.goto_function_page()

        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.create"]'))
        self.helper.get_element_selector(CssSelector('span[translate="specimen_list.create_list"]'))

        self.helper.type_in_textbox_selector(CssSelector('input[ng-model="list.name"]'), text='Fred')

        self.helper.click_element_selector(CssSelector('input[placeholder="Users"]'))
        self.helper.click_element_selector(self.edit_user_item_selector())

        self.helper.type_in_textbox_selector(CssSelector('textarea[ng-model="list.description"]'), text='Lorem Ipsum')

        self.helper.type_in_textbox_selector(CssSelector('textarea[ng-model="input.labelText"]'), text='241996102950120')

        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.create"]'))
        sleep(5)
        self.helper.get_element_selector(CssSelector('span[title="Fred"]'))


    def validate_item(self):
        self.goto_function_page()

        self.helper.get_element_selector(CssSelector('span[title="Fred"]'))


    def cleanup_item(self):
        self.goto_function_page()

        self.helper.click_element_selector(CssSelector('span[title="Fred"]'))
        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.more"]'))
        self.helper.click_element_selector(CssSelector('span[translate="specimen_list.edit_or_delete"]'))
        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.delete"]'))
        self.helper.click_element_selector(CssSelector('span[translate="common.yes"]'))


class CartTester_v5_1(CartTester_v5_0):
    def edit_user_item_selector(self):
        return XpathSelector('//span[text()="Andre Ng"]')
