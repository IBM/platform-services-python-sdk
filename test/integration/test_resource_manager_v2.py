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
import os
import os.path
import datetime
import random
from ibm_cloud_sdk_core import *
from ibm_platform_services.resource_manager_v2 import *
from dotenv import load_dotenv

# Read config file
configFile = 'resource_manager.env'
configLoaded = None

if os.path.exists(configFile):
    load_dotenv(dotenv_path=configFile)
    configLoaded = True
else:
    print('External configuration was not found, skipping tests...')

class TestResourceManagerV2(unittest.TestCase):
    """
    Integration Test Class for ResourceManagerV2
    """

    @classmethod
    def setUpClass(cls):
        if not configLoaded:
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        # Construct the first service instance.
        cls.service1 = ResourceManagerV2.new_instance(service_name='RMGR1')
        assert cls.service1 is not None

        # Construct the second service instance.
        cls.service2 = ResourceManagerV2.new_instance(service_name='RMGR2')
        assert cls.service2 is not None

        # setup default values
        cls.test_quota_id = '7ce89f4a-4381-4600-b814-3cd9a4f4bdf4'
        cls.test_user_account_id = '60ce10d1d94749bf8dceff12065db1b0'
        cls.new_resource_group_id = ''

        print('\nSetup complete.')

    @classmethod
    def tearDownClass(cls):
        # Perform any cleanup needed after all the test methods are finished.
        print('\nClean up complete.')

    def test_00_check_service(self):
        assert self.service1 is not None

    def test_01_list_quota_definitions(self):
        response = self.service1.list_quota_definitions()
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        resources = result.get('resources')
        assert resources is not None

    def test_02_get_quota_definition(self):
        response = self.service1.get_quota_definition(id=self.test_quota_id)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None

    def test_03_list_resource_groups_in_an_account(self):
        response = self.service1.list_resource_groups(
            account_id=self.test_user_account_id)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None

        resources = result.get('resources')[0]
        assert resources is not None

        # confirm fields
        assert resources.get('id') is not None
        assert resources.get('name') is not None
        assert resources.get('crn') is not None
        assert resources.get('account_id') is not None
        assert resources.get('state') is not None
        assert resources.get('quota_id') is not None
        assert resources.get('quota_url') is not None
        assert resources.get('created_at') is not None
        assert resources.get('updated_at') is not None

    def test_04_create_resource_group_in_an_account(self):
        response = self.service1.create_resource_group(
            name='TestGroup', account_id=self.test_user_account_id)
        assert response is not None
        assert response.get_status_code() == 201

        result = response.get_result()
        assert result is not None
        assert result.get('id') is not None

        self.__class__.new_resource_group_id = result.get('id')

    def test_05_get_resource_group_by_id(self):
        response = self.service1.get_resource_group(
            id=self.new_resource_group_id)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None

    def test_06_update_resource_group_by_id(self):
        response = self.service1.update_resource_group(
            id=self.new_resource_group_id, name='TestGroup2', state='ACTIVE')
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None

    def test_07_delete_resource_group_by_id(self):
        response = self.service2.delete_resource_group(
            id=self.new_resource_group_id)
        assert response is not None
        assert response.get_status_code() == 204
