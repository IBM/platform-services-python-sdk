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
 This class contains an integration test for User Management service.
"""

import os
import sys
import unittest
import urllib.parse as urlparse
from urllib.parse import parse_qs

from ibm_cloud_sdk_core.utils import read_external_sources
from ibm_platform_services.user_management_v1 import *

# Read config file
config_file = 'user_management.env'

REMOVED_USERID = None


class TestUserManagementV1(unittest.TestCase):
    """
    Integration Test Class for UserManagementV1
    """
    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file
        else:
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        cls.config = read_external_sources(
            UserManagementV1.DEFAULT_SERVICE_NAME
        )
        assert cls.config is not None

        cls.user_management_service = UserManagementV1.new_instance(
            service_name=UserManagementV1.DEFAULT_SERVICE_NAME)
        assert cls.user_management_service is not None

        cls.user_management_admin_service = UserManagementV1.new_instance(
            service_name='USER_MANAGEMENT_ADMIN')
        assert cls.user_management_admin_service is not None

        cls.ACCOUNT_ID = cls.config['ACCOUNT_ID']
        cls.IAM_USERID = cls.config['USER_ID']
        cls.INVITED_USER_EMAIL = cls.config['MEMBER_EMAIL']
        cls.VIEWER_ROLEID = cls.config['VIEWER_ROLE_ID']
        cls.ACCESS_GROUP_ID = cls.config['ACCESS_GROUP_ID']

        print('\nService URL: ', cls.user_management_service.service_url)
        print('Setup complete.')

    def test_01_get_user_settings(self):

        user_settings = self.user_management_service.get_user_settings(
            account_id=self.ACCOUNT_ID, iam_id=self.IAM_USERID)

        assert user_settings.get_status_code() == 200
        assert user_settings.get_result() is not None
        print('\nget_user_settings() result: ',
              json.dumps(user_settings.get_result(), indent=2))

    def test_02_update_user_settings(self):

        user_settings = self.user_management_service.update_user_settings(
            account_id=self.ACCOUNT_ID,
            iam_id=self.IAM_USERID,
            language='French',
            notification_language='English',
            allowed_ip_addresses='32.96.110.50,172.16.254.1',
            self_manage=True)

        assert user_settings.get_status_code() == 204

    def test_03_list_users(self):
        results = []
        start = None

        while True:
            response = self.user_management_service.list_users(
                account_id=self.ACCOUNT_ID, limit=10, start=start)
            assert response.get_status_code() == 200

            user_list = response.get_result()
            assert user_list is not None

            assert 'resources' in user_list

            results.extend(user_list['resources'])

            next_url = user_list.get('next_url')
            start = None
            if next_url is not None:
                start = self.get_start_token_from_url(next_url)

            if start is None:
                break

        num_users = len(results)
        print(f'\nlist_users() returned a total of {num_users} users.')

    def test_04_invite_users(self):

        # Construct a dict representation of a InviteUser model
        invite_user_model = {
            'email': self.INVITED_USER_EMAIL,
            'account_role': 'Member'
        }

        # Construct a dict representation of a Role model
        role_model = {'role_id': self.VIEWER_ROLEID}

        # Construct a dict representation of a Attribute model
        attribute_model = {'name': 'accountId', 'value': self.ACCOUNT_ID}

        attribute_model2 = {'name': 'resourceGroupId', 'value': '*'}

        # Construct a dict representation of a Resource model
        resource_model = {'attributes': [attribute_model, attribute_model2]}

        # Construct a dict representation of a InviteUserIamPolicy model
        invite_user_iam_policy_model = {
            'type': 'access',
            'roles': [role_model],
            'resources': [resource_model]
        }

        response = self.user_management_admin_service.invite_users(
            account_id=self.ACCOUNT_ID,
            users=[invite_user_model],
            iam_policy=[invite_user_iam_policy_model],
            access_groups=[self.ACCESS_GROUP_ID])

        assert response.get_status_code() == 202
        assert response.get_result() is not None
        print('\ninvite_users() result: ',
              json.dumps(response.get_result(), indent=2))

        invited_users = response.get_result().get('resources')
        assert invited_users is not None

        global REMOVED_USERID
        REMOVED_USERID = invited_users[0].get('id')
        assert REMOVED_USERID is not None

    def test_05_get_user_profile(self):

        user_profile = self.user_management_service.get_user_profile(
            account_id=self.ACCOUNT_ID, iam_id=self.IAM_USERID)

        assert user_profile.get_status_code() == 200
        assert user_profile.get_result() is not None
        print('\nget_user_profile() result: ',
              json.dumps(user_profile.get_result(), indent=2))

    def test_06_update_user_profile(self):

        response = self.user_management_service.update_user_profile(
            account_id=self.ACCOUNT_ID,
            iam_id=self.IAM_USERID,
            firstname='John',
            lastname='Doe',
            state='ACTIVE',
            email=
            'do_not_delete_user_without_iam_policy_stage@mail.test.ibm.com')

        assert response.get_status_code() == 204

    def test_07_remove_user(self):
        global REMOVED_USERID
        assert REMOVED_USERID is not None

        response = self.user_management_service.remove_user(
            account_id=self.ACCOUNT_ID, iam_id=REMOVED_USERID)

        assert response.get_status_code() == 204

    def get_start_token_from_url(self, url):
        if url is None:
            return None
        try:
            parsed = urlparse.urlparse(url)
            query_value = parse_qs(parsed.query).get('_start')
            if query_value is not None:
                return query_value[0]
            return None
        except Exception as e:
            print('Error parsing URL', e)
            return None
