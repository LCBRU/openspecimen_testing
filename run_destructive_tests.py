import logging
import os
from time import sleep
from lbrc_selenium.selenium import CssSelector, get_selenium
from open_specimen_tester import OpenSpecimenHelper
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


def login(helper):
    helper.get('')
    login_input = helper.wait_to_appear(CssSelector('input[ng-model="loginData.loginName"]'))
    sleep(1)
    helper.type_in_textbox(CssSelector('input[ng-model="loginData.loginName"]'), os.environ["USERNAME"])
    helper.type_in_textbox(CssSelector('input[ng-model="loginData.password"]'), os.environ["PASSWORD"])
    helper.click_element(CssSelector('span[translate="user.sign_in"]'))

started = datetime.now()

h = get_selenium(helper_class=OpenSpecimenHelper)

testers = [
    # get_cart_tester(h),
    # get_collection_protocol_tester(h),
    # get_container_tester(h),
    # get_participant_standard_tester(h),
    # get_participant_brc_tester(h),
    # get_distribution_protocol_tester(h),
    # get_institute_tester(h),
    # get_order_tester(h),
    # get_query_tester(h),
    # get_role_tester(h),
    # get_site_tester(h),
    get_user_tester(h),
]

try:
    login(h)

    for t in testers:
        t.run()
        sleep(1)
finally:
    h.close()

print(datetime.now() - started)