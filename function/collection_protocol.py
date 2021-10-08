from selenium_test_helper import CssSelector, XpathSelector


class CollectionProtocolFunction:
    VERSION_SPECIMEN_REQUIREMENTS_COLUMNS = {
        '5.1': ["Name", "Type"],
    }
    VERSION_EVENTS_COLUMNS = {
        '5.1': [],
    }

    def object_name(self):
        return 'collection_protocol'

    def function_page_url(self):
        return 'cps'

    def export_link_css_selector(self):
        return 'td:nth-of-type(2) a[ui-sref="cp-summary-view({cpId: cp.id})"]'

    def item_page_loaded_css_selector(self):
        return 'span[translate="cp.view_specimens"]'

    def create_button_selector(self):
        return CssSelector('button[title="Click to add new Collection Protocol"]')

    def create_link_selector(self):
        return CssSelector('a > span[translate="common.buttons.create"]')

    def create_page_loaded_selector(self):
        return CssSelector('span[translate="cp.create_cp_title"]')

    def create_page_create_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def item_title_selector(self):
        return XpathSelector('//span[text()="Fred"]')
