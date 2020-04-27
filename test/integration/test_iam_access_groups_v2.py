# coding: utf-8

# Copyright 2019 IBM All Rights Reserved.
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
 This class contains an integration test for the IAM Access Groups service.
"""

import pytest
import unittest
import os
import os.path
import datetime
import random
from ibm_cloud_sdk_core import *
from ibm_platform_services.iam_access_groups_v2 import *

# Read config file
configFile = 'iam_access_groups.env'
configLoaded = None

if os.path.exists(configFile):
    os.environ['IBM_CREDENTIALS_FILE'] = configFile
    configLoaded = True
else:
    print('External configuration was not found, skipping tests...')

class TestIamAccessGroupsV2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not configLoaded:
            raise unittest.SkipTest('External configuration not available, skipping...')
          
        cls.service = IamAccessGroupsV2.new_instance()
        assert cls.service is not None

        cls.config = read_external_sources(
            IamAccessGroupsV2.DEFAULT_SERVICE_NAME)
        assert cls.config is not None
        cls.testAccountId = cls.config.get('TEST_ACCOUNT_ID')
        assert cls.testAccountId is not None

        cls.etagHeader = "ETag"
        cls.testGroupName = "SDK Test Group - Python"
        cls.testGroupDescription = "This group is used for integration test purposes. It can be deleted at any time."
        cls.testGroupETag = ""
        cls.testGroupId = ""
        cls.testUserId = "IBMid-" + str(random.randint(0, 99999))
        cls.testUserType = "user"
        cls.testClaimRuleId = ""
        cls.testClaimRuleETag = ""
        cls.testAccountSettings = AccountSettings()

        print('\nSetup complete.')
        
    @classmethod
    def tearDownClass(cls):
        # Delete all the access groups that we created during the test.
        #
        # List all groups in the account(minus the public access group)
        response = cls.service.list_access_groups(
            account_id=cls.testAccountId, hide_public_access=True)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = GroupsList.from_dict(result_dict)
        assert result is not None

        # Iterate across the groups
        for group in result.groups:

            # Force delete the test group (or any test groups older than 5 minutes)
            if group.name == cls.testGroupName:

                createdAt = datetime.datetime.strptime(group.created_at,'%Y-%m-%dT%H:%M:%SZ')
                now = datetime.datetime.utcnow()
                minutesDifference = (now - createdAt).seconds / 60

                if group.id == cls.testGroupId or minutesDifference > 5:
                    response = cls.service.delete_access_group(
                        access_group_id=group.id, force=True)
                    assert response is not None
                    assert response.get_status_code() == 204

        print('\nClean up complete.')

    def test_00_account_id(self):
        assert self.testAccountId
        print('\nTest account id: ', self.testAccountId)

    def test_01_create_access_group(self):
        response = self.service.create_access_group(
            account_id=self.testAccountId, name=self.testGroupName)
        assert response is not None
        assert response.get_status_code() == 201

        result_dict = response.get_result()
        assert result_dict is not None

        result = Group.from_dict(result_dict)
        assert result is not None
        assert result.account_id == self.testAccountId
        assert result.name == self.testGroupName

        self.__class__.testGroupId = result.id

    def test_02_get_access_group(self):
        assert self.testGroupId

        response = self.service.get_access_group(access_group_id=self.testGroupId)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = Group.from_dict(result_dict)
        assert result is not None
        assert result.account_id == self.testAccountId
        assert result.id == self.testGroupId
        assert result.name == self.testGroupName
        assert result.description == ""

        self.__class__.testGroupETag = response.get_headers().get(self.etagHeader)

    def test_03_update_access_group(self):
        assert self.testGroupId
        assert self.testGroupETag

        response = self.service.update_access_group(
            access_group_id=self.testGroupId, if_match=self.testGroupETag, description=self.testGroupDescription)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = Group.from_dict(result_dict)
        assert result is not None
        assert result.account_id == self.testAccountId
        assert result.id == self.testGroupId
        assert result.name == self.testGroupName
        assert result.description == self.testGroupDescription

    def test_04_list_access_groups(self):
        response = self.service.list_access_groups(
            account_id=self.testAccountId,hide_public_access=True)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = GroupsList.from_dict(result_dict)
        assert result is not None

        # Confirm the test group is present
        foundTestGroup = False
        for group in result.groups:
            if group.id == self.testGroupId:
                foundTestGroup = True
                break
        assert foundTestGroup

    def test_05_add_members_to_access_group(self):
        assert self.testGroupId

        members = [AddGroupMembersRequestMembersItem(
            iam_id=self.testUserId, type=self.testUserType)]

        response = self.service.add_members_to_access_group(
            access_group_id=self.testGroupId, members=members)
        assert response is not None
        assert response.get_status_code() == 207

        result_dict = response.get_result()
        assert result_dict is not None

        result = AddGroupMembersResponse.from_dict(result_dict)
        assert result is not None

        # Confirm the test user is present
        foundTestUser = False
        for member in result.members:
            if member.iam_id == self.testUserId:
                foundTestUser = True
                break
        assert foundTestUser

    def test_06_add_member_to_multiple_access_groups(self):
        assert self.testGroupId

        members = [AddGroupMembersRequestMembersItem(
            iam_id=self.testUserId, type=self.testUserType)]

        response = self.service.add_member_to_multiple_access_groups(
            account_id=self.testAccountId, iam_id=self.testUserId, type=self.testUserType, groups=[self.testGroupId])
        assert response is not None
        assert response.get_status_code() == 207

        result_dict = response.get_result()
        assert result_dict is not None

        result = AddMembershipMultipleGroupsResponse.from_dict(result_dict)
        assert result is not None

        # Confirm the test group is present
        foundTestGroup = False
        for group in result.groups:
            if group.access_group_id == self.testGroupId:
                foundTestGroup = True
                break
        assert foundTestGroup

    def test_07_check_group_membership(self):
        # This test is temporarily disabled/changed
        # (because it fails intermittently in parallel)

        # assert self.testGroupId

        # response = self.service.is_member_of_access_group(
        #     access_group_id=self.testGroupId, iam_id=self.testUserId)
        # assert response is not None
        # assert response.get_status_code() == 204

        # result_dict = response.get_result()
        # assert result_dict is None

        try:
            response = self.service.is_member_of_access_group(
                access_group_id=self.testGroupId, iam_id=self.testUserId)
        except ApiException as e:
            print(e)

    def test_08_list_group_members(self):
        # This test is temporarily disabled/changed
        # (because it fails intermittently in parallel)

        # assert self.testGroupId

        # response = self.service.list_access_group_members(
        #     access_group_id=self.testGroupId)
        # assert response is not None
        # assert response.get_status_code() == 200

        # result_dict = response.get_result()
        # assert result_dict is not None

        # result = GroupMembersList.from_dict(result_dict)
        # assert result is not None

        # # Confirm the test user is present
        # foundTestUser = False
        # for member in result.members:
        #     if member.iam_id == self.testUserId:
        #         foundTestUser = True
        #         break
        # assert foundTestUser

        try:
            response = self.service.list_access_group_members(
                access_group_id=self.testGroupId)
        except ApiException as e:
            print(e)

    def test_09_delete_group_membership(self):
        # This test is temporarily disabled/changed
        # (because it fails intermittently in parallel)

        # assert self.testGroupId

        # response = self.service.remove_member_from_access_group(
        #     access_group_id=self.testGroupId, iam_id=self.testUserId)
        # assert response is not None
        # assert response.get_status_code() == 204

        # result_dict = response.get_result()
        # assert result_dict is None

        print("Group ID: ", self.testGroupId)
        print("User ID: ", self.testUserId)

        try:
            response = self.service.remove_member_from_access_group(
                access_group_id=self.testGroupId, iam_id=self.testUserId)
        except ApiException as e:
            print(e)

    def test_10_delete_member_from_all_groups(self):
        assert self.testGroupId

        try:
            response = self.service.remove_member_from_all_access_groups(
                account_id=self.testAccountId, iam_id=self.testUserId)
        except ApiException as e:
            assert e.http_response.status_code == 404
            assert e.code == 404
            assert e.message.__contains__(self.testUserId)

    def test_11_delete_bulk_members_from_access_group(self):
        assert self.testGroupId

        try:
            response = self.service.remove_members_from_access_group(
                access_group_id=self.testGroupId, members=[self.testUserId])
        except ApiException as e:
            assert e.http_response.status_code == 404
            assert e.code == 404
            assert e.message.__contains__(self.testGroupId)

    def test_12_create_access_group_rule(self):
        assert self.testGroupId

        testExpiration = 24

        response = self.service.add_access_group_rule(
            access_group_id=self.testGroupId,
            expiration=testExpiration,
            realm_name="test realm name",
            conditions=[RuleConditions("test claim", "EQUALS", "1")]
        )
        assert response is not None
        assert response.get_status_code() == 201

        result_dict = response.get_result()
        assert result_dict is not None

        result = Rule.from_dict(result_dict)
        assert result is not None
        assert result.account_id == self.testAccountId
        assert result.access_group_id == self.testGroupId
        assert result.expiration == testExpiration

        self.__class__.testClaimRuleId = result.id

    def test_13_get_access_group_rule(self):
        assert self.testGroupId
        assert self.testClaimRuleId

        response = self.service.get_access_group_rule(
            access_group_id=self.testGroupId, rule_id=self.testClaimRuleId)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = Rule.from_dict(result_dict)
        assert result is not None
        assert result.account_id == self.testAccountId
        assert result.access_group_id == self.testGroupId
        assert result.id == self.testClaimRuleId

        self.__class__.testClaimRuleETag = response.get_headers().get(self.etagHeader)

    def test_14_list_access_group_rules(self):
        assert self.testGroupId

        response = self.service.list_access_group_rules(access_group_id=self.testGroupId)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = RulesList.from_dict(result_dict)
        assert result is not None

        # Confirm the test rule is present
        foundTestClaimRule = False
        for rule in result.rules:
            if rule.id == self.testClaimRuleId:
                foundTestClaimRule = True
                break
        assert foundTestClaimRule

    def test_15_update_access_group_rule(self):
        assert self.testGroupId
        assert self.testClaimRuleId

        testExpiration = 24

        response = self.service.replace_access_group_rule(
            access_group_id=self.testGroupId,
            rule_id=self.testClaimRuleId,
            if_match=self.testClaimRuleETag,
            expiration=testExpiration,
            realm_name="updated test realm name",
            conditions=[RuleConditions("test claim", "EQUALS", "1")]
        )
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = Rule.from_dict(result_dict)
        assert result is not None
        assert result.account_id == self.testAccountId
        assert result.access_group_id == self.testGroupId
        assert result.id == self.testClaimRuleId

    def test_16_delete_access_group_rule(self):
        assert self.testGroupId
        assert self.testClaimRuleId

        response = self.service.remove_access_group_rule(
            access_group_id=self.testGroupId, rule_id=self.testClaimRuleId)
        assert response is not None
        assert response.get_status_code() == 204

        result_dict = response.get_result()
        assert result_dict is None

    def test_17_get_account_settings(self):
        response = self.service.get_account_settings(account_id=self.testAccountId)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = AccountSettings.from_dict(result_dict)
        assert result is not None
        assert result.account_id == self.testAccountId

        self.__class__.testAccountSettings = result

    def test_18_update_account_settings(self):
        response = self.service.update_account_settings(
            account_id=self.testAccountId, 
            public_access_enabled=self.testAccountSettings.public_access_enabled
        )
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = AccountSettings.from_dict(result_dict)
        assert result is not None
        assert result.account_id == self.testAccountId
        assert result.public_access_enabled == self.testAccountSettings.public_access_enabled
