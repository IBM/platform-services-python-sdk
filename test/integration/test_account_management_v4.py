# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.
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
Integration Tests for AccountManagementV4
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_platform_services.account_management_v4 import *

# Config file name
config_file = 'account_management_v4.env'
account_id = None


class TestAccountManagementV4:
    """
    Integration Test Class for AccountManagementV4
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.account_management_service = AccountManagementV4.new_instance()
            assert cls.account_management_service is not None

            cls.config = read_external_sources(AccountManagementV4.DEFAULT_SERVICE_NAME)
            assert cls.config is not None
            global account_id
            account_id = cls.config['ACCOUNT_ID']

            cls.account_management_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_account(self):
        response = self.account_management_service.get_account(
            account_id=account_id,
        )

        assert response.get_status_code() == 200
        account_response = response.get_result()
        assert account_response is not None
