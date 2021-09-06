from selenium.webdriver.common.by import By
from open_specimen_tester import OpenSpecimenDestructiveTester


class CartTester(OpenSpecimenDestructiveTester):
    def object_name(self):
        return 'cart'

    def function_page_url(self):
        return 'specimen-lists'

    def item_page_loaded_css_selector(self):
        return 'span[translate="specimen_list.distribute_all"]'

    def create_button_css_selector(self):
        return 'span[translate="common.buttons.create"]'

    def create_page_loaded_css_selector(self):
        return 'span[translate="specimen_list.create_list"]'

    def create_page_create_css_selector(self):
        return 'span[translate="common.buttons.create"]'

    def item_title_css_selector(self):
        return 'span[title="Fred"]'

    values = {
            'Name': {
                'query': 'input[ng-model="list.name"]',
                'by': By.CSS_SELECTOR,
                'value': 'Fred',
                'type': 'type',
            },
            'Share': {
                'select_query': 'input[placeholder="Users"]',
                'select_by': By.CSS_SELECTOR,
                'item_query': '//span[text()="Bramley, Richard"]',
                'item_by': By.XPATH,
                'type': 'select',
            },
            'Description': {
                'query': 'textarea[ng-model="list.description"]',
                'by': By.CSS_SELECTOR,
                'value': 'Lorem Ipsum', 
                'type': 'type',
            },
            'Specimens': {
                'query': 'textarea[ng-model="input.labelText"]',
                'by': By.CSS_SELECTOR,
                'value': '241996102950120', 
                'type': 'type',

            },
        }

    def create_item(self):
        self.goto_function_page()

        self.helper.click_element(self.create_button_css_selector(), By.CSS_SELECTOR)
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
            by=By.CSS_SELECTOR,
        )


    def validate_item(self):
        self.goto_function_page()

        self.helper.get_element(
            query=self.item_title_css_selector(),
            by=By.CSS_SELECTOR,
        )


    def cleanup_item(self):
        self.goto_function_page()

        self.helper.click_element(
            query=self.item_title_css_selector(),
            by=By.CSS_SELECTOR,
        )

        self.helper.click_element(
            query='span[translate="common.buttons.more"]',
            by=By.CSS_SELECTOR,
        )

        self.helper.click_element(
            query='span[translate="specimen_list.edit_or_delete"]',
            by=By.CSS_SELECTOR,
        )

        self.helper.click_element(
            query='span[translate="common.buttons.delete"]',
            by=By.CSS_SELECTOR,
        )

        self.helper.click_element(
            query='span[translate="common.yes"]',
            by=By.CSS_SELECTOR,
        )
