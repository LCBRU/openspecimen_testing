import logging
import os
from time import sleep
from lbrc_selenium.selenium import CssSelector, get_selenium, XpathSelector
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
from open_specimen_tester import OpenSpecimenHelper


load_dotenv()

logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='errors.log', level=logging.ERROR)



def login(helper):
    helper.get('')
    helper.type_in_textbox(XpathSelector('//input[@ng-model="loginData.loginName"]'), os.environ["USERNAME"])
    helper.type_in_textbox(XpathSelector('//input[@ng-model="loginData.password"]'), os.environ["PASSWORD"])
    helper.click_element(CssSelector('span[translate="user.sign_in"]'))

started = datetime.now()

h = get_selenium(helper_class=OpenSpecimenHelper)

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

try:
    login(h)

    for t in testers:
        t.run()
        sleep(1)
finally:
    h.close()

print(datetime.now() - started)