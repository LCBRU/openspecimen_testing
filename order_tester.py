from open_specimen_tester import OpenSpecimenTester
from time import sleep


class OrderTester(OpenSpecimenTester):
    def object_name(self):
        return 'order'

    def function_page_url(self):
        return 'orders'

    def export_link_css_selector(self):
        return 'a[ui-sref="order-detail.overview({orderId: order.id})"]'

    def item_page_loaded_css_selector(self):
        return 'h3[translate="audit.activity"]'

    def visit_item(self, o):
        details = super().visit_item(o)

        self.goto_item_sub_page(o, page_name='items', loaded_css_selector='span[translate="orders.spec.label"]')
        sleep(2)

        details['items'] = self.helper.get_table_details()

        return details
