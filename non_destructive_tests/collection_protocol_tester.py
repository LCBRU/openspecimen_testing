from lbrc_selenium.selenium import CssSelector
from open_specimen_tester import OpenSpecimenNonDestructiveTester


class CollectionProtocolTester(OpenSpecimenNonDestructiveTester):
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
        return CssSelector('td:nth-of-type(2) a[ui-sref="cp-summary-view({cpId: cp.id})"]')

    def item_page_loaded_css_selector(self):
        return CssSelector('span[translate="cp.view_specimens"]')

    def visit_item(self, x):
        details = {}

        # Overview
        overview_url = x['href'].replace('cp-view', 'cps').replace('summary-view', 'overview')

        self.goto_item_custom_page(overview_url, CssSelector('span[translate="cp.menu_options.clone"]'))

        details['overview'] = self.helper.get_overview_details()

        # Events
        events_url = overview_url.replace('overview', 'specimen-requirements')

        self.goto_item_custom_page(events_url, CssSelector('span[translate="cp.cpe_list"]'))

        details['events'] = self.helper.get_list_group_details(parent_element_css_selector='div.col-xs-3', columns=self.VERSION_SPECIMEN_REQUIREMENTS_COLUMNS.get(self.helper.compare_version, None))
        details['specimens requirements'] = self.helper.get_div_table_details(parent_element_css_selector='div.col-xs-9', columns=self.VERSION_SPECIMEN_REQUIREMENTS_COLUMNS.get(self.helper.compare_version, None))

        # Participants
        self.goto_item_page(x)

        details['participants'] = self.helper.get_table_details()

        cppt = CollectionProtocolParticipantTester(self.helper, details['overview']['Title'], overview_url.replace('overview', 'participants').split('#/')[1])
        cppt.run()

        return details


class CollectionProtocolParticipantTester(OpenSpecimenNonDestructiveTester):
    VERSION_OVERVIEW_COLUMNS = {
        '5.1': ["Registration Date", "Registration Site", "Birth Date", "Master Patient Index", "National ID", "Gender", "Ethnicity", "Race", "Vital Status", "Created By", "Created On"],
    }

    def __init__(self, helper, collection_protocol_name, cp_url):
        super().__init__(helper)

        self.collection_protocol_name = collection_protocol_name
        self.cp_url = cp_url

    def object_name(self):
        return f'collection_protocol_{self.collection_protocol_name}'

    def function_page_url(self):
        return self.cp_url

    def export_link_css_selector(self):
        return CssSelector('a[ui-sref="participant-detail.overview({cprId: row.hidden.cprId})"]')

    def item_page_loaded_css_selector(self):
        return CssSelector('span[translate="participant.buttons.anonymize"]')

    def visit_item(self, x):
        details = {}

        self.goto_item_page(x)

        details['overview'] = self.helper.get_overview_details(self.VERSION_OVERVIEW_COLUMNS.get(self.helper.compare_version, None))

        self.goto_item_sub_page(x, 'visits-summary', CssSelector('span[translate="visits.list"]'))

        details['visits'] = self.helper.get_div_table_details(parent_element_css_selector='div.col-xs-3')
        details['visit-specimens'] = self.helper.get_div_table_details(parent_element_css_selector='div.col-xs-9')

        self.goto_item_sub_page(x, 'specimens', CssSelector('span[translate="specimens.list"]'))

        details['specimens'] = self.helper.get_table_details()

        cppt = CollectionProtocolParticipantSampleTester(self.helper, x['name'], self.function_page_url().replace('overview', 'specimens'))
        cppt.run()

        return details


class CollectionProtocolParticipantSampleTester(OpenSpecimenNonDestructiveTester):
    VERSION_OVERVIEW_COLUMNS = {
        '5.1': ["Lineage", "Collection Status", "Anatomic Site", "Laterality", "Initial Quantity", "Available Quantity", "Concentration", "Pathology", "Storage Location", "Biohazards", "Created On", "Freeze/Thaw Cycles"],
    }

    def __init__(self, helper, ppid, participant_url):
        super().__init__(helper)

        self.ppid = ppid
        self.participant_url = participant_url

    def object_name(self):
        return f'collection_protocol_participant_{self.ppid}'

    def function_page_url(self):
        return self.participant_url

    def export_link_css_selector(self):
        return CssSelector('a[ui-sref^="specimen-detail.overview({eventId: specimen.eventId, visitId: specimen.visitId"]')

    def item_page_loaded_css_selector(self):
        return CssSelector('span[translate="common.buttons.hide_activity"]')

    def visit_item(self, x):
        details = {}

        self.goto_item_page(x)

        details['overview'] = self.helper.get_overview_details(self.VERSION_OVERVIEW_COLUMNS.get(self.helper.compare_version, None))

        return details

