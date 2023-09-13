# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2023.
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
Integration Tests for IamAccessGroupsV2
"""

from ibm_cloud_sdk_core import *
import os
import time
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
            cls.testPolicyTemplateId = cls.config.get('TEST_POLICY_TEMPLATE_ID')
            cls.testAccountGroupId = cls.config.get('TEST_ACCOUNT_GROUP_ID')
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
            cls.testTemplateId = ""
            cls.testTemplateEtag = ""
            cls.testTemplateLatestEtag = ""
            cls.testAssignmentId = ""
            cls.testAssignmentEtag = ""

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

    @needscredentials
    def test_create_template(self):
        # Construct a dict representation of a MembersActionControls model
        members_action_controls_model = {
            'add': True,
            'remove': False,
        }
        # Construct a dict representation of a MembersInput model
        members_input_model = {
            'users': ['IBMid-50PJGPKYJJ', 'IBMid-665000T8WY'],
            'action_controls': members_action_controls_model,
        }
        # Construct a dict representation of a ConditionInput model
        condition_input_model = {
            'claim': 'blueGroup',
            'operator': 'CONTAINS',
            'value': '\"test-bluegroup-saml\"',
        }
        # Construct a dict representation of a RulesActionControls model
        rules_action_controls_model = {
            'remove': False,
        }
        # Construct a dict representation of a RuleInput model
        rule_input_model = {
            'name': 'Manager group rule',
            'expiration': 12,
            'realm_name': 'https://idp.example.org/SAML2',
            'conditions': [condition_input_model],
            'action_controls': rules_action_controls_model,
        }
        # Construct a dict representation of a AssertionsActionControls model
        assertions_action_controls_model = {
            'add': False,
            'remove': True,
        }
        # Construct a dict representation of a AssertionsInput model
        assertions_input_model = {
            'rules': [rule_input_model],
            'action_controls': assertions_action_controls_model,
        }
        # Construct a dict representation of a AccessActionControls model
        access_action_controls_model = {
            'add': False,
        }
        # Construct a dict representation of a GroupActionControls model
        group_action_controls_model = {
            'access': access_action_controls_model,
        }
        # Construct a dict representation of a AccessGroupInput model
        access_group_input_model = {
            'name': 'IAM Admin Group',
            'description': 'This access group template allows admin access to all IAM platform services in the account.',
            'members': members_input_model,
            'assertions': assertions_input_model,
            'action_controls': group_action_controls_model,
        }
        # Construct a dict representation of a PolicyTemplatesInput model
        policy_templates_input_model = {
            'id': self.testPolicyTemplateId,
            'version': '1',
        }

        response = self.iam_access_groups_service.create_template(
            name='IAM Admin Group template',
            account_id=self.testAccountId,
            description='This access group template allows admin access to all IAM platform services in the account.',
            group=access_group_input_model,
            policy_template_references=[policy_templates_input_model],
            transaction_id='testString',
        )

        assert response.get_status_code() == 201
        create_template_response = response.get_result()
        assert create_template_response is not None
        self.__class__.testTemplateId = create_template_response['id']

    @needscredentials
    def test_list_templates(self):
        response = self.iam_access_groups_service.list_templates(
            account_id=self.testAccountId,
            transaction_id='testString',
            limit=50,
            offset=0,
            verbose=True,
        )

        assert response.get_status_code() == 200
        list_templates_response = response.get_result()
        assert list_templates_response is not None

    @needscredentials
    def test_list_templates_with_pager(self):
        all_results = []

        # Test get_next().
        pager = TemplatesPager(
            client=self.iam_access_groups_service,
            account_id=self.testAccountId,
            transaction_id='testString',
            limit=50,
            verbose=True,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = TemplatesPager(
            client=self.iam_access_groups_service,
            account_id=self.testAccountId,
            transaction_id='testString',
            limit=50,
            verbose=True,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_templates() returned a total of {len(all_results)} items(s) using TemplatesPager.')

    @needscredentials
    def test_create_template_version(self):
        # Construct a dict representation of a MembersActionControls model
        members_action_controls_model = {
            'add': True,
            'remove': False,
        }
        # Construct a dict representation of a MembersInput model
        members_input_model = {
            'users': ['IBMid-50PJGPKYJJ', 'IBMid-665000T8WY'],
            'action_controls': members_action_controls_model,
        }
        # Construct a dict representation of a ConditionInput model
        condition_input_model = {
            'claim': 'blueGroup',
            'operator': 'CONTAINS',
            'value': '\"test-bluegroup-saml\"',
        }
        # Construct a dict representation of a RulesActionControls model
        rules_action_controls_model = {
            'remove': True,
        }
        # Construct a dict representation of a RuleInput model
        rule_input_model = {
            'name': 'Manager group rule',
            'expiration': 12,
            'realm_name': 'https://idp.example.org/SAML2',
            'conditions': [condition_input_model],
            'action_controls': rules_action_controls_model,
        }
        # Construct a dict representation of a AssertionsActionControls model
        assertions_action_controls_model = {
            'add': False,
            'remove': True,
        }
        # Construct a dict representation of a AssertionsInput model
        assertions_input_model = {
            'rules': [rule_input_model],
            'action_controls': assertions_action_controls_model,
        }
        # Construct a dict representation of a AccessActionControls model
        access_action_controls_model = {
            'add': False,
        }
        # Construct a dict representation of a GroupActionControls model
        group_action_controls_model = {
            'access': access_action_controls_model,
        }
        # Construct a dict representation of a AccessGroupInput model
        access_group_input_model = {
            'name': 'IAM Admin Group 8',
            'description': 'This access group template allows admin access to all IAM platform services in the account.',
            'members': members_input_model,
            'assertions': assertions_input_model,
            'action_controls': group_action_controls_model,
        }
        # Construct a dict representation of a PolicyTemplatesInput model
        policy_templates_input_model = {
            'id': self.testPolicyTemplateId,
            'version': '1',
        }

        response = self.iam_access_groups_service.create_template_version(
            template_id=self.testTemplateId,
            name='IAM Admin Group template 2',
            description='This access group template allows admin access to all IAM platform services in the account.',
            group=access_group_input_model,
            policy_template_references=[policy_templates_input_model],
            transaction_id='testString',
        )

        assert response.get_status_code() == 201
        create_template_response = response.get_result()
        assert create_template_response is not None

    @needscredentials
    def test_list_template_versions(self):
        response = self.iam_access_groups_service.list_template_versions(
            template_id=self.testTemplateId,
            limit=100,
            offset=0,
        )

        assert response.get_status_code() == 200
        list_template_versions_response = response.get_result()
        assert list_template_versions_response is not None

    @needscredentials
    def test_list_template_versions_with_pager(self):
        all_results = []

        # Test get_next().
        pager = TemplateVersionsPager(
            client=self.iam_access_groups_service,
            template_id=self.testTemplateId,
            limit=100,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = TemplateVersionsPager(
            client=self.iam_access_groups_service,
            template_id=self.testTemplateId,
            limit=100,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(
            f'\nlist_template_versions() returned a total of {len(all_results)} items(s) using TemplateVersionsPager.'
        )

    @needscredentials
    def test_get_template_version(self):
        response = self.iam_access_groups_service.get_template_version(
            template_id=self.testTemplateId,
            version_num='1',
            transaction_id='testString',
        )

        assert response.get_status_code() == 200
        create_template_response = response.get_result()
        assert create_template_response is not None

        self.__class__.testTemplateEtag = response.get_headers().get(self.etagHeader)

    @needscredentials
    def test_update_template_version(self):
        # Construct a dict representation of a MembersActionControls model
        members_action_controls_model = {
            'add': True,
            'remove': False,
        }
        # Construct a dict representation of a MembersInput model
        members_input_model = {
            'users': ['IBMid-665000T8WY'],
            'action_controls': members_action_controls_model,
        }
        # Construct a dict representation of a ConditionInput model
        condition_input_model = {
            'claim': 'blueGroup',
            'operator': 'CONTAINS',
            'value': '\"test-bluegroup-saml\"',
        }
        # Construct a dict representation of a RulesActionControls model
        rules_action_controls_model = {
            'remove': False,
        }
        # Construct a dict representation of a RuleInput model
        rule_input_model = {
            'name': 'Manager group rule',
            'expiration': 12,
            'realm_name': 'https://idp.example.org/SAML2',
            'conditions': [condition_input_model],
            'action_controls': rules_action_controls_model,
        }
        # Construct a dict representation of a AssertionsActionControls model
        assertions_action_controls_model = {
            'add': False,
            'remove': True,
        }
        # Construct a dict representation of a AssertionsInput model
        assertions_input_model = {
            'rules': [rule_input_model],
            'action_controls': assertions_action_controls_model,
        }
        # Construct a dict representation of a AccessActionControls model
        access_action_controls_model = {
            'add': False,
        }
        # Construct a dict representation of a GroupActionControls model
        group_action_controls_model = {
            'access': access_action_controls_model,
        }
        # Construct a dict representation of a AccessGroupInput model
        access_group_input_model = {
            'name': 'IAM Admin Group 8',
            'description': 'This access group template allows admin access to all IAM platform services in the account.',
            'members': members_input_model,
            'assertions': assertions_input_model,
            'action_controls': group_action_controls_model,
        }
        # Construct a dict representation of a PolicyTemplatesInput model
        policy_templates_input_model = {
            'id': self.testPolicyTemplateId,
            'version': '1',
        }

        response = self.iam_access_groups_service.update_template_version(
            template_id=self.testTemplateId,
            version_num='1',
            if_match=self.testTemplateEtag,
            name='IAM Admin Group template 2',
            description='This access group template allows admin access to all IAM platform services in the account.',
            group=access_group_input_model,
            policy_template_references=[policy_templates_input_model],
            transaction_id='83adf5bd-de790caa3',
        )

        assert response.get_status_code() == 201
        create_template_response = response.get_result()
        assert create_template_response is not None

    @needscredentials
    def test_get_latest_template_version(self):
        response = self.iam_access_groups_service.get_latest_template_version(
            template_id=self.testTemplateId,
            transaction_id='testString',
        )

        assert response.get_status_code() == 200
        create_template_response = response.get_result()
        assert create_template_response is not None

        self.__class__.testTemplateLatestEtag = response.get_headers().get(self.etagHeader)

    @needscredentials
    def test_commit_template(self):
        response = self.iam_access_groups_service.commit_template(
            template_id=self.testTemplateId,
            version_num='2',
            if_match=self.testTemplateLatestEtag,
            transaction_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_create_assignment(self):
        response = self.iam_access_groups_service.create_assignment(
            template_id=self.testTemplateId,
            template_version='2',
            target_type='AccountGroup',
            target=self.testAccountGroupId,
            transaction_id='testString',
        )

        assert response.get_status_code() == 202
        template_create_assignment_response = response.get_result()
        assert template_create_assignment_response is not None

        self.__class__.testAssignmentId = template_create_assignment_response['id']
        time.sleep(60)

    @needscredentials
    def test_list_assignments(self):
        response = self.iam_access_groups_service.list_assignments(
            account_id=self.testTemplateId,
        )

        assert response.get_status_code() == 200
        templates_list_assignment_response = response.get_result()
        assert templates_list_assignment_response is not None

    @needscredentials
    def test_get_assignment(self):
        response = self.iam_access_groups_service.get_assignment(
            assignment_id=self.testAssignmentId,
            transaction_id='testString',
        )

        assert response.get_status_code() == 200
        get_assignment_response = response.get_result()
        assert get_assignment_response is not None

        self.__class__.testAssignmentEtag = response.get_headers().get(self.etagHeader)

    @needscredentials
    def test_update_assignment(self):
        response = self.iam_access_groups_service.update_assignment(
            assignment_id=self.testAssignmentId,
            if_match=self.testAssignmentEtag,
            template_version="2",
        )

        assert response.get_status_code() == 202
        update_template_assignment_response = response.get_result()
        assert update_template_assignment_response is not None

        time.sleep(60)

    @needscredentials
    def test_delete_assignment(self):
        response = self.iam_access_groups_service.delete_assignment(
            assignment_id=self.testAssignmentId,
            transaction_id='testString',
        )

        assert response.get_status_code() == 202

        time.sleep(90)

    @needscredentials
    def test_delete_template_version(self):
        response = self.iam_access_groups_service.delete_template_version(
            template_id=self.testTemplateId,
            version_num='2',
            transaction_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_template(self):
        response = self.iam_access_groups_service.delete_template(
            template_id=self.testTemplateId,
            transaction_id='testString',
        )

        assert response.get_status_code() == 204
