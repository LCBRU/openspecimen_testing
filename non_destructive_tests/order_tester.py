from lbrc_selenium.selenium import CssSelector, XpathSelector, VersionTranslator, TableScrubber
from open_specimen_tester import OpenSpecimenNonDestructiveTester, OSOverviewScrubber


class OrderTester(OpenSpecimenNonDestructiveTester):
    VERSION_EXPORT_LINK_SELECTOR = {
        '5.0': CssSelector('a[ui-sref="order-detail.overview({orderId: order.id})"]'),
        '10.0': CssSelector('a[href^="#/orders/"][href$="/overview"]'),
    }
    VERSION_LOADED_SELECTOR = {
        '5.0': CssSelector('strong[translate="orders.requestor"]'),
        '10.0': XpathSelector('//button/span[contains(text(), "Download Report")]'),
    }
    VERSION_SPECIMENS_LOADED_SELECTOR = {
        '5.0': CssSelector('span[translate="list_pager.showing"]'),
        '10.0': XpathSelector('//span[normalize-space(text()) = normalize-space("Label")]'),
    }
    VERSION_SPECIMENS_PAGE_NAME = {
        '5.0': 'items',
        '10.0': 'specimens',
    }
    VERSION_FUNCTION_PAGE_NAME = {
        '5.0': 'orders',
        '10.0': 'orders/-1',
    }

    def object_name(self):
        return 'order'

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
        vt.set_columns_for_version('5.0', ["Requestor", "Receiving Site", "Distribution Protocol", "Distributor", "Status", "Distribution Date", "Tracking URL", "Created By", "Created On"])
        
        details['overview'] = OSOverviewScrubber(helper=self.helper, version_comparator=vt).get_details()

        self.goto_item_sub_page(
            o,
            page_name=self.helper.get_version_item(self.VERSION_SPECIMENS_PAGE_NAME),
            selector=self.helper.get_version_item(self.VERSION_SPECIMENS_LOADED_SELECTOR),
        )

        VERSION_SPECIMEN_PARENT_SELECTOR = {
            '5.0': CssSelector('div.os-detail-sublist'),
            '10.0': CssSelector('div.results'),
        }

        vt: VersionTranslator = VersionTranslator()
        vt.set_columns_for_version('5.1', ["Label", "Collection Protocol", "Quantity"])
        
        details['items'] = TableScrubber(helper=self.helper, version_comparator=vt, parent_selector=self.helper.get_version_item(VERSION_SPECIMEN_PARENT_SELECTOR)).get_details()

        return details
