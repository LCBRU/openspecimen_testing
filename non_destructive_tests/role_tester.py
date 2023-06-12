from selenium.webdriver.common.by import By
from open_specimen_tester import OpenSpecimenNonDestructiveTester
from lbrc_selenium.selenium import CssSelector


class RoleTester(OpenSpecimenNonDestructiveTester):
    VERSION_RESOURCES_RENAME = {
        '5.0': {"Path Report": "Surgical Pathology Report"},
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
        result = []

        for row in self.helper.get_elements(CssSelector('div.os-table-body div.row')):
            details = {}

            resource = self.helper.get_text(self.helper.get_element(CssSelector('div.col span'), element=row))

            resource = self.VERSION_RESOURCES_RENAME.get(self.helper.compare_version, {}).get(resource, resource)

            details['resource'] = resource 

            details['permissions'] = [self.helper.get_text(x) for x in self.helper.get_elements(CssSelector('div.os-permissions span[translate]'), element=row)]

            result.append(details)

        return sorted(result, key=lambda d: d['resource'])
