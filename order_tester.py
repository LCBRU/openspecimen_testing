import logging
import jsonlines
from selenium.webdriver.common.by import By
from os_tester import OsTester
from time import sleep

class OrderTester(OsTester):
    EXPORT_FILENAME = 'orders_export.jsonl'
    DETAILS_FILENAME = 'orders_details.jsonl'

    def goto_function_page(self):
        self.get('#/orders')

    def goto_overview(self, o):
        self.goto_function_page()
        self.get(o['href'])
        self.get_element('h3[translate="audit.activity"]', By.CSS_SELECTOR)

    def goto_items(self, o):
        self.goto_function_page()
        self.get(o['href'].replace('overview', 'items'))
        sleep(2)

    def get_export(self):
        logging.info('Exporting Orders')

        self.goto_function_page()

        with jsonlines.open(self._output_directory / self.EXPORT_FILENAME, mode='w') as writer:
            for x in self.get_elements('a[ui-sref="order-detail.overview({orderId: order.id})"]', By.CSS_SELECTOR):
                details = {
                    'name': self.get_text(x),
                    'href': self.get_href(x),
                }
                writer.write(details)

    def visit_orders(self):
        logging.info('Visiting Orders')

        with jsonlines.open(self._output_directory / self.DETAILS_FILENAME, mode='w') as writer:
            with jsonlines.open(self._output_directory / self.EXPORT_FILENAME) as reader:
                for i, o in enumerate(reader):
                    if self.is_sampling_pick(i):
                        logging.info(f'Processing Order: {o["name"]}')

                        dets = self.visit_order(o)
                        writer.write(dets)
                    else:
                        logging.info(f'Skipping Order: {o["name"]}')

    def visit_order(self, o):
        details = {}

        self.goto_overview(o)

        details['overview'] = self.get_overview_details()

        self.goto_items(o)

        details['items'] = self.get_table_details()

    def run(self):
        self.get_export()
        self.visit_orders()
