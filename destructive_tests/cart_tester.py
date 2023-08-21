from time import sleep
from lbrc_selenium.selenium import CssSelector, XpathSelector
from open_specimen_tester import OpenSpecimenDestructiveTester


def get_cart_tester(helper):
    return CartTester_v5_0(helper)


class CartTester_v5_0(OpenSpecimenDestructiveTester):
    VERSION_EDIT_USER_SELECTOR = {
        '5.0': XpathSelector('//span[text()="Bramley, Richard"]'),
        '5.1': XpathSelector('//span[text()="Andre Ng"]'),
    }
    VERSION_CREATE_BTN_SELECTOR = {
        '5.0': CssSelector('span[translate="common.buttons.create"]'),
        '10.0': XpathSelector('//button/span[text()="Create"]'),
    }
    VERSION_CANCEL_BTN_SELECTOR = {
        '5.0': CssSelector('span[translate="specimen_list.create_list"]'),
        '10.0': XpathSelector('//button/span[text()="Cancel"]'),
    }
    VERSION_NAME_FIELD_SELECTOR = {
        '5.0': CssSelector('input[ng-model="list.name"]'),
        '10.0': CssSelector('div[name="cart.name"] input'),
    }
    VERSION_USERS_FIELD_SELECTOR = {
        '5.0': CssSelector('input[placeholder="Users"]'),
        '10.0': CssSelector('span[type="user"] .p-multiselect'),
    }
    VERSION_DESCRIPTION_FIELD_SELECTOR = {
        '5.0': CssSelector('textarea[ng-model="list.description"]'),
        '10.0': CssSelector('div[name="cart.description"] textarea'),
    }
    VERSION_SPECIMENS_FIELD_SELECTOR = {
        '5.0': CssSelector('textarea[ng-model="input.labelText"]'),
        '10.0': CssSelector('div[name="cart.specimenLabels"] textarea'),
    }
    VERSION_CREATE_CART_BTN_SELECTOR = {
        '5.0': CssSelector('span[translate="common.buttons.create"]'),
        '10.0': XpathSelector('//button/span[text()="Create"]'),
    }
    VERSION_CART_ITEM = {
        '5.0': CssSelector('span[title="Fred"]'),
        '10.0': XpathSelector('//span[text()="Fred"]'),
    }
    VERSION_MORE_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.more"]'),
        '10.0': XpathSelector('//button/span[text()="More"]'),
    }
    VERSION_EDIT_DELETE_BTN = {
        '5.0': CssSelector('span[translate="specimen_list.edit_or_delete"]'),
        '10.0': XpathSelector('//a/span[text()="Edit or Delete Cart"]'),
    }
    VERSION_DELETE_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.delete"]'),
        '10.0': XpathSelector('//button/span[text()="Delete"]'),
    }
    VERSION_YES_BTN = {
        '5.0': CssSelector('span[translate="common.yes"]'),
        '10.0': XpathSelector('//button/span[text()="Yes"]'),
    }
    VERSION_FUNCTION_NAMES = {
        '5.0': 'specimen-lists',
        '10.0': 'carts/-1',
    }

    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return self.helper.get_version_item(self.VERSION_FUNCTION_NAMES)

    def edit_user_item_selector(self):
        return self.helper.get_version_item(self.VERSION_EDIT_USER_SELECTOR)

    def create_item(self):
        self.goto_function_page()

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CREATE_BTN_SELECTOR))
        self.helper.get_element(self.helper.get_version_item(self.VERSION_CANCEL_BTN_SELECTOR))

        self.helper.type_in_textbox(self.helper.get_version_item(self.VERSION_NAME_FIELD_SELECTOR), text='Fred')

        self.helper.click_element(self.helper.get_version_item(self.VERSION_USERS_FIELD_SELECTOR))
        self.helper.click_element(self.edit_user_item_selector())

        self.helper.type_in_textbox(self.helper.get_version_item(self.VERSION_DESCRIPTION_FIELD_SELECTOR), text='Lorem Ipsum')

        self.helper.type_in_textbox(self.helper.get_version_item(self.VERSION_SPECIMENS_FIELD_SELECTOR), text='241996102950120')

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CREATE_CART_BTN_SELECTOR))
        sleep(5)
        self.helper.get_element(self.helper.get_version_item(self.VERSION_CART_ITEM))


    def validate_item(self):
        self.goto_function_page()

        self.helper.get_element(self.helper.get_version_item(self.VERSION_CART_ITEM))


    def cleanup_item(self):
        self.goto_function_page()

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CART_ITEM))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_MORE_BTN))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_EDIT_DELETE_BTN))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_DELETE_BTN))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_YES_BTN))
