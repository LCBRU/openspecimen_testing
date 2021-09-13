from time import sleep
from open_specimen_tester import OpenSpecimenNonDestructiveTester


class CartTester(OpenSpecimenNonDestructiveTester):
    VERSION_COLUMNS = {
        '5.0': ['Label', 'Type', 'Anatomic Site', 'Collection Protocol', 'Quantity', 'Lineage'],
    }

    def object_name(self):
        return 'cart'

    def function_page_url(self):
        return 'specimen-lists'

    def export_link_css_selector(self):
        return 'a[ui-sref="specimen-list({listId: list.id})"]'

    def item_page_loaded_css_selector(self):
        return 'span[translate="specimen_list.distribute_all"]'

    def visit_item(self, x):
        details = x.copy()

        self.goto_item_page(x)

        details['samples'] = self.helper.get_table_details(self.VERSION_COLUMNS[self.helper.compare_version])

        return details