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
import random
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.iam_policy_management_v1 import *

#
# Below are examples on how to use IAM Policy Management service
#
# The following environment variables are assumed to be defined when running examples below:
#
# IAM_POLICY_MANAGEMENT_URL=https://iam.cloud.ibm.com
# IAM_POLICY_MANAGEMENT_AUTH_TYPE=iam
# IAM_POLICY_MANAGEMENT_AUTH_URL=https://iam.cloud.ibm.com/identity/token
# IAM_POLICY_MANAGEMENT_APIKEY= <YOUR_APIKEY>
# IAM_POLICY_MANAGEMENT_TEST_ACCOUNT_ID= <YOUR_ACCOUNT_ID>
#
# Alternatively, above environment variables can be placed in a "credentials" file and then:
# export IBM_CREDENTIALS_FILE=<name of credentials file>
#

# Config file name
config_file = 'iam_policy_management.env'

iam_policy_management_service = None

config = None

test_account_id = None
test_policy_id = None
test_policy_etag = None
test_custom_role_id = None
test_custom_role_etag = None
test_user_id = "IBMid-SDKPython" + str(random.randint(0, 99999))
test_service_name = "iam-groups"

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
            global config, test_account_id
            config = read_external_sources(IamPolicyManagementV1.DEFAULT_SERVICE_NAME)
            test_account_id = config['TEST_ACCOUNT_ID']

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
            global test_policy_id
            # begin-create_policy

            policy_subject = PolicySubject(
                attributes=[SubjectAttribute(name='iam_id', value=test_user_id)])
            policy_role = PolicyRole(
                role_id='crn:v1:bluemix:public:iam::::role:Viewer')
            resource_account_attribute = ResourceAttribute(
                name='accountId', value=test_account_id)
            resource_service_attribute = ResourceAttribute(
                name='serviceName', value=test_service_name)
            resource_tag = ResourceTag(name='project', value='prototype')
            policy_resource = PolicyResource(
                attributes=[resource_account_attribute,
                            resource_service_attribute],
                tags=[resource_tag])

            policy = iam_policy_management_service.create_policy(
                type='access',
                subjects=[policy_subject],
                roles=[policy_role],
                resources=[policy_resource]
            ).get_result()

            print(policy)

            # end-create_policy
            test_policy_id = policy['id']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_policy_example(self):
        """
        get_policy request example
        """
        try:
            global test_policy_etag
            # begin-get_policy

            response = iam_policy_management_service.get_policy(
                policy_id=test_policy_id
            )
            policy = response.get_result()

            print(policy)

            # end-get_policy
            test_policy_etag = response.get_headers().get("Etag")

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_policy_example(self):
        """
        update_policy request example
        """
        try:
            # begin-update_policy

            policy_subject = PolicySubject(
                attributes=[SubjectAttribute(name='iam_id', value=test_user_id)])
            updated_policy_role = PolicyRole(
                role_id='crn:v1:bluemix:public:iam::::role:Editor')
            resource_account_attribute = ResourceAttribute(
                name='accountId', value=test_account_id)
            resource_service_attribute = ResourceAttribute(
                name='serviceName', value=test_service_name)
            resource_tag = ResourceTag(name='project', value='prototype')
            policy_resource = PolicyResource(
                attributes=[resource_account_attribute,
                            resource_service_attribute],
                tags=[resource_tag])

            policy = iam_policy_management_service.update_policy(
                type='access',
                policy_id=test_policy_id,
                if_match=test_policy_etag,
                subjects=[policy_subject],
                roles=[updated_policy_role],
                resources=[policy_resource]
            ).get_result()

            print(policy)

            # end-update_policy

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
                account_id=test_account_id, iam_id=test_user_id, format='include_last_permit'
            ).get_result()

            print(policy_list)

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
                policy_id=test_policy_id
            )

            print(response)

            # end-delete_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_role_example(self):
        """
        create_role request example
        """
        try:
            global test_custom_role_id
            # begin-create_role

            custom_role = iam_policy_management_service.create_role(
                display_name='IAM Groups read access',
                actions=['iam-groups.groups.read'],
                name='ExampleRoleIAMGroups',
                account_id=test_account_id,
                service_name=test_service_name
            ).get_result()

            print(custom_role)

            # end-create_role
            test_custom_role_id = custom_role["id"]

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_role_example(self):
        """
        get_role request example
        """
        try:
            global test_custom_role_etag
            # begin-get_role

            response = iam_policy_management_service.get_role(
                role_id=test_custom_role_id
            )
            custom_role = response.get_result()

            print(custom_role)

            # end-get_role
            test_custom_role_etag = response.get_headers().get("Etag")

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_role_example(self):
        """
        update_role request example
        """
        try:
            # begin-update_role

            updated_role_actions = ['iam-groups.groups.read', 'iam-groups.groups.list']
            custom_role = iam_policy_management_service.update_role(
                role_id=test_custom_role_id,
                if_match=test_custom_role_etag,
                actions=updated_role_actions
            ).get_result()

            print(custom_role)

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
                account_id=test_account_id
            ).get_result()

            print(role_list)

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
                role_id=test_custom_role_id
            )

            print(response)

            # end-delete_role

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: IamPolicyManagementV1
##############################################################################
