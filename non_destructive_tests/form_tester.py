from lbrc_selenium.selenium import CssSelector
from open_specimen_tester import OpenSpecimenNonDestructiveTester
from time import sleep


class FormTester(OpenSpecimenNonDestructiveTester):
    def object_name(self):
        return 'form'

    def function_page_url(self):
        return 'forms'

    def export_link_css_selector(self):
        return CssSelector('a[ui-sref="form-addedit({formId: form.formId})"]')

    def item_page_loaded_css_selector(self):
        return CssSelector('')

    def goto_preview(self, dp):
        self.goto_function_page()
        self.helper.get(dp['href'])
        sleep(1)
        self.helper.driver.switch_to.frame(0)
        self.helper.click_element(CssSelector('div[tab_id="previewTab"]'))

    def visit_item(self, o):
        details = {}

        self.goto_preview(o)

        details['name'] = o['name']

        sleep(30)

        details['preview'] = self.get_form_preview()

        return details

    def get_form_preview(self):
        result = []

        for row in self.helper.get_elements(CssSelector('div.form-group')):
            details = {}

            details['control'] = self.helper.get_innerHtml(row)

            result.append(details)

        return result
