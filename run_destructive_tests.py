from destructive_tests.container_tester import ContainerTester
import logging
import os
from open_specimen_tester import OpenSpecimenSeleniumTestHelper
from destructive_tests.cart_tester import CartTester
from destructive_tests.collection_protocol_tester import CollectionProtocolTester
from destructive_tests.participant_tester import ParticipantStandardTester, ParticipantBrcTester
from destructive_tests.container_tester import ContainerTester
from destructive_tests.distribution_protocol_tester import DistricutionProtocolTester
from destructive_tests.institute_tester import InstituteTester
from destructive_tests.order_tester import OrderTester
# from destructive_tests.query_tester import QueryTester
# from destructive_tests.role_tester import RoleTester
# from destructive_tests.site_tester import SiteTester
# from destructive_tests.user_tester import UserTester
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
    compare_version=os.environ["OS_COMPARE_VERSION"],
)

started = datetime.now()

h.login()

testers = [
    # CartTester(h),
    # CollectionProtocolTester(h),
    # ContainerTester(h),
    # ParticipantStandardTester(h),
    # ParticipantBrcTester(h),
    # DistricutionProtocolTester(h),
    # InstituteTester(h),

    OrderTester(h),
    # QueryTester(h),
    # RoleTester(h),
    # SiteTester(h),
    # UserTester(h),
]

for t in testers:
    t.run()

h.close()

print(datetime.now() - started)