# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Integration Tests for IamIdentityV1
"""

import os
import json
import pytest
import urllib.parse as urlparse
from urllib.parse import parse_qs
from ibm_cloud_sdk_core import *
from ibm_platform_services.iam_identity_v1 import *

# Location of our config file.
config_file = 'iam_identity.env'

# Global variables used to share values between test operations.
apikey_id1 = None
apikey_etag1 = None
apikey_id2 = None

serviceid_id1 = None
serviceid_etag1 = None


class TestIamIdentityV1():
    """
    Integration Test Class for IamIdentityV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.iam_identity_service = IamIdentityV1.new_instance()
            assert cls.iam_identity_service is not None
            assert cls.iam_identity_service.service_url is not None

            cls.config = read_external_sources(
                IamIdentityV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None
            assert cls.config['URL'] == cls.iam_identity_service.service_url

            cls.account_id = cls.config['ACCOUNT_ID']
            cls.iam_id = cls.config['IAM_ID']
            cls.apikey = cls.config['APIKEY']

            assert cls.account_id is not None
            assert cls.iam_id is not None
            assert cls.apikey is not None

            cls.apikey_name = 'Python-SDK-IT-ApiKey'
            cls.serviceid_name = 'Python-SDK-IT-ServiceId'

            cls.cleanup_resources()

        print('Setup complete.')

    @classmethod
    def teardown_class(cls):
        cls.cleanup_resources()

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @classmethod
    def cleanup_resources(cls):
        print('\nCleaning up resources...')
        # list apikeys
        response = cls.iam_identity_service.list_api_keys(
            account_id=cls.account_id,
            iam_id=cls.iam_id,
            pagesize=100,
        )
        assert response.get_status_code() == 200
        api_key_list = response.get_result()
        if len(api_key_list['apikeys']) > 0:
            for apikey in api_key_list['apikeys']:
                if apikey['name'] == cls.apikey_name:
                    print('>>> deleting apikey: ', apikey['id'])
                    delete_response = cls.iam_identity_service.delete_api_key(
                        id=apikey['id']
                    )
                    assert delete_response.get_status_code() == 204

        # list serviceIDs
        response = cls.iam_identity_service.list_service_ids(
            account_id=cls.account_id,
            name=cls.serviceid_name,
            pagesize=100
        )
        assert response.get_status_code() == 200
        service_id_list = response.get_result()
        if len(service_id_list['serviceids']) > 0:
            for serviceid in service_id_list['serviceids']:
                if serviceid['name'] == cls.serviceid_name:
                    print('>>> deleting serviceid: ', serviceid['id'])
                    delete_response = cls.iam_identity_service.delete_service_id(
                        id=serviceid['id']
                    )
                    assert delete_response.get_status_code() == 204

        print('Finished cleaning up resources!')

    def get_api_key(self, service, resource_id):
        try:
            response = service.get_api_key(id=resource_id)
            return response.get_result()
        except Exception:
            return None

    def get_service_id(self, service, resource_id):
        try:
            response = service.get_service_id(id=resource_id)
            return response.get_result()
        except Exception:
            return None

    def get_page_token(self, url):
        if url is None:
            return None
        try:
            parsed = urlparse.urlparse(url)
            query_value = parse_qs(parsed.query).get('pagetoken')
            if query_value is not None:
                return query_value[0]
            return None
        except Exception:
            return None

    @needscredentials
    def test_create_api_key1(self):
        create_api_key_response = self.iam_identity_service.create_api_key(
            name=self.apikey_name,
            iam_id=self.iam_id,
            description='PythonSDK test apikey #1',
            account_id=self.account_id
        )

        assert create_api_key_response.get_status_code() == 201
        api_key = create_api_key_response.get_result()
        assert api_key is not None
        print('\ncreate_api_key1() response: ', json.dumps(api_key, indent=2))

        global apikey_id1
        apikey_id1 = api_key['id']
        assert apikey_id1 is not None

    @needscredentials
    def test_create_api_key2(self):
        create_api_key_response = self.iam_identity_service.create_api_key(
            name=self.apikey_name,
            iam_id=self.iam_id,
            description='PythonSDK test apikey #2',
            account_id=self.account_id
        )

        assert create_api_key_response.get_status_code() == 201
        api_key = create_api_key_response.get_result()
        assert api_key is not None
        print('\ncreate_api_key2() response: ', json.dumps(api_key, indent=2))

        global apikey_id2
        apikey_id2 = api_key['id']
        assert apikey_id2 is not None

    @needscredentials
    def test_get_api_key(self):
        global apikey_id1
        assert apikey_id1 is not None

        get_api_key_response = self.iam_identity_service.get_api_key(
            id=apikey_id1,
            include_history=True
        )

        assert get_api_key_response.get_status_code() == 200
        api_key = get_api_key_response.get_result()
        assert api_key is not None
        print('\nget_api_key response: ', json.dumps(api_key, indent=2))

        assert api_key['id'] == apikey_id1
        assert api_key['name'] == self.apikey_name
        assert api_key['iam_id'] == self.iam_id
        assert api_key['account_id'] == self.account_id
        assert api_key['created_by'] == self.iam_id
        assert api_key['created_at'] is not None
        assert api_key['locked'] == False
        assert api_key['crn'] is not None

        global apikey_etag1
        apikey_etag1 = get_api_key_response.get_headers()['Etag']
        apikey_etag1 is not None

    @needscredentials
    def test_get_api_keys_details(self):
        get_api_keys_details_response = self.iam_identity_service.get_api_keys_details(
            iam_api_key=self.apikey
        )

        assert get_api_keys_details_response.get_status_code() == 200
        api_key = get_api_keys_details_response.get_result()
        assert api_key is not None
        print('\nget_api_key_details() response: ',
              json.dumps(api_key, indent=2))

        assert api_key['iam_id'] == self.iam_id
        assert api_key['account_id'] == self.account_id
        assert api_key['created_by'] == self.iam_id
        assert api_key['created_at'] is not None
        assert api_key['locked'] == False

    @needscredentials
    def test_list_api_keys(self):
        apikeys = []

        # Retrieve one apikey at a time to test the pagination.
        pagetoken = None
        pagetoken_present = True
        while pagetoken_present:
            list_api_keys_response = self.iam_identity_service.list_api_keys(
                account_id=self.account_id,
                iam_id=self.iam_id,
                pagesize=1,
                pagetoken=pagetoken
            )
            assert list_api_keys_response.get_status_code() == 200
            api_key_list = list_api_keys_response.get_result()
            assert api_key_list is not None
            print('\nlist_api_keys() response: ',
                  json.dumps(api_key_list, indent=2))

            if len(api_key_list['apikeys']) > 0:
                for apikey in api_key_list['apikeys']:
                    if apikey['name'] == self.apikey_name:
                        apikeys.append(apikey)

            # fetch pagetoken value
            pagetoken = self.get_page_token(api_key_list.get('next'))
            pagetoken_present = (pagetoken is not None)

        # make sure we retrieved the two apikeys that we created previously.
        assert len(apikeys) == 2

    @needscredentials
    def test_update_api_key(self):
        global apikey_id1
        assert apikey_id1 is not None

        global apikey_etag1
        assert apikey_etag1 is not None

        new_description = 'This is an updated description'
        update_api_key_response = self.iam_identity_service.update_api_key(
            id=apikey_id1,
            if_match=apikey_etag1,
            description=new_description
        )

        assert update_api_key_response.get_status_code() == 200
        api_key = update_api_key_response.get_result()
        print('\nupdate_api_key() response: ', json.dumps(api_key, indent=2))
        assert api_key is not None
        assert api_key['description'] == new_description

    @needscredentials
    def test_lock_api_key(self):
        global apikey_id1
        assert apikey_id1 is not None

        lock_api_key_response = self.iam_identity_service.lock_api_key(
            id=apikey_id1
        )

        assert lock_api_key_response.get_status_code() == 204

        api_key = self.get_api_key(
            self.iam_identity_service, apikey_id1)
        assert api_key is not None
        assert api_key['id'] == apikey_id1
        assert api_key['locked'] == True

    @needscredentials
    def test_unlock_api_key(self):
        global apikey_id1
        assert apikey_id1 is not None

        unlock_api_key_response = self.iam_identity_service.unlock_api_key(
            id=apikey_id1
        )

        assert unlock_api_key_response.get_status_code() == 204

        api_key = self.get_api_key(self.iam_identity_service, apikey_id1)
        assert api_key is not None
        assert api_key['id'] == apikey_id1
        assert api_key['locked'] == False

    @needscredentials
    def test_delete_api_key1(self):
        global apikey_id1
        assert apikey_id1 is not None

        delete_api_key_response = self.iam_identity_service.delete_api_key(
            id=apikey_id1
        )

        assert delete_api_key_response.get_status_code() == 204

        api_key = self.get_api_key(self.iam_identity_service, apikey_id1)
        assert api_key is None

    @needscredentials
    def test_delete_api_key2(self):
        global apikey_id2
        assert apikey_id2 is not None

        delete_api_key_response = self.iam_identity_service.delete_api_key(
            id=apikey_id2
        )

        assert delete_api_key_response.get_status_code() == 204

        api_key = self.get_api_key(self.iam_identity_service, apikey_id2)
        assert api_key is None

    @needscredentials
    def test_create_service_id(self):
        create_service_id_response = self.iam_identity_service.create_service_id(
            account_id=self.account_id,
            name=self.serviceid_name,
            description='PythonSDK test serviceid',
        )

        assert create_service_id_response.get_status_code() == 201
        service_id = create_service_id_response.get_result()
        assert service_id is not None
        print('\ncreate_service_id() response: ',
              json.dumps(service_id, indent=2))

        global serviceid_id1
        serviceid_id1 = service_id['id']
        assert serviceid_id1 is not None

    @needscredentials
    def test_get_service_id(self):
        global serviceid_id1
        assert serviceid_id1 is not None

        get_service_id_response = self.iam_identity_service.get_service_id(
            id=serviceid_id1,
            include_history=True
        )

        assert get_service_id_response.get_status_code() == 200
        service_id = get_service_id_response.get_result()
        assert service_id is not None
        print('\nget_service_id() response: ',
              json.dumps(service_id, indent=2))

        assert service_id['id'] == serviceid_id1
        assert service_id['name'] == self.serviceid_name

        global serviceid_etag1
        serviceid_etag1 = get_service_id_response.get_headers()['Etag']
        serviceid_etag1 is not None

    @needscredentials
    def test_list_service_ids(self):

        list_service_ids_response = self.iam_identity_service.list_service_ids(
            account_id=self.account_id,
            name=self.serviceid_name,
            pagesize=100
        )

        assert list_service_ids_response.get_status_code() == 200
        service_id_list = list_service_ids_response.get_result()
        print('\nlist_service_ids() response: ',
              json.dumps(service_id_list, indent=2))

        assert service_id_list is not None
        assert len(service_id_list['serviceids']) == 1

    @needscredentials
    def test_update_service_id(self):
        global serviceid_id1
        assert serviceid_id1 is not None

        global serviceid_etag1
        assert serviceid_etag1 is not None

        new_description = 'This is an updated description'

        update_service_id_response = self.iam_identity_service.update_service_id(
            id=serviceid_id1,
            if_match=serviceid_etag1,
            description=new_description
        )

        assert update_service_id_response.get_status_code() == 200
        service_id = update_service_id_response.get_result()
        assert service_id is not None
        print('\nupdate_service_id() response: ',
              json.dumps(service_id, indent=2))
        assert service_id['description'] == new_description

    @needscredentials
    def test_lock_service_id(self):
        global serviceid_id1
        assert serviceid_id1 is not None

        lock_service_id_response = self.iam_identity_service.lock_service_id(
            id=serviceid_id1
        )

        assert lock_service_id_response.get_status_code() == 204

        service_id = self.get_service_id(
            self.iam_identity_service, serviceid_id1)
        assert service_id is not None
        assert service_id['locked'] == True

    @needscredentials
    def test_unlock_service_id(self):
        global serviceid_id1
        assert serviceid_id1 is not None

        unlock_service_id_response = self.iam_identity_service.unlock_service_id(
            id=serviceid_id1
        )

        assert unlock_service_id_response.get_status_code() == 204

        service_id = self.get_service_id(
            self.iam_identity_service, serviceid_id1)
        assert service_id is not None
        assert service_id['locked'] == False

    @needscredentials
    def test_delete_service_id(self):
        global serviceid_id1
        assert serviceid_id1 is not None

        delete_service_id_response = self.iam_identity_service.delete_service_id(
            id=serviceid_id1
        )

        assert delete_service_id_response.get_status_code() == 204

        service_id = self.get_service_id(
            self.iam_identity_service, serviceid_id1)
        assert service_id is None

    @needscredentials
    def test_get_account_settings(self):

        get_account_settings_response = self.iam_identity_service.get_account_settings(
            account_id='testString',
            include_history=True
        )

        assert get_account_settings_response.get_status_code() == 200
        account_settings_response = get_account_settings_response.get_result()
        assert account_settings_response is not None

    @needscredentials
    def test_update_account_settings(self):

        update_account_settings_response = self.iam_identity_service.update_account_settings(
            if_match='testString',
            account_id='testString',
            restrict_create_service_id='RESTRICTED',
            restrict_create_platform_apikey='RESTRICTED',
            allowed_ip_addresses='testString',
            mfa='NONE',
            session_expiration_in_seconds='testString',
            session_invalidation_in_seconds='testString'
        )

        assert update_account_settings_response.get_status_code() == 200
        account_settings_response = update_account_settings_response.get_result()
        assert account_settings_response is not None
