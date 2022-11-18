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
import time
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

profile_id1 = None
profile_id2 = None
profile_iamId = None
profile_etag = None

claimRule_id1 = None
claimRule_id2 = None
claimRule_etag = None

link_id = None

account_setting_etag = None

report_reference = None

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
            cls.profile_name1 = 'Python-SDK-IT-Profile1'
            cls.profile_name2 = 'Python-SDK-IT-Profile2'
            cls.claimRule_type = 'Profile-SAML'
            cls.realm_name = 'https://w3id.sso.ibm.com/auth/sps/samlidp2/saml20'

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

        # list profiles
        response = cls.iam_identity_service.list_profiles(
            account_id=cls.account_id
        )
        assert response.get_status_code() == 200
        profile_list = response.get_result()
        if len(profile_list['profiles']) > 0:
            for profile in profile_list['profiles']:
                if profile['name'] == cls.profile_name1 or profile['name'] == cls.profile_name2:
                    print('>>> deleting profile: ', profile['id'])
                    delete_response = cls.iam_identity_service.delete_profile(
                        profile_id=profile['id']
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

    def get_profile(self, service, resource_id):
        try:
            response = service.get_profile(id=resource_id)
            return response.get_result()
        except Exception:
            return None

    def get_claimRule(self, service, profileId, claimRuleId):
        try:
            response = service.get_claim_rule(profile_id=profileId,rule_id=claimRuleId)
            return response.get_result()
        except Exception:
            return None

    def get_link(self, service, profileId, linkId):
        try:
            response = service.get_link(profile_id=profileId,link_id=linkId)
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
            include_history=True,
            include_activity=True,
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
            include_history=True,
            include_activity=True,
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
    def test_create_profile1(self):
        create_profile_response = self.iam_identity_service.create_profile(
            name=self.profile_name1,
            description='PythonSDK test profile #1',
            account_id=self.account_id
        )

        assert create_profile_response.get_status_code() == 201
        profile = create_profile_response.get_result()
        assert profile is not None
        print('\ncreate_profile1() response: ', json.dumps(profile, indent=2))

        global profile_id1
        global profile_iamId
        profile_id1 = profile['id']
        profile_iamId = profile['iam_id']
        assert profile_id1 is not None
        assert profile_iamId is not None

    @needscredentials
    def test_create_profile2(self):
        create_profile_response = self.iam_identity_service.create_profile(
            name=self.profile_name2,
            description='PythonSDK test profile #2',
            account_id=self.account_id
        )

        assert create_profile_response.get_status_code() == 201
        profile = create_profile_response.get_result()
        assert profile is not None
        print('\ncreate_profile1() response: ', json.dumps(profile, indent=2))

        global profile_id2
        profile_id2 = profile['id']
        assert profile_id2 is not None

    @needscredentials
    def test_get_profile(self):
        global profile_id1
        assert profile_id1 is not None

        get_profile_response = self.iam_identity_service.get_profile(
            profile_id=profile_id1,
            include_activity=True,
        )

        assert get_profile_response.get_status_code() == 200
        profile = get_profile_response.get_result()
        assert profile is not None
        print('\nget_profile response: ', json.dumps(profile, indent=2))

        assert profile['id'] == profile_id1
        assert profile['name'] == self.profile_name1
        assert profile['iam_id'] == profile_iamId
        assert profile['account_id'] == self.account_id
        assert profile['crn'] is not None

        global profile_etag
        profile_etag = get_profile_response.get_headers()['Etag']
        profile_etag is not None

    @needscredentials
    def test_list_profiles(self):
        profiles = []

        pagetoken = None
        pagetoken_present = True
        while pagetoken_present:
            list_profiles_response = self.iam_identity_service.list_profiles(
                account_id=self.account_id,
                pagesize=1,
                pagetoken=pagetoken,
                include_history= False
            )
            assert list_profiles_response.get_status_code() == 200
            profile_list = list_profiles_response.get_result()
            assert profile_list is not None
            print('\nlist_profiles() response: ',
                  json.dumps(profile_list, indent=2))

            if len(profile_list['profiles']) > 0:
                for profile in profile_list['profiles']:
                    if profile['name'] == self.profile_name1 or profile['name'] == self.profile_name2:
                        profiles.append(profile)

            pagetoken = self.get_page_token(profile_list.get('next'))
            pagetoken_present = (pagetoken is not None)

        assert len(profiles) == 2

    @needscredentials
    def test_update_profile(self):
        global profile_id1
        assert profile_id1 is not None

        global profile_etag
        assert profile_etag is not None

        new_description = 'This is an updated description'
        update_profile_response = self.iam_identity_service.update_profile(
            profile_id=profile_id1,
            if_match=profile_etag,
            description=new_description
        )

        assert update_profile_response.get_status_code() == 200
        profile = update_profile_response.get_result()
        print('\nupdate_profile() response: ', json.dumps(profile, indent=2))
        assert profile is not None
        assert profile['description'] == new_description

    @needscredentials
    def test_delete_profile1(self):
        global profile_id1
        assert profile_id1 is not None

        delete_profile_response = self.iam_identity_service.delete_profile(
            profile_id=profile_id1
        )

        assert delete_profile_response.get_status_code() == 204

        profile = self.get_profile(self.iam_identity_service, profile_id1)
        assert profile is None

    @needscredentials
    def test_create_claimRule1(self):
        profile_claim_rule_conditions_model = {}
        profile_claim_rule_conditions_model['claim'] = 'blueGroups'
        profile_claim_rule_conditions_model['operator'] = 'EQUALS'
        profile_claim_rule_conditions_model['value'] = '\"cloud-docs-dev\"'

        create_claimRule_response = self.iam_identity_service.create_claim_rule(
            profile_id = profile_id2,
            type = self.claimRule_type,
            realm_name = self.realm_name,
            expiration = 43200,
            conditions = [profile_claim_rule_conditions_model]
        )

        assert create_claimRule_response.get_status_code() == 201
        claimRule = create_claimRule_response.get_result()
        assert claimRule is not None
        print('\ncreate_profile1() response: ', json.dumps(claimRule, indent=2))

        global claimRule_id1
        claimRule_id1 = claimRule['id']
        assert claimRule_id1 is not None

    @needscredentials
    def test_create_claimRule2(self):
        profile_claim_rule_conditions_model = {}
        profile_claim_rule_conditions_model['claim'] = 'blueGroups'
        profile_claim_rule_conditions_model['operator'] = 'EQUALS'
        profile_claim_rule_conditions_model['value'] = '\"Europe_Group\"'

        create_claimRule_response = self.iam_identity_service.create_claim_rule(
            profile_id = profile_id2,
            type = self.claimRule_type,
            realm_name = self.realm_name,
            expiration = 43200,
            conditions = [profile_claim_rule_conditions_model]
        )

        assert create_claimRule_response.get_status_code() == 201
        claimRule = create_claimRule_response.get_result()
        assert claimRule is not None
        print('\ncreate_profile1() response: ', json.dumps(claimRule, indent=2))

        global claimRule_id2
        claimRule_id2 = claimRule['id']
        assert claimRule_id2 is not None

    @needscredentials
    def test_get_claimRule(self):
        global claimRule_id1
        assert claimRule_id1 is not None

        get_claimRule_response = self.iam_identity_service.get_claim_rule(
            profile_id=profile_id2,
            rule_id=claimRule_id1
        )

        assert get_claimRule_response.get_status_code() == 200
        claimRule = get_claimRule_response.get_result()
        assert claimRule is not None
        print('\nget_claimRule response: ', json.dumps(claimRule, indent=2))

        assert claimRule['id'] == claimRule_id1
        assert claimRule['type'] == self.claimRule_type
        assert claimRule['realm_name'] == self.realm_name
        assert claimRule['conditions'] is not None

        global claimRule_etag
        claimRule_etag = get_claimRule_response.get_headers()['Etag']
        claimRule_etag is not None

    @needscredentials
    def test_list_claimRules(self):
        claimRules = []

        list_claimRules_response = self.iam_identity_service.list_claim_rules(
            profile_id=profile_id2
        )
        assert list_claimRules_response.get_status_code() == 200
        claimRule_list = list_claimRules_response.get_result()
        assert claimRule_list is not None
        print('\nlist_claimRules() response: ',
            json.dumps(claimRule_list, indent=2))

        if len(claimRule_list['rules']) > 0:
            for claimRule in claimRule_list['rules']:
                if claimRule['id'] == claimRule_id1 or claimRule['id'] == claimRule_id2:
                    claimRules.append(claimRule)

        assert len(claimRules) == 2

    @needscredentials
    def test_update_claimRule(self):
        global claimRule_id1
        assert claimRule_id1 is not None

        global claimRule_etag
        assert claimRule_etag is not None

        profile_claim_rule_conditions_model = {}
        profile_claim_rule_conditions_model['claim'] = 'blueGroups'
        profile_claim_rule_conditions_model['operator'] = 'EQUALS'
        profile_claim_rule_conditions_model['value'] = '\"Europe_Group\"'

        update_claimRule_response = self.iam_identity_service.update_claim_rule(
            profile_id = profile_id2,
            rule_id = claimRule_id1,
            if_match = claimRule_etag,
            expiration = 33200,
            conditions = [profile_claim_rule_conditions_model],
            type = self.claimRule_type,
            realm_name = self.realm_name
        )

        assert update_claimRule_response.get_status_code() == 200
        claimRule = update_claimRule_response.get_result()
        print('\nupdate_claimRule() response: ', json.dumps(claimRule, indent=2))
        assert claimRule is not None

    @needscredentials
    def test_delete_claimRule1(self):
        global claimRule_id1
        assert claimRule_id1 is not None

        delete_claimRule_response = self.iam_identity_service.delete_claim_rule(
            profile_id=profile_id2,
            rule_id=claimRule_id1
        )

        assert delete_claimRule_response.get_status_code() == 204

        claimRule = self.get_claimRule(self.iam_identity_service, profile_id2, claimRule_id1)
        assert claimRule is None

    @needscredentials
    def test_delete_claimRule2(self):
        global claimRule_id2
        assert claimRule_id2 is not None

        delete_claimRule_response = self.iam_identity_service.delete_claim_rule(
            profile_id=profile_id2,
            rule_id=claimRule_id2
        )

        assert delete_claimRule_response.get_status_code() == 204

        claimRule = self.get_claimRule(self.iam_identity_service, profile_id2, claimRule_id2)
        assert claimRule is None

    @needscredentials
    def test_create_link(self):
        CreateProfileLinkRequestLink = {}
        CreateProfileLinkRequestLink['crn'] = 'crn:v1:staging:public:iam-identity::a/'+ self.account_id +'::computeresource:Fake-Compute-Resource'
        CreateProfileLinkRequestLink['namespace'] = 'default'
        CreateProfileLinkRequestLink['name'] = 'nice name'

        create_link_response = self.iam_identity_service.create_link(
            profile_id = profile_id2,
            name = 'nice link',
            cr_type = 'ROKS_SA',
            link = CreateProfileLinkRequestLink
        )

        assert create_link_response.get_status_code() == 201
        link = create_link_response.get_result()
        assert link is not None
        print('\ncreate_link() response: ', json.dumps(link, indent=2))

        global link_id
        link_id = link['id']
        assert link_id is not None

    @needscredentials
    def test_get_link(self):
        global link_id
        assert link_id is not None

        get_link_response = self.iam_identity_service.get_link(
            profile_id=profile_id2,
            link_id=link_id
        )

        assert get_link_response.get_status_code() == 200
        link = get_link_response.get_result()
        assert link is not None
        print('\nget_claimRule response: ', json.dumps(link, indent=2))

        assert link['id'] == link_id
        assert link['name'] == 'nice link'
        assert link['cr_type'] == 'ROKS_SA'
        assert link['link'] is not None

    @needscredentials
    def test_list_links(self):
        links = []

        list_links_response = self.iam_identity_service.list_links(
            profile_id=profile_id2
        )
        assert list_links_response.get_status_code() == 200
        links_list = list_links_response.get_result()
        assert links_list is not None
        print('\nlist_links() response: ',
            json.dumps(links_list, indent=2))

        if len(links_list['links']) > 0:
            for link in links_list['links']:
                if link['id'] == link_id:
                    links.append(link)

        assert len(links) == 1

    @needscredentials
    def test_delete_link(self):
        global link_id
        assert link_id is not None

        delete_link_response = self.iam_identity_service.delete_link(
            profile_id=profile_id2,
            link_id=link_id
        )

        assert delete_link_response.get_status_code() == 204

        link = self.get_link(self.iam_identity_service, profile_id2, link_id)
        assert link is None

    @needscredentials
    def test_delete_profile2(self):
        global profile_id2
        assert profile_id2 is not None

        delete_profile_response = self.iam_identity_service.delete_profile(
            profile_id=profile_id2
        )

        assert delete_profile_response.get_status_code() == 204

        profile = self.get_profile(self.iam_identity_service, profile_id2)
        assert profile is None

    def test_create_profile_bad_request(self):
        with pytest.raises(ApiException) as e:
            self.iam_identity_service.create_profile(
                name=self.profile_name1,
                description='PythonSDK test profile #1',
                account_id='invalid'
            )
        assert e.value.code == 400

    def test_get_profile_not_found(self):
        with pytest.raises(ApiException) as e:
            self.iam_identity_service.get_profile(
                profile_id='invalid'
            )
        assert e.value.code == 404

    def test_update_profile_not_found(self):
        with pytest.raises(ApiException) as e:
            self.iam_identity_service.update_profile(
                profile_id='invalid',
                if_match='invalid',
                description='invalid'
            )
        assert e.value.code == 404

    def test_delete_profile_not_found(self):
        with pytest.raises(ApiException) as e:
            self.iam_identity_service.delete_profile(
                profile_id='invalid'
            )
        assert e.value.code == 404

    def test_create_claimRule_bad_request(self):
        profile_claim_rule_conditions_model = {}
        profile_claim_rule_conditions_model['claim'] = 'blueGroups'
        profile_claim_rule_conditions_model['operator'] = 'EQUALS'
        profile_claim_rule_conditions_model['value'] = '\"cloud-docs-dev\"'
        with pytest.raises(ApiException) as e:
            self.iam_identity_service.create_claim_rule(
                profile_id = 'invalid',
                type = self.claimRule_type,
                realm_name = self.realm_name,
                expiration = 43200,
                conditions = [profile_claim_rule_conditions_model]
            )
        assert e.value.code == 404

    def test_get_claimRule_not_found(self):
        with pytest.raises(ApiException) as e:
            self.iam_identity_service.get_claim_rule(
                profile_id='invalid',
                rule_id='invalid'
            )
        assert e.value.code == 404

    def test_update_claimRule_not_found(self):
        profile_claim_rule_conditions_model = {}
        profile_claim_rule_conditions_model['claim'] = 'blueGroups'
        profile_claim_rule_conditions_model['operator'] = 'EQUALS'
        profile_claim_rule_conditions_model['value'] = '\"Europe_Group\"'
        with pytest.raises(ApiException) as e:
            self.iam_identity_service.update_claim_rule(
                profile_id = 'invalid',
                rule_id = 'invalid',
                if_match = 'invalid',
                expiration = 33200,
                conditions = [profile_claim_rule_conditions_model],
                type = self.claimRule_type,
                realm_name = self.realm_name
            )
        assert e.value.code == 404

    def test_delete_claimRule_not_found(self):
        with pytest.raises(ApiException) as e:
            self.iam_identity_service.delete_claim_rule(
                profile_id='invalid',
                rule_id='invalid'
            )
        assert e.value.code == 404

    def test_create_link_bad_request(self):
        CreateProfileLinkRequestLink = {}
        CreateProfileLinkRequestLink['crn'] = 'crn:v1:staging:public:iam-identity::a/' + self.account_id + '::computeresource:Fake-Compute-Resource'
        CreateProfileLinkRequestLink['namespace'] = 'default'
        CreateProfileLinkRequestLink['name'] = 'nice name'
        with pytest.raises(ApiException) as e:
            self.iam_identity_service.create_link(
                profile_id = 'invalid',
                name = 'nice link',
                cr_type = 'ROKS_SA',
                link = CreateProfileLinkRequestLink
            )
        assert e.value.code == 404

    def test_get_link_not_found(self):
        with pytest.raises(ApiException) as e:
            self.iam_identity_service.get_link(
                profile_id='invalid',
                link_id='invalid'
            )
        assert e.value.code == 404

    def test_delete_link_not_found(self):
        with pytest.raises(ApiException) as e:
            self.iam_identity_service.delete_link(
                profile_id='invalid',
                link_id='invalid'
            )
        assert e.value.code == 404

    @needscredentials
    def test_get_account_settings(self):
        global account_setting_etag
        assert account_setting_etag is None

        get_account_settings_response = self.iam_identity_service.get_account_settings(
            account_id=self.account_id,
            include_history=False
        )

        assert get_account_settings_response.get_status_code() == 200
        settings = get_account_settings_response.get_result()
        assert settings is not None

        assert settings["account_id"] == self.account_id
        assert settings["restrict_create_service_id"] is not None
        assert settings["restrict_create_platform_apikey"] is not None
        assert settings["entity_tag"] is not None
        assert settings["mfa"] is not None
        assert settings["history"] is not None
        assert settings["session_expiration_in_seconds"] is not None
        assert settings["session_invalidation_in_seconds"] is not None

        account_setting_etag = get_account_settings_response.get_headers()['Etag']
        assert account_setting_etag is not None

    @needscredentials
    def test_update_account_settings(self):
        global account_setting_etag
        assert account_setting_etag is not None

        update_account_settings_response = self.iam_identity_service.update_account_settings(
            if_match=account_setting_etag,
            account_id=self.account_id,
            restrict_create_service_id="NOT_RESTRICTED",
            restrict_create_platform_apikey="NOT_RESTRICTED",
            # allowed_ip_addresses='testString',
            mfa='NONE',
            session_expiration_in_seconds="86400",
            session_invalidation_in_seconds="7200",
            max_sessions_per_identity='10',
        )

        assert update_account_settings_response.get_status_code() == 200
        settings = update_account_settings_response.get_result()
        assert settings is not None
        print('\ntest_update_account_settings() response: ',
              json.dumps(settings, indent=2))

        assert settings["account_id"] == self.account_id
        assert settings["restrict_create_service_id"] == "NOT_RESTRICTED"
        assert settings["restrict_create_platform_apikey"] == "NOT_RESTRICTED"
        assert settings["entity_tag"] != account_setting_etag
        assert settings["mfa"] == "NONE"
        assert settings["history"] is not None
        assert settings["session_expiration_in_seconds"] == "86400"
        assert settings["session_invalidation_in_seconds"] == "7200"

    @needscredentials
    def test_create_report(self):
        global report_reference
        assert report_reference is None

        create_report_response = self.iam_identity_service.create_report(
            account_id=self.account_id,
            type="inactive",
            duration="120",
        )

        assert create_report_response.get_status_code() == 202
        reportReference = create_report_response.get_result()
        assert reportReference is not None
        print('\ncreate_report() response: ', json.dumps(reportReference, indent=2))


        report_reference = reportReference['reference']
        assert report_reference is not None

    @needscredentials
    def test_get_inactivity_report_incomplete(self):
        get_report_response = self.iam_identity_service.get_report(
            account_id=self.account_id,
            reference=report_reference,
        )

        assert get_report_response.get_status_code() == 204
        report = get_report_response.get_result()

    @needscredentials
    def test_get_inactivity_report_complete(self):
        get_report_response = self.iam_identity_service.get_report(
            account_id=self.account_id,
            reference=report_reference,
        )

        for x in range(30):
            get_report_response = self.iam_identity_service.get_report(
              account_id=self.account_id,
              reference=report_reference,
            )

            if(get_report_response.get_status_code()!=204):
              report = get_report_response.get_result()
              assert report is not None
              assert report['created_by'] is not None
              assert report['reference'] is not None
              assert report['report_duration'] is not None
              assert report['report_start_time'] is not None
              assert report['report_end_time'] is not None
              break
            time.sleep(1)
    @needscredentials
    def test_get_inactivity_report_notfound(self):
        with pytest.raises(ApiException) as e:
            self.iam_identity_service.get_report(
                account_id=self.account_id,
                reference='test123',
            )
        assert e.value.code == 404

