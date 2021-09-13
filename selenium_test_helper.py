import zipfile
import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from urllib.parse import urljoin
from pathlib import Path


class SeleniumTestHelper:
    SAMPLING_TYPE_ALL = 'all'
    SAMPLING_TYPE_FIBONACCI = 'fibonacci'
    SAMPLING_TYPE_FIRST = 'first'

    def __init__(
        self,
        output_directory,
        download_directory,
        base_url,
        version,
        compare_version,
        headless=True,
        implicit_wait_time=1,
        click_wait_time=0.2,
        download_wait_time=5,
        page_wait_time=1,
        username='',
        password='',
        sampling_type='fibonacci',
    ):
        self.implicit_wait_time = implicit_wait_time
        self.click_wait_time = click_wait_time
        self.download_wait_time = download_wait_time
        self.page_wait_time = page_wait_time
        self.sampling_type = sampling_type
        self.version = version
        self.compare_version = compare_version

        self._username = username
        self._password = password

        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", download_directory)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")

        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")

        self.driver = webdriver.Firefox(options=options, firefox_profile=profile)
        self.driver.implicitly_wait(implicit_wait_time)
        self.base_url = base_url

        self._download_directory = Path(download_directory)
        self._download_directory.mkdir(parents=True, exist_ok=True)
        self.clear_download_directory()

        self.output_directory = Path(output_directory) / version

        self.output_directory.mkdir(parents=True, exist_ok=True)

    def close(self):
        self.driver.close()
    
    def unzip_download_directory_contents(self):
        for zp in self._download_directory.iterdir():
            with zipfile.ZipFile(zp, "r") as zf:
                zf.extractall(self._download_directory)
    
    def clear_download_directory(self):
        for f in self._download_directory.iterdir():
            f.unlink()
    
    def get(self, url):
        self.driver.get(urljoin(self.base_url, url))
        self.get_element('body', By.CSS_SELECTOR, allow_null=False)

    def get_element(self, query, by, allow_null=False, wait=10):
        try:
            return self.driver.find_element(by, query)
        except (NoSuchElementException, TimeoutException) as ex:
            if not allow_null:
                raise ex
    
    def get_elements(self, query, by):
        return self.driver.find_elements(by, query)
    
    def type_in_textbox(self, query, by, text):
        element = self.get_element(query, by)
        element.clear()
        element.send_keys(text)

    def click_element(self, query, by):
        element = self.get_element(query, by)
        element.click()
        sleep(self.click_wait_time)
    
    def click_all(self, query, by):
        wait=10
        while True:
            element = self.get_element(query, by, allow_null=True, wait=wait)
            wait=0.1

            if element is None:
                break
            
            element.click()
            sleep(self.click_wait_time)
    
    def get_text(self, element):
        result = (element.text or '').strip()

        if len(result) == 0:
            result = (element.get_attribute("text") or '').strip()

            if len(result) == 0:
                result = self.get_innerHtml(element)
        
        return result
    
    def get_href(self, element):
        return (element.get_attribute("href") or '').strip()
    
    def get_value(self, element):
        return (element.get_attribute("value") or '').strip()
    
    def get_innerHtml(self, element):
        return (self.driver.execute_script("return arguments[0].innerHTML", element) or '').strip()
    
    def get_select_option_values(self, id):
        select = self.driver.find_element_by_id(id)

        return [o.get_attribute('value') for o in select.find_elements_by_tag_name('option')]

    def is_sampling_pick(self, n):
        is_perfect_square = lambda x: int(math.sqrt(x))**2 == x

        if self.sampling_type.isnumeric():
            if (n % 100) < int(self.sampling_type.isnumeric()):
                return True
            else:
                return False

        if self.sampling_type == SeleniumTestHelper.SAMPLING_TYPE_ALL:
            return True
        elif self.sampling_type == SeleniumTestHelper.SAMPLING_TYPE_FIRST:
            return n == 0
        else:
            return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)