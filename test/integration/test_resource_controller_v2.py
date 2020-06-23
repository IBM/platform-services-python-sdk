# coding: utf-8

# Copyright 2019 IBM All Rights Reserved.
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
 This class contains an integration test for the Resource Controller service.
"""

import pytest
import unittest
import os
import os.path
import uuid
import time
from ibm_cloud_sdk_core import *
from ibm_platform_services.resource_controller_v2 import *
from dotenv import load_dotenv

# Read config file
configFile = 'resource_controller.env'

class TestResourceControllerV2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if os.path.exists(configFile):
            os.environ['IBM_CREDENTIALS_FILE'] = configFile
        else:
            raise unittest.SkipTest('External configuration not available, skipping...')
        
        cls.service = ResourceControllerV2.new_instance()
        assert cls.service is not None

        cls.testAccountId = 'bc2b2fca0af84354a916dc1de6eee42e'
        cls.testResourceGroupGuid = '13aa3ee48c3b44ddb64c05c79f7ab8ef'
        cls.testOrgGuid = 'd35d4f0e-5076-4c89-9361-2522894b6548'
        cls.testSpaceGuid = '336ba5f3-f185-488e-ac8d-02195eebb2f3'
        cls.testAppGuid = 'bf692181-1f0e-46be-9faf-eb0857f4d1d5'
        cls.testRegionId1 = 'global';
        cls.testPlanId1 = 'a10e4820-3685-11e9-b210-d663bd873d93'
        cls.testRegionId2 = 'us-south';
        cls.testPlanId2 = '2580b607-db64-4883-9793-445b694ed57b'

        cls.testInstanceCrn = ''
        cls.testInstanceGuid = ''
        cls.testAliasCrn = ''
        cls.testAliasGuid = ''
        cls.testBindingCrn = ''
        cls.testBindingGuid = ''
        cls.testInstanceKeyCrn = ''
        cls.testInstanceKeyGuid = ''
        cls.testAliasKeyCrn = ''
        cls.testAliasKeyGuid = ''
        cls.aliasTargetCrn = ''
        cls.bindTargetCrn = ''
        cls.testReclaimInstanceCrn = ''
        cls.testReclaimInstanceGuid = ''
        cls.testReclamationId1 = ''
        cls.testReclamationId2 = ''

        cls.transactionId = str(uuid.uuid4())
        print('\nTransaction-Id for Test Run: ' + cls.transactionId)
        print('Setup complete.')
        
    @classmethod
    def tearDownClass(cls):
        cls.cleanupResources()
        cls.cleanupReclamationInstance()
        print('\nClean up complete.')

    def test_00_create_resource_instance(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test00-" + self.transactionId

        response = self.service.create_resource_instance(
            "RcSdkInstance1", 
            self.testRegionId1,
            self.testResourceGroupGuid,
            self.testPlanId1,
            headers=customHeaders
        )
        assert response is not None
        assert response.get_status_code() == 201

        result = response.get_result()
        assert result is not None
        assert result.get('id') is not None
        assert result.get('guid') is not None
        assert result.get('crn') is not None
        assert result.get('id') == result.get('crn')
        assert result.get('name') == "RcSdkInstance1"
        assert result.get('account_id') == self.testAccountId
        assert result.get('resource_group_id') == self.testResourceGroupGuid
        assert result.get('resource_plan_id') == self.testPlanId1
        assert result.get('state') == "active"
        assert not result.get('locked')
        assert result.get('last_operation').get('type') == "create"
        assert not result.get('last_operation').get('async')
        assert result.get('last_operation').get('state') == "succeeded"

        self.__class__.testInstanceCrn = result.get('id')
        self.__class__.testInstanceGuid = result.get('guid')
        assert self.testInstanceCrn != ''
        assert self.testInstanceGuid != '' 

    def test_01_get_resource_instance(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test01-" + self.transactionId

        response = self.service.get_resource_instance(self.testInstanceGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testInstanceCrn
        assert result.get('guid') == self.testInstanceGuid
        assert result.get('crn') == self.testInstanceCrn
        assert result.get('name') == "RcSdkInstance1"
        assert result.get('account_id') == self.testAccountId
        assert result.get('resource_group_id') == self.testResourceGroupGuid
        assert result.get('resource_plan_id') == self.testPlanId1
        assert result.get('state') == "active"
        assert not result.get('locked')
        assert result.get('last_operation').get('type') == "create"
        assert not result.get('last_operation').get('async')
        assert result.get('last_operation').get('state') == "succeeded"

    def test_02_update_resource_instance(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test02-" + self.transactionId

        params = {}
        params["hello"] = "bye"

        response = self.service.update_resource_instance(
            self.testInstanceGuid,
            name="RcSdkInstanceUpdate1",
            parameters=params,
            headers=customHeaders
        )
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testInstanceCrn
        assert result.get('name') == "RcSdkInstanceUpdate1"
        assert result.get('state') == "active"
        assert result.get('last_operation').get('type') == "update"
        assert result.get('last_operation').get('sub_type') == "config"
        assert not result.get('last_operation').get('async')
        assert result.get('last_operation').get('state') == "succeeded"

    def test_03_list_resource_instances_no_filter(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test03-" + self.transactionId

        response = self.service.list_resource_instances(headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert len(result.get('resources')) >= 1
        assert result.get('rows_count') >= 1

    def test_04_list_resource_instances_by_guid(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test04-" + self.transactionId

        response = self.service.list_resource_instances(guid=self.testInstanceGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert len(result.get('resources')) == 1
        assert result.get('rows_count') == 1

        instance = result.get('resources')[0]
        assert instance.get('id') == self.testInstanceCrn
        assert instance.get('guid') == self.testInstanceGuid
        assert instance.get('name') == "RcSdkInstanceUpdate1"
        assert instance.get('state') == "active"
        assert instance.get('last_operation').get('type') == "update"
        assert instance.get('last_operation').get('sub_type') == "config"
        assert not instance.get('last_operation').get('async')
        assert instance.get('last_operation').get('state') == "succeeded"

    def test_05_list_resource_instances_by_name(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test05-" + self.transactionId

        response = self.service.list_resource_instances(name='RcSdkInstance1', headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert len(result.get('resources')) == 0
        assert result.get('rows_count') == 0

    def test_06_create_resource_alias(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test06-" + self.transactionId 

        target = "crn:v1:bluemix:public:bluemix:us-south:o/" + self.testOrgGuid + "::cf-space:" + self.testSpaceGuid
        self.__class__.aliasTargetCrn = "crn:v1:bluemix:public:cf:us-south:o/" + self.testOrgGuid + "::cf-space:" + self.testSpaceGuid
        assert self.aliasTargetCrn != '' 

        response = self.service.create_resource_alias(
            "RcSdkAlias1", 
            self.testInstanceGuid,
            target,
            headers=customHeaders
        )
        assert response is not None
        assert response.get_status_code() == 201

        result = response.get_result()
        assert result is not None
        assert result.get('id') is not None
        assert result.get('guid') is not None
        assert result.get('crn') is not None
        assert result.get('id') == result.get('crn')
        assert result.get('name') == "RcSdkAlias1"
        assert result.get('account_id') == self.testAccountId
        assert result.get('resource_group_id') == self.testResourceGroupGuid
        assert result.get('target_crn') == self.aliasTargetCrn
        assert result.get('state') == "active"
        assert result.get('resource_instance_id') == self.testInstanceCrn

        self.__class__.testAliasCrn = result.get('id')
        self.__class__.testAliasGuid = result.get('guid')
        assert self.testAliasCrn != ''
        assert self.testAliasGuid != '' 

    def test_07_get_resource_alias(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test07-" + self.transactionId

        response = self.service.get_resource_alias(self.testAliasGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testAliasCrn
        assert result.get('guid') == self.testAliasGuid
        assert result.get('crn') == self.testAliasCrn
        assert result.get('name') == "RcSdkAlias1"
        assert result.get('account_id') == self.testAccountId
        assert result.get('resource_group_id') == self.testResourceGroupGuid
        assert result.get('target_crn') == self.aliasTargetCrn
        assert result.get('state') == "active"
        assert result.get('resource_instance_id') == self.testInstanceCrn

    def test_08_update_resource_alias(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test08-" + self.transactionId

        response = self.service.update_resource_alias(
            self.testAliasGuid,
            name="RcSdkAliasUpdate1",
            headers=customHeaders
        )
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testAliasCrn
        assert result.get('name') == "RcSdkAliasUpdate1"
        assert result.get('state') == "active"

    def test_09_list_resource_aliases_no_filter(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test09-" + self.transactionId

        response = self.service.list_resource_aliases(headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert len(result.get('resources')) >= 1
        assert result.get('rows_count') >= 1

    def test_10_list_resource_aliases_by_guid(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test10-" + self.transactionId

        response = self.service.list_resource_aliases(guid=self.testAliasGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert len(result.get('resources')) == 1
        assert result.get('rows_count') == 1

        alias = result.get('resources')[0]
        assert alias.get('id') == self.testAliasCrn
        assert alias.get('guid') == self.testAliasGuid
        assert alias.get('name') == "RcSdkAliasUpdate1"
        assert alias.get('resource_group_id') == self.testResourceGroupGuid
        assert alias.get('target_crn') == self.aliasTargetCrn
        assert alias.get('state') == "active"
        assert alias.get('resource_instance_id') == self.testInstanceCrn

    def test_11_list_resource_aliases_by_name(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test11-" + self.transactionId

        response = self.service.list_resource_aliases(name='RcSdkAlias1', headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert len(result.get('resources')) == 0
        assert result.get('rows_count') == 0

    def test_12_create_resource_binding(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test12-" + self.transactionId 

        target = "crn:v1:staging:public:bluemix:us-south:s/" + self.testSpaceGuid + "::cf-application:" + self.testAppGuid
        self.__class__.bindTargetCrn = "crn:v1:staging:public:cf:us-south:s/" + self.testSpaceGuid + "::cf-application:" + self.testAppGuid
        assert self.bindTargetCrn != '' 

        response = self.service.create_resource_binding(
            self.testAliasGuid,
            target,
            name="RcSdkBinding1", 
            headers=customHeaders
        )
        assert response is not None
        assert response.get_status_code() == 201

        result = response.get_result()
        assert result is not None
        assert result.get('id') is not None
        assert result.get('guid') is not None
        assert result.get('crn') is not None
        assert result.get('id') == result.get('crn')
        assert result.get('name') == "RcSdkBinding1"
        assert result.get('account_id') == self.testAccountId
        assert result.get('resource_group_id') == self.testResourceGroupGuid
        assert result.get('source_crn') == self.testAliasCrn
        assert result.get('target_crn') == self.bindTargetCrn
        assert result.get('state') == "active"

        self.__class__.testBindingCrn = result.get('id')
        self.__class__.testBindingGuid = result.get('guid')
        assert self.testBindingCrn != ''
        assert self.testBindingGuid != '' 

    def test_13_get_resource_binding(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test13-" + self.transactionId

        response = self.service.get_resource_binding(self.testBindingGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testBindingCrn
        assert result.get('guid') == self.testBindingGuid
        assert result.get('crn') == self.testBindingCrn
        assert result.get('name') == "RcSdkBinding1"
        assert result.get('account_id') == self.testAccountId
        assert result.get('resource_group_id') == self.testResourceGroupGuid
        assert result.get('source_crn') == self.testAliasCrn
        assert result.get('target_crn') == self.bindTargetCrn
        assert result.get('state') == "active"

    def test_14_update_resource_alias(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test14-" + self.transactionId

        response = self.service.update_resource_binding(self.testBindingGuid, "RcSdkBindingUpdate1", headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testBindingCrn
        assert result.get('name') == "RcSdkBindingUpdate1"
        assert result.get('state') == "active"

    def test_15_list_resource_bindings_no_filter(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test15-" + self.transactionId

        response = self.service.list_resource_bindings(headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert len(result.get('resources')) >= 1
        assert result.get('rows_count') >= 1

    def test_16_list_resource_bindings_by_guid(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test16-" + self.transactionId

        response = self.service.list_resource_bindings(guid=self.testBindingGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert len(result.get('resources')) == 1
        assert result.get('rows_count') == 1

        binding = result.get('resources')[0]
        assert binding.get('id') == self.testBindingCrn
        assert binding.get('guid') == self.testBindingGuid
        assert binding.get('name') == "RcSdkBindingUpdate1"
        assert binding.get('resource_group_id') == self.testResourceGroupGuid
        assert binding.get('source_crn') == self.testAliasCrn
        assert binding.get('target_crn') == self.bindTargetCrn
        assert binding.get('state') == "active"

    def test_17_list_resource_bindings_by_name(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test17-" + self.transactionId

        response = self.service.list_resource_bindings(name='RcSdkBinding1', headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert len(result.get('resources')) == 0
        assert result.get('rows_count') == 0

    def test_18_create_resource_key_for_instance(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test18-" + self.transactionId

        response = self.service.create_resource_key('RcSdkKey1', self.testInstanceGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 201

        result = response.get_result()
        assert result is not None
        assert result.get('id') is not None
        assert result.get('guid') is not None
        assert result.get('crn') is not None
        assert result.get('id') == result.get('crn')
        assert result.get('name') == "RcSdkKey1"
        assert result.get('account_id') == self.testAccountId
        assert result.get('resource_group_id') == self.testResourceGroupGuid
        assert result.get('source_crn') == self.testInstanceCrn
        assert result.get('state') == "active"

        self.__class__.testInstanceKeyCrn = result.get('id')
        self.__class__.testInstanceKeyGuid = result.get('guid')
        assert self.testInstanceKeyCrn != ''
        assert self.testInstanceKeyGuid != '' 

    def test_19_get_resource_key(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test19-" + self.transactionId

        response = self.service.get_resource_key(self.testInstanceKeyGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testInstanceKeyCrn
        assert result.get('guid') == self.testInstanceKeyGuid
        assert result.get('crn') == self.testInstanceKeyCrn
        assert result.get('name') == "RcSdkKey1"
        assert result.get('account_id') == self.testAccountId
        assert result.get('resource_group_id') == self.testResourceGroupGuid
        assert result.get('source_crn') == self.testInstanceCrn
        assert result.get('state') == "active"

    def test_20_update_resource_key(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test20-" + self.transactionId

        response = self.service.update_resource_key(self.testInstanceKeyGuid, "RcSdkKeyUpdate1", headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testInstanceKeyCrn
        assert result.get('name') == "RcSdkKeyUpdate1"
        assert result.get('state') == "active"

    def test_21_list_resource_keys_no_filter(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test21-" + self.transactionId

        response = self.service.list_resource_keys(headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert len(result.get('resources')) >= 1
        assert result.get('rows_count') >= 1

    def test_22_list_resource_keys_by_guid(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test22-" + self.transactionId

        response = self.service.list_resource_keys(guid=self.testInstanceKeyGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert len(result.get('resources')) == 1
        assert result.get('rows_count') == 1

        key = result.get('resources')[0]
        assert key.get('id') == self.testInstanceKeyCrn
        assert key.get('guid') == self.testInstanceKeyGuid
        assert key.get('name') == "RcSdkKeyUpdate1"
        assert key.get('resource_group_id') == self.testResourceGroupGuid
        assert key.get('source_crn') == self.testInstanceCrn
        assert key.get('state') == "active"

    def test_23_list_resource_keys_by_name(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test23-" + self.transactionId

        response = self.service.list_resource_keys(name='RcSdkKey1', headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert len(result.get('resources')) == 0
        assert result.get('rows_count') == 0

    def test_24_create_resource_key_for_alias(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test24-" + self.transactionId

        response = self.service.create_resource_key('RcSdkKey2', self.testAliasGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 201

        result = response.get_result()
        assert result is not None
        assert result.get('id') is not None
        assert result.get('guid') is not None
        assert result.get('crn') is not None
        assert result.get('id') == result.get('crn')
        assert result.get('name') == "RcSdkKey2"
        assert result.get('account_id') == self.testAccountId
        assert result.get('resource_group_id') == self.testResourceGroupGuid
        assert result.get('source_crn') == self.testAliasCrn
        assert result.get('state') == "active"

        self.__class__.testAliasKeyCrn = result.get('id')
        self.__class__.testAliasKeyGuid = result.get('guid')
        assert self.testAliasKeyCrn != ''
        assert self.testAliasKeyCrn != '' 

    def test_25_get_resource_key(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test25-" + self.transactionId

        response = self.service.get_resource_key(self.testAliasKeyGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testAliasKeyCrn
        assert result.get('guid') == self.testAliasKeyGuid
        assert result.get('crn') == self.testAliasKeyCrn
        assert result.get('name') == "RcSdkKey2"
        assert result.get('account_id') == self.testAccountId
        assert result.get('resource_group_id') == self.testResourceGroupGuid
        assert result.get('source_crn') == self.testAliasCrn
        assert result.get('state') == "active"

    def test_26_update_resource_key(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test26-" + self.transactionId

        response = self.service.update_resource_key(self.testAliasKeyGuid, "RcSdkKeyUpdate2", headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testAliasKeyCrn
        assert result.get('name') == "RcSdkKeyUpdate2"
        assert result.get('state') == "active"

    def test_27_list_resource_keys_no_filter(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test27-" + self.transactionId

        response = self.service.list_resource_keys(headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert len(result.get('resources')) >= 1
        assert result.get('rows_count') >= 1

    def test_28_list_resource_keys_by_guid(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test28-" + self.transactionId

        response = self.service.list_resource_keys(guid=self.testAliasKeyGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert len(result.get('resources')) == 1
        assert result.get('rows_count') == 1

        key = result.get('resources')[0]
        assert key.get('id') == self.testAliasKeyCrn
        assert key.get('guid') == self.testAliasKeyGuid
        assert key.get('name') == "RcSdkKeyUpdate2"
        assert key.get('resource_group_id') == self.testResourceGroupGuid
        assert key.get('source_crn') == self.testAliasCrn
        assert key.get('state') == "active"

    def test_29_list_resource_keys_by_name(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test29-" + self.transactionId

        response = self.service.list_resource_keys(name='RcSdkKey2', headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert len(result.get('resources')) == 0
        assert result.get('rows_count') == 0

    def test_30_delete_resource_alias_fail(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test30-" + self.transactionId

        with pytest.raises(ApiException) as e:
            response = self.service.delete_resource_alias(self.testAliasGuid, headers=customHeaders)
            assert response is not None
            assert response.get_status_code() == 400

    def test_31_delete_resource_instance_fail(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test31-" + self.transactionId

        with pytest.raises(ApiException) as e:
            response = self.service.delete_resource_instance(self.testInstanceGuid, headers=customHeaders)
            assert response is not None
            assert response.get_status_code() == 400

    def test_32_delete_resource_binding(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test32-" + self.transactionId

        response = self.service.delete_resource_binding(self.testBindingGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 204

    def test_33_verify_resource_binding_was_deleted(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test33-" + self.transactionId

        response = self.service.get_resource_binding(self.testBindingGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testBindingCrn
        assert result.get('state') == "removed"

    def test_34_delete_resource_keys(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test34-" + self.transactionId

        response = self.service.delete_resource_key(self.testInstanceKeyGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 204

        customHeaders2 = {}
        customHeaders2["Transaction-Id"] = "rc-sdk-python-test34-" + self.transactionId

        response2 = self.service.delete_resource_key(self.testAliasKeyGuid, headers=customHeaders2)
        assert response2 is not None
        assert response2.get_status_code() == 204

    def test_35_verify_resource_keys_were_deleted(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test35-" + self.transactionId

        response = self.service.get_resource_key(self.testInstanceKeyGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testInstanceKeyCrn
        assert result.get('state') == "removed"

        customHeaders2 = {}
        customHeaders2["Transaction-Id"] = "rc-sdk-python-test35-" + self.transactionId

        response2 = self.service.get_resource_key(self.testAliasKeyGuid, headers=customHeaders2)
        assert response2 is not None
        assert response2.get_status_code() == 200

        result2 = response2.get_result()
        assert result2 is not None
        assert result2.get('id') == self.testAliasKeyCrn
        assert result2.get('state') == "removed"

    def test_36_delete_resource_alias(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test36-" + self.transactionId

        response = self.service.delete_resource_alias(self.testAliasGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 204

    def test_37_verify_resource_alias_was_deleted(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test37-" + self.transactionId

        response = self.service.get_resource_alias(self.testAliasGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testAliasCrn
        assert result.get('state') == "removed"

    def test_38_lock_resource_instance(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test38-" + self.transactionId

        response = self.service.lock_resource_instance(self.testInstanceGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testInstanceCrn
        assert result.get('locked')
        assert result.get('last_operation').get('type') == "lock"
        assert not result.get('last_operation').get('async')
        assert result.get('last_operation').get('state') == "succeeded"

    def test_39_update_locked_resource_instance_fail(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test39-" + self.transactionId

        with pytest.raises(ApiException) as e:
            response = self.service.update_resource_instance(
                self.testInstanceGuid, 
                name='RcSdkLockedInstanceUpdate1',
                headers=customHeaders
            )
            assert response is not None
            assert response.get_status_code() == 400

    def test_40_delete__locked_resource_instance_fail(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test40-" + self.transactionId

        with pytest.raises(ApiException) as e:
            response = self.service.delete_resource_instance(self.testInstanceGuid, headers=customHeaders)
            assert response is not None
            assert response.get_status_code() == 400

    def test_41_unlock_resource_instance(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test41-" + self.transactionId

        response = self.service.unlock_resource_instance(self.testInstanceGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testInstanceCrn
        assert not result.get('locked')
        assert result.get('last_operation').get('type') == "unlock"
        assert not result.get('last_operation').get('async')
        assert result.get('last_operation').get('state') == "succeeded"

    def test_42_delete_resource_instance(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test42-" + self.transactionId

        response = self.service.delete_resource_instance(self.testInstanceGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 204

    def test_43_verify_resource_instance_was_deleted(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test43-" + self.transactionId

        response = self.service.get_resource_instance(self.testInstanceGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testInstanceCrn
        assert result.get('state') == "removed"

    def test_44_create_resource_instance_for_reclamation_enabled_plan(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test44-" + self.transactionId 

        response = self.service.create_resource_instance(
            "RcSdkReclaimInstance1", 
            self.testRegionId2,
            self.testResourceGroupGuid,
            self.testPlanId2,
            headers=customHeaders
        )
        assert response is not None
        assert response.get_status_code() == 201

        result = response.get_result()
        assert result is not None
        assert result.get('id') is not None
        assert result.get('guid') is not None
        assert result.get('crn') is not None
        assert result.get('id') == result.get('crn')
        assert result.get('name') == "RcSdkReclaimInstance1"
        assert result.get('account_id') == self.testAccountId
        assert result.get('resource_group_id') == self.testResourceGroupGuid
        assert result.get('resource_plan_id') == self.testPlanId2
        assert result.get('state') == "active"
        assert not result.get('locked')
        assert result.get('last_operation').get('type') == "create"
        assert not result.get('last_operation').get('async')
        assert result.get('last_operation').get('state') == "succeeded"

        self.__class__.testReclaimInstanceCrn = result.get('id')
        self.__class__.testReclaimInstanceGuid = result.get('guid')
        assert self.testReclaimInstanceCrn != ''
        assert self.testReclaimInstanceGuid != '' 

    def test_45_schedule_resource_instance_for_reclamation(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test45-" + self.transactionId

        response = self.service.delete_resource_instance(self.testReclaimInstanceGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 204

        time.sleep(20)

    def test_46_verify_resource_instance_is_pending_reclamation(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test46-" + self.transactionId

        response = self.service.get_resource_instance(self.testReclaimInstanceGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testReclaimInstanceCrn
        assert result.get('state') == "pending_reclamation"
        assert result.get('last_operation').get('type') == "reclamation"
        assert result.get('last_operation').get('sub_type') == "pending"
        assert not result.get('last_operation').get('async')
        assert result.get('last_operation').get('state') == "succeeded"

    def test_47_list_reclamation_for_account_id(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test47-" + self.transactionId

        response = self.service.list_reclamations(
            account_id=self.testAccountId,
            headers=customHeaders
        )
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert len(result.get('resources')) >= 1

        foundReclamation = False
        for res in result.get('resources'):
            if res.get('resource_instance_id') == self.testReclaimInstanceGuid:
                assert res.get('resource_instance_id') == self.testReclaimInstanceGuid
                assert res.get('account_id') == self.testAccountId
                assert res.get('resource_group_id') == self.testResourceGroupGuid
                assert res.get('state') == 'SCHEDULED'

                foundReclamation = True
                self.__class__.testReclamationId1 = res.get('id')
        assert foundReclamation
        assert self.testReclamationId1 != ''

    def test_48_restore_resource_instance(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test48-" + self.transactionId

        response = self.service.run_reclamation_action(self.testReclamationId1, 'restore', headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result.get('id') == self.testReclamationId1
        assert result.get('resource_instance_id') == self.testReclaimInstanceGuid
        assert result.get('account_id') == self.testAccountId
        assert result.get('resource_group_id') == self.testResourceGroupGuid
        assert result.get('state') == 'RESTORING'

        time.sleep(20)

    def test_49_verify_resource_instance_is_restored(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test49-" + self.transactionId

        response = self.service.get_resource_instance(self.testReclaimInstanceGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testReclaimInstanceCrn
        assert result.get('state') == "active"
        assert result.get('last_operation').get('type') == "reclamation"
        assert result.get('last_operation').get('sub_type') == "restore"
        assert not result.get('last_operation').get('async')
        assert result.get('last_operation').get('state') == "succeeded"

    def test_50_schedule_resource_instance_for_reclamation2(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test50-" + self.transactionId

        response = self.service.delete_resource_instance(self.testReclaimInstanceGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 204

        time.sleep(20)

    def test_51_list_reclamation_for_account_id_and_resource_instance_id(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test51-" + self.transactionId

        response = self.service.list_reclamations(
            account_id=self.testAccountId,
            resource_instance_id=self.testReclaimInstanceGuid,
            headers=customHeaders
        )
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert len(result.get('resources')) == 1

        res = result.get('resources')[0]
        assert res.get('resource_instance_id') == self.testReclaimInstanceGuid
        assert res.get('account_id') == self.testAccountId
        assert res.get('resource_group_id') == self.testResourceGroupGuid
        assert res.get('state') == 'SCHEDULED'

        self.__class__.testReclamationId2 = res.get('id')
        assert self.testReclamationId2 != ''

    def test_52_reclaim_resource_instance(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test52-" + self.transactionId

        response = self.service.run_reclamation_action(self.testReclamationId2, 'reclaim', headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result.get('id') == self.testReclamationId2
        assert result.get('resource_instance_id') == self.testReclaimInstanceGuid
        assert result.get('account_id') == self.testAccountId
        assert result.get('resource_group_id') == self.testResourceGroupGuid
        assert result.get('state') == 'RECLAIMING'

        time.sleep(20)

    def test_53_verify_resource_instance_is_reclaimed(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "rc-sdk-python-test53-" + self.transactionId

        response = self.service.get_resource_instance(self.testReclaimInstanceGuid, headers=customHeaders)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('id') == self.testReclaimInstanceCrn
        assert result.get('state') == "removed"
        assert result.get('last_operation').get('type') == "reclamation"
        assert result.get('last_operation').get('sub_type') == "delete"
        assert not result.get('last_operation').get('async')
        assert result.get('last_operation').get('state') == "succeeded"

    @classmethod
    def cleanupResources(cls):
        if cls.testInstanceKeyGuid != '':
            try:
                customHeaders = {}
                customHeaders["Transaction-Id"] = "rc-sdk-python-cleanup-" + cls.transactionId
                cls.service.delete_resource_key(cls.testInstanceKeyGuid, headers=customHeaders)
                print('\nSuccessfully cleaned up key ' + cls.testInstanceKeyGuid + '.')
            except ApiException as errResponse:
                if errResponse.code == 410:
                    print('\nKey ' + cls.testInstanceKeyGuid + ' was already deleted by the tests.')
                else:
                    print('\nFailed to clean up key ' + cls.testInstanceKeyGuid + '. Error: ' + errResponse.message)
        else:
            print('\nKey was not created. No cleanup needed.')

        if cls.testAliasKeyGuid != '':
            try:
                customHeaders = {}
                customHeaders["Transaction-Id"] = "rc-sdk-python-cleanup-" + cls.transactionId
                cls.service.delete_resource_key(cls.testAliasKeyGuid, headers=customHeaders)
                print('\nSuccessfully cleaned up key ' + cls.testAliasKeyGuid + '.')
            except ApiException as errResponse:
                if errResponse.code == 410:
                    print('\nKey ' + cls.testAliasKeyGuid + ' was already deleted by the tests.')
                else:
                    print('\nFailed to clean up key ' + cls.testAliasKeyGuid + '. Error: ' + errResponse.message)
        else:
            print('\nKey was not created. No cleanup needed.')

        if cls.testBindingGuid != '':
            try:
                customHeaders = {}
                customHeaders["Transaction-Id"] = "rc-sdk-python-cleanup-" + cls.transactionId
                cls.service.delete_resource_binding(cls.testBindingGuid, headers=customHeaders)
                print('\nSuccessfully cleaned up binding ' + cls.testBindingGuid + '.')
            except ApiException as errResponse:
                if errResponse.code == 410:
                    print('\nBinding ' + cls.testBindingGuid + ' was already deleted by the tests.')
                else:
                    print('\nFailed to clean up binding ' + cls.testBindingGuid + '. Error: ' + errResponse.message)
        else:
            print('\nBinding was not created. No cleanup needed.')

        if cls.testAliasGuid != '':
            try:
                customHeaders = {}
                customHeaders["Transaction-Id"] = "rc-sdk-python-cleanup-" + cls.transactionId
                cls.service.delete_resource_alias(cls.testAliasGuid, headers=customHeaders)
                print('\nSuccessfully cleaned up alias ' + cls.testAliasGuid + '.')
            except ApiException as errResponse:
                if errResponse.code == 410:
                    print('\nAlias ' + cls.testAliasGuid + ' was already deleted by the tests.')
                else:
                    print('\nFailed to clean up alias ' + cls.testAliasGuid + '. Error: ' + errResponse.message)
        else:
            print('\nAlias was not created. No cleanup needed.')

        if cls.testInstanceGuid != '':
            cls.cleanupInstance()
        else:
            print('\nInstance was not created. No cleanup needed.')

    @classmethod
    def cleanupInstance(cls):
        try:
            customHeaders = {}
            customHeaders["Transaction-Id"] = "rc-sdk-python-cleanup-" + cls.transactionId
            response = cls.service.get_resource_instance(cls.testInstanceGuid, headers=customHeaders)
        except ApiException as errResponse:
            print('\nFailed to retrieve instance ' + cls.testInstanceGuid + ' for cleanup. Error: ' + errResponse.message)
        else:
            if response.get_result().get('state') == "active" and response.get_result().get('locked'):
                try:
                    customHeaders = {}
                    customHeaders["Transaction-Id"] = "rc-sdk-python-cleanup-" + cls.transactionId
                    cls.service.unlock_resource_instance(cls.testInstanceGuid, headers=customHeaders)
                    print('\nSuccessfully unlocked instance ' + cls.testInstanceGuid + ' for cleanup.')
                except ApiException as errResponse:
                    print('\nFailed to unlock instance ' + cls.testInstanceGuid + ' for cleanup. Error: ' + errResponse.message)

        try:
            customHeaders = {}
            customHeaders["Transaction-Id"] = "rc-sdk-python-cleanup-" + cls.transactionId
            cls.service.delete_resource_instance(cls.testInstanceGuid, headers=customHeaders)
            print('\nSuccessfully cleaned up instance ' + cls.testInstanceGuid + '.')
        except ApiException as errResponse:
            if errResponse.code == 410:
                print('\nInstance ' + cls.testInstanceGuid + ' was already deleted by the tests.')
            else:
                print('\nFailed to clean up instance ' + cls.testInstanceGuid + '. Error: ' + errResponse.message)
    
    @classmethod
    def cleanupReclamationInstance(cls):
        if cls.testReclaimInstanceGuid != '':
            try:
                customHeaders = {}
                customHeaders["Transaction-Id"] = "rc-sdk-python-cleanup-" + cls.transactionId
                response = cls.service.get_resource_instance(cls.testReclaimInstanceGuid, headers=customHeaders)
            except ApiException as errResponse:
                print('\nFailed to retrieve instance ' + cls.testReclaimInstanceGuid + ' for cleanup. Error: ' + errResponse.message)
            else:
                if response.get_result().get('state') == "removed":
                    print('\nInstance ' + cls.testReclaimInstanceGuid + ' was already reclaimed by the tests.')
                elif response.get_result().get('state') == "pending_reclamation":
                    cls.cleanupInstancePendingReclamation()
                else:
                    try:
                        customHeaders = {}
                        customHeaders["Transaction-Id"] = "rc-sdk-python-cleanup-" + cls.transactionId
                        cls.service.delete_resource_instance(cls.testReclaimInstanceGuid, headers=customHeaders)
                        print('\nSuccessfully scheduled instance ' + cls.testReclaimInstanceGuid + ' for reclamation.')
                    except ApiException as errResponse:
                        print('\nFailed to schedule instance ' + cls.testReclaimInstanceGuid + ' for reclamation. Error: ' + errResponse.message)
                    else:
                        time.sleep(20)
                        cls.cleanupInstancePendingReclamation()
        else:
            print('\nReclamation instance was not created. No cleanup needed.')

    @classmethod
    def cleanupInstancePendingReclamation(cls):
        try:
            customHeaders = {}
            customHeaders["Transaction-Id"] = "rc-sdk-python-cleanup-" + cls.transactionId
            response = cls.service.list_reclamations(
                account_id=cls.testAccountId,
                resource_instance_id=cls.testReclaimInstanceGuid,
                headers=customHeaders
            )
        except ApiException as errResponse:
            print('\nFailed to retrieve reclamation to process to reclaim instance ' + cls.testReclaimInstanceGuid + ' for cleanup. Error: ' + errResponse.message)
        else:
            res = response.get_result().get('resources')
            if len(res) == 0:
                print('\nNo reclamations for instance ' + cls.testReclaimInstanceGuid + ' were returned.')
            else:
                reclamationId = res[0].get('id')
                try:
                    customHeaders = {}
                    customHeaders["Transaction-Id"] = "rc-sdk-python-cleanup-" + cls.transactionId
                    response = cls.service.run_reclamation_action(reclamationId, 'reclaim', headers=customHeaders)
                    print('\nSuccessfully reclaimed instance ' + cls.testReclaimInstanceGuid)
                except ApiException as errResponse:
                    print('\nFailed to process reclamation ' + reclamationId + ' for instance ' + cls.testInstanceGuid + '. Error: ' + errResponse.message)

    