from open_specimen_tester import OpenSpecimenNonDestructiveTester


class UserTester(OpenSpecimenNonDestructiveTester):
    def object_name(self):
        return 'user'

    def function_page_url(self):
        return 'users'

    def export_link_css_selector(self):
        return 'a[ui-sref="user-detail.overview({userId: user.id})"]'

    def item_page_loaded_css_selector(self):
        return 'span[translate="common.buttons.edit"]'


    def visit_item(self, o):
        details = super().visit_item(o)

        self.goto_item_sub_page(o, page_name='roles', loaded_css_selector='span[translate="user.role.roles"]')
        details['roles'] = self.helper.get_div_table_details()

        return details
