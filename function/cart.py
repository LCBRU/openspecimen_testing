from selenium_test_helper import CssSelector, SelectAction, XpathSelector


def selectors(version):
    if version > '5.0':
        return Selectors_v5_1()
    else:
        return Selectors_v5_0()


def outputs(version):
    return Outputs_v5_0()


class Outputs_v5_0:
    VERSION_COLUMNS = {
        '5.0': ['Label', 'Type', 'Anatomic Site', 'Collection Protocol', 'Quantity', 'Lineage'],
    }


class Selectors_v5_0:

    def object_name(self):
        return 'cart'

    def function_page_url(self):
        return 'specimen-lists'

    def export_link_css_selector(self):
        return 'a[ui-sref="specimen-list({listId: list.id})"]'

    def item_page_loaded_css_selector(self):
        return 'span[translate="specimen_list.distribute_all"]'

    def create_button_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def create_page_loaded_selector(self):
        return CssSelector('span[translate="specimen_list.create_list"]')

    def create_page_create_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def item_title_selector(self):
        return CssSelector('span[title="Fred"]')

    def edit_name_field_selector(self):
        return CssSelector('input[ng-model="list.name"]')

    def edit_user_field_selector(self):
        return CssSelector('input[placeholder="Users"]')

    def edit_user_item_selector(self):
        return XpathSelector('//span[text()="Bramley, Richard"]')

    def edit_description_field_selector(self):
        return CssSelector('textarea[ng-model="list.description"]')

    def edit_specimens_field_selector(self):
        return CssSelector('textarea[ng-model="input.labelText"]')

    def function_more_selector(self):
        return CssSelector('span[translate="common.buttons.more"]')

    def function_edit_selector(self):
        return CssSelector('span[translate="specimen_list.edit_or_delete"]')

    def function_delete_selector(self):
        return CssSelector('span[translate="common.buttons.delete"]')

    def function_yes_selector(self):
        return CssSelector('span[translate="common.yes"]')


class Selectors_v5_1(Selectors_v5_0):
    def edit_user_item_selector(self):
        return XpathSelector('//span[text()="Andre Ng"]')

