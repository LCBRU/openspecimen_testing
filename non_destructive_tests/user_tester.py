from lbrc_selenium.selenium import CssSelector, XpathSelector, VersionTranslator
from open_specimen_tester import OpenSpecimenNonDestructiveTester, OSOverviewScrubber, get_versioned_table_scrubber
from time import sleep


class UserTester(OpenSpecimenNonDestructiveTester):
    VERSION_RECORDS_TO_DISPLAY = {
        '5.0': CssSelector('input[ng-checked="opts.recordsPerPage == 500"]'),
        '10.0': XpathSelector('//div[div/input[@name="pageSize" and @value="500"]]'),
    }
    VERSION_EXPORT_LINK_SELECTOR = {
        '5.0': CssSelector('a[ui-sref="user-detail.overview({userId: user.id})"]'),
        '10.0': CssSelector('a[href^="#/users/"][href$="/overview"]'),
    }
    VERSION_LOADED_SELECTOR = {
        '5.0': CssSelector('span[translate="common.buttons.edit"]'),
        '10.0': XpathSelector('//button/span[contains(text(), "Edit")]'),
    }
    VERSION_ROLES_LOADED_SELECTOR = {
        '5.0': CssSelector('a[translate="user.role.add_role"]'),
        '10.0': XpathSelector('//button/span[contains(text(), "Add Role")]'),
    }

    def object_name(self):
        return 'user'

    def function_page_url(self):
        return 'users'

    def export_link_css_selector(self):
        return self.helper.get_version_item(self.VERSION_EXPORT_LINK_SELECTOR)

    def item_page_loaded_css_selector(self):
        return self.helper.get_version_item(self.VERSION_LOADED_SELECTOR)

    def goto_function_page(self):
        self.helper.get(f'#/{self.function_page_url()}')
        sleep(self.helper.page_wait_time)
        display_500 = self.helper.get_element(self.helper.get_version_item(self.VERSION_RECORDS_TO_DISPLAY))

        if not display_500.is_displayed():
            self.helper.click_element(XpathSelector('//button/span[text()="Search"]'))
            sleep(self.helper.page_wait_time)

        self.helper.click_element(self.helper.get_version_item(self.VERSION_RECORDS_TO_DISPLAY))
        sleep(self.helper.page_wait_time)

    def visit_item(self, o):
        vt: VersionTranslator = VersionTranslator()
        vt.set_columns_for_version('6.0', ['Last Name', 'First Name', 'Domain Name', 'Login Name', 'Email Address', 'Phone Number', 'Institute', 'Primary Site', 'Created By', 'Created On'])
        vt.set_value_translators_for_version('6.0', {
            '-': 'Not Specified',
            '': 'Not Specified',
        })
        vt.set_label_translators_for_version('6.0', {
            'Entered By': 'Created By',
            'Entered On': 'Created On',
        })
        
        details = {}

        self.goto_item_page(o)

        details['overview'] = OSOverviewScrubber(helper=self.helper, version_comparator=vt).get_details()

        self.goto_item_sub_page(
            o,
            page_name='roles',
            selector=self.helper.get_version_item(self.VERSION_ROLES_LOADED_SELECTOR))

        details['roles'] = get_versioned_table_scrubber(helper=self.helper).get_details()

        return details
