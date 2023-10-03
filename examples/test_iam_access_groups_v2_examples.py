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
Examples for IamAccessGroupsV2
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import os
import time
import pytest
from ibm_platform_services.iam_access_groups_v2 import *

#
# This file provides an example of how to use the iam-access-groups service.
#
# The following configuration properties are assumed to be defined:
#
# IAM_ACCESS_GROUPS_URL=<service url>
# IAM_ACCESS_GROUPS_AUTHTYPE=iam
# IAM_ACCESS_GROUPS_APIKEY=<your iam apikey>
# IAM_ACCESS_GROUPS_AUTH_URL=<IAM token service URL - omit this if using the production environment>
# IAM_ACCESS_GROUPS_TEST_ACCOUNT_ID=<id of an account used for testing>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'iam_access_groups_v2.env'

iam_access_groups_service = None

config = None

test_account_id = None
test_profile_id = None
test_group_etag = None
test_group_id = None
test_claim_rule_id = None
test_claim_rule_etag = None
test_policy_template_id = None
test_template_id = None
test_template_etag = None
test_template_latest_etag = None
test_account_group_id = None
test_assignment_id = None
test_assignment_etag = None
access_group_e_tag_link = None


##############################################################################
# Start of Examples for Service: IamAccessGroupsV2
##############################################################################
# region
class TestIamAccessGroupsV2Examples:
    """
    Example Test Class for IamAccessGroupsV2
    """

    @classmethod
    def setup_class(cls):
        global iam_access_groups_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            iam_access_groups_service = IamAccessGroupsV2.new_instance()

            # end-common
            assert iam_access_groups_service is not None

            # Load the configuration
            global config, test_account_id, test_profile_id, test_policy_template_id, test_account_group_id
            config = read_external_sources(IamAccessGroupsV2.DEFAULT_SERVICE_NAME)
            test_account_id = config['TEST_ACCOUNT_ID']
            test_profile_id = config['TEST_PROFILE_ID']
            test_policy_template_id = config['TEST_POLICY_TEMPLATE_ID']
            test_account_group_id = config['TEST_ACCOUNT_GROUP_ID']

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_access_group_example(self):
        """
        create_access_group request example
        """
        try:
            print('\ncreate_access_group() result:')
            # begin-create_access_group

            response = iam_access_groups_service.create_access_group(
                account_id=test_account_id,
                name='Managers',
                description='Group for managers',
            )
            group = response.get_result()

            print(json.dumps(group, indent=2))

            # end-create_access_group

            global test_group_id
            test_group_id = group['id']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_access_group_example(self):
        """
        get_access_group request example
        """
        try:
            print('\nget_access_group() result:')
            # begin-get_access_group

            response = iam_access_groups_service.get_access_group(
                access_group_id=test_group_id,
            )
            group = response.get_result()

            print(json.dumps(group, indent=2))

            # end-get_access_group

            global access_group_e_tag_link
            access_group_e_tag_link = response.get_headers().get('ETag')
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_access_group_example(self):
        """
        update_access_group request example
        """
        try:
            print('\nupdate_access_group() result:')
            # begin-update_access_group

            response = iam_access_groups_service.update_access_group(
                access_group_id=test_group_id,
                if_match=access_group_e_tag_link,
                name='Awesome Managers',
                description='Group for awesome managers.',
            )
            group = response.get_result()

            print(json.dumps(group, indent=2))

            # end-update_access_group

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_access_groups_example(self):
        """
        list_access_groups request example
        """
        try:
            print('\nlist_access_groups() result:')
            # begin-list_access_groups

            all_results = []
            pager = AccessGroupsPager(
                client=iam_access_groups_service,
                account_id=test_account_id,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_access_groups
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_add_members_to_access_group_example(self):
        """
        add_members_to_access_group request example
        """
        try:
            print('\nadd_members_to_access_group() result:')
            # begin-add_members_to_access_group

            member1 = AddGroupMembersRequestMembersItem(iam_id='IBMid-user1', type='user')
            member2 = AddGroupMembersRequestMembersItem(iam_id='iam-ServiceId-123', type='service')
            member3 = AddGroupMembersRequestMembersItem(iam_id=test_profile_id, type='profile')
            members = [member1, member2, member3]

            response = iam_access_groups_service.add_members_to_access_group(
                access_group_id=test_group_id,
                members=members,
            )
            add_group_members_response = response.get_result()

            print(json.dumps(add_group_members_response, indent=2))

            # end-add_members_to_access_group

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_is_member_of_access_group_example(self):
        """
        is_member_of_access_group request example
        """
        try:
            # begin-is_member_of_access_group

            response = iam_access_groups_service.is_member_of_access_group(
                access_group_id=test_group_id, iam_id='IBMid-user1'
            )

            # end-is_member_of_access_group
            print('\nis_member_of_access_group() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_access_group_members_example(self):
        """
        list_access_group_members request example
        """
        try:
            print('\nlist_access_group_members() result:')
            # begin-list_access_group_members

            all_results = []
            pager = AccessGroupMembersPager(
                client=iam_access_groups_service,
                access_group_id=test_group_id,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_access_group_members
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_remove_member_from_access_group_example(self):
        """
        remove_member_from_access_group request example
        """
        try:
            # begin-remove_member_from_access_group

            response = iam_access_groups_service.remove_member_from_access_group(
                access_group_id=test_group_id,
                iam_id='IBMid-user1',
            )

            # end-remove_member_from_access_group
            print('\nremove_member_from_access_group() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_remove_members_from_access_group_example(self):
        """
        remove_members_from_access_group request example
        """
        try:
            print('\nremove_members_from_access_group() result:')
            # begin-remove_members_from_access_group

            response = iam_access_groups_service.remove_members_from_access_group(
                access_group_id=test_group_id,
                members=['IBMId-user1', 'iam-ServiceId-123', test_profile_id],
            )
            delete_group_bulk_members_response = response.get_result()

            print(json.dumps(delete_group_bulk_members_response, indent=2))

            # end-remove_members_from_access_group

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_add_member_to_multiple_access_groups_example(self):
        """
        add_member_to_multiple_access_groups request example
        """
        try:
            print('\nadd_member_to_multiple_access_groups() result:')
            # begin-add_member_to_multiple_access_groups

            response = iam_access_groups_service.add_member_to_multiple_access_groups(
                account_id=test_account_id,
                iam_id='IBMid-user1',
                type='user',
                groups=[test_group_id],
            )
            add_membership_multiple_groups_response = response.get_result()

            print(json.dumps(add_membership_multiple_groups_response, indent=2))

            # end-add_member_to_multiple_access_groups

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_remove_member_from_all_access_groups_example(self):
        """
        remove_member_from_all_access_groups request example
        """
        try:
            print('\nremove_member_from_all_access_groups() result:')
            # begin-remove_member_from_all_access_groups

            response = iam_access_groups_service.remove_member_from_all_access_groups(
                account_id=test_account_id, iam_id='IBMid-user1'
            )
            delete_from_all_groups_response = response.get_result()

            print(json.dumps(delete_from_all_groups_response, indent=2))

            # end-remove_member_from_all_access_groups

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_add_access_group_rule_example(self):
        """
        add_access_group_rule request example
        """
        try:
            print('\nadd_access_group_rule() result:')
            # begin-add_access_group_rule

            rule_conditions_model = {
                'claim': 'isManager',
                'operator': 'EQUALS',
                'value': 'true',
            }

            response = iam_access_groups_service.add_access_group_rule(
                access_group_id=test_group_id,
                expiration=12,
                realm_name='https://idp.example.org/SAML3',
                conditions=[rule_conditions_model],
                name='Manager group rule',
            )
            rule = response.get_result()

            # end-add_access_group_rule
            global test_claim_rule_id
            test_claim_rule_id = rule['id']
            # end-add_access_group_rule

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_access_group_rules_example(self):
        """
        list_access_group_rules request example
        """
        try:
            print('\nlist_access_group_rules() result:')
            # begin-list_access_group_rules

            response = iam_access_groups_service.list_access_group_rules(
                access_group_id=test_group_id,
            )
            rules_list = response.get_result()

            print(json.dumps(rules_list, indent=2))

            # end-list_access_group_rules

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_access_group_rule_example(self):
        """
        get_access_group_rule request example
        """
        try:
            print('\nget_access_group_rule() result:')
            # begin-get_access_group_rule

            response = iam_access_groups_service.get_access_group_rule(
                access_group_id=test_group_id,
                rule_id=test_claim_rule_id,
            )
            rule = response.get_result()

            print(json.dumps(rule, indent=2))

            # end-get_access_group_rule
            global test_claim_rule_etag
            test_claim_rule_etag = response.get_headers().get('Etag')

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_access_group_rule_example(self):
        """
        replace_access_group_rule request example
        """
        try:
            print('\nreplace_access_group_rule() result:')
            # begin-replace_access_group_rule

            rule_conditions_model = {
                'claim': 'isManager',
                'operator': 'EQUALS',
                'value': 'true',
            }

            response = iam_access_groups_service.replace_access_group_rule(
                access_group_id=test_group_id,
                rule_id=test_claim_rule_id,
                if_match=test_claim_rule_etag,
                expiration=12,
                realm_name='https://idp.example.org/SAML3',
                conditions=[rule_conditions_model],
                name='Manager group rule',
            )
            rule = response.get_result()

            print(json.dumps(rule, indent=2))

            # end-replace_access_group_rule

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_remove_access_group_rule_example(self):
        """
        remove_access_group_rule request example
        """
        try:
            # begin-remove_access_group_rule

            response = iam_access_groups_service.remove_access_group_rule(
                access_group_id=test_group_id,
                rule_id=test_claim_rule_id,
            )

            # end-remove_access_group_rule
            print('\nremove_access_group_rule() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_account_settings_example(self):
        """
        get_account_settings request example
        """
        try:
            print('\nget_account_settings() result:')
            # begin-get_account_settings

            response = iam_access_groups_service.get_account_settings(
                account_id=test_account_id,
            )
            account_settings = response.get_result()

            print(json.dumps(account_settings, indent=2))

            # end-get_account_settings

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_account_settings_example(self):
        """
        update_account_settings request example
        """
        try:
            print('\nupdate_account_settings() result:')
            # begin-update_account_settings

            response = iam_access_groups_service.update_account_settings(
                account_id=test_account_id,
                public_access_enabled=True,
            )
            account_settings = response.get_result()

            print(json.dumps(account_settings, indent=2))

            # end-update_account_settings

        except ApiException as e:
            pytest.fail(str(e))

    def test_create_template_example(self):
        """
        create_template request example
        """
        try:
            print('\ncreate_template() result:')
            # begin-create_template

            members_action_controls_model = {
                'add': True,
                'remove': False,
            }

            members_input_model = {
                'users': ['IBMid-50PJGPKYJJ', 'IBMid-665000T8WY'],
                'action_controls': members_action_controls_model,
            }

            condition_input_model = {
                'claim': 'blueGroup',
                'operator': 'CONTAINS',
                'value': '\"test-bluegroup-saml\"',
            }

            rules_action_controls_model = {
                'remove': False,
            }

            rule_input_model = {
                'name': 'Manager group rule',
                'expiration': 12,
                'realm_name': 'https://idp.example.org/SAML2',
                'conditions': [condition_input_model],
                'action_controls': rules_action_controls_model,
            }

            assertions_action_controls_model = {
                'add': False,
                'remove': True,
            }

            assertions_input_model = {
                'rules': [rule_input_model],
                'action_controls': assertions_action_controls_model,
            }

            access_action_controls_model = {
                'add': False,
            }

            group_action_controls_model = {
                'access': access_action_controls_model,
            }

            access_group_input_model = {
                'name': 'IAM Admin Group',
                'description': 'This access group template allows admin access to all IAM platform services in the account.',
                'members': members_input_model,
                'assertions': assertions_input_model,
                'action_controls': group_action_controls_model,
            }

            policy_templates_input_model = {
                'id': test_policy_template_id,
                'version': '1',
            }

            response = iam_access_groups_service.create_template(
                name='IAM Admin Group template',
                account_id=test_account_id,
                description='This access group template allows admin access to all IAM platform services in the account.',
                group=access_group_input_model,
                policy_template_references=[policy_templates_input_model],
            )
            create_template_response = response.get_result()

            print(json.dumps(create_template_response, indent=2))
            # end-create_template

            global test_template_id
            test_template_id = create_template_response['id']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_templates_example(self):
        """
        list_templates request example
        """
        try:
            print('\nlist_templates() result:')
            # begin-list_templates

            all_results = []
            pager = TemplatesPager(
                client=iam_access_groups_service,
                account_id=test_account_id,
                transaction_id='testString',
                limit=50,
                verbose=True,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_templates
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_template_version_example(self):
        """
        create_template_version request example
        """
        try:
            print('\ncreate_template_version() result:')
            # begin-create_template_version

            members_action_controls_model = {
                'add': True,
                'remove': False,
            }

            members_input_model = {
                'users': ['IBMid-50PJGPKYJJ', 'IBMid-665000T8WY'],
                'action_controls': members_action_controls_model,
            }

            condition_input_model = {
                'claim': 'blueGroup',
                'operator': 'CONTAINS',
                'value': '\"test-bluegroup-saml\"',
            }

            rule_input_model = {
                'name': 'Manager group rule',
                'expiration': 12,
                'realm_name': 'https://idp.example.org/SAML2',
                'conditions': [condition_input_model],
            }

            assertions_action_controls_model = {
                'add': False,
            }

            assertions_input_model = {
                'rules': [rule_input_model],
                'action_controls': assertions_action_controls_model,
            }

            access_action_controls_model = {
                'add': False,
            }

            group_action_controls_model = {
                'access': access_action_controls_model,
            }

            access_group_input_model = {
                'name': 'IAM Admin Group 8',
                'description': 'This access group template allows admin access to all IAM platform services in the account.',
                'members': members_input_model,
                'assertions': assertions_input_model,
                'action_controls': group_action_controls_model,
            }

            policy_templates_input_model = {
                'id': test_policy_template_id,
                'version': '1',
            }

            response = iam_access_groups_service.create_template_version(
                template_id=test_template_id,
                name='IAM Admin Group template 2',
                description='This access group template allows admin access to all IAM platform services in the account.',
                group=access_group_input_model,
                policy_template_references=[policy_templates_input_model],
            )
            create_template_version_response = response.get_result()

            print(json.dumps(create_template_version_response, indent=2))

            # end-create_template_version

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_template_versions_example(self):
        """
        list_template_versions request example
        """
        try:
            print('\nlist_template_versions() result:')
            # begin-list_template_versions

            all_results = []
            pager = TemplateVersionsPager(
                client=iam_access_groups_service,
                template_id=test_template_id,
                limit=100,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_template_versions
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_template_version_example(self):
        """
        get_template_version request example
        """
        try:
            print('\nget_template_version() result:')
            # begin-get_template_version

            response = iam_access_groups_service.get_template_version(
                template_id=test_template_id,
                version_num='1',
            )
            get_template_version_response = response.get_result()

            print(json.dumps(get_template_version_response, indent=2))

            # end-get_template_version

            global test_template_etag
            test_template_etag = response.get_headers().get('ETag')

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_template_version_example(self):
        """
        update_template_version request example
        """
        try:
            print('\nupdate_template_version() result:')
            # begin-update_template_version

            members_action_controls_model = {
                'add': True,
                'remove': False,
            }

            members_input_model = {
                'users': ['IBMid-665000T8WY'],
                'action_controls': members_action_controls_model,
            }

            condition_input_model = {
                'claim': 'blueGroup',
                'operator': 'CONTAINS',
                'value': '\"test-bluegroup-saml\"',
            }

            rules_action_controls_model = {
                'remove': False,
            }

            rule_input_model = {
                'name': 'Manager group rule',
                'expiration': 12,
                'realm_name': 'https://idp.example.org/SAML2',
                'conditions': [condition_input_model],
                'action_controls': rules_action_controls_model,
            }

            assertions_action_controls_model = {
                'add': False,
            }

            assertions_input_model = {
                'rules': [rule_input_model],
                'action_controls': assertions_action_controls_model,
            }

            access_action_controls_model = {
                'add': False,
            }

            group_action_controls_model = {
                'access': access_action_controls_model,
            }

            access_group_input_model = {
                'name': 'IAM Admin Group 8',
                'description': 'This access group template allows admin access to all IAM platform services in the account.',
                'members': members_input_model,
                'assertions': assertions_input_model,
                'action_controls': group_action_controls_model,
            }

            policy_templates_input_model = {
                'id': test_policy_template_id,
                'version': '1',
            }

            response = iam_access_groups_service.update_template_version(
                template_id=test_template_id,
                version_num='1',
                if_match=test_template_etag,
                name='IAM Admin Group template 2',
                description='This access group template allows admin access to all IAM platform services in the account.',
                group=access_group_input_model,
                policy_template_references=[policy_templates_input_model],
                transaction_id='83adf5bd-de790caa3',
            )
            update_template_version_response = response.get_result()

            print(json.dumps(update_template_version_response, indent=2))

            # end-update_template_version

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_latest_template_version_example(self):
        """
        get_latest_template_version request example
        """
        try:
            print('\nget_latest_template_version() result:')
            # begin-get_latest_template_version

            response = iam_access_groups_service.get_latest_template_version(
                template_id=test_template_id,
            )
            get_latest_template_response = response.get_result()

            print(json.dumps(get_latest_template_response, indent=2))

            # end-get_latest_template_version

            global test_template_latest_etag
            test_template_latest_etag = response.get_headers().get('ETag')

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_commit_template_example(self):
        """
        commit_template request example
        """
        try:
            print('\ncommit_template() result:')
            # begin-commit_template

            response = iam_access_groups_service.commit_template(
                template_id=test_template_id,
                version_num='2',
                if_match=test_template_latest_etag,
            )
            commit_template_response = response.get_result()

            print(json.dumps(commit_template_response, indent=2))

            # end-commit_template

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_assignment_example(self):
        """
        create_assignment request example
        """
        try:
            print('\ncreate_assignment() result:')
            # begin-create_assignment

            response = iam_access_groups_service.create_assignment(
                template_id=test_template_id,
                template_version='2',
                target_type='AccountGroup',
                target=test_account_group_id,
            )
            create_assignment_response = response.get_result()

            print(json.dumps(create_assignment_response, indent=2))

            # end-create_assignment
            global test_assignment_id
            test_assignment_id = create_assignment_response['id']
            time.sleep(30)

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_assignments_example(self):
        """
        list_assignments request example
        """
        try:
            print('\nlist_assignments() result:')
            # begin-list_assignments

            response = iam_access_groups_service.list_assignments(
                account_id=test_account_id,
            )
            list_assignment_response = response.get_result()

            print(json.dumps(list_assignment_response, indent=2))

            # end-list_assignments
            time.sleep(30)
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_assignment_example(self):
        """
        get_assignment request example
        """
        try:
            print('\nget_assignment() result:')
            # begin-get_assignment

            response = iam_access_groups_service.get_assignment(
                assignment_id=test_assignment_id,
            )
            get_assignment_response = response.get_result()

            print(json.dumps(get_assignment_response, indent=2))

            # end-get_assignment

            global test_assignment_etag
            test_assignment_etag = response.get_headers().get('ETag')

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_assignment_example(self):
        """
        update_assignment request example
        """
        try:
            print('\nupdate_assignment() result:')
            # begin-update_assignment

            response = iam_access_groups_service.update_assignment(
                assignment_id=test_assignment_id,
                template_version="2",
                if_match=test_assignment_etag,
            )
            update_assignment_response = response.get_result()

            print(json.dumps(update_assignment_response, indent=2))

            # end-update_assignment
            time.sleep(60)
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_assignment_example(self):
        """
        delete_assignment request example
        """
        try:
            print('\ndelete_assignment() result:')
            # begin-delete_assignment

            response = iam_access_groups_service.delete_assignment(
                assignment_id=test_assignment_id,
            )
            delete_assignment_response = response.get_result()

            print(json.dumps(delete_assignment_response, indent=2))

            # end-delete_assignment
            time.sleep(90)
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_template_version_example(self):
        """
        delete_template_version request example
        """
        try:
            # begin-delete_template_version

            response = iam_access_groups_service.delete_template_version(
                template_id=test_template_id,
                version_num='2',
                transaction_id='testString',
            )

            # end-delete_template_version
            print('\ndelete_template_version() response status code: ', response.get_status_code())
            time.sleep(30)
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_template_example(self):
        """
        delete_access_group request example
        """
        try:
            # begin-delete_template

            response = iam_access_groups_service.delete_template(
                template_id=test_template_id,
                transaction_id='testString',
            )

            # end-delete_template
            print('\ndelete_template() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_access_group_example(self):
        """
        delete_access_group request example
        """
        try:
            # begin-delete_access_group

            response = iam_access_groups_service.delete_access_group(
                access_group_id=test_group_id,
            )

            # end-delete_access_group
            print('\ndelete_access_group() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: IamAccessGroupsV2
##############################################################################
