from selenium_test_helper import ClickAction, CssSelector, EnsureAction, SelectAction, TypeInTextboxAction, XpathSelector
from function.distribution_protocol import DistricutionProtocolFunction
from selenium.webdriver.common.by import By
from open_specimen_tester import OpenSpecimenDestructiveTester


class DistricutionProtocolTester(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper, DistricutionProtocolFunction())


        self.values = {
            'Title': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('input[ng-model="distributionProtocol.title"]'),
                text='Distro',
            ),
            'Short Title': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('input[ng-model="distributionProtocol.shortTitle"]'),
                text='Diso',
            ),
            'Receiving Institute': SelectAction(
                helper=self.helper,
                select_selector=CssSelector('div[placeholder="Receiving Institute"]'),
                item_selector=XpathSelector('//span[text()="University of Leicester"]'),
            ),
            'Principal Investigator': SelectAction(
                helper=self.helper,
                select_selector=CssSelector('div[placeholder="Principal Investigator"]'),
                item_selector=XpathSelector('//span[normalize-space(text())="Arnold, Ranjit"]'),
            ),
            'Institute': SelectAction(
                helper=self.helper,
                select_selector=CssSelector('div[placeholder="Institute"]'),
                item_selector=XpathSelector('//span[text()="Kettering General Hospital"]'),
            ),
        }

    def create_item(self):
        self.goto_function_page()

        ClickAction(helper=self.helper, selector=self.function.create_button_selector()).do()
        EnsureAction(helper=self.helper, selector=self.function.create_page_loaded_selector()).do()

        for v in self.values.values():
            v.do()

        ClickAction(helper=self.helper, selector=self.function.create_page_create_selector()).do()
        EnsureAction(helper=self.helper, selector=self.function.item_title_selector()).do()


    def validate_item(self):
        self.goto_function_page()

        EnsureAction(helper=self.helper, selector=self.function.item_title_selector()).do()


    def cleanup_item(self):
        self.goto_function_page()

        ClickAction(helper=self.helper, selector=self.function.item_title_selector()).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="dp.menu_options.delete"]')).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="common.yes"]')).do()
