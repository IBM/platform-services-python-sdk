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
Examples for GlobalSearchV2
"""

import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.global_search_v2 import *

# This file provides an example of how to use the Global Tagging service.
#
# The following configuration properties are assumed to be defined in the external configuration file:
# GLOBAL_TAGGING_URL=<service url>
# GLOBAL_TAGGING_AUTHTYPE=iam
# GLOBAL_TAGGING_APIKEY=<IAM api key>
# GLOBAL_TAGGING_AUTH_URL=<IAM token service URL - omit this if using the production environment>
# GLOBAL_TAGGING_RESOURCE_CRN=<the crn of the resource to be used in the examples>

# Config file name
config_file = 'global_search.env'

global_search_service = None


##############################################################################
# Start of Examples for Service: GlobalSearchV2
##############################################################################
# region
class TestGlobalSearchV2Examples():
    """
    Example Test Class for GlobalSearchV2
    """
    @classmethod
    def setup_class(cls):
        global global_search_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            global_search_service = GlobalSearchV2.new_instance()

            # end-common
            assert global_search_service is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file),
        reason="External configuration not available, skipping...")

    @needscredentials
    def test_search_example(self):
        """
        search request example
        """
        try:
            # begin-search

            response = global_search_service.search(query='GST-sdk-*',
                                                    fields=['*'])
            scan_result = response.get_result()

            print(json.dumps(scan_result, indent=2))

            # end-search

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_supported_types_example(self):
        """
        get_supported_types request example
        """
        try:
            # begin-get_supported_types

            supported_types_list = global_search_service.get_supported_types(
            ).get_result()

            print(json.dumps(supported_types_list, indent=2))

            # end-get_supported_types

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: GlobalSearchV2
##############################################################################
