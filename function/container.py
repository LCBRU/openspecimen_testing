from selenium_test_helper import CssSelector, XpathSelector


class ContainerFunction:
    VERSION_OVERVIEW_LABEL_RENAMES = {
        '5.0': {'Collection Protocols': 'Collection Protocol'},
    }

    def object_name(self):
        return 'container'

    def function_page_url(self):
        return 'containers'

    def export_link_css_selector(self):
        return 'a[ui-sref="container-detail.locations({containerId: container.id})"]'

    def item_page_loaded_css_selector(self):
        # return 'span[translate="container.assign_positions"]'
        return 'span.slot-desc' # v5.1

    def create_button_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def create_page_loaded_selector(self):
        return CssSelector('span[translate="container.create_container"]')

    def create_page_create_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def item_title_selector(self):
        return XpathSelector('//span[text()="Frederick"]')

    def user_menu_item_selector(self):
        return CssSelector('span.fa-user')
