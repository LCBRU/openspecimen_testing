from lbrc_selenium.selenium import CssSelector, ListScrubber, Selector, SeleniumHelper, VersionTranslator
from open_specimen_tester import OpenSpecimenNonDestructiveTester, OSOverviewScrubber, OSTableScrubberOld, OSTableScrubberNew
from time import sleep


class CPListScrubber(ListScrubber):
    def __init__(self, helper: SeleniumHelper, version_comparator: VersionTranslator = None) -> None:
        super().__init__(
            helper=helper,
            parent_selector=CssSelector('div.col-xs-3'),
            value_selector=CssSelector('div.list-group-item span.ng-isolate-scope'),
            version_comparator=version_comparator,
            )


class CollectionProtocolTester(OpenSpecimenNonDestructiveTester):
    def url_prefixes(self):
        return {
            '5.0': '#',
        }
        
    def object_name(self):
        return 'collection_protocol'

    def function_page_url(self):
        return 'cps'

    def export_link_css_selector(self):
        return CssSelector('td:nth-of-type(2) a[ui-sref^="cp-summary-view"]')

    def item_page_loaded_css_selector(self):
        return CssSelector('span[translate="cp.view_specimens"]')

    def visit_item(self, x):
        details = {}

        # Overview
        overview_url = x['href'].replace('cp-view', 'cps').replace('summary-view', 'overview')

        self.goto_item_custom_page(overview_url, CssSelector('span[translate="cp.menu_options.clone"]'))

        details['overview'] = OSOverviewScrubber(helper=self.helper).get_details()

        # Events
        events_url = overview_url.replace('overview', 'specimen-requirements')

        self.goto_item_custom_page(events_url, CssSelector('span[translate="cp.cpe_list"]'))

        details['events'] = CPListScrubber(helper=self.helper).get_details()
        
        vt: VersionTranslator = VersionTranslator()
        vt.set_columns_for_version('5.1', ["Name", "Type"])

        details['specimens requirements'] = OSTableScrubberOld(
            helper=self.helper,
            version_comparator=vt,
        ).get_details()

        # Participants
        self.goto_item_page(x)

        vt: VersionTranslator = VersionTranslator()
        vt.set_columns_for_version('5.1', ['Participant Protocol ID', 'Name', 'Master Patient Index', 'Registration Date', 'Age'])

        details['participants'] = OSTableScrubberNew(helper=self.helper, version_comparator=vt).get_details()

        cppt = CollectionProtocolParticipantTester(
            self.helper,
            details['overview']['Title'],
            overview_url.replace('overview', 'participants'),
        )
        cppt.run()

        return details


class CollectionProtocolParticipantTester(OpenSpecimenNonDestructiveTester):
    def url_prefixes(self):
        return {
            '5.0': '#',
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

        vt: VersionTranslator = VersionTranslator()
        vt.set_columns_for_version('5.1', ["Registration Date", "Registration Site", "Birth Date", "Master Patient Index", "National ID", "Gender", "Ethnicity", "Race", "Vital Status", "Created By", "Created On"])
        vt.set_value_translators_for_version('6.0', {
            '': 'Not Specified',
        })

        details['overview'] = OSOverviewScrubber(
            helper=self.helper,
            version_comparator=vt,
        ).get_details()

        self.goto_item_sub_page(x, 'visits-summary', CssSelector('span[translate="visits.list"]'))

        details['visits'] = CPListScrubber(helper=self.helper).get_details()
        
        details['visit-specimens'] = OSTableScrubberNew(helper=self.helper).get_details()

        self.goto_item_sub_page(x, 'specimens', CssSelector('span[translate="specimens.list"]'))

        details['specimens'] = OSTableScrubberNew(helper=self.helper).get_details()

        cppt = CollectionProtocolParticipantSampleTester(self.helper, x['name'], self.function_page_url().replace('overview', 'specimens'))
        cppt.run()

        return details


class CollectionProtocolParticipantSampleTester(OpenSpecimenNonDestructiveTester):
    def url_prefixes(self):
        return {
            '5.0': '#',
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
        sleep(self.helper.page_wait_time)
        return CssSelector('span[translate="common.buttons.hide_activity"]')

    def visit_item(self, x):
        details = {}

        self.goto_item_page(x)

        vt: VersionTranslator = VersionTranslator()
        vt.set_columns_for_version('5.1', ["Lineage", "Collection Status", "Anatomic Site", "Laterality", "Initial Quantity", "Available Quantity", "Concentration", "Pathology", "Storage Location", "Biohazards", "Created On", "Freeze/Thaw Cycles"],)
        vt.set_value_translators_for_version('6.0', {
            '': 'Not Specified',
        })

        details['overview'] = OSOverviewScrubber(
            helper=self.helper,
            version_comparator=vt,
        ).get_details()

        return details

