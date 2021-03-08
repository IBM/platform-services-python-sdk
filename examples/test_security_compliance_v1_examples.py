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
Examples for SecurityComplianceV1
"""

import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.security_compliance_v1 import *

#
# This file provides an example of how to use the Security Compliance service.
#
# The following configuration properties are assumed to be defined:
# SECURITY_COMPLIANCE_URL=<service base url>
# SECURITY_COMPLIANCE_AUTH_TYPE=iam
# SECURITY_COMPLIANCE_APIKEY=<IAM apikey>
# SECURITY_COMPLIANCE_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'security_compliance_v1.env'

security_compliance_service = None

config = None


##############################################################################
# Start of Examples for Service: SecurityComplianceV1
##############################################################################
# region
class TestSecurityComplianceV1Examples():
    """
    Example Test Class for SecurityComplianceV1
    """

    @classmethod
    def setup_class(cls):
        global security_compliance_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            security_compliance_service = SecurityComplianceV1.new_instance(
            )

            # end-common
            assert security_compliance_service is not None

            # Load the configuration
            global config
            config = read_external_sources(SecurityComplianceV1.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_validation_scan_example(self):
        """
        create_validation_scan request example
        """
        try:
            # begin-create_validation_scan

            result = security_compliance_service.create_validation_scan(
                account_id='testString',
            ).get_result()

            print(json.dumps(result, indent=2))

            # end-create_validation_scan

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_profile_example(self):
        """
        list_profile request example
        """
        try:
            # begin-list_profile

            profiles_list = security_compliance_service.list_profile(
                account_id='testString'
            ).get_result()

            print(json.dumps(profiles_list, indent=2))

            # end-list_profile

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_scopes_example(self):
        """
        list_scopes request example
        """
        try:
            # begin-list_scopes

            scopes_list = security_compliance_service.list_scopes(
                account_id='testString'
            ).get_result()

            print(json.dumps(scopes_list, indent=2))

            # end-list_scopes

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: SecurityComplianceV1
##############################################################################