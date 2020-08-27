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
Integration Tests for ConfigurationGovernanceV1
"""

import os
import pytest
from ibm_platform_services.configuration_governance_v1 import *

# Config file name
config_file = 'configuration_governance_v1.env'

class TestConfigurationGovernanceV1():
    """
    Integration Test Class for ConfigurationGovernanceV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.configuration_governance_service = ConfigurationGovernanceV1.new_instance(
                )
            assert cls.configuration_governance_service is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_rules(self):

        # Construct a dict representation of a UISupport model
        ui_support_model = {
            'display_name': 'testString',
            'description': 'testString'
        }

        # Construct a dict representation of a RuleImport model
        rule_import_model = {
            'name': 'testString',
            'ui_support': ui_support_model
        }

        # Construct a dict representation of a RuleTargetAttribute model
        rule_target_attribute_model = {
            'name': 'resource_id',
            'operator': 'string_equals',
            'value': 'f0f8f7994e754ff38f9d370201966561'
        }

        # Construct a dict representation of a TargetResource model
        target_resource_model = {
            'service_name': 'iam-groups',
            'resource_kind': 'zone',
            'additional_target_attributes': [rule_target_attribute_model]
        }

        # Construct a dict representation of a RuleRequiredConfigSingleProperty model
        rule_required_config_model = {
            'description': 'testString',
            'property': 'public_access_enabled',
            'operator': 'is_true',
            'value': 'testString'
        }

        # Construct a dict representation of a EnforcementAction model
        enforcement_action_model = {
            'action': 'disallow'
        }

        # Construct a dict representation of a RuleRequest model
        rule_request_model = {
            'account_id': 'testString',
            'name': 'testString',
            'description': 'testString',
            'version': '1.0.0',
            'rule_type': 'user_defined',
            'imports': [rule_import_model],
            'target': target_resource_model,
            'required_config': rule_required_config_model,
            'enforcement_actions': [enforcement_action_model],
            'labels': ['testString']
        }

        # Construct a dict representation of a CreateRuleRequest model
        create_rule_request_model = {
            'request_id': '3cebc877-58e7-44a5-a292-32114fa73558',
            'rule': rule_request_model
        }

        create_rules_response = self.configuration_governance_service.create_rules(
            rules=[create_rule_request_model],
            transaction_id='testString'
        )

        assert create_rules_response.get_status_code() == 201
        create_rules_response = create_rules_response.get_result()
        assert create_rules_response is not None

    @needscredentials
    def test_list_rules(self):

        list_rules_response = self.configuration_governance_service.list_rules(
            account_id='testString',
            transaction_id='testString',
            attached=True,
            labels='SOC2,ITCS300',
            scopes='scope_id',
            limit=1000,
            offset=38
        )

        assert list_rules_response.get_status_code() == 200
        rule_list = list_rules_response.get_result()
        assert rule_list is not None

    @needscredentials
    def test_get_rule(self):

        get_rule_response = self.configuration_governance_service.get_rule(
            rule_id='testString',
            transaction_id='testString'
        )

        assert get_rule_response.get_status_code() == 200
        rule = get_rule_response.get_result()
        assert rule is not None

    @needscredentials
    def test_update_rule(self):

        # Construct a dict representation of a RuleTargetAttribute model
        rule_target_attribute_model = {
            'name': 'resource_id',
            'operator': 'string_equals',
            'value': 'f0f8f7994e754ff38f9d370201966561'
        }

        # Construct a dict representation of a TargetResource model
        target_resource_model = {
            'service_name': 'iam-groups',
            'resource_kind': 'zone',
            'additional_target_attributes': [rule_target_attribute_model]
        }

        # Construct a dict representation of a RuleRequiredConfigSingleProperty model
        rule_required_config_model = {
            'description': 'testString',
            'property': 'public_access_enabled',
            'operator': 'is_true',
            'value': 'testString'
        }

        # Construct a dict representation of a EnforcementAction model
        enforcement_action_model = {
            'action': 'audit_log'
        }

        # Construct a dict representation of a UISupport model
        ui_support_model = {
            'display_name': 'testString',
            'description': 'testString'
        }

        # Construct a dict representation of a RuleImport model
        rule_import_model = {
            'name': 'testString',
            'ui_support': ui_support_model
        }

        update_rule_response = self.configuration_governance_service.update_rule(
            rule_id='testString',
            if_match='testString',
            name='Disable public access',
            description='Ensure that public access to account resources is disabled.',
            target={"service_name":"iam-groups","resource_kind":"service","additional_target_attributes":[]},
            required_config={"property":"public_access_enabled","operator":"is_false"},
            enforcement_actions=[enforcement_action_model],
            account_id='531fc3e28bfc43c5a2cea07786d93f5c',
            version='1.0.0',
            rule_type='user_defined',
            imports=[rule_import_model],
            labels=['testString'],
            transaction_id='testString'
        )

        assert update_rule_response.get_status_code() == 200
        rule = update_rule_response.get_result()
        assert rule is not None

    @needscredentials
    def test_create_attachments(self):

        # Construct a dict representation of a RuleScope model
        rule_scope_model = {
            'note': 'testString',
            'scope_id': 'testString',
            'scope_type': 'enterprise'
        }

        # Construct a dict representation of a AttachmentRequest model
        attachment_request_model = {
            'account_id': 'testString',
            'included_scope': rule_scope_model,
            'excluded_scopes': [rule_scope_model]
        }

        create_attachments_response = self.configuration_governance_service.create_attachments(
            rule_id='testString',
            attachments=[attachment_request_model],
            transaction_id='testString'
        )

        assert create_attachments_response.get_status_code() == 201
        create_attachments_response = create_attachments_response.get_result()
        assert create_attachments_response is not None

    @needscredentials
    def test_list_attachments(self):

        list_attachments_response = self.configuration_governance_service.list_attachments(
            rule_id='testString',
            transaction_id='testString',
            limit=1000,
            offset=38
        )

        assert list_attachments_response.get_status_code() == 200
        attachment_list = list_attachments_response.get_result()
        assert attachment_list is not None

    @needscredentials
    def test_get_attachment(self):

        get_attachment_response = self.configuration_governance_service.get_attachment(
            rule_id='testString',
            attachment_id='testString',
            transaction_id='testString'
        )

        assert get_attachment_response.get_status_code() == 200
        attachment = get_attachment_response.get_result()
        assert attachment is not None

    @needscredentials
    def test_update_attachment(self):

        # Construct a dict representation of a RuleScope model
        rule_scope_model = {
            'note': 'testString',
            'scope_id': 'testString',
            'scope_type': 'enterprise'
        }

        update_attachment_response = self.configuration_governance_service.update_attachment(
            rule_id='testString',
            attachment_id='testString',
            if_match='testString',
            account_id='testString',
            included_scope=rule_scope_model,
            excluded_scopes=[rule_scope_model],
            transaction_id='testString'
        )

        assert update_attachment_response.get_status_code() == 200
        attachment = update_attachment_response.get_result()
        assert attachment is not None

    @needscredentials
    def test_delete_rule(self):

        delete_rule_response = self.configuration_governance_service.delete_rule(
            rule_id='testString',
            transaction_id='testString'
        )

        assert delete_rule_response.get_status_code() == 204

    @needscredentials
    def test_delete_attachment(self):

        delete_attachment_response = self.configuration_governance_service.delete_attachment(
            rule_id='testString',
            attachment_id='testString',
            transaction_id='testString'
        )

        assert delete_attachment_response.get_status_code() == 204

