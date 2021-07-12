import logging
import jsonlines
from selenium.webdriver.common.by import By
from os_tester import OsTester


class DistributionProtocolTester(OsTester):
    EXPORT_FILENAME = 'distribution_protocol_export.jsonl'
    DETAILS_FILENAME = 'distribution_protocol_details.jsonl'

    def goto_function_page(self):
        self.get('#/dps')

    def goto_overview(self, dp):
        self.goto_function_page()
        self.get(dp['href'])
        self.get_element('button[ui-sref="dp-addedit({dpId: distributionProtocol.id})"]', By.CSS_SELECTOR)

    def goto_history(self, dp):
        self.goto_function_page()
        self.get(dp['href'].replace('overview', 'history'))
        self.get_element('span[translate="common.buttons.export"]', By.CSS_SELECTOR)

    def goto_requirements(self, dp):
        self.goto_function_page()
        self.get(dp['href'].replace('overview', 'requirements/list'))
        self.get_element('span[translate="common.buttons.add"]', By.CSS_SELECTOR)

    def goto_reserved(self, dp):
        self.goto_function_page()
        self.get(dp['href'].replace('overview', 'reserved-specimens'))
        self.get_element('span[translate="specimens.ppid"]', By.CSS_SELECTOR)

    def get_export(self):
        logging.info('Exporting Distribution Protocol')

        self.goto_function_page()

        with jsonlines.open(self._output_directory / self.EXPORT_FILENAME, mode='w') as writer:
            for x in self.get_elements('a[ui-sref="dp-detail.overview({dpId: dp.id})"]', By.CSS_SELECTOR):
                details = {
                    'name': self.get_text(x),
                    'href': self.get_href(x),
                }
                writer.write(details)

    def visit_distribution_protocols(self):
        logging.info('Visiting Distribution Protocols')

        with jsonlines.open(self._output_directory / self.DETAILS_FILENAME, mode='w') as writer:
            with jsonlines.open(self._output_directory / self.EXPORT_FILENAME) as reader:
                for i, dp in enumerate(reader):
                    if self.is_sampling_pick(i):
                        logging.info(f'Processing Distribution Protocol: {dp["name"]}')

                        dets = self.visit_distribution_protocol(dp)
                        writer.write(dets)
                    else:
                        logging.info(f'Skipping Distribution Protocol: {dp["name"]}')


    def visit_distribution_protocol(self, dp):
        details = {}

        self.goto_overview(dp)

        details['overview'] = self.get_overview_details()

        self.goto_history(dp)

        details['history'] = self.get_div_table_details()

        self.goto_requirements(dp)

        details['requirements'] = self.get_table_details()

        self.goto_reserved(dp)

        details['reserved'] = self.get_table_details()

        return details

    def run(self):
        self.get_export()
        self.visit_distribution_protocols()
