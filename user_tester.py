import logging
import jsonlines
from selenium.webdriver.common.by import By
from os_tester import OsTester


class UserTester(OsTester):
    USER_EXPORT_FILENAME = 'user_export.jsonl'
    USER_DETAILS_FILENAME = 'user_details.jsonl'

    def goto_users_page(self):
        self.get('#/users')

    def get_user_export(self):
        logging.info('Exporting Users')

        self.goto_users_page()
        self.save_export(self.USER_EXPORT_FILENAME)

    def goto_user(self, user):
        self.goto_users_page()

        if self.get_element('div.os-right-drawer.active', By.CSS_SELECTOR, allow_null=True) is not None:
            self.type_in_textbox('input[placeholder="Login Name"]', By.CSS_SELECTOR, user['Login Name'])
    
        fullname = f'{user["First Name"]} {user["Last Name"]}'
        self.click_element(f'//span[normalize-space(text()) = normalize-space("{fullname}")]', By.XPATH)

    def visit_users(self):
        logging.info('Visiting Users')

        with jsonlines.open(self._output_directory / self.USER_DETAILS_FILENAME, mode='w') as writer:
            with jsonlines.open(self._output_directory / self.USER_EXPORT_FILENAME) as reader:
                for i, u in enumerate(reader):
                    if self.is_sampling_pick(i):
                        logging.info(f'Processing user: {u["Login Name"]}')

                        dets = self.visit_user(u)
                        writer.write(dets)
                    else:
                        logging.info(f'Skipping user: {u["Login Name"]}')


    def visit_user(self, user):
        details = self.get_user_details(user)
        details['role'] = self.get_user_roles(user)

        return details

    def get_user_details(self, user):
        self.goto_user(user)

        details = {}

        for kvpair in self.driver.find_elements_by_css_selector('ul.os-key-values li'):
            title = kvpair.find_element_by_tag_name('strong')
            value = kvpair.find_element_by_tag_name('span')

            details[self.get_innerHtml(title)] = self.get_innerHtml(value)

        return details

    def get_user_roles(self, user):
        self.goto_user(user)

        if self.get_element('i.fa-users', By.CSS_SELECTOR, allow_null=True) is None:
            return []

        self.click_element(f'i.fa-users', By.CSS_SELECTOR)

        roles = []

        for row in self.driver.find_elements_by_css_selector('div.os-table-body div.row'):
            cols = row.find_elements_by_css_selector('div.col')

            roles.append({
                'site': self.get_innerHtml(cols[0]),
                'collection protocol': self.get_innerHtml(cols[1]),
                'role': self.get_innerHtml(cols[2]),
            })
            
        return roles

    def run(self):
        # self.get_user_export()
        self.visit_users()
