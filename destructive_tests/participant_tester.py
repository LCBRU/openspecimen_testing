from selenium_test_helper import ClickAction, CssSelector, EnsureAction, TypeInTextboxAction, XpathSelector
from time import sleep
from open_specimen_tester import OpenSpecimenDestructiveTester


def get_participant_standard_tester(helper):
    if helper.version >= '5.1':
        return ParticipantStandardTester_v5_1(helper)
    else:
        return ParticipantStandardTester_v5_0(helper)


def get_participant_brc_tester(helper):
    if helper.version >= '5.1':
        return ParticipantBrcTester_v5_1(helper)
    else:
        return ParticipantBrcTester_v5_0(helper)


class ParticipantStandardTester_v5_0(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return 'cps'

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
        self.goto_collection_protocol()

        sleep(15)

        self.helper.click_element_selector(self.create_button_selector())
        self.helper.get_element_selector(self.create_page_loaded_selector())

        self.helper.type_in_textbox_selector(CssSelector('input[placeholder="Participant Protocol ID"]'), 'Fred')

        self.helper.click_element_selector(self.create_page_create_selector())
        self.helper.get_element_selector(self.item_title_selector())


    def validate_item(self):
        self.goto_collection_protocol()

        sleep(15)

        self.helper.get_element_selector(self.item_title_selector())


    def cleanup_item(self):
        self.goto_collection_protocol()

        self.helper.click_element_selector(self.item_title_selector())

        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.delete"]'))
        self.helper.click_element_selector(CssSelector('span[translate="common.yes"]'))


    def goto_collection_protocol(self):
        self.goto_function_page()

        sleep(15)

        self.helper.click_element_selector(self.cp_title_selector())


class ParticipantStandardTester_v5_1(ParticipantStandardTester_v5_0):
    def cleanup_item(self):
        self.goto_collection_protocol()

        self.helper.click_element_selector(self.item_title_selector())

        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.delete"]'))
        self.helper.type_in_textbox_selector(CssSelector('textarea[ng-model="entityProps.reason"]'), 'Tiny creepy monsters')
        self.helper.click_element_selector(CssSelector('span[translate="common.yes"]'))


class ParticipantBrcTester_v5_0(OpenSpecimenDestructiveTester):
    def __init__(self, helper):
        super().__init__(helper)

    def function_page_url(self):
        return 'cps'

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

        self.helper.click_element_selector(self.create_button_selector())
        self.helper.get_element_selector(self.create_page_loaded_selector())
        self.helper.click_element_selector(self.create_page_create_selector())

        self.helper.type_in_textbox_selector(CssSelector('input[name="empi"]'), 'Fred')
        self.helper.type_in_textbox_selector(CssSelector('input[name="ppid"]'), 'Bav99999')
        self.helper.type_in_textbox_selector(CssSelector('input[name="regDate"]'), '01 Aug 2020')

        self.helper.click_element_selector(XpathSelector('//span[text()="Register"]'))
        self.helper.get_element_selector(XpathSelector('//h3[text()="Collect Primary Specimens"]'))

    def validate_item(self):
        self.goto_collection_protocol()

        sleep(15)

        self.helper.get_element_selector(self.item_title_selector())

    def cleanup_item(self):
        self.goto_collection_protocol()

        self.helper.click_element_selector(self.item_title_selector())
        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.delete"]'))
        self.helper.click_element_selector(CssSelector('span[translate="common.yes"]'))

    def goto_collection_protocol(self):
        self.goto_function_page()

        sleep(15)

        self.helper.click_element_selector(self.cp_title_selector())


class ParticipantBrcTester_v5_1(ParticipantBrcTester_v5_0):
    def cleanup_item(self):
        self.goto_collection_protocol()

        self.helper.click_element_selector(self.item_title_selector())

        self.helper.click_element_selector(CssSelector('span[translate="common.buttons.delete"]'))
        self.helper.type_in_textbox_selector(CssSelector('textarea[ng-model="entityProps.reason"]'), 'Tiny creepy monsters')
        self.helper.click_element_selector(CssSelector('span[translate="common.yes"]'))

