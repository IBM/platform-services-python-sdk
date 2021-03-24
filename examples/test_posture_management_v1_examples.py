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
Examples for PostureManagementV1
"""

import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.posture_management_v1 import *

#
# This file provides an example of how to use the Posture Management service.
#
# The following configuration properties are assumed to be defined:
# POSTURE_MANAGEMENT_URL=<service base url>
# POSTURE_MANAGEMENT_AUTH_TYPE=iam
# POSTURE_MANAGEMENT_APIKEY=<IAM apikey>
# POSTURE_MANAGEMENT_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
# POSTURE_MANAGEMENT_ACCOUNT_ID=<IBM CLOUD ACCOUNT ID>
# POSTURE_MANAGEMENT_SCOPES_NAME=<The name of the scope>
# POSTURE_MANAGEMENT_PROFILE_NAME=<The name of profile - CIS IBM Foundations Benchmark 1.0.0>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'posture_management.env'

posture_management_service = None

config = None

account_id = None
profile_name = None
scopes_name = None

profile_id = None
scope_id = None
group_profile_id = 0


##############################################################################
# Start of Examples for Service: PostureManagementV1
##############################################################################
# region
class TestPostureManagementV1Examples():
    """
    Example Test Class for PostureManagementV1
    """

    @classmethod
    def setup_class(cls):
        global posture_management_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            posture_management_service = PostureManagementV1.new_instance()

            # end-common
            assert posture_management_service is not None

            # Load the configuration
            global config
            config = read_external_sources(PostureManagementV1.DEFAULT_SERVICE_NAME)

            global account_id
            account_id   = config['ACCOUNT_ID']

            global profile_name
            profile_name = config['PROFILE_NAME']

            global scopes_name
            scopes_name  = config['SCOPES_NAME']

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )


    @needscredentials
    def test_list_profiles_example(self):
        """
        list_profiles request example
        """
        try:
            # begin-list_profiles

            profiles_list = posture_management_service.list_profiles(
                account_id=account_id,
                name=profile_name,
            ).get_result()

            print(json.dumps(profiles_list, indent=2))

            # end-list_profile

            global profile_id
            profile_id = profiles_list['profiles'][0]['profile_id']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_scopes_example(self):
        """
        list_scopes request example
        """
        try:
            # begin-list_scopes

            scopes_list = posture_management_service.list_scopes(
                account_id=account_id,
                name=scopes_name,
            ).get_result()

            print(json.dumps(scopes_list, indent=2))

            # end-list_scopes

            global scope_id
            scope_id = scopes_list['scopes'][0]['scope_id']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_validation_example(self):
        """
        create_validation request example
        """
        try:
            # begin-create_validation

            result = posture_management_service.create_validation(
                account_id=account_id,
                scope_id=scope_id,
                profile_id=profile_id,
                group_profile_id=group_profile_id,
            ).get_result()

            print(json.dumps(result, indent=2))

            # end-create_validation

        except ApiException as e:
            pytest.fail(str(e))
# endregion
##############################################################################
# End of Examples for Service: PostureManagementV1
##############################################################################
