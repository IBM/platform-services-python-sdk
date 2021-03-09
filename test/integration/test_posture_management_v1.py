# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
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
Integration Tests for PostureManagementV1
"""

import os
import pytest
from ibm_cloud_sdk_core import *
from ibm_platform_services.posture_management_v1 import *

# Config file name
config_file = 'posture_management_v1.env'

class TestPostureManagementV1():
    """
    Integration Test Class for PostureManagementV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.posture_management_service = PostureManagementV1.new_instance(
                )
            assert cls.posture_management_service is not None

            cls.config = read_external_sources(
                PostureManagementV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_validation_scan(self):

        create_validation_scan_response = self.posture_management_service.create_validation_scan(
            account_id='testString',
            scope_id=1,
            profile_id=6,
            group_profile_id=13
        )

        assert create_validation_scan_response.get_status_code() == 200
        result = create_validation_scan_response.get_result()
        assert result is not None

    @needscredentials
    def test_list_profile(self):

        list_profile_response = self.posture_management_service.list_profile(
            account_id='testString',
            name='testString'
        )

        assert list_profile_response.get_status_code() == 200
        profiles_list = list_profile_response.get_result()
        assert profiles_list is not None

    @needscredentials
    def test_list_scopes(self):

        list_scopes_response = self.posture_management_service.list_scopes(
            account_id='testString',
            name='testString'
        )

        assert list_scopes_response.get_status_code() == 200
        scopes_list = list_scopes_response.get_result()
        assert scopes_list is not None

