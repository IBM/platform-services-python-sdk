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
Test methods in the common module
"""

import unittest
from ibm_platform_services import common


class TestCommon(unittest.TestCase):
    """
    Test methods in the common module
    """

    def test_get_sdk_headers(self):
        """
        Test the get_sdk_headers method
        """
        headers = common.get_sdk_headers('resource_controller', 'V2', 'create_resource_instance')
        self.assertIsNotNone(headers)
        self.assertIsNotNone(headers.get('User-Agent'))
        print("User-Agent: {0}".format(headers.get('User-Agent')))
        self.assertTrue(headers.get('User-Agent').startswith('platform-services-python-sdk'))
