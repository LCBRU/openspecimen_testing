from open_specimen_tester import OpenSpecimenNonDestructiveTester


class DistributionProtocolTester(OpenSpecimenNonDestructiveTester):
    def object_name(self):
        return 'distribution_protocol'

    def function_page_url(self):
        return 'dps'

    def export_link_css_selector(self):
        return 'a[ui-sref="dp-detail.overview({dpId: dp.id})"]'

    def item_page_loaded_css_selector(self):
        return 'button[ui-sref="dp-addedit({dpId: distributionProtocol.id})"]'

    def visit_item(self, o):

        details = super().visit_item(o)

        self.goto_item_sub_page(o, 'history', 'span[translate="common.buttons.export"]')

        details['history'] = self.helper.get_div_table_details()

        self.goto_item_sub_page(o, 'requirements/list', 'span[translate="common.buttons.add"]')

        details['requirements'] = self.helper.get_table_details()

        self.goto_item_sub_page(o, 'reserved-specimens', 'span[translate="specimens.ppid"]')

        details['reserved'] = self.helper.get_table_details()

        return details
