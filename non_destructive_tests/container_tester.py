from lbrc_selenium.selenium import CssSelector, XpathSelector, SeleniumHelper, VersionTranslator, ListScrubber
from open_specimen_tester import OpenSpecimenNonDestructiveTester, PDataTableScrubberNew, OSTableScrubberNew, OSOverviewScrubber


class SpecimenTableScrubberOld(OSTableScrubberNew):
    def __init__(self, helper: SeleniumHelper) -> None:
        super().__init__(helper)
        self.parent_selector=CssSelector('div.container table.os-table')


class ContainerTester(OpenSpecimenNonDestructiveTester):
    VERSION_EXPORT_LINK_SELECTOR = {
        '5.0': CssSelector('a[ui-sref="container-detail.locations({containerId: container.id})"]'),
        '10.0': CssSelector('a[href^="#/containers/"][href$="/detail/overview"]'),
    }
    VERSION_LOADED_SELECTOR = {
        '5.0': CssSelector('table.os-container-map'),
        '10.0': XpathSelector('//button/span[contains(text(), "Edit")]'),
    }
    VERSION_OVERVIEW_LOADED_SELECTOR = {
        '5.0': CssSelector('span[translate="container.replicate"]'),
        '10.0': XpathSelector('//button/span[contains(text(), "Edit")]'),
    }
    VERSION_SPECIMENS_LOADED_SELECTOR = {
        '5.0': CssSelector('span[translate="common.buttons.download_report"]'),
        '10.0': XpathSelector('//button/span[contains(text(), "Download Report")]'),
    }
    VERSION_ROWS_PARENT_SELECTOR = {
        '5.0': CssSelector('div.panel'),
        '10.0': CssSelector('div.p-tree'),
    }
    VERSION_ROWS_VALUE_SELECTOR = {
        '5.0': CssSelector('a[ng-click="selectContainer(container)"] span'),
        '10.0': CssSelector('span.p-treenode-label a span'),
    }
    VERSION_SLOTS_PARENT_SELECTOR = {
        '5.0': CssSelector('table.os-container-map'),
        '10.0': CssSelector('div.os-container-layout'),
    }
    VERSION_SLOTS_VALUE_SELECTOR = {
        '5.0': CssSelector('span.slot-desc'),
        '10.0': CssSelector('td.occupant span.name'),
    }
    VERSION_SPECIMENS_TABLE_SELECTOR = {
        '5.0': SpecimenTableScrubberOld,
        '10.0': PDataTableScrubberNew,
    }
    VERSION_SLOTS_LOADED_SELECTOR = {
        '5.0': CssSelector('table.os-container-map'),
        '10.0': CssSelector('div.os-container-layout'),
    }
    VERSION_ORIGINAL_SELECTOR = {
        '5.0': 'locations',
        '10.0': 'overview',
    }

    def object_name(self):
        return 'container'

    def function_page_url(self):
        return 'containers'

    def export_link_css_selector(self):
        return self.helper.get_version_item(self.VERSION_EXPORT_LINK_SELECTOR)

    def item_page_loaded_css_selector(self):
        return self.helper.get_version_item(self.VERSION_LOADED_SELECTOR)

    def visit_item(self, o):
        details = {}

        self.goto_item_sub_page(
            o,
            page_name='overview',
            selector=self.helper.get_version_item(self.VERSION_OVERVIEW_LOADED_SELECTOR),
            original=self.helper.get_version_item(self.VERSION_ORIGINAL_SELECTOR),
        )

        vt: VersionTranslator = VersionTranslator()
        vt.set_label_translators_for_version('5.0', {'Collection Protocols': 'Collection Protocol'})

        details['overview'] = OSOverviewScrubber(helper=self.helper, version_comparator=vt).get_details()

        self.goto_item_sub_page(
            o,
            page_name='locations',
            selector=self.helper.get_version_item(self.VERSION_SLOTS_LOADED_SELECTOR),
            original=self.helper.get_version_item(self.VERSION_ORIGINAL_SELECTOR),
        )

        details['rows'] = ListScrubber(
            helper=self.helper,
            parent_selector=self.helper.get_version_item(self.VERSION_ROWS_PARENT_SELECTOR),
            value_selector=self.helper.get_version_item(self.VERSION_ROWS_VALUE_SELECTOR),
        ).get_details()
        details['slots'] = ListScrubber(
            helper=self.helper,
            parent_selector=self.helper.get_version_item(self.VERSION_SLOTS_PARENT_SELECTOR),
            value_selector=self.helper.get_version_item(self.VERSION_SLOTS_VALUE_SELECTOR),
        ).get_details()

        self.goto_item_sub_page(
            o,
            page_name='specimens',
            selector=self.helper.get_version_item(self.VERSION_SPECIMENS_LOADED_SELECTOR),
            original=self.helper.get_version_item(self.VERSION_ORIGINAL_SELECTOR),
        )

        vt: VersionTranslator = VersionTranslator()
        vt.set_columns_for_version('5.0', ['PPID', 'Label'])

        details['specimens'] = self.helper.get_version_item(self.VERSION_SPECIMENS_TABLE_SELECTOR)(helper=self.helper, version_comparator=vt).get_details()

        return details
