from selenium_test_helper import ClickAction, CssSelector, EnsureAction, SelectAction, TypeInTextboxAction, XpathSelector
from function.cart import CartFunction
from open_specimen_tester import OpenSpecimenDestructiveTester


class CartTester(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper, CartFunction())

        self.values = {
            'Name': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('input[ng-model="list.name"]'),
                text='Fred',
            ),
            'Share': SelectAction(
                helper=self.helper,
                select_selector=CssSelector('input[placeholder="Users"]'),
                item_selector=XpathSelector('//span[text()="Bramley, Richard"]'),
            ),
            'Description': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('textarea[ng-model="list.description"]'),
                text='Lorem Ipsum',
            ),
            'Specimens': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('textarea[ng-model="input.labelText"]'),
                text='241996102950120',
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
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="common.buttons.more"]')).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="specimen_list.edit_or_delete"]')).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="common.buttons.delete"]')).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="common.yes"]')).do()
