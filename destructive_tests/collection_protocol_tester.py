from selenium_test_helper import ClickAction, CssSelector, EnsureAction, SelectAction, TypeInTextboxAction, XpathSelector
from function.collection_protocol import CollectionProtocolFunction
from time import sleep
from selenium.webdriver.common.by import By
from open_specimen_tester import OpenSpecimenDestructiveTester


class CollectionProtocolTester(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper, CollectionProtocolFunction())

        self.values = {
            'Sites': SelectAction(
                helper=self.helper,
                select_selector=CssSelector('input[placeholder="Sites"]'),
                item_selector=XpathSelector('//span[text()="Glenfield Hospital"]'),
            ),
            'Title': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('input[placeholder="Title"]'),
                text='Frederick',
            ),
            'Short Title': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('input[placeholder="Short Title"]'),
                text='Fred',
            ),
            'PI': SelectAction(
                helper=self.helper,
                select_selector=CssSelector('div[placeholder="Principal Investigator"]'),
                item_selector=XpathSelector('//span[text()="Adlam, Dave"]'),
            ),
            'PC': SelectAction(
                helper=self.helper,
                select_selector=CssSelector('div[placeholder="Protocol Coordinators"]'),
                item_selector=XpathSelector('//span[text()="Abanto, Camille"]'),
            ),
            'Start Date': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('input[placeholder="Start Date"]'),
                text='01-01-2020',
            ),
            'End Date': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('input[placeholder="End Date"]'),
                text='01-01-2030',
            ),
            'Ethics ID': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('input[placeholder="Ethics ID"]'),
                text='FR1-1',
            ),
            'Type': ClickAction(
                helper=self.helper,
                selector=CssSelector('span[translate="cp.participant_centric"]'),
            ),
            'Participant Count': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('input[placeholder="Anticipated Participants Count"]'),
                text='12345',
            ),
        }

    def create_item(self):
        self.create_collection_protocol()


    def create_collection_protocol(self):
        self.goto_function_page()

        sleep(15)

        ClickAction(helper=self.helper, selector=self.function.create_button_selector()).do()

        sleep(1)

        ClickAction(helper=self.helper, selector=self.function.create_link_selector()).do()
        EnsureAction(helper=self.helper, selector=self.function.create_page_loaded_selector()).do()

        for v in self.values.values():
            v.do()

        ClickAction(helper=self.helper, selector=self.function.create_page_create_selector()).do()
        EnsureAction(helper=self.helper, selector=self.function.item_title_selector()).do()


    def validate_item(self):
        self.goto_function_page()

        sleep(15)

        EnsureAction(helper=self.helper, selector=self.function.item_title_selector()).do()


    def cleanup_item(self):
        self.goto_collection_protocol()

        ClickAction(helper=self.helper, selector=CssSelector('span[translate="cp.menu_options.delete"]')).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="common.yes"]')).do()


    def goto_collection_protocol(self):
        self.goto_function_page()

        sleep(15)

        ClickAction(helper=self.helper, selector=self.function.item_title_selector()).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="common.buttons.more"]')).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="cp.view_details"]')).do()
