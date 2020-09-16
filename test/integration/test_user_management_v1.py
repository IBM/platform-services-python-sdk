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
Integration Tests for UserManagementV1
"""

import os
import pytest
from ibm_platform_services.user_management_v1 import *

# Config file name
config_file = 'user_management.env'

class TestUserManagementV1():
    """
    Integration Test Class for UserManagementV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.user_management_service = UserManagementV1.new_instance(
                )
            assert cls.user_management_service is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_user_settings(self):

        get_user_settings_response = self.user_management_service.get_user_settings(
            account_id='testString',
            iam_id='testString'
        )

        assert get_user_settings_response.get_status_code() == 200
        user_settings = get_user_settings_response.get_result()
        assert user_settings is not None

    @needscredentials
    def test_update_user_settings(self):

        update_user_settings_response = self.user_management_service.update_user_settings(
            account_id='testString',
            iam_id='testString',
            language='testString',
            notification_language='testString',
            allowed_ip_addresses='32.96.110.50,172.16.254.1',
            self_manage=True
        )

        assert update_user_settings_response.get_status_code() == 200
        user_settings = update_user_settings_response.get_result()
        assert user_settings is not None

    @needscredentials
    def test_list_users(self):

        list_users_response = self.user_management_service.list_users(
            account_id='testString',
            state='testString'
        )

        assert list_users_response.get_status_code() == 200
        user_list = list_users_response.get_result()
        assert user_list is not None

    @needscredentials
    def test_invite_users(self):

        # Construct a dict representation of a InviteUser model
        invite_user_model = {
            'email': 'testString',
            'account_role': 'testString'
        }

        # Construct a dict representation of a Role model
        role_model = {
            'role_id': 'testString'
        }

        # Construct a dict representation of a Attribute model
        attribute_model = {
            'name': 'testString',
            'value': 'testString'
        }

        # Construct a dict representation of a Resource model
        resource_model = {
            'attributes': [attribute_model]
        }

        # Construct a dict representation of a InviteUserIamPolicy model
        invite_user_iam_policy_model = {
            'type': 'testString',
            'roles': [role_model],
            'resources': [resource_model]
        }

        invite_users_response = self.user_management_service.invite_users(
            account_id='testString',
            users=[invite_user_model],
            iam_policy=[invite_user_iam_policy_model],
            access_groups=['testString']
        )

        assert invite_users_response.get_status_code() == 202
        user_list = invite_users_response.get_result()
        assert user_list is not None

    @needscredentials
    def test_get_user_profile(self):

        get_user_profile_response = self.user_management_service.get_user_profile(
            account_id='testString',
            iam_id='testString'
        )

        assert get_user_profile_response.get_status_code() == 200
        user_profile = get_user_profile_response.get_result()
        assert user_profile is not None

    @needscredentials
    def test_update_user_profiles(self):

        update_user_profiles_response = self.user_management_service.update_user_profiles(
            account_id='testString',
            iam_id='testString',
            firstname='testString',
            lastname='testString',
            state='testString',
            email='testString',
            phonenumber='testString',
            altphonenumber='testString',
            photo='testString'
        )

        assert update_user_profiles_response.get_status_code() == 204

    @needscredentials
    def test_remove_users(self):

        remove_users_response = self.user_management_service.remove_users(
            account_id='testString',
            iam_id='testString'
        )

        assert remove_users_response.get_status_code() == 204

