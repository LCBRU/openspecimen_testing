from selenium_test_helper import ClickAction, CssSelector, EnsureAction, TypeInTextboxAction, XpathSelector
from time import sleep
from open_specimen_tester import OpenSpecimenDestructiveTester
from function.participant import ParticipantFunction


class ParticipantStandardTester(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper, ParticipantFunction())

        self.values = {
            'Participant Protocol ID': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('input[placeholder="Participant Protocol ID"]'),
                text='Fred',
            ),
        }

    def item_title_selector(self):
        return XpathSelector('//span[normalize-space(text())="Fred"]')

    def create_page_loaded_selector(self):
        return CssSelector('span[translate="participant.register_participant"]')

    def create_button_selector(self):
        return CssSelector('span[translate="participant.buttons.register"]')

    def create_page_create_selector(self):
        return CssSelector('span[translate="participant.buttons.register"]')

    def cp_title_selector(self):
        return XpathSelector('//span[text()="CHINOOK"]')

    def create_item(self):
        self.create_participant()

    def create_participant(self):
        self.goto_collection_protocol()

        sleep(15)

        ClickAction(helper=self.helper, selector=self.create_button_selector()).do()
        EnsureAction(helper=self.helper, selector=self.create_page_loaded_selector()).do()

        for v in self.values.values():
            v.do()

        ClickAction(helper=self.helper, selector=self.create_page_create_selector()).do()
        EnsureAction(helper=self.helper, selector=self.item_title_selector()).do()


    def validate_item(self):
        self.goto_collection_protocol()

        sleep(15)

        EnsureAction(helper=self.helper, selector=self.item_title_selector()).do()


    def cleanup_item(self):
        self.goto_collection_protocol()

        ClickAction(helper=self.helper, selector=self.item_title_selector()).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="common.buttons.delete"]')).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="common.yes"]')).do()


    def goto_collection_protocol(self):
        self.goto_function_page()

        sleep(15)

        ClickAction(helper=self.helper, selector=self.cp_title_selector()).do()


class ParticipantBrcTester(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper, ParticipantFunction())

        self.values = {
            'Participant ID': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('input[name="empi"]'),
                text='Fred',
            ),
            'Participant Protocol ID': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('input[name="ppid"]'),
                text='Bav99999',
            ),
            'Registration Date': TypeInTextboxAction(
                helper=self.helper,
                selector=CssSelector('input[name="regDate"]'),
                text='01 Aug 2020',
            ),
        }

    def item_title_selector(self):
        return XpathSelector('//span[normalize-space(text())="Bav99999"]')

    def create_page_loaded_selector(self):
        return XpathSelector('//h3[text()="Register Participants"]')

    def create_button_selector(self):
        return CssSelector('span[translate="participant.buttons.register"]')

    def create_page_create_selector(self):
        return XpathSelector('//span[text()="Add Participant"]')

    def cp_title_selector(self):
        return XpathSelector('//span[text()="BRAVE"]')

    def create_item(self):
        self.create_participant()

    def create_participant(self):
        self.goto_collection_protocol()

        sleep(15)

        ClickAction(helper=self.helper, selector=self.create_button_selector()).do()
        EnsureAction(helper=self.helper, selector=self.create_page_loaded_selector()).do()
        ClickAction(helper=self.helper, selector=self.create_page_create_selector()).do()

        for v in self.values.values():
            v.do()

        ClickAction(helper=self.helper, selector=self.function.create_page_register_selector()).do()
        EnsureAction(helper=self.helper, selector=self.function.collect_samples_page_loaded_selector()).do()


    def validate_item(self):
        self.goto_collection_protocol()

        sleep(15)

        EnsureAction(helper=self.helper, selector=self.item_title_selector()).do()


    def cleanup_item(self):
        self.goto_collection_protocol()

        ClickAction(helper=self.helper, selector=self.item_title_selector()).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="common.buttons.delete"]')).do()
        ClickAction(helper=self.helper, selector=CssSelector('span[translate="common.yes"]')).do()


    def goto_collection_protocol(self):
        self.goto_function_page()

        sleep(15)

        ClickAction(helper=self.helper, selector=self.cp_title_selector()).do()
