from time import sleep
from selenium.webdriver.common.by import By
from open_specimen_tester import OpenSpecimenDestructiveTester


class CollectionProtocolTester(OpenSpecimenDestructiveTester):
    def object_name(self):
        return 'collection_protocol'

    def function_page_url(self):
        return 'cps'

    def item_page_loaded_css_selector(self):
        return 'span[translate="cp.view_specimens"]'

    def create_button_css_selector(self):
        return 'button[title="Click to add new Collection Protocol"]'

    def create_link_css_selector(self):
        return 'a > span[translate="common.buttons.create"]'

    def create_page_loaded_css_selector(self):
        return 'span[translate="cp.create_cp_title"]'

    def create_page_create_css_selector(self):
        return 'span[translate="common.buttons.create"]'

    def item_title_css_selector(self):
        return '//span[text()="Fred"]'

    values = {
            'Sites': {
                'select_query': 'input[placeholder="Sites"]',
                'select_by': By.CSS_SELECTOR,
                'item_query': '//span[text()="Glenfield Hospital"]',
                'item_by': By.XPATH,
                'type': 'select',
            },
            'Title': {
                'query': 'input[placeholder="Title"]',
                'by': By.CSS_SELECTOR,
                'value': 'Frederick',
                'type': 'type',
            },
            'Short Title': {
                'query': 'input[placeholder="Short Title"]',
                'by': By.CSS_SELECTOR,
                'value': 'Fred',
                'type': 'type',
            },
            'PI': {
                'select_query': 'div[placeholder="Principal Investigator"]',
                'select_by': By.CSS_SELECTOR,
                'item_query': '//span[text()="Adlam, Dave"]',
                'item_by': By.XPATH,
                'type': 'select',
            },
            'PC': {
                'select_query': 'div[placeholder="Protocol Coordinators"]',
                'select_by': By.CSS_SELECTOR,
                'item_query': '//span[text()="Abanto, Camille"]',
                'item_by': By.XPATH,
                'type': 'select',
            },
            'Start Date': {
                'query': 'input[placeholder="Start Date"]',
                'by': By.CSS_SELECTOR,
                'value': '01-01-2020',
                'type': 'type',
            },
            'End Date': {
                'query': 'input[placeholder="End Date"]',
                'by': By.CSS_SELECTOR,
                'value': '01-01-2030',
                'type': 'type',
            },
            'Ethics ID': {
                'query': 'input[placeholder="Ethics ID"]',
                'by': By.CSS_SELECTOR,
                'value': 'FR1-1',
                'type': 'type',
            },
            'Type': {
                'query': 'input[translate="cp.participant_centric"]',
                'by': By.CSS_SELECTOR,
                'type': 'radio',
            },
            'Participant Count': {
                'query': 'input[placeholder="Anticipated Participants Count"]',
                'by': By.CSS_SELECTOR,
                'value': '12345',
                'type': 'type',
            },
        }

    def create_item(self):
        self.create_collection_protocol()


    def create_collection_protocol(self):
        self.goto_function_page()

        sleep(15)

        self.helper.click_element(self.create_button_css_selector(), By.CSS_SELECTOR)

        sleep(1)

        self.helper.click_element(self.create_link_css_selector(), By.CSS_SELECTOR)

        self.helper.get_element(self.create_page_loaded_css_selector(), By.CSS_SELECTOR)

        for name, details in self.values.items():
            if details['type'] == 'type':
                self.helper.type_in_textbox(
                    query=details['query'],
                    by=details['by'],
                    text=details['value'],
                )
            elif details['type'] == 'select':
                self.helper.click_element(
                    query=details['select_query'],
                    by=details['select_by'],
                )
                self.helper.click_element(
                    query=details['item_query'],
                    by=details['item_by'],
                )

        self.helper.click_element(
            query=self.create_page_create_css_selector(),
            by=By.CSS_SELECTOR,
        )

        self.helper.get_element(
            query=self.item_title_css_selector(),
            by=By.XPATH,
        )


    def validate_item(self):
        self.goto_function_page()

        sleep(15)

        self.helper.get_element(
            query=self.item_title_css_selector(),
            by=By.XPATH,
        )


    def cleanup_item(self):
        return

        self.goto_collection_protocol()

        self.helper.click_element(
            query='span[translate="cp.menu_options.delete"]',
            by=By.CSS_SELECTOR,
        )

        self.helper.click_element(
            query='span[translate="common.yes"]',
            by=By.CSS_SELECTOR,
        )


    def goto_collection_protocol(self):
        self.goto_function_page()

        sleep(15)

        self.helper.click_element(
            query=self.item_title_css_selector(),
            by=By.XPATH,
        )

        self.helper.click_element(
            query='span[translate="common.buttons.more"]',
            by=By.CSS_SELECTOR,
        )

        self.helper.click_element(
            query='span[translate="cp.view_details"]',
            by=By.CSS_SELECTOR,
        )
