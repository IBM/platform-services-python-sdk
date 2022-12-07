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

        cls.etagHeader = "ETag"
        cls.testPolicyETag = ""
        cls.testPolicyId = ""
        cls.testUserId = "IBMid-Py" + str(random.randint(0, 99999))
        cls.testUserType = "user"
        cls.testViewerRoleCrn = "crn:v1:bluemix:public:iam::::role:Viewer"
        cls.testEditorRoleCrn = "crn:v1:bluemix:public:iam::::role:Editor"
        cls.testServiceName = "iam-groups"
        cls.testPolicySubject = PolicySubject(attributes=[SubjectAttribute(name='iam_id', value=cls.testUserId)])
        cls.testPolicyRole = PolicyRole(role_id=cls.testViewerRoleCrn)
        resource_tag = ResourceTag(name='project', value='prototype', operator='stringEquals')
        cls.testPolicyResources = PolicyResource(
            attributes=[
                ResourceAttribute(name='accountId', value=cls.testAccountId, operator='stringEquals'),
                ResourceAttribute(name='serviceType', value='service', operator='stringEquals'),
            ],
            tags=[resource_tag],
        )

        cls.testV2PolicySubject = V2PolicyBaseSubject(
            attributes=[V2PolicyAttribute(key='iam_id', value=cls.testUserId, operator='stringEquals')]
        )
        cls.testV2PolicyResource = V2PolicyBaseResource(
            attributes=[
                V2PolicyAttribute(key='accountId', value=cls.testAccountId, operator='stringEquals'),
                V2PolicyAttribute(key='serviceType', value='service', operator='stringEquals'),
            ],
        )
        cls.testV2PolicyControl = V2PolicyBaseControl(grant=V2PolicyBaseControlGrant(roles=[cls.testPolicyRole]))
        cls.testV2PolicyRule = V2PolicyBaseRuleV2RuleWithConditions(
            operator='and',
            conditions=[
                V2PolicyAttribute(
                    key='{{environment.attributes.day_of_week}}', operator='dayOfWeekAnyOf', value=[1, 2, 3, 4, 5]
                ),
                V2PolicyAttribute(
                    key='{{environment.attributes.current_time}}',
                    operator='timeGreaterThanOrEquals',
                    value='09:00:00+00:00',
                ),
                V2PolicyAttribute(
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

        result = PolicyList.from_dict(result_dict)
        assert result is not None

        # Iterate across the policies
        for policy in result.policies:
            now = datetime.now(timezone.utc)
            minutesDifference = (now - policy.created_at).seconds / 60

            if "v2/policies" in policy.href:
                if policy.id == cls.testPolicyId or minutesDifference < 5:
                    response = cls.service.v2_delete_policy(policy_id=policy.id)
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

        response = self.service.update_policy(
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

        result = PolicyList.from_dict(result_dict)
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

        response = self.service.update_role(
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

        result = RoleList.from_dict(result_dict)
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

        response = self.service.patch_policy(policy_id=self.testPolicyId, if_match=self.testPolicyETag, state='active')
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
        response = self.service.v2_create_policy(
            type='access',
            subject=self.testV2PolicySubject,
            control=self.testV2PolicyControl,
            resource=self.testV2PolicyResource,
            pattern='time-based-restrictions:weekly',
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
        assert result.control == self.testV2PolicyControl

        print('\nTest policy: ', result)

        self.__class__.testPolicyId = result.id

    def test_11_get_v2_access_policy(self):
        assert self.testPolicyId
        print("Policy ID: ", self.testPolicyId)

        response = self.service.v2_get_policy(policy_id=self.testPolicyId)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = V2Policy.from_dict(result_dict)
        assert result is not None
        assert result.subject == self.testV2PolicySubject
        assert result.resource == self.testV2PolicyResource
        assert result.control.grant.roles[0].role_id == self.testViewerRoleCrn
        assert result.state == 'active'

        self.__class__.testPolicyETag = response.get_headers().get(self.etagHeader)

    def test_12_update_v2_access_policy(self):
        assert self.testPolicyId
        assert self.testPolicyETag
        print("Policy ID: ", self.testPolicyId)

        self.testV2PolicyControl.grant.roles[0].role_id = self.testEditorRoleCrn

        response = self.service.v2_update_policy(
            policy_id=self.testPolicyId,
            if_match=self.testPolicyETag,
            type='access',
            subject=self.testV2PolicySubject,
            control=self.testV2PolicyControl,
            resource=self.testV2PolicyResource,
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
        assert result.control.grant.roles[0].role_id == self.testEditorRoleCrn

        self.__class__.testPolicyETag = response.get_headers().get(self.etagHeader)

    def test_13_list_v2_access_policies(self):
        print("Policy ID: ", self.testPolicyId)

        response = self.service.v2_list_policies(account_id=self.testAccountId, iam_id=self.testUserId)
        assert response is not None
        assert response.get_status_code() == 200

        result_dict = response.get_result()
        assert result_dict is not None

        result = V2PolicyList.from_dict(result_dict)
        assert result is not None

        print("Policy list: ", result)

        # Confirm the test policy is present
        foundTestPolicy = False
        for policy in result.policies:
            if policy.id == self.testPolicyId:
                foundTestPolicy = True
                break
        assert foundTestPolicy
