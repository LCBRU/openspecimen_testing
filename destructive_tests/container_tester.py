from selenium_test_helper import ClickAction, CssSelector, EnsureAction, SelectAction, TypeInTextboxAction, XpathSelector
from function.container import selectors, outputs
from open_specimen_tester import OpenSpecimenDestructiveTester


class ContainerTester(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper, selectors(helper.version), outputs(helper.compare_version))

        self.values = {
            'Type': SelectAction(
                helper=self.helper,
                select_selector=CssSelector('div[placeholder="Type"]'),
                item_selector=XpathSelector('//span[text()="-20 Box"]'),
            ),
            'Name': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('input[placeholder="Name"]'),
                text='Frederick',
            ),
            'Parent Site': SelectAction(
                helper=self.helper,
                select_selector=CssSelector('div[placeholder="Site"]'),
                item_selector=XpathSelector('//span[text()="Glenfield Hospital"]'),
            ),
        }

    def create_item(self):
        self.goto_function_page()

        ClickAction(helper=self.helper, selector=self.selectors.create_button_selector()).do()
        EnsureAction(helper=self.helper, selector=self.selectors.create_page_loaded_selector()).do()

        for v in self.values.values():
            v.do()

        ClickAction(helper=self.helper, selector=self.selectors.create_page_create_selector()).do()
        EnsureAction(helper=self.helper, selector=self.selectors.item_title_selector()).do()

    def validate_item(self):
        self.goto_function_page()

        EnsureAction(helper=self.helper, selector=self.selectors.item_title_selector()).do()

    def cleanup_item(self):
        self.goto_function_page()

        ClickAction(helper=self.helper, selector=self.selectors.item_title_selector()).do()
        ClickAction(helper=self.helper, selector=self.selectors.user_menu_item_selector()).do()
        ClickAction(helper=self.helper, selector=CssSelector('span.fa-eye')).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="common.buttons.delete"]')).do()
        ClickAction(helper=self.helper, selector=CssSelector('button.btn-danger')).do()
