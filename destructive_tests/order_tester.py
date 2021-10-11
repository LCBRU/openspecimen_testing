from selenium_test_helper import ClickAction, CssSelector, EnsureAction, SelectAction, TypeInTextboxAction, XpathSelector
from function.order import selectors, outputs
from open_specimen_tester import OpenSpecimenDestructiveTester


class OrderTester(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper, selectors(helper.version), outputs(helper.compare_version))

        self.values = {
            'Sites': SelectAction(
                helper=self.helper,
                select_selector=CssSelector('div[placeholder="Distribution Protocol"]'),
                item_selector=XpathSelector('//span[text()="BRAVE DNA"]'),
            ),
        }

    def create_item(self):
        # It seems impossible to create an order and then
        # delete it, so I'm just going to check the first page and
        # not actually create it.
        
        self.goto_function_page()

        ClickAction(helper=self.helper, selector=self.selectors.create_button_selector()).do()
        EnsureAction(helper=self.helper, selector=self.selectors.create_page_loaded_selector()).do()

        for v in self.values.values():
            v.do()

        ClickAction(helper=self.helper, selector=CssSelector('span[translate="common.buttons.cancel"]')).do()


    def validate_item(self):
        pass

    def cleanup_item(self):
        pass
