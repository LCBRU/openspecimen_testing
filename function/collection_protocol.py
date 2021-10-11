from selenium_test_helper import CssSelector, XpathSelector


def selectors(version):
    if version >= '5.1':
        return Selectors_v5_1()
    else:
        return Selectors_v5_0()


def outputs(version):
    return Outputs_v5_0()


class Outputs_v5_0:
    VERSION_SPECIMEN_REQUIREMENTS_COLUMNS = {
        '5.1': ["Name", "Type"],
    }
    VERSION_EVENTS_COLUMNS = {
        '5.1': [],
    }


class Selectors_v5_0:

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

    def sites_field(self):
        return CssSelector('input[placeholder="Sites"]')

    def sites_item(self):
        return XpathSelector('//span[text()="Glenfield Hospital"]')

    def title_field(self):
        return CssSelector('input[placeholder="Title"]')

    def short_title_field(self):
        return CssSelector('input[placeholder="Short Title"]')

    def pi_field(self):
        return CssSelector('div[placeholder="Principal Investigator"]')

    def pi_value(self):
        return XpathSelector('//span[text()="Adlam, Dave"]')


class Selectors_v5_1(Selectors_v5_0):
    def create_button_selector(self):
        return CssSelector('span[translate="common.buttons.import"]')

    def create_link_selector(self):
        return CssSelector('span[translate="common.buttons.create"]')

    def sites_field(self):
        return CssSelector('input[ng-model="$select.search"]')

    def title_field(self):
        return CssSelector('input[ng-model="cp.title"]')

    def short_title_field(self):
        return CssSelector('input[ng-model="cp.shortTitle"]')

    def pi_field(self):
        return CssSelector('div[placeholder="Principal Investigator"] > div > div > span')

    def pi_value(self):
        return XpathSelector('//span[text()="Abi Al-Hussaini"]')

    def pc_field(self):
        return CssSelector('div[placeholder="Protocol Coordinators"]')

    def pc_value(self):
        return XpathSelector('//span[text()="Abi Al-Hussaini"]')
