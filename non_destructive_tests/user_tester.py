from lbrc_selenium.selenium import CssSelector
from open_specimen_tester import OpenSpecimenNonDestructiveTester
from time import sleep


class UserTester(OpenSpecimenNonDestructiveTester):
    def object_name(self):
        return 'user'

    def function_page_url(self):
        return 'users'

    def export_link_css_selector(self):
        return CssSelector('a[ui-sref="user-detail.overview({userId: user.id})"]')

    def item_page_loaded_css_selector(self):
        return CssSelector('span[translate="common.buttons.edit"]')

    def goto_function_page(self):
        self.helper.get(f'#/{self.function_page_url()}')
        sleep(self.helper.page_wait_time)
        self.helper.click_element(CssSelector('input[ng-checked="opts.recordsPerPage == 500"]'))
        sleep(self.helper.page_wait_time)

    def visit_item(self, o):
        details = super().visit_item(o)

        self.goto_item_sub_page(o, page_name='roles', selector=CssSelector('span[translate="user.role.roles"]'))
        details['roles'] = self.helper.get_div_table_details()

        return details
