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
example_template_id = None
example_template_etag = None
example_template_version = None
example_basic_template_version = None
example_assignment_id = None
example_user_id = "IBMid-user1"
example_service_name = "iam-groups"
example_assignment_policy_id = None
example_updated_policy_etag = None
example_target_account_id = None
example_assignment_etag = None

##############################################################################
# Start of Examples for Service: IamPolicyManagementV1
##############################################################################
# region


class TestIamPolicyManagementV1Examples:
    """
    Example Test Class for IamPolicyManagementV1
    """

    @classmethod
    def setup_class(cls):
        global iam_policy_management_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            iam_policy_management_service = IamPolicyManagementV1.new_instance()

            # end-common
            assert iam_policy_management_service is not None

            # Load the configuration
            global config, example_account_id, example_target_account_id
            config = read_external_sources(IamPolicyManagementV1.DEFAULT_SERVICE_NAME)
            example_account_id = config['TEST_ACCOUNT_ID']
            example_target_account_id = config['TEST_TARGET_ACCOUNT_ID']

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
            print('\ncreate_policy() result:')
            # begin-create_policy

            policy_subjects = PolicySubject(attributes=[SubjectAttribute(name='iam_id', value=example_user_id)])
            policy_roles = PolicyRole(role_id='crn:v1:bluemix:public:iam::::role:Viewer')
            account_id_resource_attribute = ResourceAttribute(name='accountId', value=example_account_id)
            service_name_resource_attribute = ResourceAttribute(name='serviceType', value='service')
            policy_resource_tag = ResourceTag(name='project', value='prototype')
            policy_resources = PolicyResource(
                attributes=[account_id_resource_attribute, service_name_resource_attribute], tags=[policy_resource_tag]
            )

            policy = iam_policy_management_service.create_policy(
                type='access', subjects=[policy_subjects], roles=[policy_roles], resources=[policy_resources]
            ).get_result()

            global example_policy_id
            example_policy_id = policy['id']
            print(json.dumps(policy, indent=2))

            # end-create_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_policy_example(self):
        """
        get_policy request example
        """
        try:
            print('\nget_policy() result:')
            # begin-get_policy

            response = iam_policy_management_service.get_policy(policy_id=example_policy_id)
            policy = response.get_result()
            global example_policy_etag
            example_policy_etag = response.get_headers().get("Etag")

            print(json.dumps(policy, indent=2))

            # end-get_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_policy_example(self):
        """
        replace_policy request example
        """
        try:
            print('\nreplace_policy() result:')
            # begin-replace_policy

            policy_subjects = PolicySubject(attributes=[SubjectAttribute(name='iam_id', value=example_user_id)])
            account_id_resource_attribute = ResourceAttribute(name='accountId', value=example_account_id)
            service_name_resource_attribute = ResourceAttribute(name='serviceType', value='service')
            policy_resource_tag = ResourceTag(name='project', value='prototype')
            policy_resources = PolicyResource(
                attributes=[account_id_resource_attribute, service_name_resource_attribute], tags=[policy_resource_tag]
            )
            updated_policy_roles = PolicyRole(role_id='crn:v1:bluemix:public:iam::::role:Editor')

            response = iam_policy_management_service.replace_policy(
                type='access',
                policy_id=example_policy_id,
                if_match=example_policy_etag,
                subjects=[policy_subjects],
                roles=[updated_policy_roles],
                resources=[policy_resources],
            )
            policy = response.get_result()
            global example_updated_policy_etag
            example_updated_policy_etag = response.get_headers().get("Etag")

            print(json.dumps(policy, indent=2))

            # end-replace_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_policy_state_example(self):
        """
        update_policy_state request example
        """
        try:
            print('\nupdate_policy_state() result:')
            # begin-update_policy_state

            policy = iam_policy_management_service.update_policy_state(
                policy_id=example_policy_id, if_match=example_updated_policy_etag, state='active'
            ).get_result()

            print(json.dumps(policy, indent=2))

            # end-update_policy_state

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_policies_example(self):
        """
        list_policies request example
        """
        try:
            print('\nlist_policies() result:')
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
            print('\ndelete_policy() result:')
            # begin-delete_policy

            response = iam_policy_management_service.delete_policy(policy_id=example_policy_id).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_v2_policy_example(self):
        """
        create_v2_policy request example
        """
        try:
            print('\ncreate_v2_policy() result:')
            # begin-create_v2_policy

            policy_subject = V2PolicySubject(
                attributes=[V2PolicySubjectAttribute(key='iam_id', value=example_user_id, operator='stringEquals')]
            )
            policy_role = PolicyRole(role_id='crn:v1:bluemix:public:iam::::role:Viewer')
            account_id_resource_attribute = V2PolicyResourceAttribute(
                key='accountId', value=example_account_id, operator='stringEquals'
            )
            service_name_resource_attribute = V2PolicyResourceAttribute(
                key='serviceType', value='service', operator='stringEquals'
            )
            policy_resource_tag = V2PolicyResourceTag(key='project', value='prototype', operator='stringEquals')
            policy_resource = V2PolicyResource(
                attributes=[account_id_resource_attribute, service_name_resource_attribute], tags=[policy_resource_tag]
            )
            policy_control = Control(grant=Grant(roles=[policy_role]))
            policy_rule = V2PolicyRuleRuleWithNestedConditions(
                operator='and',
                conditions=[
                    RuleAttribute(
                        key='{{environment.attributes.day_of_week}}',
                        operator='dayOfWeekAnyOf',
                        value=['1+00:00', '2+00:00', '3+00:00', '4+00:00', '5+00:00'],
                    ),
                    RuleAttribute(
                        key='{{environment.attributes.current_time}}',
                        operator='timeGreaterThanOrEquals',
                        value='09:00:00+00:00',
                    ),
                    RuleAttribute(
                        key='{{environment.attributes.current_time}}',
                        operator='timeLessThanOrEquals',
                        value='17:00:00+00:00',
                    ),
                ],
            )
            policy_pattern = 'time-based-conditions:weekly:custom-hours'

            policy = iam_policy_management_service.create_v2_policy(
                type='access',
                subject=policy_subject,
                control=policy_control,
                resource=policy_resource,
                rule=policy_rule,
                pattern=policy_pattern,
            ).get_result()

            global example_policy_id
            example_policy_id = policy['id']

            print(json.dumps(policy, indent=2))

            # end-create_v2_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_v2_policy_example(self):
        """
        get_v2_policy request example
        """
        try:
            print('\nget_v2_policy() result:')
            # begin-get_v2_policy

            response = iam_policy_management_service.get_v2_policy(id=example_policy_id)
            policy = response.get_result()

            global example_policy_etag
            example_policy_etag = response.get_headers().get("Etag")

            print(json.dumps(policy, indent=2))

            # end-get_v2_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_v2_policy_example(self):
        """
        replace_v2_policy request example
        """
        try:
            print('\nreplace_v2_policy() result:')
            # begin-replace_v2_policy

            policy_subject = V2PolicySubject(
                attributes=[V2PolicySubjectAttribute(key='iam_id', value=example_user_id, operator='stringEquals')]
            )
            updated_policy_role = PolicyRole(role_id='crn:v1:bluemix:public:iam::::role:Editor')
            account_id_resource_attribute = V2PolicyResourceAttribute(
                key='accountId', value=example_account_id, operator='stringEquals'
            )
            service_name_resource_attribute = V2PolicyResourceAttribute(
                key='serviceType', value='service', operator='stringEquals'
            )
            policy_resource_tag = V2PolicyResourceTag(key='project', value='prototype', operator='stringEquals')
            policy_resource = PolicyResource(
                attributes=[account_id_resource_attribute, service_name_resource_attribute], tags=[policy_resource_tag]
            )
            policy_control = Control(grant=Grant(roles=[updated_policy_role]))
            policy_rule = V2PolicyRuleRuleWithNestedConditions(
                operator='and',
                conditions=[
                    RuleAttribute(
                        key='{{environment.attributes.day_of_week}}',
                        operator='dayOfWeekAnyOf',
                        value=['1+00:00', '2+00:00', '3+00:00', '4+00:00', '5+00:00'],
                    ),
                    RuleAttribute(
                        key='{{environment.attributes.current_time}}',
                        operator='timeGreaterThanOrEquals',
                        value='09:00:00+00:00',
                    ),
                    RuleAttribute(
                        key='{{environment.attributes.current_time}}',
                        operator='timeLessThanOrEquals',
                        value='17:00:00+00:00',
                    ),
                ],
            )
            policy_pattern = 'time-based-conditions:weekly:custom-hours'

            response = iam_policy_management_service.replace_v2_policy(
                type='access',
                id=example_policy_id,
                if_match=example_policy_etag,
                subject=policy_subject,
                control=policy_control,
                resource=policy_resource,
                rule=policy_rule,
                pattern=policy_pattern,
            )
            policy = response.get_result()

            print(json.dumps(policy, indent=2))

            # end-replace_v2_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_v2_policies_example(self):
        """
        list_v2_policies request example
        """
        try:
            print('\nlist_v2_policies() result:')
            # begin-list_v2_policies

            policy_list = iam_policy_management_service.list_v2_policies(
                account_id=example_account_id, iam_id=example_user_id, format='include_last_permit'
            ).get_result()

            print(json.dumps(policy_list, indent=2))

            # end-list_v2_policies

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_v2_policy_example(self):
        """
        delete_v2_policy request example
        """
        try:
            print('\ndelete_v2_policy() result:')
            # begin-delete_v2_policy

            response = iam_policy_management_service.delete_v2_policy(id=example_policy_id).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_v2_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_role_example(self):
        """
        create_role request example
        """
        try:
            print('\ncreate_role() result:')
            # begin-create_role

            custom_role = iam_policy_management_service.create_role(
                display_name='IAM Groups read access',
                actions=['iam-groups.groups.read'],
                name='ExampleRoleIAMGroups',
                account_id=example_account_id,
                service_name=example_service_name,
            ).get_result()

            global example_custom_role_id
            example_custom_role_id = custom_role["id"]

            print(json.dumps(custom_role, indent=2))

            # end-create_role

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_role_example(self):
        """
        get_role request example
        """
        try:
            print('\nget_role() result:')
            # begin-get_role

            response = iam_policy_management_service.get_role(role_id=example_custom_role_id)
            custom_role = response.get_result()

            global example_custom_role_etag
            example_custom_role_etag = response.get_headers().get("Etag")

            print(json.dumps(custom_role, indent=2))

            # end-get_role

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_role_example(self):
        """
        replace_role request example
        """
        try:
            print('\nreplace_role() result:')
            # begin-replace_role

            updated_role_actions = ['iam-groups.groups.read', 'iam-groups.groups.list']
            custom_role = iam_policy_management_service.replace_role(
                role_id=example_custom_role_id,
                if_match=example_custom_role_etag,
                actions=updated_role_actions,
                display_name='IAM Groups read access',
            ).get_result()

            print(json.dumps(custom_role, indent=2))

            # end-replace_role

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_roles_example(self):
        """
        list_roles request example
        """
        try:
            print('\nlist_roles() result:')
            # begin-list_roles

            role_list = iam_policy_management_service.list_roles(account_id=example_account_id).get_result()

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
            print('\ndelete_role() result:')
            # begin-delete_role

            response = iam_policy_management_service.delete_role(role_id=example_custom_role_id).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_role

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_policy_template_example(self):
        """
        create_policy_template request example
        """
        try:
            print('\ncreate_policy_s2s_template() result:')
            # begin-create_policy_template

            v2_policy_resource_attribute_model = {
                'key': 'serviceName',
                'operator': 'stringEquals',
                'value': 'cloud-object-storage',
            }

            v2_policy_resource_model = {
                'attributes': [v2_policy_resource_attribute_model],
            }

            v2_policy_subject_attribute_model = {
                'key': 'serviceName',
                'operator': 'stringEquals',
                'value': 'compliance',
            }

            v2_policy_subject_model = {
                'attributes': [v2_policy_subject_attribute_model],
            }

            roles_model = {
                'role_id': 'crn:v1:bluemix:public:iam::::serviceRole:Writer',
            }

            grant_model = {
                'roles': [roles_model],
            }

            control_model = {
                'grant': grant_model,
            }

            template_policy_model = {
                'type': 'authorization',
                'resource': v2_policy_resource_model,
                'control': control_model,
                'subject': v2_policy_subject_model,
            }

            response = iam_policy_management_service.create_policy_template(
                name='SDKExamplesTest',
                account_id=example_account_id,
                policy=template_policy_model,
            )
            policy_template = response.get_result()

            global example_template_id
            example_template_id = policy_template['id']
            global example_basic_template_version
            example_basic_template_version = policy_template['version']

            print(json.dumps(policy_template, indent=2))

            # end-create_policy_template

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_policy_template_example(self):
        """
        get_policy_template request example
        """
        try:
            print('\nget_policy_template() result:')
            # begin-get_policy_template

            print('example_template_id: ', example_template_id)
            response = iam_policy_management_service.get_policy_template(
                policy_template_id=example_template_id,
            )
            policy_template = response.get_result()

            global example_template_etag
            example_template_etag = response.get_headers().get("Etag")

            print(json.dumps(policy_template, indent=2))

            # end-get_policy_template

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_policy_template_example(self):
        """
        replace_policy_template request example
        """
        try:
            print('\nreplace_policy_s2s_template() result:')
            # begin-replace_policy_template

            v2_policy_resource_attribute_model = {
                'key': 'serviceName',
                'operator': 'stringEquals',
                'value': 'kms',
            }

            v2_policy_resource_model = {
                'attributes': [v2_policy_resource_attribute_model],
            }

            v2_policy_subject_attribute_model = {
                'key': 'serviceName',
                'operator': 'stringEquals',
                'value': 'compliance',
            }

            v2_policy_subject_model = {
                'attributes': [v2_policy_subject_attribute_model],
            }

            roles_model = {
                'role_id': 'crn:v1:bluemix:public:iam::::serviceRole:Reader',
            }

            grant_model = {
                'roles': [roles_model],
            }

            control_model = {
                'grant': grant_model,
            }

            template_policy_model = {
                'type': 'authorization',
                'resource': v2_policy_resource_model,
                'subject': v2_policy_subject_model,
                'control': control_model,
            }

            response = iam_policy_management_service.replace_policy_template(
                policy_template_id=example_template_id,
                version=example_basic_template_version,
                if_match=example_template_etag,
                policy=template_policy_model,
            )
            policy_template = response.get_result()

            print(json.dumps(policy_template, indent=2))

            # end-replace_policy_template

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_policy_templates_example(self):
        """
        list_policy_templates request example
        """
        try:
            print('\nlist_policy_templates() result:')
            # begin-list_policy_templates

            response = iam_policy_management_service.list_policy_templates(
                account_id=example_account_id,
            )
            policy_template_collection = response.get_result()

            print(json.dumps(policy_template_collection, indent=2))

            # end-list_policy_templates

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_policy_template_version_example(self):
        """
        create_policy_template_version request example
        """
        try:
            print('\ncreate_policy_template_version() result:')
            # begin-create_policy_template_version

            v2_policy_resource_attribute_model = {
                'key': 'serviceName',
                'operator': 'stringEquals',
                'value': 'appid',
            }

            v2_policy_resource_model = {
                'attributes': [v2_policy_resource_attribute_model],
            }

            v2_policy_subject_attribute_model = {
                'key': 'serviceName',
                'operator': 'stringEquals',
                'value': 'compliance',
            }

            v2_policy_subject_model = {
                'attributes': [v2_policy_subject_attribute_model],
            }

            roles_model = {
                'role_id': 'crn:v1:bluemix:public:iam::::serviceRole:Reader',
            }

            grant_model = {
                'roles': [roles_model],
            }

            control_model = {
                'grant': grant_model,
            }

            template_policy_model = {
                'type': 'authorization',
                'resource': v2_policy_resource_model,
                'control': control_model,
                'subject': v2_policy_subject_model,
            }

            response = iam_policy_management_service.create_policy_template_version(
                policy_template_id=example_template_id,
                policy=template_policy_model,
                committed=True,
            )
            policy_template = response.get_result()
            global example_template_version
            example_template_version = policy_template['version']
            print(json.dumps(policy_template, indent=2))

            # end-create_policy_template_version

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_policy_template_versions_example(self):
        """
        list_policy_template_versions request example
        """
        try:
            print('\nlist_policy_template_versions() result:')
            # begin-list_policy_template_versions

            response = iam_policy_management_service.list_policy_template_versions(
                policy_template_id=example_template_id,
            )
            policy_template_versions_collection = response.get_result()

            print(json.dumps(policy_template_versions_collection, indent=2))

            # end-list_policy_template_versions

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_policy_template_version_example(self):
        """
        get_policy_template_version request example
        """
        try:
            print('\nget_policy_template_version() result:')
            # begin-get_policy_template_version

            response = iam_policy_management_service.get_policy_template_version(
                policy_template_id=example_template_id,
                version=example_template_version,
            )
            policy_template = response.get_result()

            global example_template_etag
            example_template_etag = response.get_headers().get("Etag")

            print(json.dumps(policy_template, indent=2))

            # end-get_policy_template_version

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_commit_policy_template_example(self):
        """
        commit_policy_template request example
        """
        try:
            # begin-commit_policy_template

            response = iam_policy_management_service.commit_policy_template(
                policy_template_id=example_template_id,
                version=example_basic_template_version,
            )

            # end-commit_policy_template
            print('\ncommit_policy_template() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    
    @needscredentials
    def test_create_policy_assignment_example(self):
        """
        create_policy_template_assignment request example
        """
        try:
            print('\ncreate_policy_template_assignment() result:')
            # begin-create_policy_template_assignment
            response=iam_policy_management_service.create_policy_template_assignment(
            version="1.0",
            target=AssignmentTargetDetails(
                type="Account",
                id=example_target_account_id,
            ),
            options=PolicyAssignmentV1Options(root=PolicyAssignmentV1OptionsRoot(requester_id="test_sdk", assignment_id="test")),
            templates=[AssignmentTemplateDetails(id=example_template_id, version=example_basic_template_version)],
         )
            result = response.get_result()
            assert result is not None

            global example_assignment_id
            example_assignment_id = result['assignments'][0]['id']
            global example_assignment_etag
            example_assignment_etag = response.get_headers().get("Etag")
            print(json.dumps(result, indent=2))

            # end-create_policy_template_assignment

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_update_policy_assignment_example(self):
        """
        update_policy_assignment request example
        """
        try:
            print('\nupdate_policy_assignment() result:')
            # begin-update_policy_assignment

            response = iam_policy_management_service.update_policy_assignment(
                assignment_id=example_assignment_id,
                version="1.0",
                if_match=example_assignment_etag,
                template_version=example_template_version,
            )
            assignment = response.get_result()

            print(json.dumps(assignment, indent=2))

            # end-update_policy_assignment

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_policy_assignments_example(self):
        """
        list_policy_assignments request example
        """
        try:
            print('\nlist_policy_assignments() result:')
            # begin-list_policy_assignments

            response = iam_policy_management_service.list_policy_assignments(
                account_id=example_account_id,
                version="1.0",
            )
            polcy_template_assignment_collection = response.get_result()

            print(json.dumps(polcy_template_assignment_collection, indent=2))

            # end-list_policy_assignments

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_policy_assignment_example(self):
        """
        get_policy_assignment request example
        """
        try:
            print('\nget_policy_assignment() result:')
            # begin-get_policy_assignment

            response = iam_policy_management_service.get_policy_assignment(
                assignment_id=example_assignment_id,
                version="1.0",
            )
            policy_assignment_record = response.get_result()

            global example_assignment_policy_id
            example_assignment_policy_id = policy_assignment_record['resources'][0]['policy']['resource_created']['id']

            print(json.dumps(policy_assignment_record, indent=2))

            # end-get_policy_assignment

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_v2_assignment_policy_example(self):
        """
        get_v2_assignment_policy request example
        """
        try:
            print('\nget_v2_assignment_policy() result:')
            # begin-get_v2_assignment_policy

            response = iam_policy_management_service.get_v2_policy(id=example_assignment_policy_id)
            policy = response.get_result()

            print(json.dumps(policy, indent=2))

            # end-get_v2_assignment_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_policy_assignment_example(self):
        """
        delete_policy_assignment request example
        """
        try:
            # begin-delete_policy_assignment

            response = iam_policy_management_service.delete_policy_assignment(
            assignment_id=example_assignment_id,
        )

            # end-delete_policy_assignment
            print('\ndelete_policy_assignment() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_policy_template_example(self):
        """
        delete_policy_template request example
        """
        try:
            # begin-delete_policy_template

            response = iam_policy_management_service.delete_policy_template(
                policy_template_id=example_template_id,
            )

            # end-delete_policy_template
            print('\ndelete_policy_template() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: IamPolicyManagementV1
##############################################################################
