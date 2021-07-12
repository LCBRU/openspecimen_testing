import logging
from re import L
from time import sleep
import jsonlines
from selenium.webdriver.common.by import By
from os_tester import OsTester


class FormTester(OsTester):
    EXPORT_FILENAME = 'form_export.jsonl'
    DETAILS_FILENAME = 'form_details.jsonl'

    def goto_function_page(self):
        self.get('#/forms')

    def goto_preview(self, dp):
        self.goto_function_page()
        self.get(dp['href'])
        sleep(1)
        self.driver.switch_to_frame(0)
        self.click_element('div[tab_id="previewTab"]', By.CSS_SELECTOR)

    def get_export(self):
        logging.info('Exporting Form')

        self.goto_function_page()

        with jsonlines.open(self._output_directory / self.EXPORT_FILENAME, mode='w') as writer:
            for x in self.get_elements('a[ui-sref="form-addedit({formId: form.formId})"]', By.CSS_SELECTOR):
                details = {
                    'name': self.get_text(x),
                    'href': self.get_href(x),
                }
                writer.write(details)

    def visit_forms(self):
        logging.info('Visiting Forms')

        with jsonlines.open(self._output_directory / self.DETAILS_FILENAME, mode='w') as writer:
            with jsonlines.open(self._output_directory / self.EXPORT_FILENAME) as reader:
                for i, f in enumerate(reader):
                    logging.info(f'Processing Form: {f["name"]}')

                    dets = self.visit_form(f)
                    writer.write(dets)

    def visit_form(self, dp):
        details = {}

        self.goto_preview(dp)

        details['preview'] = self.get_form_preview()

        return details

    def get_form_preview(self):
        result = []

        for row in self.get_elements('div.form-group', By.CSS_SELECTOR):
            details = {}

            l = row.find_element(By.CSS_SELECTOR, 'label')
            c = row.find_element(By.CSS_SELECTOR, 'div')

            details['label'] = self.get_innerHtml(l)
            details['control'] = self.get_innerHtml(c)

            result.append(details)

        return result

    def run(self):
        self.get_export()
        self.visit_forms()
