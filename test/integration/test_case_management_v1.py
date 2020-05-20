# coding: utf-8

# Copyright 2020 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''
 This class contains an integration test for the Case Management service.
'''

import pytest
import unittest
import os
import os.path
import io
from ibm_cloud_sdk_core import *
from ibm_platform_services.case_management_v1 import *

# Read config file
configFile = 'case_management.env'
configLoaded = None

if os.path.exists(configFile):
    os.environ['IBM_CREDENTIALS_FILE'] = configFile
    configLoaded = True

class TestCaseManagementV1(unittest.TestCase):

    # Used to store newly created case number
    new_case_number = ''
    # Used to store newly uploaded file id
    file_attachment_id = ''

    @classmethod
    def setUpClass(cls):

        if not configLoaded:
            raise unittest.SkipTest('External configuration not available, skipping...')

        cls.service = CaseManagementV1.new_instance()
        assert cls.service is not None

        cls.config = read_external_sources(CaseManagementV1.DEFAULT_SERVICE_NAME)
        assert cls.config is not None
        assert cls.config['APIKEY'] is not None
        assert cls.config['AUTHTYPE'] is not None
        assert cls.config['AUTH_URL'] is not None

        print('\nSetup complete.')
        print('config: \n', cls.config)

    def test_01_create_case(self):

        # Offering info can be retrieved via /case-management/utilities/v1/offerings/technical
        offering_payload_type_model = {}
        offering_payload_type_model['group'] = 'crn_service_name'
        offering_payload_type_model['key'] = 'cloud-object-storage'
        offering_payload_type_model['id'] = 'dff97f5c-bc5e-4455-b470-411c3edbe49c'

        offering_payload_model = {}
        offering_payload_model['name'] = 'Cloud Object Storage'
        offering_payload_model['type'] = offering_payload_type_model

        type = 'technical'
        subject = 'Python - Integration test'
        description = 'Please -ignore this is a test case.'
        severity = 4
        offering = offering_payload_model

        response = self.service.create_case(
            type,
            subject,
            description,
            severity=severity,
            offering=offering,
            headers={}
        )

        # Storing the new case number for subsequent test cases
        TestCaseManagementV1.new_case_number = response.result['number']

        assert response.get_status_code() == 200
        assert subject == response.result['short_description']
        assert description == response.result['description']

    def test_02_create_case_with_empty_offering(self):

        type = 'technical'
        subject = 'Python - Integration test'
        description = 'Please -ignore this is a test case.'
        severity = 4

        with pytest.raises(ApiException) as e:
            self.service.create_case(
                type,
                subject,
                description,
                severity=severity,
                headers={}
                )
        assert e.value.code == 400

    def test_03_create_case_with_empty_subject_and_description(self):

        # Offering info can be retrieved via /case-management/utilities/v1/offerings/technical
        offering_payload_type_model = {}
        offering_payload_type_model['group'] = 'crn_service_name'
        offering_payload_type_model['key'] = 'cloud-object-storage'
        offering_payload_type_model['id'] = 'dff97f5c-bc5e-4455-b470-411c3edbe49c'

        offering_payload_model = {}
        offering_payload_model['name'] = 'Cloud Object Storage'
        offering_payload_model['type'] = offering_payload_type_model

        type = 'technical'
        subject = ''
        description = ''
        severity = 4
        offering = offering_payload_model

        # Subject and description are required
        with pytest.raises(ApiException) as e:
            self.service.create_case(
                type,
                subject,
                description,
                severity=severity,
                offering=offering,
                headers={}
            )
        assert e.value.code == 500

    def test_04_get_cases(self):

        offset = 0
        limit = 2
        sort = 'number'
        fields = ['number']

        response = self.service.get_cases(
            offset=offset,
            limit=limit,
            sort=sort,
            fields=fields,
            headers={}
        )

        assert response.status_code == 200
        assert response.result['total_count'] > 0

    def test_05_get_case(self):

        fields = ['number', 'short_description']
        case_number = TestCaseManagementV1.new_case_number

        response = self.service.get_case(
            self.new_case_number,
            fields=fields,
            headers={}
        )

        assert TestCaseManagementV1.new_case_number == response.result['number']
        assert response.result['short_description'] != ''

    def test_06_get_case_with_invalid_field(self):

        fields = ['number', 'short_description', 'invalid_field']
        case_number = TestCaseManagementV1.new_case_number

        with pytest.raises(ApiException) as e:
            self.service.get_case(
                self.new_case_number,
                fields=fields,
                headers={}
            )
        assert e.value.code == 400

    def test_07_add_comment(self):

        case_number = TestCaseManagementV1.new_case_number
        comment = 'This is a test comment!'

        response = self.service.add_comment(
            case_number,
            comment,
            headers={}
        )

        assert response.status_code == 200
        assert comment == response.result["value"]

    def test_08_add_comment_to_nonexisting_case(self):

        case_number = 'fake-case-number'
        comment = 'This is a test comment!'

        with pytest.raises(ApiException) as e:
            self.service.add_comment(
                case_number,
                comment,
                headers={}
            )
        assert e.value.code == 404

    def test_09_add_watch_list_member(self):

        # Users can be retrieved via the User Management API.
        user_id_and_realm_model = {}
        user_id_and_realm_model['realm'] = 'IBMid'
        user_id_and_realm_model['user_id'] = 'abc@ibm.com'

        watchlist = [user_id_and_realm_model]

        response = self.service.add_watchlist(
            TestCaseManagementV1.new_case_number,
            watchlist=watchlist,
            headers={}
        )

        # Non-account member cannot be added to the watch-list,
        # therefore the response will include a "failed" list
        assert response.status_code == 200

        # Loop over all returned users and find the matching one by user id
        found_users = [user for user in response.result['failed']
            if user['user_id'] == user_id_and_realm_model['user_id']]
        assert len(found_users) == 1

    def test_10_file_upload(self):

        fileName = "test_file.txt"

        file_with_metadata_model = {}
        file_with_metadata_model['data'] = io.BytesIO(b'This is a mock file.').getvalue()
        file_with_metadata_model['filename'] = fileName

        file = [file_with_metadata_model]

        response = self.service.upload_file(
            TestCaseManagementV1.new_case_number,
            file,
            headers={}
        )

        TestCaseManagementV1.file_attachment_id = response.result['id']

        assert response.status_code == 200
        assert response.result['filename'] == fileName

    def test_11_download_file(self):

        response = self.service.download_file(
            TestCaseManagementV1.new_case_number,
            TestCaseManagementV1.file_attachment_id,
            headers={}
        )

        assert response.status_code == 200
        assert 'content-type' in response.headers

    def test_12_delete_file(self):

        response = self.service.delete_file(
            TestCaseManagementV1.new_case_number,
            TestCaseManagementV1.file_attachment_id,
            headers={}
        )

        assert response.status_code == 200
        # Assert the file attachment list is empty
        assert len(response.result['attachments']) == 0

    def test_13_add_resource(self):

        # Adding a resource requires a valid CRN (Cloud Resource Name)
        # CRN's can be retrieved via the Search and Tagging API
        crn = 'invalid:crn'
        type = 'testString'
        id = 36.0
        note = 'testString'

        with pytest.raises(ApiException) as e:
            response = self.service.add_resource(
                TestCaseManagementV1.new_case_number,
                crn=crn,
                type=type,
                id=id,
                note=note,
                headers={}
            )
        assert e.value.code == 500

    def test_14_resolve_case(self):

        status_payload = {}
        status_payload['action'] = 'resolve'
        status_payload['comment'] = 'testString'
        status_payload['resolution_code'] = 1

        response = self.service.update_case_status(
            TestCaseManagementV1.new_case_number,
            status_payload,
            headers={}
        )

        assert response.status_code == 200
        assert TestCaseManagementV1.new_case_number == response.result["number"]