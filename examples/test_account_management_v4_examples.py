# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.
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
Examples for AccountManagementV4
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from ibm_platform_services.account_management_v4 import *

#
# This file provides an example of how to use the account_management service.
#
# The following configuration properties are assumed to be defined:
# ACCOUNT_MANAGEMENT_URL=<service base url>
# ACCOUNT_MANAGEMENT_AUTH_TYPE=iam
# ACCOUNT_MANAGEMENT_APIKEY=<IAM apikey>
# ACCOUNT_MANAGEMENT_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
# ACCOUNT_MANAGEMENT_ACCOUNT_ID=<account id>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'account_management_v4.env'

account_management_service = None

config = None

account_id = None


##############################################################################
# Start of Examples for Service: AccountManagementV4
##############################################################################
# region
class TestAccountManagementV4Examples:
    """
    Example Test Class for AccountManagementV4
    """

    @classmethod
    def setup_class(cls):
        global account_management_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            account_management_service = AccountManagementV4.new_instance()

            # end-common
            assert account_management_service is not None

            # Load the configuration
            global config
            config = read_external_sources(AccountManagementV4.DEFAULT_SERVICE_NAME)
            global account_id
            account_id = config['ACCOUNT_ID']
        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_account_example(self):
        """
        get_account request example
        """
        try:
            print('\nget_account() result:')

            # begin-getAccount

            response = account_management_service.get_account(
                account_id=account_id,
            )
            account_response = response.get_result()

            print(json.dumps(account_response, indent=2))

            # end-getAccount

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: AccountManagementV4
##############################################################################
