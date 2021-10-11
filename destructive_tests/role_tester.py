from function.role import RoleFunction
from open_specimen_tester import OpenSpecimenDestructiveTester
from selenium_test_helper import ClickAction, CssSelector, EnsureAction, SelectAction, TypeInTextboxAction, XpathSelector


class RoleTester(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper, RoleFunction())

        self.values = {
            'Title': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('input[ng-model="role.name"]'),
                text='Fred',
            ),
            'Resource': SelectAction(
                helper=self.helper,
                select_selector=CssSelector('div[placeholder="Resource"]'),
                item_selector=XpathSelector('//span[text()="Orders"]'),
            ),
        }

    def create_item(self):
        # No option to delete, so never save.

        self.goto_function_page()

        ClickAction(helper=self.helper, selector=self.function.create_button_selector()).do()
        EnsureAction(helper=self.helper, selector=self.function.create_page_loaded_selector()).do()

        for v in self.values.values():
            v.do()

        ClickAction(helper=self.helper, selector=CssSelector('button[translate="common.buttons.discard"]')).do()


    def validate_item(self):
        pass


    def cleanup_item(self):
        pass
