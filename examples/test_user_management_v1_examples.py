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
Examples for UserManagementV1
"""

import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.user_management_v1 import *

# Config file name
config_file = 'user_management_v1.env'

user_management_service = None

config = None


##############################################################################
# Start of Examples for Service: UserManagementV1
##############################################################################
# region
class TestUserManagementV1Examples():
    """
    Example Test Class for UserManagementV1
    """

    @classmethod
    def setup_class(cls):
        global user_management_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            user_management_service = UserManagementV1.new_instance(
            )

            # end-common
            assert user_management_service is not None

            # Load the configuration
            global config
            config = read_external_sources(UserManagementV1.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_invite_users_example(self):
        """
        invite_users request example
        """
        try:
            # begin-invite_users

            invited_user_list = user_management_service.invite_users(
                account_id='testString'
            ).get_result()

            print(json.dumps(invited_user_list, indent=2))

            # end-invite_users

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_users_example(self):
        """
        list_users request example
        """
        try:
            # begin-list_users

            user_list = user_management_service.list_users(
                account_id='testString'
            ).get_result()

            print(json.dumps(user_list, indent=2))

            # end-list_users

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_remove_user_example(self):
        """
        remove_user request example
        """
        try:
            # begin-remove_user

            response = user_management_service.remove_user(
                account_id='testString',
                iam_id='testString'
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-remove_user

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_user_profile_example(self):
        """
        get_user_profile request example
        """
        try:
            # begin-get_user_profile

            user_profile = user_management_service.get_user_profile(
                account_id='testString',
                iam_id='testString'
            ).get_result()

            print(json.dumps(user_profile, indent=2))

            # end-get_user_profile

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_user_profile_example(self):
        """
        update_user_profile request example
        """
        try:
            # begin-update_user_profile

            response = user_management_service.update_user_profile(
                account_id='testString',
                iam_id='testString'
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-update_user_profile

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_user_settings_example(self):
        """
        get_user_settings request example
        """
        try:
            # begin-get_user_settings

            user_settings = user_management_service.get_user_settings(
                account_id='testString',
                iam_id='testString'
            ).get_result()

            print(json.dumps(user_settings, indent=2))

            # end-get_user_settings

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_user_settings_example(self):
        """
        update_user_settings request example
        """
        try:
            # begin-update_user_settings

            response = user_management_service.update_user_settings(
                account_id='testString',
                iam_id='testString'
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-update_user_settings

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: UserManagementV1
##############################################################################
