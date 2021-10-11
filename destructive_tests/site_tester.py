from function.site import selectors, outputs
from open_specimen_tester import OpenSpecimenDestructiveTester
from selenium_test_helper import ClickAction, CssSelector, EnsureAction, SelectAction, TypeInTextboxAction, XpathSelector


class SiteTester(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper, selectors(helper.version), outputs(helper.compare_version))

        self.values = {
            'PI': SelectAction(
                helper=self.helper,
                select_selector=CssSelector('div[placeholder="Institute"]'),
                item_selector=XpathSelector('//span[text()="University of Leicester"]'),
            ),
            'Name': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('input[placeholder="Name"]'),
                text='Fred',
            ),
            'Type': SelectAction(
                helper=self.helper,
                select_selector=CssSelector('div[placeholder="Type"]'),
                item_selector=XpathSelector('//span[text()="Collection Site"]'),
            ),
        }

    def create_item(self):
        self.goto_function_page()

        ClickAction(helper=self.helper, selector=self.selectors.create_button_selector()).do()
        EnsureAction(helper=self.helper, selector=self.selectors.create_page_loaded_selector()).do()

        for v in self.values.values():
            v.do()

        ClickAction(helper=self.helper, selector=self.selectors.create_page_create_selector()).do()
        EnsureAction(helper=self.helper, selector=XpathSelector('//h3[normalize-space(text())="Fred"]')).do()


    def validate_item(self):
        self.goto_function_page()

        EnsureAction(helper=self.helper, selector=self.selectors.item_title_selector()).do()


    def cleanup_item(self):
        self.goto_function_page()

        ClickAction(helper=self.helper, selector=self.selectors.item_title_selector()).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="common.buttons.delete"]')).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="common.yes"]')).do()
