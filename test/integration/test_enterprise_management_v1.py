# coding: utf-8

# Copyright 2020 IBM All Rights Reserved.
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
 This class contains an integration test for Resource Manager service.
"""

import pytest
import unittest
import requests
import os
import os.path
import datetime
import random
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import *
from ibm_platform_services.enterprise_management_v1 import *
from dotenv import load_dotenv
import time, datetime
import math
import random
import couchdb
import time

# Read config file
configFile = 'enterprise-management.env'
config = {}
configLoaded = None

    
class TestEnterpriseManagementV1(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        if os.path.exists(configFile):
            os.environ['IBM_CREDENTIALS_FILE'] = configFile
        else:
            raise unittest.SkipTest('External configuration not available, skipping...')

        # Construct the service instance.
        cls.service = EnterpriseManagementV1.new_instance()
        assert cls.service is not None

        # Load the "EMTEST_CONFIG" properties.
        cls.config = read_external_sources('EMTEST_CONFIG')
        assert cls.config is not None
        
        cls.am_host = cls.config['AM_HOST']
        cls.db_url = cls.config['DB_URL']
        cls.db_user = cls.config['DB_USER']
        cls.db_pass = cls.config['DB_PASS']
        cls.activation_db_name = cls.config['ACTIVATION_DB_NAME']
        cls.iam_host = cls.config['IAM_HOST']
        cls.iam_basic_auth = cls.config['IAM_BASIC_AUTH']
        cls.iam_api_key = cls.config['IAM_API_KEY']
        assert cls.am_host is not None
        assert cls.db_url is not None
        assert cls.db_user is not None
        assert cls.db_pass is not None
        assert cls.activation_db_name is not None
        assert cls.iam_host is not None
        assert cls.iam_basic_auth is not None
        assert cls.iam_api_key is not None

        # Construct the second service instance.
        # cls.service2 = EnterpriseManagementV1.new_instance(service_name='RMGR2')
        # assert cls.service2 is not None

        # setup default values
        cls.parent = ''
        cls.enterpriseId = ''
        cls.enterpriseAccountId = ''
        cls.parentAccountGroupId = ''
        cls.service_token = ''
        cls.owner_iam_id = ''
        cls.activation_token = ''
        cls.account_id = ''
        cls.subscription_id = ''
        cls.crn = ''
        cls.iEmail = ''
        cls.iAccountId = ''
        cls.email = "aminttest+" + str(int(time.time() * 1000)) + "_" + str(math.floor(random.random() * 10000)) + "@mail.test.ibm.com"

        print('\nSetup complete.')

    @classmethod
    def tearDownClass(cls):
        # Perform any cleanup needed after all the test methods are finished.
        print('\nClean up complete.')

    def test_00_check_service(self):
        assert self.service is not None

    def test_01_generate_iam_service_token(self):
        
        data = {
          'apikey': self.iam_api_key,
          'grant_type':'urn:ibm:params:oauth:grant-type:apikey'
        }
        headers = {}
        headers['content-type'] = 'application/x-www-form-urlencoded'
        headers['authorization'] = self.iam_basic_auth

        url = self.iam_host + "/identity/token"
        response = requests.post(url=url, data=data, headers=headers) 
        
        resp = response.json()
        self.__class__.service_token = "Bearer " + resp["access_token"]

    def test_03_create_standard_account(self):
        jsonData = {
            'owner_user_id': self.email,
            'owner_email': self.email,
            'owner_first_name': 'TEST',
            'owner_last_name': 'TEST',
            'owner_phone': '123456789',
            'owner_company': 'IBM',
            'country_code': 'USA',
            'bluemix_subscriptions': [
              {
                'type': 'STANDARD',
                'state': 'ACTIVE',
                'part_number': 'COE-Trial',
              },
            ],
            'ibmid': {
              'password': 'password',
              'question': 'question',
              'answer': 'answer',
            }
        }
        headers = {}
        headers['content-type'] = 'application/json'
        headers['authorization'] = self.__class__.service_token
        url = self.am_host + "/coe/v2/accounts"
        response = requests.post(url=url, headers=headers, json=jsonData)
        resp = response.json()
        
        self.__class__.account_id = resp["id"]

    def test_04_get_activation_code(self):
        headers = {}
        headers['content-type'] = 'application/json'
        headers['authorization'] = self.service_token
        url = self.am_host + "/v1/activation-codes/" + self.email
        time.sleep(20)
        response = requests.get(url=url, headers=headers)
        resp = response.json()
        x = resp["resources"]
        y = x[0]
        self.__class__.activationToken = y["id"]

    def test_05_get_am_coe_v2_accounts_verify(self):
        url = self.am_host + "/coe/v2/accounts/verify"
        params = {
            'token': self.activationToken,
            'email': self.email
        }
        response = requests.get(url=url, params=params)

    def test_06_get_am_coe_v2_account_by_id(self):
        url = self.am_host + "/coe/v2/accounts/" + self.account_id
        headers = {}
        headers['content-type'] = 'application/json'
        headers['authorization'] = self.service_token
        response = requests.get(url=url, headers=headers)
        resp = response.json()
        x = resp["entity"]
        self.__class__.ownerIamId = x["owner_iam_id"]
        self.__class__.subscriptionId = x["subscription_id"]

    def test_07_get_activate_subscription_payload(self):
        jsonData = {
            'type': 'SUBSCRIPTION',
            'state': 'ACTIVE',
            'payment_method': {
              'start_date': '2020-03-01T07:00:00.000Z',
              'end_date':   '2020-11-30T08:00:00.000Z'
            },
            'subscription_amount': 100,
            'quantity': 10,
            'billing_frequency': 'M',
            'charge_agreement_number': '0099342614',
            'partner_customer_number': '0003615466',
            'configuration_id': '5900A5D20190517',
            'part_number': 'D019JZX',
            'order_id_number': '150418156',
            'sales_doc_type_code': '',
            'renewal_mode_code': 'T',
            'renewal_date': '',
            'terminate_renewal': False,
            'line_item_id': 10,
            'tags': ['TEST_ACCOUNT']
        }   
        headers = {}
        headers['content-type'] = 'application/json'
        headers['authorization'] = self.service_token
        url = self.am_host + "/coe/v2/accounts/" + self.account_id + "/bluemix_subscriptions/" + self.subscriptionId
        response = requests.patch(url=url, headers=headers, json=jsonData)

    def test_08_get_am_coe_v2_account_by_id(self):
        url = self.am_host + "/coe/v2/accounts/" + self.account_id
        headers = {}
        headers['content-type'] = 'application/json'
        headers['authorization'] = self.service_token
        response = requests.get(url=url, headers=headers)
        resp = response.json()

    def test_09_create_enterprise(self):
        response = self.service.create_enterprise(
            source_account_id=self.account_id,
            name="IBM",
            primary_contact_iam_id=self.ownerIamId,
            domain="IBM.com")
        assert response is not None
        assert response.get_status_code() == 202
        x = response.get_result()
        self.__class__.enterprise_id = x["enterprise_id"]
        self.__class__.enterprise_account_id = x["enterprise_account_id"]

    def test_10_get_am_coe_v2_account_by_id(self):
        url = self.am_host + "/coe/v2/accounts/" + self.account_id
        headers = {}
        headers['content-type'] = 'application/json'
        headers['authorization'] = self.service_token
        response = requests.get(url=url, headers=headers)
        resp = response.json()
        
        x = resp["entity"]
        self.__class__.parent = x["parent"]

    def test_11_create_account_group(self):
        response = self.service.create_account_group(
            parent=self.parent,
            name="IBM",
            primary_contact_iam_id=self.ownerIamId)
        assert response is not None
        assert response.get_status_code() == 201
        x = response.get_result()
        self.__class__.account_group_id = x["account_group_id"]

    def test_12_list_account_groups(self):
        response = self.service.list_account_groups(
            enterprise_id=self.enterprise_id,
            parent_account_group_id=self.account_group_id,
            parent=self.parent,
            limit=100)
        assert response is not None
        assert response.get_status_code() == 200
        x = response.get_result()

    def test_13_get_account_group(self):
        response = self.service.get_account_group(account_group_id=self.account_group_id)
        assert response is not None
        assert response.get_status_code() == 200
        x = response.get_result()
        self.__class__.crn = x["crn"]

    def test_14_update_account_group(self):
        response = self.service.update_account_group(
            account_group_id=self.account_group_id,
            name="IBM",
            primary_contact_iam_id=self.ownerIamId)
        assert response is not None
        assert response.get_status_code() == 204
        x = response.get_result()

    def test_16_create_standard_account(self):
        self.__class__.standard_email = "aminttest+" + str(int(time.time() * 1000)) + "_" + str(math.floor(random.random() * 10000)) + "@mail.test.ibm.com"
        jsonData = {
            'owner_user_id': self.standard_email,
            'owner_email': self.standard_email,
            'owner_first_name': 'TEST',
            'owner_last_name': 'TEST',
            'owner_phone': '123456789',
            'owner_company': 'IBM',
            'country_code': 'USA',
            'bluemix_subscriptions': [
              {
                'type': 'STANDARD',
                'state': 'ACTIVE',
                'part_number': 'COE-Trial',
              },
            ],
            'ibmid': {
              'password': 'password',
              'question': 'question',
              'answer': 'answer',
            }
        }
        headers = {}
        headers['content-type'] = 'application/json'
        headers['authorization'] = self.service_token
        url = self.am_host + "/coe/v2/accounts"
        response = requests.post(url=url, headers=headers, json=jsonData)
        resp = response.json()
        self.__class__.standard_account_id = resp["id"]

    def test_17_get_activation_code(self):
        headers = {}
        headers['content-type'] = 'application/json'
        headers['authorization'] = self.service_token
        url = self.am_host + "/v1/activation-codes/" + self.standard_email
        time.sleep(20)
        response = requests.get(url=url, headers=headers)
        
        resp = response.json()
        x = resp["resources"]
        y = x[0]
        self.__class__.activation_token = y["id"]

    def test_18_get_am_coe_v2_accounts_verify(self):
        url = self.am_host + "/coe/v2/accounts/verify"
        params = {
            'token': self.activation_token,
            'email': self.standard_email
        }
        response = requests.get(url=url, params=params)

    def test_19_import_account_to_enterprise(self):
        response = self.service.import_account_to_enterprise(
            enterprise_id=self.enterprise_id,
            account_id=self.standard_account_id,
            parent=self.parent)
        assert response is not None
        assert response.get_status_code() == 202
        x = response.get_result()

    def test_20_get_account(self):
        response = self.service.get_account(account_id=self.enterprise_account_id)
        assert response is not None
        assert response.get_status_code() == 200
        x = response.get_result()

    def test_21_create_account(self):
        response = self.service.create_account(
            parent=self.parent,
            name="IBM",
            owner_iam_id="IBMid-550006JKXX")
        assert response is not None
        assert response.get_status_code() == 202
        x = response.get_result()
        self.__class__.newAccount = x["account_id"];

    def test_22_get_account(self):
        response = self.service.get_account(account_id=self.newAccount)
        assert response is not None
        assert response.get_status_code() == 200
        x = response.get_result()

    def test_23_list_accounts(self):
        response = self.service.list_accounts(
            enterprise_id=self.enterprise_id,
            account_group_id=self.account_group_id,
            parent=self.parent,
            limit=100)
        assert response is not None
        assert response.get_status_code() == 200
        x = response.get_result()
   
    def test_24_create_account_group(self): 
        response = self.service.create_account_group(
            parent=self.parent,
            name="IBM",
            primary_contact_iam_id=self.ownerIamId)
        assert response is not None
        assert response.get_status_code() == 201
        x = response.get_result()
        self.__class__.account_group_id_2 = x["account_group_id"]  

    def test_25_list_account_groups(self):
        response = self.service.list_account_groups(
            enterprise_id=self.enterprise_id,
            parent_account_group_id=self.account_group_id,
            parent=self.parent,
            limit=100)
        assert response is not None
        assert response.get_status_code() == 200
        x = response.get_result()

    def test_26_update_account(self):
        response = self.service.update_account(
            account_id=self.newAccount,
            parent=self.crn)
        assert response is not None
        assert response.get_status_code() == 202
        x = response.get_result()

