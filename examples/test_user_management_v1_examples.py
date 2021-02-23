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

#
# This file provides an example of how to use the User Management service.
#
# The following configuration properties are assumed to be defined:
#
# USER_MANAGEMENT_URL=<service url>
# USER_MANAGEMENT_AUTHTYPE=iam
# USER_MANAGEMENT_AUTH_URL=<IAM token service URL - omit this if using the production environment>
# USER_MANAGEMENT_APIKEY=<IAM apikey>
# USER_MANAGEMENT_ACCOUNT_ID=<account ID>
# USER_MANAGEMENT_USER_ID=<user ID>
# USER_MANAGEMENT_MEMBER_EMAIL=<member email to invite>
# USER_MANAGEMENT_VIEWER_ROLE_ID=<viewer role ID>
# USER_MANAGEMENT_ACCESS_GROUP_ID=<access group ID>
# # alternateService
# USERMGMT2_URL=<service url>
# USERMGMT2_AUTHTYPE=iam
# USERMGMT2_AUTH_URL=<IAM token service URL - omit this if using the production environment>
# USERMGMT2_APIKEY=<IAM apikey>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'user_management.env'

user_management_service = None
alternate_user_management_service = None


config = None

account_id = None
user_id = None
member_email = None
viewer_role_id = None
access_group_id = None

delete_user_id = None

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

            global alternate_user_management_service

            # begin-common

            user_management_service = UserManagementV1.new_instance()

            alternate_user_management_service = UserManagementV1.new_instance(
                service_name='USERMGMT2',
            )

            # end-common
            assert user_management_service is not None

            # Load the configuration
            global config
            config = read_external_sources(
                UserManagementV1.DEFAULT_SERVICE_NAME
             )

            global account_id
            account_id = config['ACCOUNT_ID']

            global user_id
            user_id = config['USER_ID']

            global member_email
            member_email = config['MEMBER_EMAIL']

            global viewer_role_id
            viewer_role_id = config['VIEWER_ROLE_ID']

            global access_group_id
            access_group_id = config['ACCESS_GROUP_ID']

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_invite_users_example(self):
        """
        invite_users request example
        """
        assert member_email is not None
        assert viewer_role_id is not None
        assert account_id is not None
        assert access_group_id is not None

        try:
            # begin-invite_users

            invite_user_model = {
                'email': member_email,
                'account_role': 'Member'
            }

            role_model = {'role_id': viewer_role_id}

            attribute_model = {'name': 'accountId', 'value': account_id}

            attribute_model2 = {'name': 'resourceGroupId', 'value': '*'}

            resource_model = {'attributes': [attribute_model, attribute_model2]}

            invite_user_iam_policy_model = {
                'type': 'access',
                'roles': [role_model],
                'resources': [resource_model]
            }

            invite_user_response = alternate_user_management_service.invite_users(
                account_id=account_id,
                users=[invite_user_model],
                iam_policy=[invite_user_iam_policy_model],
                access_groups=[access_group_id]
            ).get_result()

            print(json.dumps(invite_user_response, indent=2))

            # end-invite_users

            global delete_user_id
            delete_user_id = invite_user_response.get('resources')[0].get('id')

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_users_example(self):
        """
        list_users request example
        """
        assert account_id is not None

        try:
            # begin-list_users

            user_list = user_management_service.list_users(
                account_id=account_id,
                state='ACTIVE',
                limit=100,
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
        assert account_id is not None
        assert delete_user_id is not None

        try:
            # begin-remove_user

            response = user_management_service.remove_user(
                account_id=account_id,
                iam_id=delete_user_id,
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
        assert account_id is not None
        assert user_id is not None

        try:
            # begin-get_user_profile

            user_profile = user_management_service.get_user_profile(
                account_id=account_id,
                iam_id=user_id,
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
        assert account_id is not None
        assert user_id is not None

        try:
            # begin-update_user_profile

            response = user_management_service.update_user_profile(
                account_id=account_id,
                iam_id=user_id,
                phonenumber='123456789',
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
        assert account_id is not None
        assert user_id is not None

        try:
            # begin-get_user_settings

            user_settings = user_management_service.get_user_settings(
                account_id=account_id,
                iam_id=user_id,
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
        assert account_id is not None
        assert user_id is not None

        try:
            # begin-update_user_settings

            response = user_management_service.update_user_settings(
                account_id=account_id,
                iam_id=user_id,
                self_manage=True,
                allowed_ip_addresses='192.168.0.2,192.168.0.3',
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-update_user_settings

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: UserManagementV1
##############################################################################
