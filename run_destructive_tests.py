import logging
import os
from open_specimen_tester import OpenSpecimenSeleniumTestHelper
from destructive_tests.cart_tester import CartTester
from destructive_tests.collection_protocol_tester import CollectionProtocolTester
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='errors.log', level=logging.ERROR)


h = OpenSpecimenSeleniumTestHelper(
    download_directory=os.environ["DOWNLOAD_DIRECTORY"],
    output_directory=os.environ["OUTPUT_DIRECTORY"],
    base_url=os.environ["OS_URL_BASE"],
    headless=False,
    implicit_wait_time=float(os.environ["IMPLICIT_WAIT_TIME"]),
    click_wait_time=float(os.environ["CLICK_WAIT_TIME"]),
    download_wait_time=float(os.environ["DOWNLOAD_WAIT_TIME"]),
    page_wait_time=float(os.environ["PAGE_WAIT_TIME"]),
    username=os.environ["USERNAME"],
    password=os.environ["PASSWORD"],
    version='5.0',
    sampling_type=os.environ["SAMPLING_TYPE"],
)

started = datetime.now()

h.login()

testers = [
    # CartTester(h),
    CollectionProtocolTester(h),
]

for t in testers:
    t.run()

h.close()

print(datetime.now() - started)