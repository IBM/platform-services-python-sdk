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
 This class contains an integration test for the IAM Policy Management service.
"""

import pytest
import unittest
import os
import os.path
import random
from datetime import datetime, timezone
from ibm_cloud_sdk_core import *
from ibm_platform_services.iam_policy_management_v1 import *

# Read config file
configFile = 'iam_policy_management.env'
configLoaded = None


class TestIamPolicyManagementV1(unittest.TestCase):
    """
    Integration Test Class for IamPolicyManagementV1
    """

    @classmethod
    def setUpClass(cls):
        if os.path.exists(configFile):
            os.environ['IBM_CREDENTIALS_FILE'] = configFile
        else:
            raise unittest.SkipTest('External configuration not available, skipping...')

        cls.service = IamPolicyManagementV1.new_instance()
        assert cls.service is not None

        cls.config = read_external_sources(IamPolicyManagementV1.DEFAULT_SERVICE_NAME)
        assert cls.config is not None
        cls.testAccountId = cls.config.get('TEST_ACCOUNT_ID')
        assert cls.testAccountId is not None
        cls.testTargetAccountId = cls.config.get('TEST_TARGET_ACCOUNT_ID')
        assert cls.testTargetAccountId is not None
        cls.testTargetEnterpriseAccountId = cls.config.get('TEST_TARGET_ENTERPRISE_ACCOUNT_ID')
        assert cls.testTargetEnterpriseAccountId is not None

        cls.etagHeader = "ETag"
        cls.testPolicyETag = ""
        cls.testPolicyId = ""
        cls.testUserId = "IBMid-Py" + str(random.randint(0, 99999))
        cls.testUserType = "user"
        cls.testViewerRoleCrn = "crn:v1:bluemix:public:iam::::role:Viewer"
        cls.testEditorRoleCrn = "crn:v1:bluemix:public:iam::::role:Editor"
        cls.testServiceName = "iam-groups"
        cls.testServiceRoleCrn = "crn:v1:bluemix:public:iam-identity::::serviceRole:ServiceIdCreator"
        cls.testPolicySubject = PolicySubject(attributes=[SubjectAttribute(name='iam_id', value=cls.testUserId)])
        cls.testPolicyRole = PolicyRole(role_id=cls.testViewerRoleCrn)
        cls.testPolicyAssignmentETag = ""
        resource_tag = ResourceTag(name='project', value='prototype', operator='stringEquals')
        cls.testPolicyResources = PolicyResource(
            attributes=[
                ResourceAttribute(name='accountId', value=cls.testAccountId, operator='stringEquals'),
                ResourceAttribute(name='serviceType', value='service', operator='stringEquals'),
            ],
            tags=[resource_tag],
        )

        cls.testV2PolicySubject = V2PolicySubject(
            attributes=[V2PolicySubjectAttribute(key='iam_id', value=cls.testUserId + '2', operator='stringEquals')]
        )
        cls.testV2PolicyResource = V2PolicyResource(
            attributes=[
                V2PolicyResourceAttribute(key='accountId', value=cls.testAccountId, operator='stringEquals'),
                V2PolicyResourceAttribute(key='serviceType', value='service', operator='stringEquals'),
            ],
            tags=[V2PolicyResourceTag(key='project', value='prototype', operator='stringEquals')],
        )
        cls.testV2PolicyControl = Control(grant=Grant(roles=[cls.testPolicyRole]))
        cls.testV2PolicyRule = V2PolicyRuleRuleWithNestedConditions(
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

        cls.testCustomRoleId = ""
        cls.testCustomRoleETag = ""
        cls.testCustomRoleName = 'TestPythonRole' + str(random.randint(0, 99999))
        cls.testCustomRole = CustomRole(
            name=cls.testCustomRoleName,
            display_name='SDK Test role',
            description='SDK Test role description ',
            account_id=cls.testAccountId,
            service_name=cls.testServiceName,
            actions=['iam-groups.groups.read'],
        )

        cls.testTemplateId = ""
        cls.testTemplateETag = ""
        cls.testTemplateVersion = ""
        cls.testNewTemplateVersion = ""
        cls.testAssignmentId = ""
        cls.testAssignmentPolicyId = ""
        cls.testS2STemplateId = ""
        cls.testS2SBaseTemplateVersion = ""
        cls.testS2STemplateVersion = ""
        cls.testV2PolicyTemplateResource = V2PolicyResource(
            attributes=[
                V2PolicyResourceAttribute(key='serviceName', value='watson', operator='stringEquals'),
            ],
        )
        cls.testTemplatePolicy = TemplatePolicy(
            type='access',
            control=cls.testV2PolicyControl,
            resource=cls.testV2PolicyTemplateResource,
            description='SDK Test Policy',
        )
        cls.testTemplatePrefix = 'SDKPython'
        cls.testTemplateName = cls.testTemplatePrefix + str(random.randint(0, 99999))

        print('\nSetup complete.')

    @classmethod
    def tearDownClass(cls):
        # Delete all the access policies that we created during the test.
        #
        # List all policies in the account for the test user
        response = cls.service.list_policies(account_id=cls.testAccountId, iam_id=cls.testUserId)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = PolicyCollection.from_dict(result_dict)
        assert result is not None

        # Iterate across the policies
        for policy in result.policies:
            now = datetime.now(timezone.utc)
            minutesDifference = (now - policy.created_at).seconds / 60

            if "v2/policies" in policy.href:
                if policy.id == cls.testPolicyId or minutesDifference < 5:
                    response = cls.service.delete_v2_policy(id=policy.id)
                    assert response is not None
                    assert response.get_status_code() == 204
            else:
                if policy.id == cls.testPolicyId or minutesDifference < 5:
                    response = cls.service.delete_policy(policy_id=policy.id)
                    assert response is not None
                    assert response.get_status_code() == 204

        # cleanup custon role
        assert cls.testCustomRoleId is not None
        response = cls.service.delete_role(role_id=cls.testCustomRoleId)
        assert response is not None
        assert response.get_status_code() == 204

        # Delete all the policy templates that we created during the test.
        #
        # List all policy templates in the account
        response = cls.service.list_policy_templates(account_id=cls.testAccountId)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = PolicyTemplateCollection.from_dict(result_dict)
        assert result is not None

        for template in result.policy_templates:
            now = datetime.now(timezone.utc)
            minutesDifference = (now - policy.created_at).seconds / 60
            if cls.testTemplatePrefix in template.name and (template.id == cls.testTemplateId or minutesDifference < 5):
                response = cls.service.delete_policy_template(policy_template_id=template.id)
                assert response is not None
                assert response.get_status_code() == 204

        print('\nClean up complete.')

    def test_00_account_id(self):
        assert self.testAccountId
        print('\nTest account id: ', self.testAccountId)

    def test_01_create_access_policy(self):
        response = self.service.create_policy(
            type='access',
            subjects=[self.testPolicySubject],
            roles=[self.testPolicyRole],
            resources=[self.testPolicyResources],
        )
        assert response is not None
        assert response.get_status_code() == 201

        result_dict = response.get_result()
        assert result_dict is not None

        result = Policy.from_dict(result_dict)
        assert result is not None
        assert result.subjects[0] == self.testPolicySubject
        assert result.resources[0] == self.testPolicyResources
        assert result.roles[0].role_id == self.testViewerRoleCrn

        print('\nTest policy: ', result)

        self.__class__.testPolicyId = result.id

    def test_02_get_access_policy(self):
        assert self.testPolicyId
        print("Policy ID: ", self.testPolicyId)

        response = self.service.get_policy(policy_id=self.testPolicyId)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = Policy.from_dict(result_dict)
        assert result is not None
        assert result.subjects[0] == self.testPolicySubject
        assert result.resources[0] == self.testPolicyResources
        assert result.roles[0].role_id == self.testViewerRoleCrn
        assert result.state == 'active'

        self.__class__.testPolicyETag = response.get_headers().get(self.etagHeader)

    def test_03_update_access_policy(self):
        assert self.testPolicyId
        assert self.testPolicyETag
        print("Policy ID: ", self.testPolicyId)

        self.testPolicyRole.role_id = self.testEditorRoleCrn

        response = self.service.replace_policy(
            policy_id=self.testPolicyId,
            if_match=self.testPolicyETag,
            type='access',
            subjects=[self.testPolicySubject],
            roles=[self.testPolicyRole],
            resources=[self.testPolicyResources],
        )
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = Policy.from_dict(result_dict)
        assert result is not None
        assert result.id == self.testPolicyId
        assert result.subjects[0] == self.testPolicySubject
        assert result.resources[0] == self.testPolicyResources
        assert result.roles[0].role_id == self.testEditorRoleCrn

        self.__class__.testPolicyETag = response.get_headers().get(self.etagHeader)

    def test_04_list_access_policies(self):
        print("Policy ID: ", self.testPolicyId)

        response = self.service.list_policies(account_id=self.testAccountId, iam_id=self.testUserId)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = PolicyCollection.from_dict(result_dict)
        assert result is not None

        print("Policy list: ", result)

        # Confirm the test policy is present
        foundTestPolicy = False
        for policy in result.policies:
            if policy.id == self.testPolicyId:
                foundTestPolicy = True
                break
        assert foundTestPolicy

    def test_05_create_custom_role(self):
        response = self.service.create_role(
            name=self.testCustomRole.name,
            account_id=self.testCustomRole.account_id,
            service_name=self.testCustomRole.service_name,
            display_name=self.testCustomRole.display_name,
            description=self.testCustomRole.description,
            actions=self.testCustomRole.actions,
        )
        assert response is not None
        assert response.get_status_code() == 201

        result_dict = response.get_result()
        assert result_dict is not None

        result = CustomRole.from_dict(result_dict)
        assert result is not None
        assert result.name == self.testCustomRole.name
        assert result.account_id == self.testCustomRole.account_id
        assert result.service_name == self.testCustomRole.service_name
        assert result.description == self.testCustomRole.description
        assert result.actions == self.testCustomRole.actions

        print('\nTest custom role: ', result)

        self.__class__.testCustomRoleId = result.id

    def test_06_get_custom_role(self):
        assert self.testCustomRoleId
        print("Custom Role ID: ", self.testCustomRoleId)

        response = self.service.get_role(role_id=self.testCustomRoleId)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = CustomRole.from_dict(result_dict)
        assert result is not None
        assert result.name == self.testCustomRole.name
        assert result.account_id == self.testCustomRole.account_id
        assert result.service_name == self.testCustomRole.service_name
        assert result.description == self.testCustomRole.description
        assert result.actions == self.testCustomRole.actions

        self.__class__.testCustomRoleETag = response.get_headers().get(self.etagHeader)

    def test_07_update_custom_role(self):
        assert self.testCustomRoleId
        assert self.testCustomRoleETag
        print("Custom Role ID: ", self.testCustomRoleId)

        response = self.service.replace_role(
            role_id=self.testCustomRoleId,
            if_match=self.testCustomRoleETag,
            display_name='Updated ' + self.testCustomRole.display_name,
            description='Updated ' + self.testCustomRole.description,
            actions=self.testCustomRole.actions,
        )
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = CustomRole.from_dict(result_dict)
        assert result is not None
        assert result.name == self.testCustomRole.name
        assert result.account_id == self.testCustomRole.account_id
        assert result.display_name == 'Updated ' + self.testCustomRole.display_name
        assert result.description == 'Updated ' + self.testCustomRole.description
        assert result.actions == self.testCustomRole.actions

    def test_08_list_custom_roles(self):
        assert self.testCustomRoleId
        print("Custom Role ID: ", self.testCustomRoleId)

        response = self.service.list_roles(
            account_id=self.testCustomRole.account_id, service_name=self.testCustomRole.service_name
        )
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = RoleCollection.from_dict(result_dict)
        assert result is not None

        print("Custom roles list: ", result)

        # Confirm the test custom role is present
        foundCustomRole = False
        for role in result.custom_roles:
            if role.id == self.testCustomRoleId:
                foundCustomRole = True
                break
        assert foundCustomRole

    def test_09_patch_access_policy(self):
        assert self.testPolicyId
        assert self.testPolicyETag
        print("Policy ID: ", self.testPolicyId)

        response = self.service.update_policy_state(
            policy_id=self.testPolicyId, if_match=self.testPolicyETag, state='active'
        )
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = Policy.from_dict(result_dict)
        assert result is not None
        assert result.id == self.testPolicyId
        assert result.state == 'active'

    def test_10_create_v2_access_policy(self):
        self.testV2PolicyControl.grant.roles[0].role_id = self.testViewerRoleCrn
        response = self.service.create_v2_policy(
            type='access',
            subject=self.testV2PolicySubject,
            control=self.testV2PolicyControl,
            resource=self.testV2PolicyResource,
            pattern='time-based-conditions:weekly:custom-hours',
            rule=self.testV2PolicyRule,
        )
        assert response is not None
        assert response.get_status_code() == 201

        result_dict = response.get_result()
        assert result_dict is not None

        result = V2Policy.from_dict(result_dict)
        assert result is not None
        assert result.subject == self.testV2PolicySubject
        assert result.resource == self.testV2PolicyResource
        assert result.control is not None
        control = Control.from_dict(result.control)
        assert control.grant.roles[0].role_id == self.testViewerRoleCrn

        print('\nTest policy: ', result)

        self.__class__.testPolicyId = result.id

    def test_11_get_v2_access_policy(self):
        assert self.testPolicyId
        print("Policy ID: ", self.testPolicyId)

        response = self.service.get_v2_policy(id=self.testPolicyId)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = V2Policy.from_dict(result_dict)
        assert result is not None
        assert result.subject == self.testV2PolicySubject
        assert result.resource == self.testV2PolicyResource
        assert result.control is not None
        control = Control.from_dict(result.control)
        assert control.grant.roles[0].role_id == self.testViewerRoleCrn
        assert result.state == 'active'

        self.__class__.testPolicyETag = response.get_headers().get(self.etagHeader)

    def test_12_update_v2_access_policy(self):
        assert self.testPolicyId
        assert self.testPolicyETag
        print("Policy ID: ", self.testPolicyId)

        self.testV2PolicyControl.grant.roles[0].role_id = self.testEditorRoleCrn

        response = self.service.replace_v2_policy(
            id=self.testPolicyId,
            if_match=self.testPolicyETag,
            type='access',
            subject=self.testV2PolicySubject,
            control=self.testV2PolicyControl,
            resource=self.testV2PolicyResource,
            pattern='time-based-conditions:weekly:custom-hours',
            rule=self.testV2PolicyRule,
        )
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = V2Policy.from_dict(result_dict)
        assert result is not None
        assert result.id == self.testPolicyId
        assert result.subject == self.testV2PolicySubject
        assert result.resource == self.testV2PolicyResource

        assert result.control is not None
        control = Control.from_dict(result.control)
        assert control.grant.roles[0].role_id == self.testEditorRoleCrn

        self.__class__.testPolicyETag = response.get_headers().get(self.etagHeader)

        # Set role_id back to default
        self.testV2PolicyControl.grant.roles[0].role_id = self.testViewerRoleCrn

    def test_13_list_v2_access_policies(self):
        print("Policy ID: ", self.testPolicyId)

        response = self.service.list_v2_policies(account_id=self.testAccountId, iam_id=self.testUserId + '2')
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = V2PolicyCollection.from_dict(result_dict)
        assert result is not None

        print("Policy list: ", result)

        # Confirm the test policy is present
        foundTestPolicy = False
        for policy in result.policies:
            if policy.id == self.testPolicyId:
                foundTestPolicy = True
                break
        assert foundTestPolicy

    def test_14_list_v2_roles(self):
        response = self.service.list_roles(account_id=self.testCustomRole.account_id, service_group_id="IAM")
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = RoleCollection.from_dict(result_dict)
        assert result is not None

        print("List roles: ", result)

        # confirm the system's viewer and service roles are present
        testSystemRolePresent = False
        testServiceRolePresent = False
        for role in result.system_roles:
            if role.crn == self.testViewerRoleCrn:
                testSystemRolePresent = True
                break
        assert testSystemRolePresent
        for role in result.service_roles:
            if role.crn == self.testServiceRoleCrn:
                testServiceRolePresent = True
                break
        assert testServiceRolePresent

    def test_15_create_policy_template(self):
        response = self.service.create_policy_template(
            name=self.testTemplateName,
            account_id=self.testAccountId,
            policy=self.testTemplatePolicy,
            description='SDK Test Policy Template',
        )
        assert response is not None

        assert response.get_status_code() == 201

        result_dict = response.get_result()
        assert result_dict is not None

        result = PolicyTemplate.from_dict(result_dict)
        assert result is not None

        self.__class__.testTemplateId = result.id
        self.__class__.testTemplateVersion = result.version
        assert result.state == "active"

    def test_16_get_policy_template(self):
        assert self.testTemplateId
        print("Policy Tempate ID: ", self.testTemplateId)

        response = self.service.get_policy_template(
            policy_template_id=self.testTemplateId,
        )
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = PolicyTemplate.from_dict(result_dict)
        assert result is not None

        self.__class__.testTemplateETag = response.get_headers().get(self.etagHeader)
        assert result.state == "active"

    def test_17_replace_policy_template(self):
        assert self.testTemplateId
        assert self.testTemplateETag
        assert self.testTemplateVersion

        print("Policy Tempate ID: ", self.testTemplateId)
        self.testV2PolicyControl.grant.roles[0].role_id = self.testEditorRoleCrn

        updated_template_description = 'SDK Updated Test Policy Template'
        response = self.service.replace_policy_template(
            policy_template_id=self.testTemplateId,
            version=self.testTemplateVersion,
            if_match=self.testTemplateETag,
            policy=self.testTemplatePolicy,
            description=updated_template_description,
        )

        result_dict = response.get_result()
        assert result_dict is not None

        result = PolicyTemplate.from_dict(result_dict)
        assert result is not None
        assert result.description == updated_template_description
        assert result.state == "active"

    def test_18_list_policy_templates(self):
        response = self.service.list_policy_templates(
            account_id=self.testAccountId,
            accept_language='default',
        )

        assert response.get_status_code() == 200
        result_dict = response.get_result()
        assert result_dict is not None

        result = PolicyTemplateCollection.from_dict(result_dict)

        print("Policy Template list: ", result)

        # Confirm the test policy template is present
        foundTestTemplate = False
        for policy_template in result.policy_templates:
            if policy_template.id == self.testTemplateId:
                foundTestTemplate = True
                break
        assert foundTestTemplate
        assert result.policy_templates[0].state == "active"

    def test_19_create_policy_template_version(self):
        self.testV2PolicyControl.grant.roles[0].role_id = self.testViewerRoleCrn
        response = self.service.create_policy_template_version(
            policy_template_id=self.testTemplateId,
            policy=self.testTemplatePolicy,
            description='SDK New Test Policy Template',
        )

        assert response.get_status_code() == 201
        result_dict = response.get_result()
        assert result_dict is not None
        result = PolicyTemplate.from_dict(result_dict)
        assert result is not None

        assert result.version > self.testTemplateVersion
        self.__class__.testNewTemplateVersion = result.version
        assert result.state == "active"

    def test_20_get_policy_template_version(self):
        response = self.service.get_policy_template_version(
            policy_template_id=self.testTemplateId,
            version=self.testNewTemplateVersion,
        )

        assert response.get_status_code() == 200
        result_dict = response.get_result()
        assert result_dict is not None

        self.__class__.testTemplateETag = response.get_headers().get(self.etagHeader)
        result = PolicyTemplate.from_dict(result_dict)
        assert result is not None
        assert result.state == "active"

    def test_21_commit_policy_template(self):
        response = self.service.commit_policy_template(
            policy_template_id=self.testTemplateId,
            version=self.testTemplateVersion,
        )

        assert response.get_status_code() == 204

        response = self.service.get_policy_template_version(
            policy_template_id=self.testTemplateId,
            version=self.testTemplateVersion,
        )

        assert response.get_status_code() == 200
        self.__class__.testTemplateETag = response.get_headers().get(self.etagHeader)
        assert self.testTemplateETag is not None

        # Now that policy template is committed, should fail to update version
        try:
            response = self.service.replace_policy_template(
                policy_template_id=self.testTemplateId,
                version=self.testTemplateVersion,
                if_match=self.testTemplateETag,
                policy=self.testTemplatePolicy,
                description='SDK Fail to Update Committed Version',
            )
        except ApiException as e:
            assert (
                e.message
                == "Policy template id '"
                + self.testTemplateId
                + "' and version '"
                + self.testTemplateVersion
                + "' is committed and cannot be updated"
            )

    def test_22_delete_policy_template_version(self):
        response = self.service.delete_policy_template_version(
            policy_template_id=self.testTemplateId,
            version=self.testNewTemplateVersion,
        )
        assert response.get_status_code() == 204

    def test_23_list_policy_template_versions(self):
        response = self.service.list_policy_template_versions(
            policy_template_id=self.testTemplateId,
        )

        assert response.get_status_code() == 200
        result_dict = response.get_result()
        assert result_dict is not None

        result = PolicyTemplateVersionsCollection.from_dict(result_dict)
        assert result is not None
        assert len(result.versions) == 1

        # Confirm the test policy template with new version is present
        foundTestTemplateVersion = False
        for version in result.versions:
            if version.version == self.testTemplateVersion:
                foundTestTemplateVersion = True
                break
        assert foundTestTemplateVersion

    def test_24_create_policy_s2s_template(self):
        response = self.service.create_policy_template(
            name="S2STest",
            account_id=self.testAccountId,
            policy=TemplatePolicy(
                type='authorization',
                control=Control(
                    grant=Grant(roles=[PolicyRole(role_id="crn:v1:bluemix:public:iam::::serviceRole:Writer")])
                ),
                resource=V2PolicyResource(
                    attributes=[
                        V2PolicyResourceAttribute(
                            key='serviceName', value='cloud-object-storage', operator='stringEquals'
                        ),
                    ],
                ),
                subject=V2PolicySubject(
                    attributes=[
                        V2PolicySubjectAttribute(key='serviceName', value='compliance', operator='stringEquals'),
                    ],
                ),
                description='SDK Test Policy',
            ),
            description='SDK Test Policy S2S Template',
            committed=True,
        )
        assert response is not None

        assert response.get_status_code() == 201

        result_dict = response.get_result()
        assert result_dict is not None

        result = PolicyTemplate.from_dict(result_dict)
        print("Policy S2S Template : ", result)
        assert result is not None
        self.__class__.testS2STemplateId = result.id
        self.__class__.testS2SBaseTemplateVersion = result.version
        assert result.state == "active"

    def test_25_create_policy_s2s_template_version(self):
        response = self.service.create_policy_template_version(
            policy=TemplatePolicy(
                type='authorization',
                control=Control(
                    grant=Grant(roles=[PolicyRole(role_id="crn:v1:bluemix:public:iam::::serviceRole:Reader")])
                ),
                resource=V2PolicyResource(
                    attributes=[
                        V2PolicyResourceAttribute(key='serviceName', value='kms', operator='stringEquals'),
                    ],
                ),
                subject=V2PolicySubject(
                    attributes=[
                        V2PolicySubjectAttribute(key='serviceName', value='compliance', operator='stringEquals'),
                    ],
                ),
                description='SDK Test Policy',
            ),
            description='SDK Test Policy S2S Template',
            committed=True,
            policy_template_id=self.testS2STemplateId,
        )
        assert response is not None

        assert response.get_status_code() == 201

        result_dict = response.get_result()
        assert result_dict is not None

        result = PolicyTemplate.from_dict(result_dict)
        print("Policy S2S Template Version: ", result)
        assert result is not None

        self.__class__.testS2STemplateVersion = result.version
        assert result.state == "active"

    def test_26_create_policy_assignment(self):
        try:
            response = self.service.create_policy_template_assignment(
                version="1.0",
                target=AssignmentTargetDetails(
                    type="Enterprise",
                    id=self.testTargetEnterpriseAccountId,
                ),
                templates=[AssignmentTemplateDetails(id=self.testS2STemplateId, version=self.testS2SBaseTemplateVersion)],
            )
        except ApiException as e:
            assert (
                e.message
                == "Invalid body format. Check the input parameters. instance.target.type is not one of enum values: Account"
            )

    def test_27_create_policy_assignment(self):
        response = self.service.create_policy_template_assignment(
            version="1.0",
            target=AssignmentTargetDetails(
                type="Account",
                id=self.testTargetAccountId,
            ),
            templates=[AssignmentTemplateDetails(id=self.testS2STemplateId, version=self.testS2SBaseTemplateVersion)],
        )
        assert response.get_status_code() == 201
        result_dict = response.get_result()
        assert result_dict is not None

        result = PolicyAssignmentV1Collection.from_dict(result_dict)
        print("Policy Assignment Creation: ", result)
        assert result is not None
        self.__class__.testAssignmentId = result.assignments[0].id
        self.__class__.testAssignmentPolicyId = result.assignments[0].resources[0].policy.resource_created.id
        self.__class__.testPolicyAssignmentETag = response.get_headers().get(self.etagHeader)


    def test_28_list_policy_assignments(self):
        response = self.service.list_policy_assignments(
            account_id=self.testAccountId,
            accept_language='default',
            version="1.0",
        )

        assert response.get_status_code() == 200
        result_dict = response.get_result()
        assert result_dict is not None
        result = PolicyTemplateAssignmentCollection.from_dict(result_dict)
        assert result is not None

    def test_29_get_policy_assignment(self):
        assert self.testAssignmentId
        print("Assignment ID: ", self.testAssignmentId)
        response = self.service.get_policy_assignment(
            assignment_id=self.testAssignmentId,
            version="1.0",
        )

        assert response.get_status_code() == 200
        result_dict = response.get_result()
        assert result_dict is not None

        result = PolicyAssignmentV1.from_dict(result_dict)
        assert result is not None
        assert result.id == self.testAssignmentId

    def test_30_update_policy_assignment(self):
        assert self.testAssignmentId
        assert self.testPolicyAssignmentETag
        print("Assignment ID: ", self.testAssignmentId)
        response = self.service.update_policy_assignment(
            assignment_id=self.testAssignmentId,
            version="1.0",
            if_match=self.testPolicyAssignmentETag,
            template_version=self.testS2STemplateVersion,
        )

        assert response.get_status_code() == 200
        result_dict = response.get_result()
        assert result_dict is not None

        result = PolicyAssignmentV1.from_dict(result_dict)
        assert result is not None
        print("Policy Assignment Update: ", result)

    def test_31_get_v2_assignment_policy(self):
        assert self.testAssignmentPolicyId
        print("Assignment Policy ID: ", self.testAssignmentPolicyId)

        response = self.service.get_v2_policy(id=self.testAssignmentPolicyId)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = V2PolicyTemplateMetaData.from_dict(result_dict)
        assert result is not None
        assert result.template is not None

    def test_32_delete_policy_assignment(self):
        response = self.service.delete_policy_assignment(
            assignment_id=self.testAssignmentId,
        )
        assert response.get_status_code() == 204

    def test_33_delete_policy_template(self):
        response = self.service.delete_policy_template(
            policy_template_id=self.testS2STemplateId,
        )
        assert response.get_status_code() == 204
