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

# Config file name
config_file = 'iam_policy_management_v1.env'

iam_policy_management_service = None

config = None


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
            global config
            config = read_external_sources(IamPolicyManagementV1.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_list_policies_example(self):
        """
        list_policies request example
        """
        try:
            # begin-list_policies

            policy_list = iam_policy_management_service.list_policies(
                account_id='testString'
            ).get_result()

            print(json.dumps(policy_list, indent=2))

            # end-list_policies

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_policy_example(self):
        """
        create_policy request example
        """
        try:
            # begin-create_policy

            policy_subject_model = {
            }

            policy_role_model = {
                'role_id': 'testString'
            }

            policy_resource_model = {
            }

            policy = iam_policy_management_service.create_policy(
                type='testString',
                subjects=[policy_subject_model],
                roles=[policy_role_model],
                resources=[policy_resource_model]
            ).get_result()

            print(json.dumps(policy, indent=2))

            # end-create_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_policy_example(self):
        """
        update_policy request example
        """
        try:
            # begin-update_policy

            policy_subject_model = {
            }

            policy_role_model = {
                'role_id': 'testString'
            }

            policy_resource_model = {
            }

            policy = iam_policy_management_service.update_policy(
                policy_id='testString',
                if_match='testString',
                type='testString',
                subjects=[policy_subject_model],
                roles=[policy_role_model],
                resources=[policy_resource_model]
            ).get_result()

            print(json.dumps(policy, indent=2))

            # end-update_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_policy_example(self):
        """
        get_policy request example
        """
        try:
            # begin-get_policy

            policy = iam_policy_management_service.get_policy(
                policy_id='testString'
            ).get_result()

            print(json.dumps(policy, indent=2))

            # end-get_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_roles_example(self):
        """
        list_roles request example
        """
        try:
            # begin-list_roles

            role_list = iam_policy_management_service.list_roles().get_result()

            print(json.dumps(role_list, indent=2))

            # end-list_roles

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_role_example(self):
        """
        create_role request example
        """
        try:
            # begin-create_role

            custom_role = iam_policy_management_service.create_role(
                display_name='testString',
                actions=['testString'],
                name='testString',
                account_id='testString',
                service_name='testString'
            ).get_result()

            print(json.dumps(custom_role, indent=2))

            # end-create_role

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_role_example(self):
        """
        update_role request example
        """
        try:
            # begin-update_role

            custom_role = iam_policy_management_service.update_role(
                role_id='testString',
                if_match='testString',
            ).get_result()

            print(json.dumps(custom_role, indent=2))

            # end-update_role

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_role_example(self):
        """
        get_role request example
        """
        try:
            # begin-get_role

            custom_role = iam_policy_management_service.get_role(
                role_id='testString'
            ).get_result()

            print(json.dumps(custom_role, indent=2))

            # end-get_role

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
                role_id='testString'
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_role

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
                policy_id='testString'
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_policy

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: IamPolicyManagementV1
##############################################################################
