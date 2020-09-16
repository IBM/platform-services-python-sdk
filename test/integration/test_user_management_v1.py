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

import os
import sys
import unittest
from ibm_platform_services.user_management_v1 import *


# Read config file
config_file = 'user-management.env'

class TestUserManagementV1(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file
        else:
            raise unittest.SkipTest('External configuration not available, skipping...')

        cls.user_management_service = UserManagementV1.new_instance(service_name='USERMGMT1')
        assert cls.user_management_service is not None

        cls.alternate_user_management_service = UserManagementV1.new_instance(service_name='USERMGMT2')
        assert cls.alternate_user_management_service is not None

        print('Setup complete.')

    def test_get_user_settings(self):


        user_settings = self.user_management_service.get_user_settings(
            account_id='1aa434630b594b8a88b961a44c9eb2a9',
            iam_id='IBMid-550008BJPR'
        )

        assert user_settings.get_status_code() == 200


    def test_update_user_settings(self):


        user_settings = self.user_management_service.update_user_settings(
            account_id='1aa434630b594b8a88b961a44c9eb2a9',
            iam_id='IBMid-550008BJPR',
            language='testString',
            notification_language='testString',
            allowed_ip_addresses='32.96.110.50,172.16.254.1',
            self_manage=True
        )

        assert user_settings.get_status_code() == 204


    def test_list_users(self):


        user_list = self.user_management_service.list_users(
            account_id='1aa434630b594b8a88b961a44c9eb2a9',
            state='ACTIVE'
        )

        assert user_list.get_status_code() == 200


    def test_invite_users(self):

        # Construct a dict representation of a InviteUser model
        invite_user_model = {
            'email': 'aminttest+linked_account_owner_11@mail.test.ibm.com',
            'account_role': 'Member'
        }

        # Construct a dict representation of a Role model
        role_model = {
            'role_id': 'crn:v1:bluemix:public:iam::::role:Viewer'
        }

        # Construct a dict representation of a Attribute model
        attribute_model = {
            'name': 'accountId',
            'value': '1aa434630b594b8a88b961a44c9eb2a9'
        }

        attribute_model2 = {
            'name': 'resourceGroupId',
            'value': '*'
        }

        # Construct a dict representation of a Resource model
        resource_model = {
            'attributes': [attribute_model, attribute_model2]
        }

        # Construct a dict representation of a InviteUserIamPolicy model
        invite_user_iam_policy_model = {
            'type': 'access',
            'roles': [role_model],
            'resources': [resource_model]
        }


        user_list = self.alternate_user_management_service.invite_users(
            account_id='1aa434630b594b8a88b961a44c9eb2a9',
            users=[invite_user_model],
            iam_policy=[invite_user_iam_policy_model],
            access_groups=['AccessGroupId-51675919-2bd7-4ce3-86e4-5faff8065574']
        )

        assert user_list.get_status_code() == 202


    def test_get_user_profile(self):


        user_profile = self.user_management_service.get_user_profile(
            account_id='1aa434630b594b8a88b961a44c9eb2a9',
            iam_id='IBMid-550008BJPR'
        )

        assert user_profile.get_status_code() == 200


    def test_update_user_profiles(self):


        response = self.user_management_service.update_user_profiles(
            account_id='1aa434630b594b8a88b961a44c9eb2a9',
            iam_id='IBMid-550008BJPR',
            firstname='testString',
            lastname='testString',
            state='ACTIVE',
            email='do_not_delete_user_without_iam_policy_stage@mail.test.ibm.com',
            phonenumber='testString',
            altphonenumber='testString',
            photo='testString'
        )

        assert response.get_status_code() == 204


    def test_remove_users(self):


        response = self.user_management_service.remove_users(
            account_id='1aa434630b594b8a88b961a44c9eb2a9',
            iam_id='de79cc26184417940e462fb814362c19'
        )

        assert response.get_status_code() == 204


