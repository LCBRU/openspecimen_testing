import logging
import jsonlines
from selenium.webdriver.common.by import By
from os_tester import OsTester


class JobTester(OsTester):
    EXPORT_FILENAME = 'job_export.jsonl'

    def goto_function_page(self):
        self.get('#/jobs')

    def get_export(self):
        logging.info('Exporting Jobs')

        self.goto_function_page()

        with jsonlines.open(self._output_directory / self.EXPORT_FILENAME, mode='w') as writer:
            for x in self.get_elements('a[ng-click="executeJob(job)"] span', By.CSS_SELECTOR):
                details = {
                    'name': self.get_innerHtml(x),
                }
                writer.write(details)

    def run(self):
        self.get_export()
