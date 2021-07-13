import logging
from re import L
from time import sleep
import jsonlines
from selenium.webdriver.common.by import By
from os_tester import OsTester


class CartTester(OsTester):
    EXPORT_FILENAME = 'cart_export.jsonl'
    DETAILS_FILENAME = 'cart_details.jsonl'

    def goto_function_page(self):
        self.get('#/specimen-lists')

    def goto_cart(self, dp):
        self.goto_function_page()
        self.get(dp['href'])
        sleep(1)
        self.get_element('span[translate="specimen_list.distribute_all"]', By.CSS_SELECTOR)

    def get_export(self):
        logging.info('Exporting')

        self.goto_function_page()

        with jsonlines.open(self._output_directory / self.EXPORT_FILENAME, mode='w') as writer:
            for x in self.get_elements('a[ui-sref="specimen-list({listId: list.id})"]', By.CSS_SELECTOR):
                details = {
                    'name': self.get_text(x),
                    'href': self.get_href(x),
                }
                writer.write(details)

    def visit_carts(self):
        logging.info('Visiting')

        with jsonlines.open(self._output_directory / self.DETAILS_FILENAME, mode='w') as writer:
            with jsonlines.open(self._output_directory / self.EXPORT_FILENAME) as reader:
                for i, f in enumerate(reader):
                    logging.info(f'Processing Cart: {f["name"]}')

                    dets = self.visit_cart(f)
                    writer.write(dets)

    def visit_cart(self, x):
        details = {}

        self.goto_cart(x)

        details['samples'] = self.get_table_details()

        return details

    def run(self):
        self.get_export()
        self.visit_carts()
