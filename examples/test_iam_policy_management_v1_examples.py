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
Examples for IamPolicyManagementV1
"""

import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.iam_policy_management_v1 import *

#
# This file provides an example of how to use the IAM Policy Management service.
#
# The following configuration properties are assumed to be defined:
#
# IAM_POLICY_MANAGEMENT_URL=<service url>
# IAM_POLICY_MANAGEMENT_AUTH_TYPE=iam
# IAM_POLICY_MANAGEMENT_AUTH_URL=<IAM token service URL - omit this if using the production environment>
# IAM_POLICY_MANAGEMENT_APIKEY=<YOUR_APIKEY>
# IAM_POLICY_MANAGEMENT_TEST_ACCOUNT_ID=<YOUR_ACCOUNT_ID>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of config file>
#
# Config file name
config_file = 'iam_policy_management.env'

iam_policy_management_service = None

config = None

example_account_id = None
example_policy_id = None
example_policy_etag = None
example_custom_role_id = None
example_custom_role_etag = None
example_user_id = "IBMid-user1"
example_service_name = "iam-groups"

##############################################################################
# Start of Examples for Service: IamPolicyManagementV1
##############################################################################
# region


class TestIamPolicyManagementV1Examples():
    """
    Example Test Class for IamPolicyManagementV1
    """

    @classmethod
    def setup_class(cls):
        global iam_policy_management_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            iam_policy_management_service = IamPolicyManagementV1.new_instance(
            )

            # end-common
            assert iam_policy_management_service is not None

            # Load the configuration
            global config, example_account_id
            config = read_external_sources(
                IamPolicyManagementV1.DEFAULT_SERVICE_NAME)
            example_account_id = config['TEST_ACCOUNT_ID']

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_policy_example(self):
        """
        create_policy request example
        """
        try:
            global example_policy_id
            # begin-create_policy

            policy_subjects = PolicySubject(
                attributes=[SubjectAttribute(name='iam_id', value=example_user_id)])
            policy_roles = PolicyRole(
                role_id='crn:v1:bluemix:public:iam::::role:Viewer')
            account_id_resource_attribute = ResourceAttribute(
                name='accountId', value=example_account_id)
            service_name_resource_attribute = ResourceAttribute(
                name='serviceType', value='service')
            policy_resource_tag = ResourceTag(
                name='project', value='prototype')
            policy_resources = PolicyResource(
                attributes=[account_id_resource_attribute,
                            service_name_resource_attribute],
                tags=[policy_resource_tag])

            policy = iam_policy_management_service.create_policy(
                type='access',
                subjects=[policy_subjects],
                roles=[policy_roles],
                resources=[policy_resources]
            ).get_result()

            print(json.dumps(policy, indent=2))

            # end-create_policy
            example_policy_id = policy['id']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_policy_example(self):
        """
        get_policy request example
        """
        try:
            global example_policy_etag
            # begin-get_policy

            response = iam_policy_management_service.get_policy(
                policy_id=example_policy_id
            )
            policy = response.get_result()

            print(json.dumps(policy, indent=2))

            # end-get_policy
            example_policy_etag = response.get_headers().get("Etag")

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_policy_example(self):
        """
        update_policy request example
        """
        try:
            # begin-update_policy

            policy_subjects = PolicySubject(
                attributes=[SubjectAttribute(name='iam_id', value=example_user_id)])
            account_id_resource_attribute = ResourceAttribute(
                name='accountId', value=example_account_id)
            service_name_resource_attribute = ResourceAttribute(
                name='serviceType', value='service')
            policy_resource_tag = ResourceTag(
                name='project', value='prototype')
            policy_resources = PolicyResource(
                attributes=[account_id_resource_attribute,
                            service_name_resource_attribute],
                tags=[policy_resource_tag])
            updated_policy_roles = PolicyRole(
                role_id='crn:v1:bluemix:public:iam::::role:Editor')

            policy = iam_policy_management_service.update_policy(
                type='access',
                policy_id=example_policy_id,
                if_match=example_policy_etag,
                subjects=[policy_subjects],
                roles=[updated_policy_roles],
                resources=[policy_resources]
            ).get_result()

            print(json.dumps(policy, indent=2))

            # end-update_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_patch_policy_example(self):
        """
        patch_policy request example
        """
        try:
            # begin-patch_policy

            policy = iam_policy_management_service.patch_policy(
                policy_id=example_policy_id,
                if_match=example_policy_etag,
                state='active'
            ).get_result()

            print(json.dumps(policy, indent=2))

            # end-patch_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_policies_example(self):
        """
        list_policies request example
        """
        try:
            # begin-list_policies

            policy_list = iam_policy_management_service.list_policies(
                account_id=example_account_id, iam_id=example_user_id, format='include_last_permit'
            ).get_result()

            print(json.dumps(policy_list, indent=2))

            # end-list_policies

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_policy_example(self):
        """
        delete_policy request example
        """
        try:
            # begin-delete_policy

            response = iam_policy_management_service.delete_policy(
                policy_id=example_policy_id
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_role_example(self):
        """
        create_role request example
        """
        try:
            global example_custom_role_id
            # begin-create_role

            custom_role = iam_policy_management_service.create_role(
                display_name='IAM Groups read access',
                actions=['iam-groups.groups.read'],
                name='ExampleRoleIAMGroups',
                account_id=example_account_id,
                service_name=example_service_name
            ).get_result()

            print(json.dumps(custom_role, indent=2))

            # end-create_role
            example_custom_role_id = custom_role["id"]

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_role_example(self):
        """
        get_role request example
        """
        try:
            global example_custom_role_etag
            # begin-get_role

            response = iam_policy_management_service.get_role(
                role_id=example_custom_role_id
            )
            custom_role = response.get_result()

            print(json.dumps(custom_role, indent=2))

            # end-get_role
            example_custom_role_etag = response.get_headers().get("Etag")

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_role_example(self):
        """
        update_role request example
        """
        try:
            # begin-update_role

            updated_role_actions = [
                'iam-groups.groups.read', 'iam-groups.groups.list']
            custom_role = iam_policy_management_service.update_role(
                role_id=example_custom_role_id,
                if_match=example_custom_role_etag,
                actions=updated_role_actions
            ).get_result()

            print(json.dumps(custom_role, indent=2))

            # end-update_role

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_roles_example(self):
        """
        list_roles request example
        """
        try:
            # begin-list_roles

            role_list = iam_policy_management_service.list_roles(
                account_id=example_account_id
            ).get_result()

            print(json.dumps(role_list, indent=2))

            # end-list_roles

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_role_example(self):
        """
        delete_role request example
        """
        try:
            # begin-delete_role

            response = iam_policy_management_service.delete_role(
                role_id=example_custom_role_id
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_role

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: IamPolicyManagementV1
##############################################################################
