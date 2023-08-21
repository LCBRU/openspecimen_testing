from lbrc_selenium.selenium import CssSelector
from open_specimen_tester import OpenSpecimenNonDestructiveTester, KeyValuePairScrubber, SeleniumHelper
from time import sleep
from packaging import version


class FormScrubber(KeyValuePairScrubber):
    def __init__(self, helper: SeleniumHelper) -> None:
        super().__init__(
            helper,
            parent_selector=CssSelector('div.form-canvas'),
            pair_selector=CssSelector('div.p-card-body'),
            key_selector=CssSelector('label'),
            value_selector=CssSelector('input, textarea'),
        )


class FormTester(OpenSpecimenNonDestructiveTester):
    VERSION_FORM_FIELD = {
        '5.0': CssSelector('div.form-group'),
        '10.0': CssSelector('div.p-field'),
    }

    def url_prefixes(self):
        return {
            '5.0': '#',
        }

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
        self.helper.get(self.translate_url(dp['href']))
        sleep(1)

        if version.parse(self.helper.version) < version.parse('10.0'):
            self.helper.driver.switch_to.frame(0)
            self.helper.click_element(CssSelector('div[tab_id="previewTab"]'))

    def visit_item(self, o):
        print(f"Processing form: {o['name']}")
        details = {}

        self.goto_preview(o)

        details['name'] = o['name']

        sleep(30)

        details['preview'] = FormScrubber(helper=self.helper).get_details()

        return details
