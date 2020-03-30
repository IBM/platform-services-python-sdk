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
Test the platform service Global Search API operations
"""

import unittest
import os
from ibm_platform_services import GlobalSearchV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from jproperties import Properties

# Read config file
configFile = '.ghostenv'
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
        configLoaded = true
except:
    print('External configuration was not found, skipping tests...')
    
# Test class
class TestGlobalSearchV2(unittest.TestCase):
    def setUp(self):
        if not configLoaded:
          self.skipTest("External configuration not available, skipping...")
        
        # Create authenticator with IAM API key (it generates bearer token automatically)
        authenticator = IAMAuthenticator(config['GST_IINTERNA_APIKEY'], url=config['GST_IAM_URL'])
        self.global_search = GlobalSearchV2(authenticator=authenticator)
        self.global_search.set_service_url(config['GST_API_URL'])
        self.items = set(config['GST_RESOURCE_NAMES'].split(','))

    def tearDown(self):
        # Delete the resources
        print("Clean up complete")

    def test_search_1(self):
        # It makes the query
        env = self.global_search.search(query='name:gst-sdk*', search_cursor=None, transaction_id=None)
        assert env is not None
        results = env.get_result()
        items = results.get('items')
        assert items is not None
        assert len(items) == 2
        items_name_set = set()
        for item in items:
            items_name_set.add(item.get('name'))
        # It checks if the resultset and expected set are equal
        assert items_name_set == self.items

    def test_search_2(self):
        items_to_check = set(self.items)  # Make a copy of the items in memory
        fields_to_search = ['crn', 'name']
        # It makes the first query
        env = self.global_search.search(query='name:gst-sdk*', search_cursor=None, transaction_id=None,
                                        fields=fields_to_search,
                                        limit=1)
        assert env is not None
        results = env.get_result()
        items = results.get('items')
        assert items is not None
        assert len(items) == 1
        items_to_check.remove(items[0]['name'])
        assert len(items_to_check) == 1

        # It makes the second query with cursor
        search_cursor_str = results.get('search_cursor')
        env = self.global_search.search(query='name:gst-sdk*', search_cursor=search_cursor_str, transaction_id=None,
                                        fields=fields_to_search,
                                        limit=1)
        assert env is not None
        results = env.get_result()
        items = results.get('items')
        assert items is not None
        assert len(items) == 1
        items_to_check.remove(items[0]['name'])
        assert len(items_to_check) == 0

    def test_get_supported_types(self):
        # It makes the query
        env = self.global_search.get_supported_types()
        assert env is not None
        results = env.get_result()
        supported_types = results.get('supported_types')
        assert supported_types is not None
        assert len(supported_types) > 0


if __name__ == '__main__':
    unittest.main()
