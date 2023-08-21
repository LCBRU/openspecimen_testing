from lbrc_selenium.selenium import CssSelector, XpathSelector, VersionTranslator
from open_specimen_tester import OpenSpecimenNonDestructiveTester, OSOverviewScrubber


class SiteTester(OpenSpecimenNonDestructiveTester):
    VERSION_EXPORT_LINK_SELECTOR = {
        '5.0': CssSelector('a[ui-sref="site-detail.overview({siteId: site.id})"]'),
        '10.0': CssSelector('a[href^="#/sites/"][href$="/overview"]'),
    }
    VERSION_LOADED_SELECTOR = {
        '5.0': CssSelector('span[translate="common.buttons.edit"]'),
        '10.0': XpathSelector('//button/span[contains(text(), "Edit")]'),
    }
    VERSION_OBJECT_NAMES = {
        '5.0': 'sites',
        '10.0': 'sites/-1',
    }

    def object_name(self):
        return 'site'

    def function_page_url(self):
        return self.helper.get_version_item(self.VERSION_OBJECT_NAMES)

    def export_link_css_selector(self):
        return self.helper.get_version_item(self.VERSION_EXPORT_LINK_SELECTOR)

    def item_page_loaded_css_selector(self):
        return self.helper.get_version_item(self.VERSION_LOADED_SELECTOR)

    def visit_item(self, o):
        vt: VersionTranslator = VersionTranslator()
        vt.set_columns_for_version('6.0', ['Institute', 'Code', 'Coordinators', 'Type'])
        vt.set_value_translators_for_version('6.0', {
            '-': 'Not Specified',
        })

        details = {}

        self.goto_item_page(o)

        details['overview'] = OSOverviewScrubber(helper=self.helper, version_comparator=vt).get_details()

        return details
