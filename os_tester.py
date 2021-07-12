import jsonlines
import csv
from time import sleep
from tester import TesterBase
from selenium.webdriver.common.by import By
from sympy import tribonacci, fibonacci


class OsTester(TesterBase):
    def login(self):
        self.get('')
        self.type_in_textbox('//input[@ng-model="loginData.loginName"]', By.XPATH, self._username)
        self.type_in_textbox('//input[@ng-model="loginData.password"]', By.XPATH, self._password)
        self.click_element('span[translate="user.sign_in"]', By.CSS_SELECTOR)

    def save_export(self, filename, in_more=False):
        sleep(1)
        if in_more:
            self.click_element('span[translate="common.buttons.more"]', By.CSS_SELECTOR)
            self.click_element('span[translate="cp.export"]', By.CSS_SELECTOR)
            self.click_element('span[translate="common.buttons.export"]', By.CSS_SELECTOR)
            self.click_element('span[translate="common.yes"]', By.CSS_SELECTOR)
        else:
            self.click_element('span[translate="common.buttons.export"]', By.CSS_SELECTOR)

        sleep(self.download_wait_time)

        self.unzip_download_directory_contents()

        with open(self._download_directory / 'output.csv') as csvfile:
            reader = csv.DictReader(csvfile)

            with jsonlines.open(self._output_directory / filename, mode='w') as writer:
                for row in reader:
                    writer.write(row)
        
        self.clear_download_directory()


