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
 This class contains an integration test for the Open Service Broker service.
"""

import pytest
import unittest
import os
import os.path
import uuid
import time
from ibm_cloud_sdk_core import *
from ibm_platform_services.open_service_broker_v1 import *

# Read config file
configFile = 'open_service_broker.env'


class TestOpenServiceBrokerV1(unittest.TestCase):
    """
    Integration Test Class for OpenServiceBrokerV1
    """

    @classmethod
    def setUpClass(cls):
        if os.path.exists(configFile):
            os.environ['IBM_CREDENTIALS_FILE'] = configFile
        else:
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        cls.service = OpenServiceBrokerV1.new_instance()
        assert cls.service is not None

        cls.testAccountId = 'bc2b2fca0af84354a916dc1de6eee42e'
        cls.testResourceGroupGuid = '13aa3ee48c3b44ddb64c05c79f7ab8ef'
        cls.testOrgGuid = 'd35d4f0e-5076-4c89-9361-2522894b6548'
        cls.testSpaceGuid = '336ba5f3-f185-488e-ac8d-02195eebb2f3'
        cls.testAppGuid = 'bf692181-1f0e-46be-9faf-eb0857f4d1d5'
        cls.testPlanId1 = 'a10e4820-3685-11e9-b210-d663bd873d93'
        cls.testPlanId2 = 'a10e4410-3685-11e9-b210-d663bd873d933'
        cls.testPlanId3 = 'a10e4960-3685-11e9-b210-d663bd873d93'
        cls.testInstanceId = 'crn:v1:staging:public:bss-monitor:global:a/bc2b2fca0af84354a916dc1de6eee42e:sdkTestInstance::'
        cls.testInstanceId2 = 'crn:v1:staging:public:bss-monitor:us-south:a/bc2b2fca0af84354a916dc1de6eee42e:osb-sdk-test00:resource-binding:osb-sdk-binding-test00'
        cls.testBindingId = 'crn:v1:staging:public:bss-monitor:us-south:a/bc2b2fca0af84354a916dc1de6eee42e:sdkTestInstance:resource-binding:sdkTestBinding'
        cls.testBindingId2 = 'crnL:v1:staging:public:bss-monitor:global:a/bc2b2fca0af84354a916dc1de6eee42e:osb-sdk-test00::'

        cls.testPlatform = 'ibmcloud'
        cls.testReasonCode = 'test_reason'
        cls.testInitiatorId = 'test_initiator'
        cls.testDashboardUrlEscaped = 'http://www.example.com/crn%3Av1%3Astaging%3Apublic%3Abss-monitor%3Aglobal%3Aa%2Fbc2b2fca0af84354a916dc1de6eee42e%3AsdkTestInstance%3A%3A'
        cls.testDashboardUrl = 'http://www.example.com/crn:v1:staging:public:bss-monitor:global:a/bc2b2fca0af84354a916dc1de6eee42e:sdkTestInstance::'
        cls.transactionId = str(uuid.uuid4())
        cls.testInstanceIdEscaped = 'crn%3Av1%3Astaging%3Apublic%3Abss-monitor%3Aglobal%3Aa%2Fbc2b2fca0af84354a916dc1de6eee42e%3AsdkTestInstance%3A%3A'
        cls.testInstanceId2Escaped = 'crn%3Av1%3Astaging%3Apublic%3Abss-monitor%3Aus-south%3Aa%2Fbc2b2fca0af84354a916dc1de6eee42e%3Aosb-sdk-test00%3Aresource-binding%3Aosb-sdk-binding-test00'
        cls.testBindingIdEscaped = 'crn%3Av1%3Astaging%3Apublic%3Abss-monitor%3Aus-south%3Aa%2Fbc2b2fca0af84354a916dc1de6eee42e%3AsdkTestInstance%3Aresource-binding%3AsdkTestBinding'
        cls.testBindingId2Escaped = 'crn%3Av1%3Astaging%3Apublic%3Abss-monitor%3Aglobal%3Aa%2Fbc2b2fca0af84354a916dc1de6eee42e%3Aosb-sdk-test00%3A%3A'
        cls.testServiceId = 'a10e46ae-3685-11e9-b210-d663bd873d93'
        cls.testEnable = True

        print('\nTransaction-Id for Test Run: ' + cls.transactionId)
        print('Setup complete.')

    def test_00_create_service_instance(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "osb-sdk-python-test00-" + \
            self.transactionId

        testContext = Context(account_id=self.testAccountId,
                              crn=self.testInstanceId, platform=self.testPlatform)
        testPars = {}

        response = self.service.replace_service_instance(
            instance_id=self.testInstanceId,
            organization_guid=self.testOrgGuid,
            plan_id=self.testPlanId1,
            service_id=self.testServiceId,
            space_guid=self.testSpaceGuid,
            context=testContext,
            parameters=testPars,
            accepts_incomplete=True,
            headers=customHeaders
        )

        assert response is not None
        assert response.get_status_code() == 201

        result = response.get_result()
        assert result is not None
        assert result.get('dashboard_url') is not None

    def test_01_update_service_instance(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "osb-sdk-python-test01-" + \
            self.transactionId

        testContext = Context(account_id=self.testAccountId,
                              crn=self.testInstanceId, platform=self.testPlatform)
        testPars = {}
        testPrevValues = {}

        response = self.service.update_service_instance(
            instance_id=self.testInstanceId,
            service_id=self.testServiceId,
            context=testContext,
            parameters=testPars,
            plan_id=self.testPlanId1,
            previous_values=testPrevValues,
            accepts_incomplete=True,
            headers=customHeaders
        )

        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('service_instance_id') == self.testInstanceId
        assert result.get('plan_id') == self.testPlanId1

    def test_02_disable_service_instance_state(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "osb-sdk-python-test02-" + \
            self.transactionId

        response = self.service.replace_service_instance_state(
            instance_id=self.testInstanceId,
            enabled=False,
            initiator_id=self.testInitiatorId,
            reason_code=self.testReasonCode,
            headers=customHeaders
        )

        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('active') is not None
        assert result.get('enabled') is not None

    def test_03_enable_service_instance_state(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "osb-sdk-python-test03-" + \
            self.transactionId

        response = self.service.replace_service_instance_state(
            instance_id=self.testInstanceId,
            enabled=True,
            initiator_id=self.testInitiatorId,
            reason_code=self.testReasonCode,
            headers=customHeaders
        )

        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('active') is not None
        assert result.get('enabled') is not None

    def test_04_bind_service_instance_state(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "osb-sdk-python-test04-" + \
            self.transactionId
        testParams = {}
        testBindResource = BindResource(
            account_id=self.testAccountId, serviceid_crn=self.testAppGuid)

        response = self.service.replace_service_binding(
            binding_id=self.testBindingId2,
            instance_id=self.testInstanceId2,
            plan_id=self.testPlanId3,
            service_id=self.testServiceId,
            bind_resource=testBindResource,
            parameters=testParams,
            headers=customHeaders
        )

        assert response is not None
        assert response.get_status_code() == 201

        result = response.get_result()
        assert result is not None
        assert result.get('credentials') is not None

    def test_05_get_service_instance_state(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "osb-sdk-python-test05-" + \
            self.transactionId

        response = self.service.get_service_instance_state(
            instance_id=self.testInstanceId,
            headers=customHeaders
        )

        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('active') is not None
        assert result.get('enabled') is not None

    def test_06_get_catalog_metadata(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "osb-sdk-python-test06-" + \
            self.transactionId

        response = self.service.list_catalog(
            headers=customHeaders
        )

        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        assert result.get('services')[0].get('id') is not None
        assert result.get('services')[0].get('name') is not None
        assert result.get('services')[0].get('bindable') is not None
        assert result.get('services')[0].get('plan_updateable') is not None

    def test_07_delete_service_binding(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "osb-sdk-python-test07-" + \
            self.transactionId

        response = self.service.delete_service_binding(
            binding_id=self.testBindingId2,
            instance_id=self.testInstanceId2,
            plan_id=self.testPlanId3,
            service_id=self.testServiceId,
            headers=customHeaders
        )

        assert response is not None
        assert response.get_status_code() == 200

    def test_08_delete_service_instance(self):
        customHeaders = {}
        customHeaders["Transaction-Id"] = "osb-sdk-python-test08-" + \
            self.transactionId

        response = self.service.delete_service_instance(
            service_id=self.testServiceId,
            plan_id=self.testPlanId3,
            instance_id=self.testInstanceId2,
            headers=customHeaders
        )

        assert response is not None
        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None
