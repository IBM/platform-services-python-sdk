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
 This class contains an integration test for the IAM Access Groups service.
"""

import pytest
import unittest
import os
import os.path
import datetime
import random
from ibm_cloud_sdk_core import *
from ibm_platform_services.resource_manager_v2 import *

# Read config file
configFile = 'resource_manager.env'
configLoaded = None

if os.path.exists(configFile):
    os.environ['IBM_CREDENTIALS_FILE'] = configFile
    configLoaded = True
else:
    print('External configuration was not found, skipping tests...')

class TestResourceManagerV2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not configLoaded:
            raise unittest.SkipTest('External configuration not available, skipping...')
          
        cls.service = ResourceManagerV2.new_instance()
        assert cls.service is not None

        cls.config = read_external_sources(
            ResourceManagerV2.DEFAULT_SERVICE_NAME)
        assert cls.config is not None
        cls.my_test_prop = cls.config.get('MY_TEST_PROP')
        assert cls.my_test_prop is not None
        print('\nSetup complete.')
        
    @classmethod
    def tearDownClass(cls):
        # Perform any cleanup needed after all the test methods are finished.
        print('\nClean up complete.')

    def test_00_check_service(self):
        assert self.service is not None
