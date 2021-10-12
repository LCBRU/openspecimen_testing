from selenium_test_helper import CssSelector, XpathSelector
from open_specimen_tester import OpenSpecimenDestructiveTester


def get_container_tester(helper):
    if helper.version >= '5.1':
        return ContainerTester_v5_1(helper)
    else:
        return ContainerTester_v5_0(helper)


class ContainerTester_v5_0(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return 'containers'

    def name_field_selector(self):
        return CssSelector('input[placeholder="Name"]')

    def create_item(self):
        self.goto_function_page()

        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.create"]'))
        self.helper.get_element_selector(CssSelector('span[translate="container.create_container"]'))

        self.helper.click_element_selector(CssSelector('div[placeholder="Type"]'))
        self.helper.click_element_selector(XpathSelector('//span[text()="-20 Box"]'))

        self.helper.type_in_textbox_selector(self.name_field_selector(), 'Frederick')

        self.helper.click_element_selector(CssSelector('div[placeholder="Site"]'))
        self.helper.click_element_selector(XpathSelector('//span[text()="Glenfield Hospital"]'))

        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.create"]'))
        self.helper.get_element_selector(XpathSelector('//span[text()="Frederick"]'))


    def validate_item(self):
        self.goto_function_page()

        self.helper.get_element_selector(XpathSelector('//span[text()="Frederick"]'))

    def cleanup_item(self):
        self.goto_function_page()

        self.helper.click_element_selector(XpathSelector('//span[text()="Frederick"]'))
        self.helper.click_element_selector(CssSelector('span.fa-user'))
        self.helper.click_element_selector(CssSelector('span.fa-eye'))
        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.delete"]'))
        self.helper.click_element_selector(CssSelector('button.btn-danger'))


class ContainerTester_v5_1(ContainerTester_v5_0):
    def name_field_selector(self):
        return CssSelector('input[name="name"]')
