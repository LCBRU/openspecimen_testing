from lbrc_selenium.selenium import CssSelector, XpathSelector, VersionTranslator
from open_specimen_tester import OpenSpecimenNonDestructiveTester, OSOverviewScrubber, get_versioned_table_scrubber


class DistributionProtocolTester(OpenSpecimenNonDestructiveTester):
    CV_RESERVERD_SPECIMEN = {
        '5.0': 'span[translate="specimens.ppid"]',
        '5.1': 'span[translate="dp.distribute_all"]',
    }
    VERSION_EXPORT_LINK_SELECTOR = {
        '5.0': CssSelector('a[ui-sref="dp-detail.overview({dpId: dp.id})"]'),
        '10.0': CssSelector('a[href^="#/dps/"][href$="/overview"]'),
    }
    VERSION_LOADED_SELECTOR = {
        '5.0': CssSelector('button[ui-sref="dp-addedit({dpId: distributionProtocol.id})"]'),
        '10.0': XpathSelector('//button/span[contains(text(), "Edit")]'),
    }
    VERSION_ADD_SELECTOR = {
        '5.0': CssSelector('span[translate="common.buttons.add"]'),
        '10.0': XpathSelector('//button/span[contains(text(), "Add")]'),
    }
    VERSION_FUNCTION_PAGE_NAME = {
        '5.0': 'dps',
        '10.0': 'dps/-1',
    }

    def object_name(self):
        return 'distribution_protocol'

    def function_page_url(self):
        return self.helper.get_version_item(self.VERSION_FUNCTION_PAGE_NAME)

    def export_link_css_selector(self):
        return self.helper.get_version_item(self.VERSION_EXPORT_LINK_SELECTOR)

    def item_page_loaded_css_selector(self):
        return self.helper.get_version_item(self.VERSION_LOADED_SELECTOR)

    def visit_item(self, o):

        details = {}

        self.goto_item_page(o)

        vt: VersionTranslator = VersionTranslator()
        vt.set_columns_for_version(
            '5.0', ["Title", "Short Title", "Receiving Institute", "Receiving Site", "Principal Investigator", "Start Date", "End Date", "Ethics ID", "Order Custom Fields", "Order Report Query", "Created By", "Created On"],
        )
        vt.set_value_translators_for_version('6.0', {
            '-': 'Not Specified',
        })
        
        details['overview'] = OSOverviewScrubber(helper=self.helper, version_comparator=vt).get_details()

        self.goto_item_sub_page(o, 'requirements/list', self.helper.get_version_item(self.VERSION_ADD_SELECTOR))

        details['requirements'] = get_versioned_table_scrubber(helper=self.helper).get_details()

        return details
