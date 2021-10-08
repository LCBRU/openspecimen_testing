from selenium_test_helper import ClickAction, CssSelector, EnsureAction, TypeInTextboxAction, XpathSelector
from function.institute import InstituteFunction
from open_specimen_tester import OpenSpecimenDestructiveTester


class InstituteTester(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper, InstituteFunction())

        self.values = {
            'Name': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('input[ng-model="institute.name"]'),
                text='Royal Institution',
            ),
        }

    def create_item(self):
        self.goto_function_page()

        ClickAction(helper=self.helper, selector=self.function.create_button_selector()).do()
        EnsureAction(helper=self.helper, selector=self.function.create_page_loaded_selector()).do()

        for v in self.values.values():
            v.do()

        ClickAction(helper=self.helper, selector=self.function.create_page_create_selector()).do()
        EnsureAction(helper=self.helper, selector=XpathSelector('//h3[normalize-space(text())="Royal Institution"]')).do()


    def validate_item(self):
        self.goto_function_page()

        EnsureAction(helper=self.helper, selector=self.function.item_title_selector()).do()


    def cleanup_item(self):
        self.goto_function_page()

        ClickAction(helper=self.helper, selector=self.function.item_title_selector()).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="common.buttons.more"]')).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="common.buttons.delete"]')).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="common.yes"]')).do()
