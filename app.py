import logging
import os
import json
from pathlib import Path
from open_specimen_tester import OpenSpecimenSeleniumTestHelper
from site_tester import SiteTester
from user_tester import UserTester
from role_tester import RoleTester
from query_tester import QueryTester
from order_tester import OrderTester
from job_tester import JobTester
from institute_tester import InstituteTester
from form_tester import FormTester
from distribution_protocol_tester import DistributionProtocolTester
from container_tester import ContainerTester
from collection_protocol_tester import CollectionProtocolTester
from cart_tester import CartTester
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
    version=os.environ["VERSION"],
    sampling_type=os.environ["SAMPLING_TYPE"],
)

started = datetime.now()

h.login()

testers = [
    SiteTester(h),
    UserTester(h),
    RoleTester(h),
    QueryTester(h),
    OrderTester(h),
    JobTester(h),
    InstituteTester(h),
    FormTester(h),
    DistributionProtocolTester(h),
    ContainerTester(h),
    CollectionProtocolTester(h),
    CartTester(h),
]

PROGRESS_FILENAME = h.output_directory / 'progress.json'

if Path(PROGRESS_FILENAME).is_file():
    with open(PROGRESS_FILENAME) as j:
        progress = json.load(j)
else:
    progress = []

for t in testers:
    tester_name = type(t).__name__

    if tester_name not in progress:
        print(f'Processing {tester_name}')

        t.run()

        print(f'Completed {tester_name}')

        progress.append(tester_name)

        with open(PROGRESS_FILENAME, 'w') as j:
            json.dump(progress, j)
    else:
        print(f'Skipping {tester_name}')

h.close()

print(datetime.now() - started)