# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
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
Test the platform service Global Tagging API operations
"""

import unittest
import pytest
import os
from ibm_platform_services import GlobalTaggingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from random import seed
from random import randint
from jproperties import Properties
unittest.TestLoader.sortTestMethodsUsing = None

def getRandomIntegerString(length=8):
    """
    Helper function which returns a random integer of lengh 'length' digits.
    """
    
    if length < 0:
        length = 0
    res = ''
    for pos in range(length):
        res += str(randint(0, 10))
    return res

# Read config file
configFile = 'ghost.env'
config = {}
configLoaded = None

try:
    with open(configFile, "rb") as f:
        p = Properties()
        p.load(f, "utf-8")
        config['GST_API_URL'] = p['GST_API_URL'].data
        config['GST_TAGS_URL'] = p['GST_TAGS_URL'].data
        config['GST_RESOURCE_NAMES'] = p['GST_RESOURCE_NAMES'].data
        config['GST_IINTERNA_APIKEY'] = p['GST_IINTERNA_APIKEY'].data
        config['GST_IAM_URL'] = p['GST_IAM_URL'].data
        config['GST_QUERY'] = p['GST_QUERY'].data
        config['GST_RESOURCE_CRN'] = p['GST_RESOURCE_CRN'].data
        configLoaded = True
except:
    print('External configuration was not found, skipping tests...')

# Test class
class TestGlobalTaggingV1(unittest.TestCase):
    """
    Integration Test Class for GlobalTaggingV1
    """

    def setUp(self):
        if not configLoaded:
          self.skipTest("External configuration not available, skipping...")
        
        # Create authenticator with IAM API key (it generates bearer token automatically)
        authenticator = IAMAuthenticator(config['GST_IINTERNA_APIKEY'], url=config['GST_IAM_URL'])
        self.global_tagging = GlobalTaggingV1(authenticator=authenticator)
        self.global_tagging.set_service_url(config['GST_TAGS_URL'])
        seed(1)
        self.tag_generated = 'python-sdk-' + getRandomIntegerString(8)
        resource = {}
        resource['resource_id'] = config['GST_RESOURCE_CRN']
        resource['resource_type'] = "cf-application"
        self.res = [ resource ]

    def tearDown(self):
        # Delete the resources
        print("Clean up complete")

    def test_1_list_tags(self):
        env = self.global_tagging.list_tags()
        assert env is not None
        results = env.get_result()
        items = results.get('items')
        assert items is not None

    def test_2_attach_tag(self):
        # Attach the tag
        env = self.global_tagging.attach_tag(tag_name=self.tag_generated, resources=self.res)
        assert env is not None

        # Check if the tag is attached to the resource
        env = self.global_tagging.list_tags(attached_to=config['GST_RESOURCE_CRN'])
        assert env is not None
        results = env.get_result()
        items = results.get('items')
        assert items is not None
        flag_found = False
        for item in items:
            if item.get('name') == self.tag_generated:
                flag_found = True
                break
        assert flag_found is True

    def test_3_detach_tag(self):
        # Detach the tag
        env = self.global_tagging.detach_tag(tag_name=self.tag_generated, resources=self.res)
        assert env is not None

        # Check if the tag is detached
        env = self.global_tagging.list_tags(attached_to=config['GST_RESOURCE_CRN'])
        assert env is not None
        results = env.get_result()
        items = results.get('items')
        assert items is not None
        flag_found = False
        for item in items:
            if item.get('name') == self.tag_generated:
                flag_found = True
                break
        assert flag_found is False

    def test_4_delete_tag(self):
        # Delete the tag
        env = self.global_tagging.delete_tag(tag_name=self.tag_generated)
        assert env is not None

        # Check if the tag is deleted
        env = self.global_tagging.list_tags()
        assert env is not None
        results = env.get_result()
        items = results.get('items')
        assert items is not None
        flag_found = False
        for item in items:
            if item.get('name') == self.tag_generated:
                flag_found = True
                break
        assert flag_found is False


if __name__ == '__main__':
    unittest.main()
