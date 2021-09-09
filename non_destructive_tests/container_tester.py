from open_specimen_tester import OpenSpecimenNonDestructiveTester
from time import sleep
from selenium.webdriver.common.by import By


class ContainerTester(OpenSpecimenNonDestructiveTester):
    VERSION_OVERVIEW_LABEL_RENAMES = {
        '5.0': {'Collection Protocols': 'Collection Protocol'},
    }

    def object_name(self):
        return 'container'

    def function_page_url(self):
        return 'containers'

    def export_link_css_selector(self):
        return 'a[ui-sref="container-detail.locations({containerId: container.id})"]'

    def item_page_loaded_css_selector(self):
        # return 'span[translate="container.assign_positions"]'
        return 'span.slot-desc' # v5.1

    def visit_item(self, o):
        details = {}

        self.goto_item_sub_page(o, page_name='overview', loaded_css_selector='span[translate="container.replicate"]', original='locations')

        overview = self.helper.get_overview_details()

        for to_rename in self.VERSION_OVERVIEW_LABEL_RENAMES[self.helper.compare_version].keys():
            overview = {self.VERSION_OVERVIEW_LABEL_RENAMES[self.helper.compare_version][to_rename] if k == to_rename else k:v for k,v in overview.items()}

        details['overview'] = overview

        self.goto_item_page(o)

        details['rows'] = self.get_container_children()
        details['slots'] = self.get_container_slots()

        self.goto_item_sub_page(o, page_name='specimens', loaded_css_selector='span[translate="common.buttons.download_report"]', original='locations')

        details['specimens'] = self.helper.get_table_details()

        return details

    def get_container_children(self):
        result = []

        for row in self.helper.get_elements('a[ng-click="selectContainer(container)"] span', By.CSS_SELECTOR):
            result.append(self.helper.get_text(row))

        return result

    def get_container_slots(self):
        result = []

        for slot in self.helper.get_elements('span.slot-desc', By.CSS_SELECTOR):
            result.append(self.helper.get_text(slot))

        return result
