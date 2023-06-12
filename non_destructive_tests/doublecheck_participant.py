import os
import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from urllib.parse import urljoin
from dotenv import load_dotenv
from pathlib import Path
from model import init_database, Participant


load_dotenv()

logging.basicConfig(filename='errors.log', level=logging.ERROR)

DOWNLOAD_DIRECTORY = os.environ["DOWNLOAD_DIRECTORY"]
PAGE_WAIT_TIME = float(os.environ["PAGE_WAIT_TIME"])
CLICK_WAIT_TIME = float(os.environ["CLICK_WAIT_TIME"])
DOWNLOAD_WAIT_TIME = float(os.environ["DOWNLOAD_WAIT_TIME"])
IMPLICIT_WAIT_TIME = int(os.environ["IMPLICIT_WAIT_TIME"])


download_directory = Path(DOWNLOAD_DIRECTORY)


class SampleSpider:
    def __init__(self, session, headless=True):
        self.session = session

        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", DOWNLOAD_DIRECTORY)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")

        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options, firefox_profile=profile)
        self.driver.implicitly_wait(IMPLICIT_WAIT_TIME)
        # self.driver.maximize_window()
        # self.driver.minimize_window();
        self.base_url = os.environ["BASE_URL"]

    def close(self):
        self.driver.close()
    
    def login(self):
        self.get('')
        self.type_in_textbox('//input[@ng-model="loginData.loginName"]', By.XPATH, os.environ["APP_USERNAME"])
        self.type_in_textbox('//input[@ng-model="loginData.password"]', By.XPATH, os.environ["APP_PASSWORD"])
        self.click_element('span[translate="user.sign_in"', By.CSS_SELECTOR)

    def get(self, url):
        self.driver.get(urljoin(self.base_url, url))
        self.get_element('body', By.CSS_SELECTOR, allow_null=False)

    def get_element(self, query, by, allow_null=False, wait=10):
        try:
            return WebDriverWait(self.driver, wait).until(EC.presence_of_element_located((by, query)))
        except (NoSuchElementException, TimeoutException) as ex:
            if not allow_null:
                raise ex
    
    def type_in_textbox(self, query, by, text):
        element = self.get_element(query, by)
        element.clear()
        element.send_keys(text)

    def click_element(self, query, by):
        element = self.get_element(query, by)
        element.click()
    
    def process_participant(self, p):
        self.get(p.collection_protocol.href)

        # If the patient ID is too short, we can't search for it.  So let's assume its OK.  For now.
        if len(p.ppid) < 4:
            p.completed = True
            self.session.add(p)
            self.session.commit()
            return

        if self.get_element('div.os-right-drawer.active', By.CSS_SELECTOR, allow_null=True) is not None:
            sleep(PAGE_WAIT_TIME)
            self.type_in_textbox('input[placeholder="Participant Protocol ID"]', By.CSS_SELECTOR, p.ppid)
    
        print(p.ppid)

        self.click_element(f'//span[normalize-space(text()) = normalize-space("{p.ppid}")]', By.XPATH)

        try:
            self.click_element('a[ui-sref=".specimens"]', By.CSS_SELECTOR)

            self.click_element('span[translate="common.buttons.more"', By.CSS_SELECTOR)

            p.has_error_checked = False
        except Exception as e:
            print(e)
            print('*' * 50)
            print('ERROR Found - Participant')
            print('*' * 50)
            p.has_error_checked = True
        finally:
            self.session.add(p)
            self.session.commit()

    def run(self):
        self.login()

        processed = 0

        for p in self.session.query(Participant).filter_by(has_error=True).filter(Participant.has_error_checked == None).all():
            self.process_participant(p)

            processed += 1
            if processed > 100:
                quit()

completed = False

while not completed:
    s = SampleSpider(session=init_database(), headless=False)

    try:
        s.run()
        completed = True
    except:
        print('Error found - restarting')
    finally:
        s.close()
