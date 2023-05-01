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
import pytest
from ibm_platform_services.iam_access_groups_v2 import *

#
# This file provides an example of how to use the iam-access-groups service.
#
# The following configuration properties are assumed to be defined:
# IAM_ACCESS_GROUPS_URL=<service base url>
# IAM_ACCESS_GROUPS_AUTH_TYPE=iam
# IAM_ACCESS_GROUPS_APIKEY=<IAM apikey>
# IAM_ACCESS_GROUPS_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'iam_access_groups_v2.env'

iam_access_groups_service = None

config = None

# Variables to hold link values
access_group_e_tag_link = None
access_group_id_link = None


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
            global config
            config = read_external_sources(IamAccessGroupsV2.DEFAULT_SERVICE_NAME)

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
            global access_group_id_link
            print('\ncreate_access_group() result:')
            # begin-create_access_group

            response = iam_access_groups_service.create_access_group(
                account_id='testString',
                name='Managers',
                description='Group for managers',
            )
            group = response.get_result()

            print(json.dumps(group, indent=2))

            # end-create_access_group

            access_group_id_link = group['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_access_group_example(self):
        """
        get_access_group request example
        """
        try:
            global access_group_e_tag_link
            print('\nget_access_group() result:')
            # begin-get_access_group

            response = iam_access_groups_service.get_access_group(
                access_group_id=access_group_id_link,
            )
            group = response.get_result()

            print(json.dumps(group, indent=2))

            # end-get_access_group

            access_group_e_tag_link = response.get_headers().get('ETag')
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
                account_id='testString',
                transaction_id='testString',
                iam_id='testString',
                search='testString',
                membership_type='static',
                limit=10,
                sort='name',
                show_federated=False,
                hide_public_access=False,
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
    def test_update_access_group_example(self):
        """
        update_access_group request example
        """
        try:
            print('\nupdate_access_group() result:')
            # begin-update_access_group

            response = iam_access_groups_service.update_access_group(
                access_group_id=access_group_id_link,
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
    def test_is_member_of_access_group_example(self):
        """
        is_member_of_access_group request example
        """
        try:
            # begin-is_member_of_access_group

            response = iam_access_groups_service.is_member_of_access_group(
                access_group_id=access_group_id_link,
                iam_id='testString',
            )

            # end-is_member_of_access_group
            print('\nis_member_of_access_group() response status code: ', response.get_status_code())

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

            add_group_members_request_members_item_model = {
                'iam_id': 'IBMid-user1',
                'type': 'user',
            }

            response = iam_access_groups_service.add_members_to_access_group(
                access_group_id=access_group_id_link,
                members=[add_group_members_request_members_item_model],
            )
            add_group_members_response = response.get_result()

            print(json.dumps(add_group_members_response, indent=2))

            # end-add_members_to_access_group

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
                access_group_id=access_group_id_link,
                transaction_id='testString',
                membership_type='static',
                limit=10,
                type='testString',
                verbose=False,
                sort='testString',
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
    def test_remove_members_from_access_group_example(self):
        """
        remove_members_from_access_group request example
        """
        try:
            print('\nremove_members_from_access_group() result:')
            # begin-remove_members_from_access_group

            response = iam_access_groups_service.remove_members_from_access_group(
                access_group_id=access_group_id_link,
                members=['IBMId-user1', 'iam-ServiceId-123', 'iam-Profile-123'],
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
                account_id='testString',
                iam_id='testString',
                type='user',
                groups=['access-group-id-1'],
            )
            add_membership_multiple_groups_response = response.get_result()

            print(json.dumps(add_membership_multiple_groups_response, indent=2))

            # end-add_member_to_multiple_access_groups

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
                access_group_id=access_group_id_link,
                expiration=12,
                realm_name='https://idp.example.org/SAML2',
                conditions=[rule_conditions_model],
                name='Manager group rule',
            )
            rule = response.get_result()

            print(json.dumps(rule, indent=2))

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
                access_group_id=access_group_id_link,
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
                access_group_id=access_group_id_link,
                rule_id='testString',
            )
            rule = response.get_result()

            print(json.dumps(rule, indent=2))

            # end-get_access_group_rule

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
                access_group_id=access_group_id_link,
                rule_id='testString',
                if_match='testString',
                expiration=12,
                realm_name='https://idp.example.org/SAML2',
                conditions=[rule_conditions_model],
                name='Manager group rule',
            )
            rule = response.get_result()

            print(json.dumps(rule, indent=2))

            # end-replace_access_group_rule

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
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
                'users': ['IBMid-123', 'IBMid-234'],
                'action_controls': members_action_controls_model,
            }

            condition_input_model = {
                'claim': 'blueGroup',
                'operator': 'CONTAINS',
                'value': 'test-bluegroup-saml',
            }

            rules_action_controls_model = {
                'remove': False,
                'update': False,
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
                'update': True,
            }

            assertions_input_model = {
                'rules': [rule_input_model],
                'action_controls': assertions_action_controls_model,
            }

            access_action_controls_model = {
                'add': False,
            }

            access_group_action_controls_model = {
                'access': access_action_controls_model,
            }

            access_group_input_model = {
                'name': 'IAM Admin Group',
                'description': 'This access group template allows admin access to all IAM platform services in the account.',
                'members': members_input_model,
                'assertions': assertions_input_model,
                'action_controls': access_group_action_controls_model,
            }

            policy_templates_input_model = {
                'id': 'policyTemplateId-123',
                'version': '1',
            }

            response = iam_access_groups_service.create_template(
                name='IAM Admin Group template',
                description='This access group template allows admin access to all IAM platform services in the account.',
                account_id='accountID-123',
                access_group=access_group_input_model,
                policy_template_references=[policy_templates_input_model],
            )
            create_template_response = response.get_result()

            print(json.dumps(create_template_response, indent=2))

            # end-create_template

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_template_example(self):
        """
        list_template request example
        """
        try:
            print('\nlist_template() result:')
            # begin-list_template

            all_results = []
            pager = TemplatePager(
                client=iam_access_groups_service,
                account_id='accountID-123',
                transaction_id='testString',
                limit=50,
                verbose=True,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_template
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

            members_input_model = {
                'users': ['IBMid-123', 'IBMid-234'],
            }

            condition_input_model = {
                'claim': 'blueGroup',
                'operator': 'CONTAINS',
                'value': 'test-bluegroup-saml',
            }

            rule_input_model = {
                'name': 'Manager group rule',
                'expiration': 12,
                'realm_name': 'https://idp.example.org/SAML2',
                'conditions': [condition_input_model],
            }

            assertions_input_model = {
                'rules': [rule_input_model],
            }

            access_group_input_model = {
                'name': 'IAM Admin Group 8',
                'description': 'This access group template allows admin access to all IAM platform services in the account.',
                'members': members_input_model,
                'assertions': assertions_input_model,
            }

            policy_templates_input_model = {
                'id': 'policyTemplateId-123',
                'version': '1',
            }

            response = iam_access_groups_service.create_template_version(
                template_id='testString',
                name='IAM Admin Group template 2',
                description='This access group template allows admin access to all IAM platform services in the account.',
                access_group=access_group_input_model,
                policy_template_references=[policy_templates_input_model],
            )
            create_template_response = response.get_result()

            print(json.dumps(create_template_response, indent=2))

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
                template_id='testString',
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
    def test_get_template_specific_version_example(self):
        """
        get_template_specific_version request example
        """
        try:
            print('\nget_template_specific_version() result:')
            # begin-get_template_specific_version

            response = iam_access_groups_service.get_template_specific_version(
                template_id='testString',
                version_num='testString',
            )
            create_template_response = response.get_result()

            print(json.dumps(create_template_response, indent=2))

            # end-get_template_specific_version

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_template_version_example(self):
        """
        replace_template_version request example
        """
        try:
            print('\nreplace_template_version() result:')
            # begin-replace_template_version

            members_input_model = {
                'users': ['IBMid-5500085Q21'],
            }

            condition_input_model = {
                'claim': 'blueGroup',
                'operator': 'CONTAINS',
                'value': 'test-bluegroup-saml',
            }

            rule_input_model = {
                'name': 'Manager group rule',
                'expiration': 12,
                'realm_name': 'https://idp.example.org/SAML2',
                'conditions': [condition_input_model],
            }

            assertions_input_model = {
                'rules': [rule_input_model],
            }

            access_group_input_model = {
                'name': 'IAM Admin Group 8',
                'description': 'This access group template allows admin access to all IAM platform services in the account.',
                'members': members_input_model,
                'assertions': assertions_input_model,
            }

            policy_templates_input_model = {
                'id': 'policyTemplateId-123',
                'version': '1',
            }

            response = iam_access_groups_service.replace_template_version(
                template_id='testString',
                version_num='testString',
                if_match='testString',
                name='IAM Admin Group template 2',
                description='This access group template allows admin access to all IAM platform services in the account.',
                access_group=access_group_input_model,
                policy_template_references=[policy_templates_input_model],
                transaction_id='83adf5bd-de790caa3',
            )
            create_template_response = response.get_result()

            print(json.dumps(create_template_response, indent=2))

            # end-replace_template_version

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
                template_id='testString',
                version_num='testString',
                if_match='testString',
            )
            create_template_response = response.get_result()

            print(json.dumps(create_template_response, indent=2))

            # end-commit_template

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_template_latest_version_example(self):
        """
        get_template_latest_version request example
        """
        try:
            print('\nget_template_latest_version() result:')
            # begin-get_template_latest_version

            response = iam_access_groups_service.get_template_latest_version(
                template_id='testString',
            )
            create_template_response = response.get_result()

            print(json.dumps(create_template_response, indent=2))

            # end-get_template_latest_version

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_assign_template_example(self):
        """
        create_assign_template request example
        """
        try:
            print('\ncreate_assign_template() result:')
            # begin-create_assign_template

            response = iam_access_groups_service.create_assign_template(
                template_id='AccessGroupTemplateId-4be4',
                template_version='1',
                target_type='accountGroup',
                target='0a45594d0f-123',
            )
            template_create_assignment_response = response.get_result()

            print(json.dumps(template_create_assignment_response, indent=2))

            # end-create_assign_template

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_assignment_example(self):
        """
        list_assignment request example
        """
        try:
            print('\nlist_assignment() result:')
            # begin-list_assignment

            response = iam_access_groups_service.list_assignment(
                account_id='accountID-123',
            )
            templates_list_assignment_response = response.get_result()

            print(json.dumps(templates_list_assignment_response, indent=2))

            # end-list_assignment

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
                assignment_id='testString',
            )
            get_template_assignment_response = response.get_result()

            print(json.dumps(get_template_assignment_response, indent=2))

            # end-get_assignment

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
                account_id='testString',
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
                account_id='testString',
                public_access_enabled=True,
            )
            account_settings = response.get_result()

            print(json.dumps(account_settings, indent=2))

            # end-update_account_settings

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
                access_group_id=access_group_id_link,
            )

            # end-delete_access_group
            print('\ndelete_access_group() response status code: ', response.get_status_code())

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
                access_group_id=access_group_id_link,
                iam_id='testString',
            )

            # end-remove_member_from_access_group
            print('\nremove_member_from_access_group() response status code: ', response.get_status_code())

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
                access_group_id=access_group_id_link,
                rule_id='testString',
            )

            # end-remove_access_group_rule
            print('\nremove_access_group_rule() response status code: ', response.get_status_code())

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
                account_id='testString',
                iam_id='testString',
            )
            delete_from_all_groups_response = response.get_result()

            print(json.dumps(delete_from_all_groups_response, indent=2))

            # end-remove_member_from_all_access_groups

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
                template_id='testString',
                version_num='testString',
            )

            # end-delete_template_version
            print('\ndelete_template_version() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_template_example(self):
        """
        delete_template request example
        """
        try:
            # begin-delete_template

            response = iam_access_groups_service.delete_template(
                template_id='testString',
            )

            # end-delete_template
            print('\ndelete_template() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_assignment_example(self):
        """
        delete_assignment request example
        """
        try:
            # begin-delete_assignment

            response = iam_access_groups_service.delete_assignment(
                assignment_id='testString',
            )

            # end-delete_assignment
            print('\ndelete_assignment() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: IamAccessGroupsV2
##############################################################################
