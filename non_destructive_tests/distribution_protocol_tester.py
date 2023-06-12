from lbrc_selenium.selenium import CssSelector
from open_specimen_tester import OpenSpecimenNonDestructiveTester


class DistributionProtocolTester(OpenSpecimenNonDestructiveTester):
    VERSION_COLUMNS = {
        '5.0': ["Title", "Short Title", "Receiving Institute", "Receiving Site", "Principal Investigator", "Start Date", "End Date", "Ethics ID", "Order Custom Fields", "Order Report Query", "Created By", "Created On"],
    }
    CV_RESERVERD_SPECIMEN = {
        '5.0': 'span[translate="specimens.ppid"]',
        '5.1': 'span[translate="dp.distribute_all"]',
    }

    def object_name(self):
        return 'distribution_protocol'

    def function_page_url(self):
        return 'dps'

    def export_link_css_selector(self):
        return CssSelector('a[ui-sref="dp-detail.overview({dpId: dp.id})"]')

    def item_page_loaded_css_selector(self):
        return CssSelector('button[ui-sref="dp-addedit({dpId: distributionProtocol.id})"]')

    def visit_item(self, o):

        details = {}

        self.goto_item_page(o)

        details['overview'] = self.helper.get_overview_details(self.VERSION_COLUMNS.get(self.helper.compare_version, None))

        self.goto_item_sub_page(o, 'history', CssSelector('span[translate="common.buttons.export"]'))

        details['history'] = self.helper.get_div_table_details()

        self.goto_item_sub_page(o, 'requirements/list', CssSelector('span[translate="common.buttons.add"]'))

        details['requirements'] = self.helper.get_table_details()

        reserved_specimen = self.helper.get_compare_version_item(self.CV_RESERVERD_SPECIMEN)

        self.goto_item_sub_page(o, 'reserved-specimens', CssSelector(reserved_specimen))

        details['reserved'] = self.helper.get_table_details()

        return details
