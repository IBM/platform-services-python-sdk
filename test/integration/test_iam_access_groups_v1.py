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
 This class contains an integration test for the IAM Access Groups service.
"""

import pytest
import unittest
import os
import os.path
from ibm_cloud_sdk_core.authenticators import NoAuthAuthenticator
from ibm_cloud_sdk_core import *
from ibm_platform_services.iam_access_groups_v2 import *

# Read config file
configFile = 'iam_access_groups.env'
configLoaded = None

if os.path.exists(configFile):
    os.environ['IBM_CREDENTIALS_FILE'] = configFile
    configLoaded = True
else:
    print('External configuration was not found, skipping tests...')

class TestIamAccessGroupsV2(unittest.TestCase):
    def setUp(self):
        if not configLoaded:
          self.skipTest('External configuration not available, skipping...')
          
        self.service = IamAccessGroupsV2.new_instance()
        assert self.service is not None

        self.config = read_external_sources(IamAccessGroupsV2.DEFAULT_SERVICE_NAME)
        assert self.config is not None
        self.testAccountId = self.config.get('TEST_ACCOUNT_ID')
        assert self.testAccountId is not None
        print('\nSetup complete.')
        
    def tearDown(self):
        # Delete the resources
        print('Clean up complete.')

    def test_account_id(self):
        assert self.testAccountId is not None
        print('\nTest account id: ', self.testAccountId)

