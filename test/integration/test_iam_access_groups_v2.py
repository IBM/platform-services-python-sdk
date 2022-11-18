# coding: utf-8

# Copyright 2019, 2022 IBM All Rights Reserved.
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
import os
import os.path
from datetime import datetime, timezone
import random
from ibm_cloud_sdk_core import *
from ibm_platform_services.iam_access_groups_v2 import *

# Config file name
config_file = 'iam_access_groups_v2.env'


class TestIamAccessGroupsV2:
    """
    Integration Test Class for IamAccessGroupsV2
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.iam_access_groups_service = IamAccessGroupsV2.new_instance()
            assert cls.iam_access_groups_service is not None

            cls.config = read_external_sources(IamAccessGroupsV2.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.iam_access_groups_service.enable_retries()

            cls.config = read_external_sources(IamAccessGroupsV2.DEFAULT_SERVICE_NAME)
            assert cls.config is not None
            cls.testAccountId = cls.config.get('TEST_ACCOUNT_ID')
            assert cls.testAccountId is not None

            cls.etagHeader = "ETag"
            cls.testGroupName = "SDK Test Group - Python"
            cls.testGroupDescription = (
                "This group is used for integration test purposes. It can be deleted at any time."
            )
            cls.testGroupETag = ""
            cls.testGroupId = ""
            cls.testUserId = "IBMid-" + str(random.randint(0, 99999))
            cls.testUserType = "user"
            cls.testClaimRuleId = ""
            cls.testClaimRuleETag = ""
            cls.testAccountSettings = AccountSettings()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @classmethod
    def teardown_class(cls):
        # Delete all the access groups that we created during the test.
        #
        # List all groups in the account(minus the public access group)
        response = cls.iam_access_groups_service.list_access_groups(
            account_id=cls.testAccountId, hide_public_access=True
        )
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
                now = datetime.now(tz=timezone.utc)
                minutesDifference = (now - group.created_at).seconds / 60

                if group.id == cls.testGroupId or minutesDifference > 5:
                    response = cls.iam_access_groups_service.delete_access_group(access_group_id=group.id, force=True)
                    assert response is not None
                    assert response.get_status_code() == 204
        print('\nClean up complete.')

    @needscredentials
    def test_00_account_id(self):
        assert self.testAccountId
        print('\nTest account id: ', self.testAccountId)

    @needscredentials
    def test_01_create_access_group(self):
        response = self.iam_access_groups_service.create_access_group(
            account_id=self.testAccountId, name=self.testGroupName
        )
        assert response is not None
        assert response.get_status_code() == 201

        result_dict = response.get_result()
        assert result_dict is not None

        result = Group.from_dict(result_dict)
        assert result is not None
        assert result.account_id == self.testAccountId
        assert result.name == self.testGroupName

        self.__class__.testGroupId = result.id

    @needscredentials
    def test_02_get_access_group(self):
        assert self.testGroupId
        print("Group ID: ", self.testGroupId)

        response = self.iam_access_groups_service.get_access_group(access_group_id=self.testGroupId)
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

    @needscredentials
    def test_03_update_access_group(self):
        assert self.testGroupId
        assert self.testGroupETag
        print("Group ID: ", self.testGroupId)

        response = self.iam_access_groups_service.update_access_group(
            access_group_id=self.testGroupId, if_match=self.testGroupETag, description=self.testGroupDescription
        )
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

    @needscredentials
    def test_04_list_access_groups(self):
        print("Group ID: ", self.testGroupId)

        response = self.iam_access_groups_service.list_access_groups(
            account_id=self.testAccountId, hide_public_access=True
        )
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

    @needscredentials
    def test_04_list_access_groups_with_pager(self):
        all_results = []

        # Test get_next().
        pager = AccessGroupsPager(
            client=self.iam_access_groups_service,
            account_id=self.testAccountId,
            hide_public_access=True,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = AccessGroupsPager(
            client=self.iam_access_groups_service,
            account_id=self.testAccountId,
            hide_public_access=True,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_access_groups() returned a total of {len(all_results)} items(s) using AccessGroupsPager.')

    @needscredentials
    def test_05_add_members_to_access_group(self):
        assert self.testGroupId
        print("Group ID: ", self.testGroupId)
        print("User ID: ", self.testUserId)

        members = [AddGroupMembersRequestMembersItem(iam_id=self.testUserId, type=self.testUserType)]

        response = self.iam_access_groups_service.add_members_to_access_group(
            access_group_id=self.testGroupId, members=members
        )
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

    @needscredentials
    def test_06_add_member_to_multiple_access_groups(self):
        assert self.testGroupId
        print("Group ID: ", self.testGroupId)
        print("User ID: ", self.testUserId)

        members = [AddGroupMembersRequestMembersItem(iam_id=self.testUserId, type=self.testUserType)]

        response = self.iam_access_groups_service.add_member_to_multiple_access_groups(
            account_id=self.testAccountId, iam_id=self.testUserId, type=self.testUserType, groups=[self.testGroupId]
        )
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

    @needscredentials
    def test_07_check_group_membership(self):
        assert self.testGroupId
        print("Group ID: ", self.testGroupId)
        print("User ID: ", self.testUserId)

        response = self.iam_access_groups_service.is_member_of_access_group(
            access_group_id=self.testGroupId, iam_id=self.testUserId
        )
        assert response is not None
        assert response.get_status_code() == 204

        result_dict = response.get_result()
        assert result_dict is None

    @needscredentials
    def test_08_list_access_group_members(self):
        assert self.testGroupId
        print("Group ID: ", self.testGroupId)
        print("User ID: ", self.testUserId)

        response = self.iam_access_groups_service.list_access_group_members(access_group_id=self.testGroupId)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = GroupMembersList.from_dict(result_dict)
        assert result is not None

        # Confirm the test user is present
        foundTestUser = False
        for member in result.members:
            if member.iam_id == self.testUserId:
                foundTestUser = True
                break
        assert foundTestUser

    @needscredentials
    def test_08a_list_access_group_members_with_pager(self):
        all_results = []

        # Test get_next().
        pager = AccessGroupMembersPager(
            client=self.iam_access_groups_service,
            access_group_id=self.testGroupId,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = AccessGroupMembersPager(
            client=self.iam_access_groups_service,
            access_group_id=self.testGroupId,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(
            f'\nlist_access_group_members() returned a total of {len(all_results)} items(s) using AccessGroupMembersPager.'
        )

    @needscredentials
    def test_09_delete_group_membership(self):
        assert self.testGroupId
        print("Group ID: ", self.testGroupId)
        print("User ID: ", self.testUserId)

        response = self.iam_access_groups_service.remove_member_from_access_group(
            access_group_id=self.testGroupId, iam_id=self.testUserId
        )
        assert response is not None
        assert response.get_status_code() == 204

        result_dict = response.get_result()
        assert result_dict is None

    @needscredentials
    def test_10_delete_member_from_all_groups(self):
        assert self.testGroupId
        print("Group ID: ", self.testGroupId)
        print("User ID: ", self.testUserId)

        try:
            response = self.iam_access_groups_service.remove_member_from_all_access_groups(
                account_id=self.testAccountId, iam_id=self.testUserId
            )
        except ApiException as e:
            assert e.http_response.status_code == 404
            assert e.code == 404
            assert self.testUserId in e.message

    @needscredentials
    def test_11_delete_bulk_members_from_access_group(self):
        assert self.testGroupId
        print("Group ID: ", self.testGroupId)
        print("User ID: ", self.testUserId)

        try:
            response = self.iam_access_groups_service.remove_members_from_access_group(
                access_group_id=self.testGroupId, members=[self.testUserId]
            )
        except ApiException as e:
            assert e.http_response.status_code == 404
            assert e.code == 404
            assert self.testGroupId in e.message

    @needscredentials
    def test_12_create_access_group_rule(self):
        assert self.testGroupId
        print("Group ID: ", self.testGroupId)

        testExpiration = 24

        response = self.iam_access_groups_service.add_access_group_rule(
            access_group_id=self.testGroupId,
            expiration=testExpiration,
            realm_name="test realm name",
            conditions=[RuleConditions("test claim", "EQUALS", "1")],
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

    @needscredentials
    def test_13_get_access_group_rule(self):
        assert self.testGroupId
        assert self.testClaimRuleId
        print("Group ID: ", self.testGroupId)
        print("Rule ID: ", self.testClaimRuleId)

        response = self.iam_access_groups_service.get_access_group_rule(
            access_group_id=self.testGroupId, rule_id=self.testClaimRuleId
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

        self.__class__.testClaimRuleETag = response.get_headers().get(self.etagHeader)

    @needscredentials
    def test_14_list_access_group_rules(self):
        assert self.testGroupId
        print("Group ID: ", self.testGroupId)
        print("Rule ID: ", self.testClaimRuleId)

        response = self.iam_access_groups_service.list_access_group_rules(access_group_id=self.testGroupId)
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

    @needscredentials
    def test_15_update_access_group_rule(self):
        assert self.testGroupId
        assert self.testClaimRuleId
        print("Group ID: ", self.testGroupId)
        print("Rule ID: ", self.testClaimRuleId)

        testExpiration = 24

        response = self.iam_access_groups_service.replace_access_group_rule(
            access_group_id=self.testGroupId,
            rule_id=self.testClaimRuleId,
            if_match=self.testClaimRuleETag,
            expiration=testExpiration,
            realm_name="updated test realm name",
            conditions=[RuleConditions("test claim", "EQUALS", "1")],
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

    @needscredentials
    def test_16_delete_access_group_rule(self):
        assert self.testGroupId
        assert self.testClaimRuleId
        print("Group ID: ", self.testGroupId)
        print("Rule ID: ", self.testClaimRuleId)

        response = self.iam_access_groups_service.remove_access_group_rule(
            access_group_id=self.testGroupId, rule_id=self.testClaimRuleId
        )
        assert response is not None
        assert response.get_status_code() == 204

        result_dict = response.get_result()
        assert result_dict is None

    @needscredentials
    def test_17_get_account_settings(self):
        response = self.iam_access_groups_service.get_account_settings(account_id=self.testAccountId)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = AccountSettings.from_dict(result_dict)
        assert result is not None
        assert result.account_id == self.testAccountId

        self.__class__.testAccountSettings = result

    @needscredentials
    def test_18_update_account_settings(self):
        response = self.iam_access_groups_service.update_account_settings(
            account_id=self.testAccountId, public_access_enabled=self.testAccountSettings.public_access_enabled
        )
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = AccountSettings.from_dict(result_dict)
        assert result is not None
        assert result.account_id == self.testAccountId
        assert result.public_access_enabled == self.testAccountSettings.public_access_enabled
