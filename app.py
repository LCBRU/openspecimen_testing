import logging
import os
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
    version='5.0',
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

for t in testers:
    t.run()

h.close()

print(datetime.now() - started)