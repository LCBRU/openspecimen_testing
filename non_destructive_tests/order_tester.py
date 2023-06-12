from lbrc_selenium.selenium import CssSelector, XpathSelector
from open_specimen_tester import OpenSpecimenNonDestructiveTester
from time import sleep


class OrderTester(OpenSpecimenNonDestructiveTester):
    VERSION_OVERVIEW_COLUMNS = {
        '5.0': ["Requestor", "Receiving Site", "Distribution Protocol", "Distributor", "Status", "Distribution Date", "Tracking URL", "Created By", "Created On"],
    }
    VERSION_SAMPLES_COLUMNS = {
        '5.1': ["Label", "Collection Protocol", "Quantity"], # v5.2 displays "Status" column as the literal name, not its value!
    }

    def object_name(self):
        return 'order'

    def function_page_url(self):
        return 'orders'

    def export_link_css_selector(self):
        return CssSelector('a[ui-sref="order-detail.overview({orderId: order.id})"]')

    def item_page_loaded_css_selector(self):
        return CssSelector('h3[translate="audit.activity"]')

    def visit_item(self, o):
        details = {}

        self.goto_item_page(o)

        details['overview'] = self.helper.get_overview_details(self.VERSION_OVERVIEW_COLUMNS.get(self.helper.compare_version, None))

        self.goto_item_sub_page(o, page_name='items', selector=XpathSelector('//span[normalize-space(text()) = normalize-space("Label")]'))

        details['items'] = self.helper.get_table_details(columns=self.VERSION_SAMPLES_COLUMNS.get(self.helper.compare_version, None), has_container=False)

        return details
