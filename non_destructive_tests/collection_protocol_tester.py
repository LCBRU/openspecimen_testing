from time import sleep
from open_specimen_tester import OpenSpecimenNonDestructiveTester


class CollectionProtocolTester(OpenSpecimenNonDestructiveTester):
    def object_name(self):
        return 'collection_protocol'

    def function_page_url(self):
        return 'cps'

    def export_link_css_selector(self):
        return 'a[ui-sref="cp-summary-view({cpId: cp.id})"]'

    def item_page_loaded_css_selector(self):
        return 'span[translate="cp.view_specimens"]'

    def visit_item(self, x):
        details = {}

        # Overview
        overview_url = x['href'].replace('cp-view', 'cps').replace('summary-view', 'overview')

        self.goto_item_custom_page(overview_url, 'span[translate="cp.menu_options.clone"]')

        details['overview'] = self.helper.get_overview_details()

        # Events
        events_url = overview_url.replace('overview', 'specimen-requirements')

        self.goto_item_custom_page(events_url, 'span[translate="cp.cpe_list"]')

        details['events'] = self.helper.get_div_table_details(parent_element_css_selector='div.col-xs-3')
        details['specimens requirements'] = self.helper.get_div_table_details(parent_element_css_selector='div.col-xs-9')

        # Participants
        self.goto_item_page(x)

        details['participants'] = self.helper.get_table_details()

        cppt = CollectionProtocolParticipantTester(self.helper, details['overview']['Title'], overview_url.replace('overview', 'participants').split('#/')[1])
        cppt.run()

        return details


class CollectionProtocolParticipantTester(OpenSpecimenNonDestructiveTester):
    def __init__(self, helper, collection_protocol_name, cp_url):
        super().__init__(helper)

        self.collection_protocol_name = collection_protocol_name
        self.cp_url = cp_url

    def object_name(self):
        return f'collection_protocol_{self.collection_protocol_name}'

    def function_page_url(self):
        return self.cp_url

    def export_link_css_selector(self):
        return 'a[ui-sref="participant-detail.overview({cprId: row.hidden.cprId})"]'

    def item_page_loaded_css_selector(self):
        return 'span[translate="participant.buttons.anonymize"]'

    def visit_item(self, x):
        details = {}

        self.goto_item_page(x)

        details['overview'] = self.helper.get_overview_details()

        self.goto_item_sub_page(x, 'visits-summary', 'span[translate="visits.list"]')

        details['visits'] = self.helper.get_div_table_details(parent_element_css_selector='div.col-xs-3')
        details['visit-specimens'] = self.helper.get_div_table_details(parent_element_css_selector='div.col-xs-9')

        self.goto_item_sub_page(x, 'specimens', 'span[translate="specimens.buttons.collect"]')

        details['specimens'] = self.helper.get_table_details()

        cppt = CollectionProtocolParticipantSampleTester(self.helper, details['overview']['PPID'], self.function_page_url().replace('overview', 'specimens'))
        cppt.run()

        return details


class CollectionProtocolParticipantSampleTester(OpenSpecimenNonDestructiveTester):
    def __init__(self, helper, ppid, participant_url):
        super().__init__(helper)

        self.ppid = ppid
        self.participant_url = participant_url

    def object_name(self):
        return f'collection_protocol_participant_{self.ppid}'

    def function_page_url(self):
        return self.participant_url

    def export_link_css_selector(self):
        return 'a[ui-sref^="specimen-detail.overview({eventId: specimen.eventId, visitId: specimen.visitId"]'

    def item_page_loaded_css_selector(self):
        return 'span[translate="common.buttons.edit"]'

    def visit_item(self, x):
        details = {}

        self.goto_item_page(x)

        details['overview'] = self.helper.get_overview_details()

