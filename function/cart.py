class CartFunction:
    VERSION_COLUMNS = {
        '5.0': ['Label', 'Type', 'Anatomic Site', 'Collection Protocol', 'Quantity', 'Lineage'],
    }

    def object_name(self):
        return 'cart'

    def function_page_url(self):
        return 'specimen-lists'

    def export_link_css_selector(self):
        return 'a[ui-sref="specimen-list({listId: list.id})"]'

    def item_page_loaded_css_selector(self):
        return 'span[translate="specimen_list.distribute_all"]'

    def create_button_css_selector(self):
        return 'span[translate="common.buttons.create"]'

    def create_page_loaded_css_selector(self):
        return 'span[translate="specimen_list.create_list"]'

    def create_page_create_css_selector(self):
        return 'span[translate="common.buttons.create"]'

    def item_title_css_selector(self):
        return 'span[title="Fred"]'
