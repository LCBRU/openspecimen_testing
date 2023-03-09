import os
import zipfile
import csv
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
from model import init_database, CollectionProtocol, Participant, Sample


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
    
    def click_all(self, query, by):
        wait=10
        while True:
            element = self.get_element(query, by, allow_null=True, wait=wait)
            wait=0.1

            if element is None:
                break
            
            element.click()
            sleep(CLICK_WAIT_TIME)
    
    def get_elements(self, query, by):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((by, query)))
    
    def get_text(self, element):
        return (element.get_attribute("text") or '').strip()
    
    def get_href(self, element):
        return (element.get_attribute("href") or '').strip()
    
    def get_innerHtml(self, element):
        return (element.get_attribute("get_innerHtml") or '').strip()
    
    def process_collection_protocol(self, cp):
        print()
        print(cp.name)

        if self.session.query(Participant).filter_by(collection_protocol_id=cp.id).count() == 0:
            self.download_export(cp)
        processed = 0

        for p in self.session.query(Participant).filter_by(collection_protocol_id=cp.id, completed=False).order_by(Participant.id).all():
            self.get(cp.href)
            self.process_participant(p)

            processed += 1

            if processed > 20:
                quit()

    def download_export(self, cp):
        self.get(cp.href)

        self.click_element('span[translate="common.buttons.more"', By.CSS_SELECTOR)
        self.click_element('span[translate="cp.export"', By.CSS_SELECTOR)
        self.click_element('span[translate="common.buttons.export"', By.CSS_SELECTOR)
        self.click_element('span[translate="common.yes"', By.CSS_SELECTOR)

        sleep(DOWNLOAD_WAIT_TIME)

        self.unzip_download_directory()

        with open(download_directory / 'output.csv') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                ppid = row['PPID']

                existing = self.session.query(Participant).filter_by(collection_protocol_id=cp.id, ppid=ppid).one_or_none()

                if existing is None:
                    print(f'Creating {ppid}')
                    self.session.add(Participant(collection_protocol_id=cp.id, ppid=ppid))

            self.session.commit()
        
        self.clear_download_directory()

    def process_participant(self, p):
        # If the patient ID is too short, we can't search for it.  So let's assume its OK.  For now.
        if len(p.ppid) < 4:
            p.completed = True
            self.session.add(p)
            self.session.commit()
            return

        if self.get_element('div.os-right-drawer.active', By.CSS_SELECTOR, allow_null=True) is not None:
            sleep(PAGE_WAIT_TIME)
            self.type_in_textbox('input[placeholder="Participant Protocol ID"]', By.CSS_SELECTOR, p.ppid)
            sleep(PAGE_WAIT_TIME)
    
        print(p.ppid)

        self.click_element(f'//span[normalize-space(text()) = normalize-space("{p.ppid}")]', By.XPATH)

        try:
            self.process_participant_samples(p)
        except Exception as e:
            print(e)
            print('*' * 50)
            print('ERROR Found - Participant')
            print('*' * 50)
            p.has_error = True
        finally:
            p.completed = True
            self.session.add(p)
            self.session.commit()

    def process_participant_samples(self, p):
        self.click_element('a[ui-sref=".specimens"]', By.CSS_SELECTOR)

        self.click_element('span[translate="common.buttons.more"', By.CSS_SELECTOR)

        while True:
            links = self.driver.find_elements_by_css_selector('a.fa-chevron-circle-right')

            if len(links) == 0:
                break

            for l in links:
                l.click()

        for s in self.get_elements('a[ui-sref^="specimen-detail.overview"]', By.CSS_SELECTOR):
            href = self.get_href(s)
            name = self.get_text(s)
            
            # existing = self.session.query(Sample).filter_by(participant_id=p.id, href=href).one_or_none()

            # if existing is None:
            #     print(f'Creating {name}')
            #     self.session.add(Sample(participant_id=p.id, href=href, name=name))
            print(f'Creating {name}')
            self.session.add(Sample(participant_id=p.id, href=href, name=name))
            
        self.session.commit()


        for s in self.session.query(Sample).filter_by(participant_id=p.id, completed=False).order_by(Sample.id).all():
            try:
                self.get(s.href)
            except:
                print('*' * 50)
                print('ERROR Found - Sample')
                print('*' * 50)
                s.has_error = True
            finally:
                s.completed = True
                self.session.add(s)
                self.session.commit()
        
    def unzip_download_directory(self):
        for zp in download_directory.iterdir():
            with zipfile.ZipFile(zp, "r") as zf:
                zf.extractall(DOWNLOAD_DIRECTORY)
    
    def clear_download_directory(self):
        for f in download_directory.iterdir():
            f.unlink()
    
    def run(self):
        self.login()

        for cp in self.get_elements('.container > table > tbody > tr > td:nth-child(2) > a', By.CSS_SELECTOR):
            name = self.get_text(cp)
            href = self.get_href(cp)

            existing = self.session.query(CollectionProtocol).filter_by(name=name).one_or_none()

            if existing is None:
                print(f'Creating {name}')
                self.session.add(CollectionProtocol(name=name, href=href))

        self.session.commit()

        for cp in self.session.query(CollectionProtocol).filter_by(completed=False).order_by(CollectionProtocol.id).all():
            self.process_collection_protocol(cp)

            cp.completed = True
            self.session.add(cp)
            self.session.commit()


if len(list(download_directory.iterdir())) > 0:
    raise RuntimeError(f'Download directory "{DOWNLOAD_DIRECTORY}" is not empty')

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
