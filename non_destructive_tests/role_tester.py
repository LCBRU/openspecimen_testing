from selenium.webdriver.common.by import By
from open_specimen_tester import OpenSpecimenNonDestructiveTester, OSTableScrubberOld
from lbrc_selenium.selenium import CssSelector, VersionTranslator


class RoleTester(OpenSpecimenNonDestructiveTester):
    VERSION_RESOURCES_RENAME = {
        '5.0': {"Path Report": "Surgical Pathology Report"},
    }

    def url_prefixes(self):
        return {
            '5.0': '#',
        }

    def object_name(self):
        return 'role'

    def function_page_url(self):
        return 'roles'

    def export_link_css_selector(self):
        return CssSelector('a[ui-sref="role-detail.overview({roleId: role.id})"]')

    def item_page_loaded_css_selector(self):
        return CssSelector('span[translate="common.buttons.edit"]')

    def visit_item(self, o):
        details = {}

        details['name'] = o['name']

        self.goto_item_page(o)

        details['overview'] = self.get_permissions()

        return details

    def get_permissions(self):
        vt: VersionTranslator = VersionTranslator()
        vt.set_label_translators_for_version('6.0', {
            "Path Report": "Surgical Pathology Report",
        })

        return OSTableScrubberOld(helper=self.helper, version_comparator=vt).get_details()
