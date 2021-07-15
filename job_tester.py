from open_specimen_tester import OpenSpecimenTester


class JobTester(OpenSpecimenTester):
    def object_name(self):
        return 'job'

    def function_page_url(self):
        return 'jobs'

    def export_link_css_selector(self):
        return 'a[ng-click="executeJob(job)"]'

    def item_page_loaded_css_selector(self):
        return ''

    def visit_item(self, o):
        return []
