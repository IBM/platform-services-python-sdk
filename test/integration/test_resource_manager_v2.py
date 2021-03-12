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

# Location of our config file.
config_file = 'resource_manager.env'

class TestResourceManagerV2(unittest.TestCase):
    """
    Integration Test Class for ResourceManagerV2
    """

    @classmethod
    def setUpClass(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.config = read_external_sources(
                ResourceManagerV2.DEFAULT_SERVICE_NAME
            )
            assert cls.config is not None

            # Construct the first service instance.
            cls.service = ResourceManagerV2.new_instance(service_name=ResourceManagerV2.DEFAULT_SERVICE_NAME)
            assert cls.service is not None

            # Construct the second service instance.
            cls.alt_service = ResourceManagerV2.new_instance(service_name='ALT_RESOURCE_MANAGER')
            assert cls.alt_service is not None

            # setup default values
            cls.test_quota_id = cls.config['QUOTA_ID']
            cls.test_user_account_id = cls.config['USER_ACCOUNT_ID']
            cls.new_resource_group_id = ''

        print('\nSetup complete.')

    @classmethod
    def tearDownClass(cls):
        # Perform any cleanup needed after all the test methods are finished.
        print('\nClean up complete.')

    def test_00_check_service(self):
        assert self.service is not None

    def test_01_list_quota_definitions(self):
        response = self.service.list_quota_definitions()
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None
        resources = result.get('resources')
        assert resources is not None

    def test_02_get_quota_definition(self):
        response = self.service.get_quota_definition(id=self.test_quota_id)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None

    def test_03_list_resource_groups_in_an_account(self):
        response = self.service.list_resource_groups(
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
        response = self.service.create_resource_group(
            name='TestGroup', account_id=self.test_user_account_id)
        assert response is not None
        assert response.get_status_code() == 201

        result = response.get_result()
        assert result is not None
        assert result.get('id') is not None

        self.__class__.new_resource_group_id = result.get('id')

    def test_05_get_resource_group_by_id(self):
        response = self.service.get_resource_group(
            id=self.new_resource_group_id)
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None

    def test_06_update_resource_group_by_id(self):
        response = self.service.update_resource_group(
            id=self.new_resource_group_id, name='TestGroup2', state='ACTIVE')
        assert response is not None
        assert response.get_status_code() == 200

        result = response.get_result()
        assert result is not None

    def test_07_delete_resource_group_by_id(self):
        response = self.alt_service.delete_resource_group(
            id=self.new_resource_group_id)
        assert response is not None
        assert response.get_status_code() == 204
