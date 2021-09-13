from open_specimen_tester import OpenSpecimenNonDestructiveTester
from time import sleep


class OrderTester(OpenSpecimenNonDestructiveTester):
    VERSION_COLUMNS = {
        '5.0': ["Requestor", "Receiving Site", "Distribution Protocol", "Distributor", "Status", "Distribution Date", "Tracking URL", "Created By", "Created On"],
    }

    def object_name(self):
        return 'order'

    def function_page_url(self):
        return 'orders'

    def export_link_css_selector(self):
        return 'a[ui-sref="order-detail.overview({orderId: order.id})"]'

    def item_page_loaded_css_selector(self):
        return 'h3[translate="audit.activity"]'

    def visit_item(self, o):
        details = {}

        self.goto_item_page(o)

        details['overview'] = self.helper.get_overview_details(self.VERSION_COLUMNS[self.helper.compare_version])

        self.goto_item_sub_page(o, page_name='items', loaded_css_selector='span[translate="orders.spec.label"]')

        details['items'] = self.helper.get_table_details()

        return details
