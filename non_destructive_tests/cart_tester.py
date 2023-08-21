from lbrc_selenium.selenium import CssSelector, XpathSelector, VersionTranslator
from open_specimen_tester import OpenSpecimenNonDestructiveTester, OSTableScrubberNew, PDataTableScrubberNew


class CartTester(OpenSpecimenNonDestructiveTester):
    VERSION_TABLE_SCRUBBER = {
        '5.0': OSTableScrubberNew,
        '10.0': PDataTableScrubberNew,
    }
    VERSION_EXPORT_LINK_SELECTOR = {
        '5.0': CssSelector('a[ui-sref="specimen-list({listId: list.id})"]'),
        '10.0': CssSelector('a[href^="#/carts/"][href$="/specimens"]'),
    }
    VERSION_LOADED_SELECTOR = {
        '5.0': CssSelector('span[translate="specimen_list.distribute_all"]'),
        '10.0': XpathSelector('//button/span[contains(text(), "Actions")]'),
    }
    VERSION_FUNCTION_NAMES = {
        '5.0': 'specimen-lists',
        '10.0': 'carts/-1',
    }
    def object_name(self):
        return 'cart'

    def function_page_url(self):
        return self.helper.get_version_item(self.VERSION_FUNCTION_NAMES)

    def export_link_css_selector(self):
        return self.helper.get_version_item(self.VERSION_EXPORT_LINK_SELECTOR)

    def item_page_loaded_css_selector(self):
        return self.helper.get_version_item(self.VERSION_LOADED_SELECTOR)

    def visit_item(self, x):
        details = x.copy()

        self.goto_item_page(x)

        vt: VersionTranslator = VersionTranslator()
        vt.set_label_translators_for_version('5.0', ['Label', 'Type', 'Anatomic Site', 'Collection Protocol', 'Quantity', 'Lineage'])

        table_scrubber = self.helper.get_version_item(self.VERSION_TABLE_SCRUBBER)(
            helper=self.helper,
            version_comparator=vt,
        )

        details['samples'] = table_scrubber.get_details()

        return details
