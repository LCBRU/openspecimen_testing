from open_specimen_tester import OpenSpecimenNonDestructiveTester


class SiteTester(OpenSpecimenNonDestructiveTester):
    def object_name(self):
        return 'site'

    def function_page_url(self):
        return 'sites'

    def export_link_css_selector(self):
        return 'a[ui-sref="site-detail.overview({siteId: site.id})"]'

    def item_page_loaded_css_selector(self):
        return 'span[translate="common.buttons.edit"]'
