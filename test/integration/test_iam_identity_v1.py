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
import pytest
import urllib.parse as urlparse
from urllib.parse import parse_qs
from ibm_cloud_sdk_core import *
from ibm_platform_services.iam_identity_v1 import *

# Location of our config file.
config_file = 'iam_identity.env'
apikeyName = 'Python-SDK-IT-ApiKey'
serviceIDName = 'Python-SDK-IT-ServiceId'
newDescription = 'This is an updated description'
apikeyList = []

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

            cls.config = read_external_sources(IamIdentityV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None
            assert cls.config["URL"] == cls.iam_identity_service.service_url

            cls.accountId = cls.config.get("ACCOUNT_ID")
            cls.iamId = cls.config.get("IAM_ID")
            cls.apikey = cls.config.get("APIKEY")

            assert cls.accountId is not None
            assert cls.iamId is not None
            assert cls.apikey is not None

        print('Setup complete.')
    @classmethod 
    def teardown_class(cls):
        print("Starting clean up...")
        cls.cleanupResources(cls)
        print("Clean up complete.")

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    def cleanupResources(self):
        # list apikeys
        list_api_keys_response = self.iam_identity_service.list_api_keys(
            account_id=self.accountId,
            iam_id=self.iamId,
            pagesize=100,
            include_history=True
        )
        assert list_api_keys_response.get_status_code() == 200
        api_key_list = list_api_keys_response.get_result()
        if len(api_key_list['apikeys']) > 0:
            for apikeys in api_key_list['apikeys']:
                if apikeys ['name'] == apikeyName:
                    delete_api_key_response = self.iam_identity_service.delete_api_key(
                        id= apikeys['id']
                    )
                    assert delete_api_key_response.get_status_code() == 204
        
        # list serviceIDs
        list_service_ids_response = self.iam_identity_service.list_service_ids(
            account_id=self.accountId,
            name=serviceIDName,
            pagesize=100
        )
        assert list_service_ids_response.get_status_code() == 200
        service_id_list = list_service_ids_response.get_result()
        if len(service_id_list['serviceids']) > 0:
            for serviceids in service_id_list['serviceids']:
                if serviceids ['name'] == serviceIDName:
                    delete_api_key_response = self.iam_identity_service.delete_service_id(
                        id= serviceids['id']
                    )
                    assert delete_api_key_response.get_status_code() == 204
        
    def getApikeybyID(self, apikeyID):
        get_api_key_response = self.iam_identity_service.get_api_key(
            id=apikeyID,
            include_history=True
        )
        apikey = get_api_key_response.get_result()
        
        return apikey
    
    def getServiceID(self, serviceID):
        get_service_id_response = self.iam_identity_service.get_service_id(
            id=serviceID,
            include_history=True
        )
        
        service_id = get_service_id_response.get_result()

        return service_id
    
    def getPageToken(self, url):
        assert url is not None
        parsed = urlparse.urlparse(url)
        return parse_qs(parsed.query)['pagetoken']

    @needscredentials
    def test_create_api_key1(self):

        create_api_key_response = self.iam_identity_service.create_api_key(
            name= apikeyName,
            iam_id=self.iamId,
            description='PythonSDK test apikey #1',
            account_id=self.accountId
        )

        assert create_api_key_response.get_status_code() == 201
        api_key = create_api_key_response.get_result()
        assert api_key is not None

        global apikeyID1
        apikeyID1 = api_key['id']
        assert apikeyID1 is not None

    @needscredentials
    def test_create_api_key2(self):

        create_api_key_response = self.iam_identity_service.create_api_key(
            name= apikeyName,
            iam_id=self.iamId,
            description='PythonSDK test apikey #2',
            account_id=self.accountId
        )

        assert create_api_key_response.get_status_code() == 201
        api_key = create_api_key_response.get_result()
        assert api_key is not None

        global apikeyID2
        apikeyID2 = api_key['id']
        assert apikeyID2 is not None

    @needscredentials
    def test_get_api_key(self):

        get_api_key_response = self.iam_identity_service.get_api_key(
            id=apikeyID1,
            include_history=True
        )

        assert get_api_key_response.get_status_code() == 200
        api_key = get_api_key_response.get_result()
        assert api_key is not None
    
        assert api_key['id'] == apikeyID1
        assert api_key['name'] == apikeyName
        assert api_key['iam_id'] == self.iamId
        assert api_key['account_id'] == self.accountId
        assert api_key['created_by'] == self.iamId
        assert api_key['created_at'] is not None
        assert api_key['locked'] == False
        assert api_key['crn'] is not None

        global apikeyEtag1
        apikeyEtag1 = api_key['entity_tag']
        apikeyEtag1 is not None

    @needscredentials
    def test_get_api_keys_details(self):
        get_api_keys_details_response = self.iam_identity_service.get_api_keys_details(
            iam_api_key=self.apikey,
            include_history=True
        )

        assert get_api_keys_details_response.get_status_code() == 200
        api_key = get_api_keys_details_response.get_result()
        assert api_key is not None

        assert api_key['iam_id'] == self.iamId
        assert api_key['account_id'] == self.accountId
        assert api_key['created_by'] == self.iamId
        assert api_key['created_at'] is not None
        assert api_key['locked'] == False
    
    @needscredentials
    def test_list_api_keys1(self):
        list_api_keys_response = self.iam_identity_service.list_api_keys(
            account_id=self.accountId,
            iam_id=self.iamId,
            pagesize=1,
            include_history=True
        )
        assert list_api_keys_response.get_status_code() == 200
        api_key_list = list_api_keys_response.get_result()
        assert api_key_list is not None

        # fetch pagetoken value
        global pagetoken 
        pagetoken = self.getPageToken(api_key_list['next'])
    
        if len(api_key_list['apikeys']) > 0:
            for apikeys in api_key_list['apikeys']:
                if apikeys ['name'] == apikeyName:
                    apikeyList.append(apikeys['name'])
    
    @needscredentials
    def test_list_api_keys2(self):
        apikeyList = []
        list_api_keys_response = self.iam_identity_service.list_api_keys(
            account_id=self.accountId,
            iam_id=self.iamId,
            pagetoken=pagetoken,
            include_history=True
        )
        assert list_api_keys_response.get_status_code() == 200
        api_key_list = list_api_keys_response.get_result()
        assert api_key_list is not None
        assert len(api_key_list['apikeys']) > 0
     
    @needscredentials
    def test_update_api_key(self):

        update_api_key_response = self.iam_identity_service.update_api_key(
            id=apikeyID1,
            if_match=apikeyEtag1,
            description='This is an updated description'
        )

        assert update_api_key_response.get_status_code() == 200
        api_key = update_api_key_response.get_result()
        assert api_key is not None
        assert api_key['description'] == 'This is an updated description'


    @needscredentials
    def test_lock_api_key(self):

        lock_api_key_response = self.iam_identity_service.lock_api_key(
            id=apikeyID1
        )

        assert lock_api_key_response.get_status_code() == 200

        apikeyResponse = self.getApikeybyID(apikeyID1)
        assert apikeyResponse is not None
        assert apikeyResponse['id'] == apikeyID1
        assert apikeyResponse['locked'] == True
    
    @needscredentials
    def test_unlock_api_key(self):

        unlock_api_key_response = self.iam_identity_service.unlock_api_key(
            id=apikeyID1
        )

        assert unlock_api_key_response.get_status_code() == 200

        apikeyResponse = self.getApikeybyID(apikeyID1)
        assert apikeyResponse is not None
        assert apikeyResponse['id'] == apikeyID1
        assert apikeyResponse['locked'] == False
    
    @needscredentials
    def test_delete_api_key1(self):

        delete_api_key_response = self.iam_identity_service.delete_api_key(
            id=apikeyID1
        )

        assert delete_api_key_response.get_status_code() == 204


    @needscredentials
    def test_delete_api_key2(self):

        delete_api_key_response = self.iam_identity_service.delete_api_key(
            id=apikeyID2
        )

        assert delete_api_key_response.get_status_code() == 204

    @needscredentials
    def test_create_service_id(self):

        create_service_id_response = self.iam_identity_service.create_service_id(
            account_id=self.accountId,
            name=serviceIDName,
            description='PythonSDK ServiceID desc',
        )

        assert create_service_id_response.get_status_code() == 201
        service_id = create_service_id_response.get_result()
        assert service_id is not None

        global serviceID
        serviceID = service_id['id']
        assert serviceID is not None

    @needscredentials
    def test_get_service_id(self):

        get_service_id_response = self.iam_identity_service.get_service_id(
            id=serviceID,
            include_history=True
        )

        assert get_service_id_response.get_status_code() == 200
        service_id = get_service_id_response.get_result()
        assert service_id is not None

        assert service_id['id'] == serviceID
        assert service_id['name'] == serviceIDName
        assert service_id['description'] == 'PythonSDK ServiceID desc'

        global serviceIDEtag
        serviceIDEtag = service_id['entity_tag']
        assert serviceIDEtag is not None

    @needscredentials
    def test_list_service_ids(self):

        list_service_ids_response = self.iam_identity_service.list_service_ids(
            account_id=self.accountId,
            name=serviceIDName,
            pagesize=100
        )

        assert list_service_ids_response.get_status_code() == 200
        service_id_list = list_service_ids_response.get_result()
        assert service_id_list is not None
        assert len(service_id_list['serviceids']) == 1

    @needscredentials
    def test_update_service_id(self):

        update_service_id_response = self.iam_identity_service.update_service_id(
            id=serviceID,
            if_match=serviceIDEtag,
            description='This is an updated description'
        )

        assert update_service_id_response.get_status_code() == 200
        service_id = update_service_id_response.get_result()
        assert service_id is not None

        assert service_id['description'] == 'This is an updated description'
        
    @needscredentials
    def test_lock_service_id(self):

        lock_service_id_response = self.iam_identity_service.lock_service_id(
            id=serviceID
        )

        assert lock_service_id_response.get_status_code() == 200
        service_id = lock_service_id_response.get_result()
        assert service_id is not None
        assert service_id['locked'] == True
        
        serviceIDResponse = self.getServiceID(serviceID)
        assert serviceIDResponse is not None
        assert serviceIDResponse['id'] == serviceID
        assert serviceIDResponse['locked'] == True

    @needscredentials
    def test_unlock_service_id(self):

        unlock_service_id_response = self.iam_identity_service.unlock_service_id(
            id=serviceID
        )

        assert unlock_service_id_response.get_status_code() == 200
        service_id = unlock_service_id_response.get_result()
        assert service_id is not None
        assert service_id['locked'] == False

        serviceIDResponse = self.getServiceID(serviceID)
        assert serviceIDResponse is not None
        assert serviceIDResponse['id'] == serviceID
        assert serviceIDResponse['locked'] == False

    @needscredentials
    def test_delete_service_id(self):

        delete_service_id_response = self.iam_identity_service.delete_service_id(
            id=serviceID
        )

        assert delete_service_id_response.get_status_code() == 204

