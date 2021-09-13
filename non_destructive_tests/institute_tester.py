from open_specimen_tester import OpenSpecimenNonDestructiveTester


class InstituteTester(OpenSpecimenNonDestructiveTester):
    def object_name(self):
        return 'institute'

    def function_page_url(self):
        return 'institutes'

    def export_link_css_selector(self):
        return 'a[ui-sref="institute-detail.overview({instituteId: institute.id})"]'

    def item_page_loaded_css_selector(self):
        return 'span[translate="common.buttons.edit"]'