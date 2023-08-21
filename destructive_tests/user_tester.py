from open_specimen_tester import OpenSpecimenDestructiveTester
from lbrc_selenium.selenium import CssSelector, XpathSelector
from time import sleep

def get_user_tester(helper):
    return UserTester(helper)


class UserTester(OpenSpecimenDestructiveTester):
    VERSION_CREATE_BTN = {
        '5.0': CssSelector('span[translate="common.buttons.create"]'),
        '10.0': XpathSelector('//button/span[text()="Create"]'),
    }
    VERSION_CANCEL_BTN = {
        '5.0': CssSelector('button[translate="common.buttons.discard"]'),
        '10.0': XpathSelector('//button/span[text()="Cancel"]'),
    }
    VERSION_DELETE_BTN = {
        '5.0': CssSelector('button[translate="common.buttons.delete"]'),
        '10.0': XpathSelector('//button/span[text()="Delete"]'),
    }
    VERSION_YES_BTN = {
        '5.0': CssSelector('button[translate="common.buttons.yes"]'),
        '10.0': XpathSelector('//button/span[text()="Yes"]'),
    }
    VERSION_LASTNAME_VALUE = {
        '5.0': CssSelector('input[name="lastName"]'),
        '10.0': CssSelector('div[name="user.lastName"] input'),
    }
    VERSION_FIRSTNAME_VALUE = {
        '5.0': CssSelector('input[name="firstName"]'),
        '10.0': CssSelector('div[name="user.firstName"] input'),
    }
    VERSION_EMAIL_VALUE = {
        '5.0': CssSelector('input[name="email"]'),
        '10.0': CssSelector('div[name="user.emailAddress"] input'),
    }
    VERSION_LOGIN_VALUE = {
        '5.0': CssSelector('input[name="loginName"]'),
        '10.0': CssSelector('div[name="user.loginName"] input'),
    }
    VERSION_DOMAIN_VALUE = {
        '5.0': CssSelector('div[placeholder="Domain"]'),
        '10.0': CssSelector('div[name="user.domainName"] div'),
    }
    VERSION_DOMAIN_ITEM = {
        '5.0': XpathSelector('//span[text()="openspecimen"]'),
        '10.0': XpathSelector('//li[text()="openspecimen"]'),
    }
    VERSION_INSTITUTE_VALUE = {
        '5.0': CssSelector('div[placeholder="Institute"]'),
        '10.0': CssSelector('div[name="user.instituteName"] div'),
    }
    VERSION_INSTITUTE_ITEM = {
        '5.0': XpathSelector('//span[text()="University of Leicester"]'),
        '10.0': XpathSelector('//li[text()="University of Leicester"]'),
    }
    VERSION_TITLE = {
        '5.0': XpathSelector('//span[normalize-space(text())="Fred Flintoff"]'),
    }
    VERSION_FUNCTION_PAGE = {
        '5.0': 'users',
        '10.0': 'users/-1',
    }

    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return self.helper.get_version_item(self.VERSION_FUNCTION_PAGE)

    def create_item(self):
        self.goto_function_page()

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CREATE_BTN))
        self.helper.get_element(self.helper.get_version_item(self.VERSION_CANCEL_BTN))

        self.helper.type_in_textbox(self.helper.get_version_item(self.VERSION_LASTNAME_VALUE), 'Flintoff')
        self.helper.type_in_textbox(self.helper.get_version_item(self.VERSION_FIRSTNAME_VALUE), 'Fred')
        self.helper.type_in_textbox(self.helper.get_version_item(self.VERSION_EMAIL_VALUE), 'fred@ecb.co.uk')
        self.helper.type_in_textbox(self.helper.get_version_item(self.VERSION_LOGIN_VALUE), 'fred.flintoff')

        self.helper.click_element(self.helper.get_version_item(self.VERSION_DOMAIN_VALUE))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_DOMAIN_ITEM))

        self.helper.click_element(self.helper.get_version_item(self.VERSION_INSTITUTE_VALUE))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_INSTITUTE_ITEM))

        self.helper.click_element(self.helper.get_version_item(self.VERSION_CREATE_BTN))
        self.helper.get_element(self.helper.get_version_item(self.VERSION_DELETE_BTN))


    def validate_item(self):
        self.goto_function_page()

        self.helper.get_element(self.helper.get_version_item(self.VERSION_TITLE))


    def cleanup_item(self):
        self.goto_function_page()

        self.helper.click_element(self.helper.get_version_item(self.VERSION_TITLE))
        self.helper.click_element(self.helper.get_version_item(self.VERSION_DELETE_BTN))
        sleep(5)
        self.helper.click_element(self.helper.get_version_item(self.VERSION_YES_BTN))
