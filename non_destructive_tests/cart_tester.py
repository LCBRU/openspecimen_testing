from lbrc_selenium.selenium import CssSelector
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
        return CssSelector('a[ui-sref="specimen-list({listId: list.id})"]')

    def item_page_loaded_css_selector(self):
        return CssSelector('span[translate="specimen_list.distribute_all"]')

    def visit_item(self, x):
        details = x.copy()

        self.goto_item_page(x)

        details['samples'] = self.helper.get_table_details(self.VERSION_COLUMNS.get(self.helper.compare_version, None))

        return details
