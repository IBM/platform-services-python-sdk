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
Examples for IamAccessGroupsV2
"""

import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.iam_access_groups_v2 import *

#
# This file provides an example of how to use the IAM Access Groups service.
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
config_file = 'iam_access_groups.env'

iam_access_groups_service = None

config = None

test_account_id = None
test_group_etag = None
test_group_id = None
test_claim_rule_id = None
test_claim_rule_etag = None

##############################################################################
# Start of Examples for Service: IamAccessGroupsV2
##############################################################################
# region


class TestIamAccessGroupsV2Examples():
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
            global config, test_account_id
            config = read_external_sources(
                IamAccessGroupsV2.DEFAULT_SERVICE_NAME)
            test_account_id = config['TEST_ACCOUNT_ID']

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
            # begin-create_access_group

            group = iam_access_groups_service.create_access_group(
                account_id=test_account_id,
                name='Managers',
                description='Group for managers'
            ).get_result()

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
            # begin-get_access_group

            response = iam_access_groups_service.get_access_group(
                access_group_id=test_group_id
            )
            group = response.get_result()

            print(json.dumps(group, indent=2))

            # end-get_access_group
            global test_group_etag
            test_group_etag = response.get_headers().get('Etag')

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_access_group_example(self):
        """
        update_access_group request example
        """
        try:
            # begin-update_access_group

            group = iam_access_groups_service.update_access_group(
                access_group_id=test_group_id,
                if_match=test_group_etag,
                name='Awesome Managers',
                description='Group for awesome managers'
            ).get_result()

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
            # begin-list_access_groups

            groups_list = iam_access_groups_service.list_access_groups(
                account_id=test_account_id
            ).get_result()

            print(json.dumps(groups_list, indent=2))

            # end-list_access_groups

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_add_members_to_access_group_example(self):
        """
        add_members_to_access_group request example
        """
        try:
            # begin-add_members_to_access_group
            member1 = AddGroupMembersRequestMembersItem(
                iam_id='IBMid-user1', type='user')
            member2 = AddGroupMembersRequestMembersItem(
                iam_id='iam-ServiceId-123', type='service')
            members = [member1, member2]

            add_group_members_response = iam_access_groups_service.add_members_to_access_group(
                access_group_id=test_group_id,
                members=members
            ).get_result()

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
                access_group_id=test_group_id,
                iam_id='IBMid-user1'
            )

            print(response)

            # end-is_member_of_access_group

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_access_group_members_example(self):
        """
        list_access_group_members request example
        """
        try:
            # begin-list_access_group_members

            group_members_list = iam_access_groups_service.list_access_group_members(
                access_group_id=test_group_id
            ).get_result()

            print(json.dumps(group_members_list, indent=2))

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
                iam_id='IBMid-user1'
            )

            print(response)

            # end-remove_member_from_access_group

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_remove_members_from_access_group_example(self):
        """
        remove_members_from_access_group request example
        """
        try:
            # begin-remove_members_from_access_group

            delete_group_bulk_members_response = iam_access_groups_service.remove_members_from_access_group(
                access_group_id=test_group_id,
                members=['iam-ServiceId-123']
            ).get_result()

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
            # begin-add_member_to_multiple_access_groups

            add_membership_multiple_groups_response = iam_access_groups_service.add_member_to_multiple_access_groups(
                account_id=test_account_id,
                iam_id='IBMid-user1',
                type='user',
                groups=[test_group_id]
            ).get_result()

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
            # begin-remove_member_from_all_access_groups

            delete_from_all_groups_response = iam_access_groups_service.remove_member_from_all_access_groups(
                account_id=test_account_id,
                iam_id='IBMid-user1'
            ).get_result()

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
            # begin-add_access_group_rule

            rule_conditions_model = {
                'claim': 'isManager',
                'operator': 'EQUALS',
                'value': 'true'
            }

            rule = iam_access_groups_service.add_access_group_rule(
                access_group_id=test_group_id,
                name='Manager group rule',
                expiration=12,
                realm_name='https://idp.example.org/SAML2"',
                conditions=[rule_conditions_model]
            ).get_result()

            print(json.dumps(rule, indent=2))

            # end-add_access_group_rule
            global test_claim_rule_id
            test_claim_rule_id = rule['id']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_access_group_rule_example(self):
        """
        get_access_group_rule request example
        """
        try:
            # begin-get_access_group_rule

            response = iam_access_groups_service.get_access_group_rule(
                access_group_id=test_group_id,
                rule_id=test_claim_rule_id
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
            # begin-replace_access_group_rule

            rule_conditions_model = {
                'claim': 'isManager',
                'operator': 'EQUALS',
                'value': 'true'
            }

            rule = iam_access_groups_service.replace_access_group_rule(
                access_group_id=test_group_id,
                rule_id=test_claim_rule_id,
                if_match=test_claim_rule_etag,
                name='Manager group rule',
                expiration=24,
                realm_name='https://idp.example.org/SAML2',
                conditions=[rule_conditions_model]
            ).get_result()

            print(json.dumps(rule, indent=2))

            # end-replace_access_group_rule

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_access_group_rules_example(self):
        """
        list_access_group_rules request example
        """
        try:
            # begin-list_access_group_rules

            rules_list = iam_access_groups_service.list_access_group_rules(
                access_group_id=test_group_id
            ).get_result()

            print(json.dumps(rules_list, indent=2))

            # end-list_access_group_rules

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
                rule_id=test_claim_rule_id
            )

            print(response)

            # end-remove_access_group_rule

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_account_settings_example(self):
        """
        get_account_settings request example
        """
        try:
            # begin-get_account_settings

            account_settings = iam_access_groups_service.get_account_settings(
                account_id=test_account_id
            ).get_result()

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
            # begin-update_account_settings

            account_settings = iam_access_groups_service.update_account_settings(
                account_id=test_account_id,
                public_access_enabled=True
            ).get_result()

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
                access_group_id=test_group_id
            )

            print(response)

            # end-delete_access_group

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: IamAccessGroupsV2
##############################################################################
