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
Test the platform service Resource Controller V2 API operations
"""

import pytest
import unittest
import os
from platform_services import ResourceControllerV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

@pytest.mark.skipif(
    os.getenv('VCAP_SERVICES') is None, reason='requires VCAP_SERVICES')
class TestResourceControllerV2(unittest.TestCase):
    def setUp(self):
        authenticator = IAMAuthenticator()
        self.resource_controller = ResourceControllerV2(authenticator)
        self.id = self.resource_controller.create_resource_instance("name", "target", "resource_group", "resource_plan_id")

    def tearDown(self):
        # Delete the resources
        print("Clean up complete.")

    def test_list_resource_instances(self):
        env = self.example_service.list_resource_instances(self.id).get_result()
        assert env is not None
