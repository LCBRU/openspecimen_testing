from lbrc_selenium.selenium import CssSelector, XpathSelector
from open_specimen_tester import OpenSpecimenNonDestructiveTester


class InstituteTester(OpenSpecimenNonDestructiveTester):
    VERSION_EXPORT_LINK_SELECTOR = {
        '5.0': CssSelector('a[ui-sref="institute-detail.overview({instituteId: institute.id})"]'),
        '10.0': CssSelector('a[href^="#/institutes/"][href$="/overview"]'),
    }
    VERSION_LOADED_SELECTOR = {
        '5.0': CssSelector('span[translate="common.buttons.edit"]'),
        '10.0': XpathSelector('//button/span[contains(text(), "Edit")]'),
    }
    VERSION_OBJECT_NAMES = {
        '5.0': 'institutes',
        '10.0': 'institutes/-1',
    }
    def object_name(self):
        return 'institute'

    def function_page_url(self):
        return self.helper.get_version_item(self.VERSION_OBJECT_NAMES)

    def export_link_css_selector(self):
        return self.helper.get_version_item(self.VERSION_EXPORT_LINK_SELECTOR)

    def item_page_loaded_css_selector(self):
        return self.helper.get_version_item(self.VERSION_LOADED_SELECTOR)
