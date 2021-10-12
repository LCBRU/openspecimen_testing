import logging
import os
from open_specimen_tester import OpenSpecimenSeleniumTestHelper
from destructive_tests.cart_tester import get_cart_tester
from destructive_tests.collection_protocol_tester import get_collection_protocol_tester
from destructive_tests.container_tester import get_container_tester
from destructive_tests.participant_tester import get_participant_standard_tester, get_participant_brc_tester
from destructive_tests.distribution_protocol_tester import get_distribution_protocol_tester
from destructive_tests.institute_tester import get_institute_tester
from destructive_tests.order_tester import get_order_tester
from destructive_tests.query_tester import get_query_tester
from destructive_tests.role_tester import get_role_tester
from destructive_tests.site_tester import get_site_tester
from destructive_tests.user_tester import get_user_tester
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
    get_cart_tester(h),
    get_collection_protocol_tester(h),
    get_container_tester(h),
    get_participant_standard_tester(h),
    get_participant_brc_tester(h),
    get_distribution_protocol_tester(h),
    get_institute_tester(h),
    get_order_tester(h),
    get_query_tester(h),
    get_role_tester(h),
    get_site_tester(h),
    get_user_tester(h),
]

for t in testers:
    t.run()

h.close()

print(datetime.now() - started)