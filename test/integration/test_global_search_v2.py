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
Integration Tests for GlobalSearchV2
"""

import os
import pytest
import uuid
from ibm_cloud_sdk_core import *
from ibm_platform_services.global_search_v2 import *

# Config file name
config_file = 'global_search.env'

transaction_id = str(uuid.uuid4())


class TestGlobalSearchV2:
    """
    Integration Test Class for GlobalSearchV2
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.global_search_service = GlobalSearchV2.new_instance()
            assert cls.global_search_service is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_search(self):
        search_results = []
        more_results = True
        search_cursor = None

        while more_results:
            search_response = self.global_search_service.search(
                query='GST-sdk-*', fields=['*'], search_cursor=search_cursor, transaction_id=transaction_id, limit=1
            )

            assert search_response.get_status_code() == 200
            scan_result = search_response.get_result()
            assert scan_result is not None
            print('\nsearch() result: ', json.dumps(scan_result, indent=2))

            if len(scan_result['items']) > 0:
                for elem in scan_result['items']:
                    search_results.append(elem)
                search_cursor = scan_result['search_cursor']
            else:
                more_results = False

        print('Total items returned by search(): ', len(search_results))
