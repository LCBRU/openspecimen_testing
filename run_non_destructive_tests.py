import logging
import os
from open_specimen_tester import OpenSpecimenSeleniumTestHelper
from non_destructive_tests.site_tester import SiteTester
from non_destructive_tests.user_tester import UserTester
from non_destructive_tests.role_tester import RoleTester
from non_destructive_tests.query_tester import QueryTester
from non_destructive_tests.order_tester import OrderTester
from non_destructive_tests.job_tester import JobTester
from non_destructive_tests.institute_tester import InstituteTester
from non_destructive_tests.form_tester import FormTester
from non_destructive_tests.distribution_protocol_tester import DistributionProtocolTester
from non_destructive_tests.container_tester import ContainerTester
from non_destructive_tests.collection_protocol_tester import CollectionProtocolTester
from non_destructive_tests.cart_tester import CartTester
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
    username=os.environ["OS_USERNAME"],
    password=os.environ["OS_PASSWORD"],
    version=os.environ["OS_VERSION"],
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