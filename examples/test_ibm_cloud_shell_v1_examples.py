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
Examples for IbmCloudShellV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from ibm_platform_services.ibm_cloud_shell_v1 import *

#
# This file provides an example of how to use the IBM Cloud Shell service.
#
# The following configuration properties are assumed to be defined:
# IBM_CLOUD_SHELL_URL=<service base url>
# IBM_CLOUD_SHELL_AUTH_TYPE=iam
# IBM_CLOUD_SHELL_APIKEY=<IAM apikey>
# IBM_CLOUD_SHELL_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
# IBM_CLOUD_SHELL_ACCOUNT_ID=<IBM Cloud account ID
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'ibm_cloud_shell_v1.env'

ibm_cloud_shell_service = None

config = None

account_id = None


##############################################################################
# Start of Examples for Service: IbmCloudShellV1
##############################################################################
# region
class TestIbmCloudShellV1Examples:
    """
    Example Test Class for IbmCloudShellV1
    """

    @classmethod
    def setup_class(cls):
        global ibm_cloud_shell_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            ibm_cloud_shell_service = IbmCloudShellV1.new_instance()

            # end-common
            assert ibm_cloud_shell_service is not None

            # Load the configuration
            global config
            config = read_external_sources(IbmCloudShellV1.DEFAULT_SERVICE_NAME)

            global account_id
            account_id = config['ACCOUNT_ID']
            assert account_id is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_account_settings_example(self):
        """
        get_account_settings request example
        """
        assert account_id is not None

        try:
            print('\nget_account_settings() result:')
            # begin-get_account_settings

            account_settings = ibm_cloud_shell_service.get_account_settings(account_id=account_id).get_result()

            print(json.dumps(account_settings, indent=2))

            # end-get_account_settings

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_account_settings_example(self):
        """
        update_account_settings request example
        """
        assert account_id is not None

        try:
            print('\nupdate_account_settings() result:')
            # begin-update_account_settings

            feature_model = [
                {
                    'enabled': True,
                    'key': 'server.file_manager',
                },
                {
                    'enabled': True,
                    'key': 'server.web_preview',
                },
            ]

            region_setting_model = [
                {
                    'enabled': True,
                    'key': 'eu-de',
                },
                {
                    'enabled': True,
                    'key': 'jp-tok',
                },
                {
                    'enabled': True,
                    'key': 'us-south',
                },
            ]

            account_settings = ibm_cloud_shell_service.update_account_settings(
                account_id=account_id,
                rev='130-12345678-abcd-1a2b-a1b2-1234567890ab',
                default_enable_new_features=False,
                default_enable_new_regions=True,
                enabled=True,
                features=feature_model,
                regions=region_setting_model,
            ).get_result()

            print(json.dumps(account_settings, indent=2))

            # end-update_account_settings

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: IbmCloudShellV1
##############################################################################
