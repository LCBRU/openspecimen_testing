import time
from lbrc_selenium.selenium import CssSelector, XpathSelector, KeyValuePairScrubber, SeleniumHelper
from open_specimen_tester import OpenSpecimenNonDestructiveTester


class QueryResultsScrubber(KeyValuePairScrubber):
    def __init__(self, helper: SeleniumHelper) -> None:
        super().__init__(
            helper,
            parent_selector=CssSelector('form'),
            pair_selector=CssSelector('div.form-group'),
            key_selector=CssSelector('label'),
            value_selector=CssSelector('input, textarea'),
        )


class JobTester(OpenSpecimenNonDestructiveTester):
    VERSION_EXPORT_LINK_SELECTOR = {
        '5.0': XpathSelector('//a[starts-with(@href,"#/job-addedit/") and contains(span/text(), "Edit")]'),
    }
    VERSION_LOADED_SELECTOR = {
        '5.0': CssSelector('span[translate="common.buttons.update"]'),
    }

    def url_prefixes(self):
        return {
            '5.0': '#',
        }
        
    def object_name(self):
        return 'job'

    def function_page_url(self):
        return 'jobs'

    def export_link_css_selector(self):
        time.sleep(4)
        return self.helper.get_version_item(self.VERSION_EXPORT_LINK_SELECTOR)

    def item_page_loaded_css_selector(self):
        return self.helper.get_version_item(self.VERSION_LOADED_SELECTOR)

    def visit_item(self, o):
        details = {}

        self.goto_item_page(o)

        details['form'] = QueryResultsScrubber(helper=self.helper).get_details()

        return details
