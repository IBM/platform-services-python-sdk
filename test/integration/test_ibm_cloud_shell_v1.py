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
Integration Tests for IbmCloudShellV1
"""

import os
import pytest
import unittest
from ibm_cloud_sdk_core import *
from ibm_platform_services.ibm_cloud_shell_v1 import *

# Config file name
config_file = 'ibm_cloud_shell_v1.env'

class IbmCloudShellV1IntegrationTests(unittest.TestCase):
    """
    Integration Test Class for IbmCloudShellV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.ibm_cloud_shell_service = IbmCloudShellV1.new_instance(
                )
            assert cls.ibm_cloud_shell_service is not None

            cls.config = read_external_sources(
                IbmCloudShellV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.ACCOUNT_ID = cls.config['ACCOUNT_ID']
            assert cls.ACCOUNT_ID is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_account_settings(self):

        get_account_settings_response = self.ibm_cloud_shell_service.get_account_settings(
            account_id=self.ACCOUNT_ID
        )

        assert get_account_settings_response.get_status_code() == 200
        account_settings = get_account_settings_response.get_result()
        assert account_settings is not None

    @needscredentials
    def test_update_account_settings(self):

        get_account_settings_response = self.ibm_cloud_shell_service.get_account_settings(
            account_id=self.ACCOUNT_ID
        )

        assert get_account_settings_response.get_status_code() == 200
        existing_account_settings = get_account_settings_response.get_result()
        assert existing_account_settings is not None

        # Construct a dict representation of a Feature model
        feature_model = [{
            'enabled': False,
            'key': 'server.file_manager',
        },
        {
            'enabled': True,
            'key': 'server.web_preview',
        }]

        # Construct a dict representation of a RegionSetting model
        region_setting_model = [{
            'enabled': True,
            'key': 'eu-de',
        },
        {
            'enabled': False,
            'key': 'jp-tok',
        },
        {
            'enabled': False,
            'key': 'us-south',
        }]

        update_account_settings_response = self.ibm_cloud_shell_service.update_account_settings(
            account_id=self.ACCOUNT_ID,
            rev=existing_account_settings.get('_rev'),
            default_enable_new_features=False,
            default_enable_new_regions=True,
            enabled=True,
            features=feature_model,
            regions=region_setting_model
        )

        assert update_account_settings_response.get_status_code() == 200
        account_settings = update_account_settings_response.get_result()
        assert account_settings is not None
        assert account_settings.get('default_enable_new_features') == False
        assert account_settings.get('default_enable_new_regions') == True
        assert account_settings.get('enabled') == True
        assert account_settings.get('features') == feature_model
        assert account_settings.get('regions') == region_setting_model


