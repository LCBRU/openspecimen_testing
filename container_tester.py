import logging
from re import L
from time import sleep
import jsonlines
from selenium.webdriver.common.by import By
from os_tester import OsTester


class ContainerTester(OsTester):
    EXPORT_FILENAME = 'container_export.jsonl'
    DETAILS_FILENAME = 'container_details.jsonl'

    def goto_function_page(self):
        self.get('#/containers')

    def goto_locations(self, dp):
        self.goto_function_page()
        self.get(dp['href'])
        sleep(5)
        self.get_element('span[translate="container.assign_positions"]', By.CSS_SELECTOR)

    def get_export(self):
        logging.info('Exporting')

        self.goto_function_page()

        with jsonlines.open(self._output_directory / self.EXPORT_FILENAME, mode='w') as writer:
            for x in self.get_elements('a[ui-sref="container-detail.locations({containerId: container.id})"]', By.CSS_SELECTOR):
                details = {
                    'name': self.get_text(x),
                    'href': self.get_href(x),
                }
                writer.write(details)

    def visit_containers(self):
        logging.info('Visiting')

        with jsonlines.open(self._output_directory / self.DETAILS_FILENAME, mode='w') as writer:
            with jsonlines.open(self._output_directory / self.EXPORT_FILENAME) as reader:
                for i, f in enumerate(reader):
                    logging.info(f'Processing Container: {f["name"]}')

                    dets = self.visit_container(f)
                    writer.write(dets)

    def visit_container(self, x):
        details = {}

        self.goto_locations(x)

        details['rows'] = self.get_container_children()
        details['slots'] = self.get_container_slots()

        return details

    def get_container_children(self):
        result = []

        for row in self.get_elements('a[ng-click="selectContainer(container)"] span', By.CSS_SELECTOR):
            result.append(self.get_innerHtml(row))

        return result

    def get_container_slots(self):
        result = []

        for slot in self.get_elements('div.slot-element', By.CSS_SELECTOR):
            pos = slot.find_element(By.CSS_SELECTOR, 'div.slot-pos')

            names = slot.find_elements(By.CSS_SELECTOR, 'span.slot-desc')

            if len(names) == 1:
                name = self.get_innerHtml(names[0])
            else:
                name = ''

            result.append({
                'position': self.get_innerHtml(pos),
                'name': name,
            })

        return result

    def run(self):
        self.get_export()
        self.visit_containers()
