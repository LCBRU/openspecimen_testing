from selenium.webdriver.common.by import By
from open_specimen_tester import OpenSpecimenNonDestructiveTester


class RoleTester(OpenSpecimenNonDestructiveTester):
    VERSION_RESOURCES_RENAME = {
        '5.0': {"Path Report": "Surgical Pathology Report"},
    }

    def object_name(self):
        return 'role'

    def function_page_url(self):
        return 'roles'

    def export_link_css_selector(self):
        return 'a[ui-sref="role-detail.overview({roleId: role.id})"]'

    def item_page_loaded_css_selector(self):
        return 'span[translate="common.buttons.edit"]'

    def visit_item(self, o):
        details = {}

        details['name'] = o['name']

        self.goto_item_page(o)

        details['overview'] = self.get_permissions()

        return details

    def get_permissions(self):
        result = []

        for row in self.helper.get_elements('div.os-table-body div.row', By.CSS_SELECTOR):
            details = {}

            resource = self.helper.get_text(row.find_element(By.CSS_SELECTOR, 'div.col span'))

            resource = self.VERSION_RESOURCES_RENAME.get(self.helper.compare_version, {}).get(resource, resource)

            details['resource'] = resource 

            details['permissions'] = [self.helper.get_text(x) for x in row.find_elements(By.CSS_SELECTOR, 'div.os-permissions span[translate]')]

            result.append(details)

        return sorted(result, key=lambda d: d['resource'])
