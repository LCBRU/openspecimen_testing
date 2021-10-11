from selenium_test_helper import ClickAction, EnsureAction, SelectAction, TypeInTextboxAction, XpathSelector
from function.cart import selectors, outputs
from open_specimen_tester import OpenSpecimenDestructiveTester


class CartTester(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper, selectors(helper.version), outputs(helper.compare_version))

        self.values = {
            'Name': TypeInTextboxAction(
                helper=self.helper,
                selector=self.selectors.edit_name_field_selector(),
                text='Fred',
            ),
            'Share': SelectAction(
                helper=self.helper,
                select_selector=self.selectors.edit_user_field_selector(),
                item_selector=self.selectors.edit_user_item_selector(),
            ),
            'Description': TypeInTextboxAction(
                helper=self.helper,
                selector=self.selectors.edit_description_field_selector(),
                text='Lorem Ipsum',
            ),
            'Specimens': TypeInTextboxAction(
                helper=self.helper,
                selector=self.selectors.edit_specimens_field_selector(),
                text='241996102950120',
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
        ClickAction(helper=self.helper, selector=self.selectors.function_more_selector()).do()
        ClickAction(helper=self.helper, selector=self.selectors.function_edit_selector()).do()
        ClickAction(helper=self.helper, selector=self.selectors.function_delete_selector()).do()
        ClickAction(helper=self.helper, selector=self.selectors.function_yes_selector()).do()
