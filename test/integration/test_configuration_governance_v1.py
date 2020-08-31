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
import uuid
from ibm_cloud_sdk_core import *
from ibm_platform_services.configuration_governance_v1 import *

# Config file name
config_file = 'configuration_governance.env'
TEST_LABEL = 'PythonSDKIntegrationTest'
TRANSACTION_ID = str(uuid.uuid4())


class TestConfigurationGovernanceV1():
    """
    Integration Test Class for ConfigurationGovernanceV1
    """

    def init_sample_data(self):

        # Construct a dict representation of a RuleTargetAttribute model
        rule_target_attribute_model = {
            'name': 'resource_id',
            'operator': RuleTargetAttribute.OperatorEnum.IS_NOT_EMPTY
        }

        # Construct a dict representation of a TargetResource model
        target_resource_model = {
            'service_name': self.TEST_SERVICE_NAME,
            'resource_kind': 'bucket',
            'additional_target_attributes': [rule_target_attribute_model]
        }

        # Construct a dict representation of a RuleRequiredConfigSingleProperty model
        allowed_gb_condition = {
            'property': 'allowed_gb',
            'operator': RuleConditionSingleProperty.OperatorEnum.NUM_LESS_THAN_EQUALS,
            'value': '20'
        }

        # Construct a dict representation of a RuleRequiredConfigSingleProperty model
        location_condition = {
            'property': 'location',
            'operator': RuleConditionSingleProperty.OperatorEnum.STRING_EQUALS,
            'value': 'us-east'
        }

        # Construct a dict representation of a RuleRequiredConfigMultiplePropertiesConditionAnd model
        rule_required_config_model_1 = RuleRequiredConfigMultiplePropertiesConditionAnd(
            description = "allowed_gb<=20 && location=='us-east'",
            and_ = [allowed_gb_condition, location_condition]
        ).to_dict()

        # Construct a dict representation of a RuleRequiredConfigSingleProperty model
        rule_required_config_model_2 = {
            'description': "allowed_gb<=30",
            'property': 'allowed_gb',
            'operator': RuleRequiredConfigSingleProperty.OperatorEnum.NUM_LESS_THAN_EQUALS,
            'value': '30'
        }

        # Construct a dict representation of a EnforcementAction model
        enforcement_action_model = {
            'action': EnforcementAction.ActionEnum.DISALLOW
        }

        # Construct a dict representation of a RuleRequest model
        self.sample_rule_1 = {
            'account_id': self.ACCOUNT_ID,
            'name': 'Java Test Rule #1',
            'description': 'This is the description for Java Test Rule #1.',
            'rule_type': Rule.RuleTypeEnum.USER_DEFINED,
            'target': target_resource_model,
            'required_config': rule_required_config_model_1,
            'enforcement_actions': [enforcement_action_model],
            'labels': [TEST_LABEL]
        }

        # Construct a dict representation of a RuleRequest model
        self.sample_rule_2 = {
            'account_id': self.ACCOUNT_ID,
            'name': 'Java Test Rule #2',
            'description': 'This is the description for Java Test Rule #2.',
            'rule_type': Rule.RuleTypeEnum.USER_DEFINED,
            'target': target_resource_model,
            'required_config': rule_required_config_model_2,
            'enforcement_actions': [enforcement_action_model],
            'labels': [TEST_LABEL]
        }

        # Construct a dict representation of a RuleRequest model
        self.bad_sample_rule = {
            'account_id': self.ACCOUNT_ID,
            'name': 'Java Test Rule #2',
            'description': 'This is the description for Java Test Rule #2.',
            'rule_type': 'service_defined',
            'target': target_resource_model,
            'required_config': rule_required_config_model_2,
            'enforcement_actions': [enforcement_action_model],
            'labels': [TEST_LABEL]
        }

        # Sample rule scopes
        self.enterprise_scope = {
            'note': 'enterprise',
            'scope_id': self.ENTERPRISE_SCOPE_ID,
            'scope_type': 'enterprise'
        }

        self.account_scope = {
            'note': 'leaf account',
            'scope_id': self.SUBACCT_SCOPE_ID,
            'scope_type': 'enterprise.account'
        }

        self.bad_scope = {
            'note': 'leaf account',
            'scope_id': self.SUBACCT_SCOPE_ID,
            'scope_type': 'enterprise.BOGUS'
        }

    # Helper function to clean rules
    def clean_rules(self, label):
        print("Cleaning rules...");
    
        list_rules_response = self.service.list_rules(
            account_id=self.ACCOUNT_ID,
            labels=label,
            limit=1000,
            offset=0
        )

        assert list_rules_response.get_status_code() == 200
        rule_list = list_rules_response.get_result()
        assert rule_list is not None

        print("Found %d rule(s) to be cleaned" % rule_list['total_count'])

        # Now walk through the returned rules and delete each one.
        if rule_list['total_count'] > 0:
            for rule in rule_list['rules']:
                print("Deleting rule: name='%s' id='%s'" % (rule['name'], rule['rule_id']))
                delete_rule_response = self.service.delete_rule(
                    rule_id=rule['rule_id']
                )
                assert delete_rule_response.get_status_code() == 204
        print("Finished cleaning rules...")

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # Construct the service client.
            cls.service = ConfigurationGovernanceV1.new_instance()
            assert cls.service is not None
            assert cls.service.service_url is not None

            # Construct a separate service client for some negative tests.
            # This service has an apikey that lacks the necessary access to create or list rules, etc.
            cls.service_no_access = ConfigurationGovernanceV1.new_instance("NO_ACCESS");
            assert cls.service_no_access is not None
            assert cls.service_no_access.service_url is not None

            # Load up our test-specific config properties.
            cls.config = read_external_sources(ConfigurationGovernanceV1.DEFAULT_SERVICE_NAME);
            assert cls.config is not None
            assert cls.config["URL"] == cls.service.service_url

            # Retrieve and verify some additional test-related config properties.
            cls.ACCOUNT_ID = cls.config.get("ACCOUNT_ID");
            cls.TEST_SERVICE_NAME = cls.config.get("TEST_SERVICE_NAME");
            cls.ENTERPRISE_SCOPE_ID = cls.config.get("ENTERPRISE_SCOPE_ID");
            cls.SUBACCT_SCOPE_ID = cls.config.get("SUBACCT_SCOPE_ID");
            assert cls.ACCOUNT_ID is not None
            assert cls.TEST_SERVICE_NAME is not None
            assert cls.ENTERPRISE_SCOPE_ID is not None
            assert cls.SUBACCT_SCOPE_ID is not None

            print("Service URL: " + cls.service.service_url)
            print("Transaction ID: " + TRANSACTION_ID)

            # Clean any existing test rules before we start the actual tests.
            cls.clean_rules(cls, TEST_LABEL)

            # Create some sample model instances that we'll use when invoking the operations.
            cls.init_sample_data(cls)

        print('Setup complete.')

    @classmethod 
    def teardown_class(cls):
        print("Starting clean up...");
        cls.clean_rules(cls, TEST_LABEL);
        print("Clean up complete.");

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    def get_rule(self, rule_id):
        get_rule_response = self.service.get_rule(
            rule_id=rule_id,
            transaction_id=TRANSACTION_ID
        )
        assert get_rule_response.get_status_code() == 200
        return get_rule_response.get_result()

    def get_attachment(self, rule_id, attachment_id):
        get_attachment_response = self.service.get_attachment(
            rule_id=rule_id,
            attachment_id=attachment_id
        )
        assert get_rule_response.get_status_code() == 200
        return get_rule_response.get_result()

    @needscredentials
    def test_create_rule_1(self):

        # Construct a dict representation of a CreateRuleRequest model
        create_rule_request_model = {
            'request_id': 'request-0',
            'rule': self.sample_rule_1
        }

        create_rules_response = self.service.create_rules(
            rules=[create_rule_request_model],
            transaction_id=TRANSACTION_ID
        )

        assert create_rules_response.get_status_code() == 201
        create_rules_response = create_rules_response.get_result()
        assert create_rules_response is not None

        global RULE_ID_1
        RULE_ID_1 = create_rules_response['rules'][0]['rule']['rule_id']
        assert RULE_ID_1 is not None

    @needscredentials
    def test_create_rule_2(self):

        # Construct a dict representation of a CreateRuleRequest model
        create_rule_request_model = {
            'request_id': 'request-0',
            'rule': self.sample_rule_2
        }

        create_rules_response = self.service.create_rules(
            rules=[create_rule_request_model],
            transaction_id=TRANSACTION_ID
        )

        assert create_rules_response.get_status_code() == 201
        create_rules_response = create_rules_response.get_result()
        assert create_rules_response is not None

        global RULE_ID_2
        RULE_ID_2 = create_rules_response['rules'][0]['rule']['rule_id']
        assert RULE_ID_2 is not None

    @needscredentials
    def test_create_rule_invalid_rule(self):

        # Construct a dict representation of a CreateRuleRequest model
        create_rule_request_model = {
            'request_id': 'request-1',
            'rule': self.bad_sample_rule
        }

        create_rules_response = self.service.create_rules(
            rules=[create_rule_request_model],
            transaction_id=TRANSACTION_ID
        )

        assert create_rules_response.get_status_code() == 207
        create_rules_response = create_rules_response.get_result()
        assert create_rules_response is not None

        rule_response = create_rules_response['rules'][0]
        assert rule_response['request_id'] == 'request-1'
        assert rule_response['status_code'] == 400
        assert rule_response['trace'] == TRANSACTION_ID
        assert len(rule_response['errors']) > 0
        assert rule_response['errors'][0]['code'] == 'rule_error'

    @needscredentials
    def test_create_rule_no_access(self):

        try:
            # Construct a dict representation of a CreateRuleRequest model
            create_rule_request_model = {
                'request_id': 'request-1',
                'rule': self.sample_rule_1
            }

            create_rules_response = self.service_no_access.create_rules(
                rules=[create_rule_request_model],
                transaction_id=TRANSACTION_ID
            )
            pytest.fail(msg='Using a no-access apikey should not have succeeded!')
        except ApiException as e:
            assert e.code == 403
            assert e.message == 'The token is not authorized to perform the operation'

    @needscredentials
    def test_list_rules(self):
    
        list_rules_response = self.service.list_rules(
            account_id=self.ACCOUNT_ID,
            transaction_id=TRANSACTION_ID,
            labels=TEST_LABEL,
            limit=1000,
            offset=0
        )

        assert list_rules_response.get_status_code() == 200
        rule_list = list_rules_response.get_result()
        assert rule_list is not None

        assert rule_list['total_count'] == 2
        assert rule_list['offset'] == 0
        assert rule_list['limit'] == 1000
        assert rule_list['first'] is not None
        assert rule_list['last'] is not None

    @needscredentials
    def test_list_rules_no_access(self):
        try:
            list_rules_response = self.service_no_access.list_rules(
                account_id=self.ACCOUNT_ID,
                transaction_id=TRANSACTION_ID,
                labels=TEST_LABEL,
                limit=1000,
                offset=0
            )
            pytest.fail(msg='Using a no-access apikey should not have succeeded!')
        except ApiException as e:
            assert e.code == 403
            assert e.message == 'The token is not authorized to perform the operation'

    @needscredentials
    def test_get_rule(self):

        get_rule_response = self.service.get_rule(
            rule_id=RULE_ID_1,
            transaction_id=TRANSACTION_ID
        )

        assert get_rule_response.get_status_code() == 200
        global RULE_1
        RULE_1 = get_rule_response.get_result()
        assert RULE_1 is not None

        # Grab the Etag value from the response for use in the update operation.
        assert get_rule_response.get_headers()['Etag'] is not None
        global RULE_ETAG_1
        RULE_ETAG_1 = get_rule_response.get_headers()['Etag']

    @needscredentials
    def test_get_rule_invalid_rule_id(self):
        try:
            get_rule_response = self.service.get_rule(
                rule_id="BOGUS_ID",
                transaction_id=TRANSACTION_ID
            )
            pytest.fail(msg="Invalid get should not have succeeded!")
        except ApiException as e:
            assert e.code == 404
            assert e.message == "The requested resource was not found"

    @needscredentials
    def test_update_rule(self):

        assert RULE_1 is not None
        assert RULE_ID_1 is not None
        assert RULE_ETAG_1 is not None

        # Starting with "rule1" (result of a get), modify the description, then call the update operation.
        update_rule_response = self.service.update_rule(
            rule_id=RULE_ID_1,
            if_match=RULE_ETAG_1,
            name=RULE_1['name'],
            description="Updated: " + RULE_1['description'],
            target=RULE_1['target'],
            required_config=RULE_1['required_config'],
            enforcement_actions=RULE_1['enforcement_actions'],
            account_id=RULE_1['account_id'],
            rule_type=RULE_1['rule_type'],
            labels=RULE_1['labels'],
            transaction_id=TRANSACTION_ID
        )

        assert update_rule_response.get_status_code() == 200
        rule = update_rule_response.get_result()
        assert rule is not None
        assert rule['description'].startswith("Updated: ")

    @needscredentials
    def test_update_rule_invalid_etag(self):

        try:
            assert RULE_1 is not None
            assert RULE_ID_1 is not None
            assert RULE_ETAG_1 is not None

            # Starting with "rule1" (result of a get), modify the description, then call the update operation.
            update_rule_response = self.service.update_rule(
                rule_id=RULE_ID_1,
                if_match=RULE_ETAG_1 + "just-foolin'",
                name=RULE_1['name'],
                description="Updated: " + RULE_1['description'],
                target=RULE_1['target'],
                required_config=RULE_1['required_config'],
                enforcement_actions=RULE_1['enforcement_actions'],
                account_id=RULE_1['account_id'],
                rule_type=RULE_1['rule_type'],
                labels=RULE_1['labels'],
                transaction_id=TRANSACTION_ID
            )
            pytest.fail(msg='Using an invalid etag should not have succeeded!')
        except ApiException as e:
            assert e.code == 400
            assert e.message == 'The provided If-Match value is malformed'

    @needscredentials
    def test_delete_rule(self):

        assert RULE_ID_2 is not None

        delete_rule_response = self.service.delete_rule(
            rule_id=RULE_ID_2,
            transaction_id=TRANSACTION_ID
        )

        assert delete_rule_response.get_status_code() == 204
    
        # Now check to make sure listRules() returns only 1 rule.
        list_rules_response = self.service.list_rules(
            account_id=self.ACCOUNT_ID,
            transaction_id=TRANSACTION_ID,
            labels=TEST_LABEL,
            limit=1000,
            offset=0
        )

        assert list_rules_response.get_status_code() == 200
        rule_list = list_rules_response.get_result()
        assert rule_list is not None

        assert rule_list['total_count'] == 1

        try:
            rule = self.get_rule(RULE_ID_2)
            pytest.fail(msg="Getting a non-existant rule should not have succeeded!")
        except ApiException as e:
            assert e.code == 404
            assert e.message == "The requested resource was not found"


    @needscredentials
    def test_delete_rule_invalid_rule_id(self):
        try:
            delete_rule_response = self.service.delete_rule(
                rule_id="BOGUS_RULE_ID",
                transaction_id=TRANSACTION_ID
            )
            pytest.fail(msg="Invalid delete should not have succeeded!")
        except ApiException as e:
            assert e.code == 404
            assert e.message == "The requested resource was not found"

    @needscredentials
    def test_create_attachment_1(self):

        assert RULE_ID_1 is not None

        # Construct a dict representation of a AttachmentRequest model
        attachment_request_model = {
            'account_id': self.ACCOUNT_ID,
            'included_scope': self.enterprise_scope,
            'excluded_scopes': [self.account_scope]
        }

        create_attachments_response = self.service.create_attachments(
            rule_id=RULE_ID_1,
            attachments=[attachment_request_model],
            transaction_id=TRANSACTION_ID
        )

        assert create_attachments_response.get_status_code() == 201
        create_attachments_response = create_attachments_response.get_result()
        assert create_attachments_response is not None

        assert len(create_attachments_response['attachments']) == 1
        assert create_attachments_response['attachments'][0] is not None
        global ATTACHMENT_ID_1
        ATTACHMENT_ID_1 = create_attachments_response['attachments'][0]['attachment_id']
        assert ATTACHMENT_ID_1 is not None

        rule = self.get_rule(RULE_ID_1)
        assert rule is not None
        assert rule['number_of_attachments'] == 1

    @needscredentials
    def test_create_attachment_2(self):

        assert RULE_ID_1 is not None

        # Construct a dict representation of a AttachmentRequest model
        attachment_request_model = {
            'account_id': self.ACCOUNT_ID,
            'included_scope': self.account_scope
        }

        create_attachments_response = self.service.create_attachments(
            rule_id=RULE_ID_1,
            attachments=[attachment_request_model],
            transaction_id=TRANSACTION_ID
        )

        assert create_attachments_response.get_status_code() == 201
        create_attachments_response = create_attachments_response.get_result()
        assert create_attachments_response is not None

        assert len(create_attachments_response['attachments']) == 1
        assert create_attachments_response['attachments'][0] is not None
        global ATTACHMENT_ID_2
        ATTACHMENT_ID_2 = create_attachments_response['attachments'][0]['attachment_id']
        assert ATTACHMENT_ID_2 is not None

        rule = self.get_rule(RULE_ID_1)
        assert rule is not None
        assert rule['number_of_attachments'] == 2


    @needscredentials
    def test_create_attachment_invalid_scope_type(self):
        try:
            assert RULE_ID_1 is not None

            # Construct a dict representation of a AttachmentRequest model
            attachment_request_model = {
                'account_id': self.ACCOUNT_ID,
                'included_scope': self.enterprise_scope,
                'excluded_scopes': [self.bad_scope]
            }

            create_attachments_response = self.service.create_attachments(
                rule_id=RULE_ID_1,
                attachments=[attachment_request_model],
                transaction_id=TRANSACTION_ID
            )
            pytest.fail(msg="Invalid attachment should not have succeeded!")
        except ApiException as e:
            assert e.code == 400
            assert e.message == "attachment[0]: The excluded scope at index 0 is not a descendant of the included scope."

    @needscredentials
    def test_get_attachment(self):

        assert RULE_ID_1 is not None
        assert ATTACHMENT_ID_1 is not None

        get_attachment_response = self.service.get_attachment(
            rule_id=RULE_ID_1,
            attachment_id=ATTACHMENT_ID_1
        )

        assert get_attachment_response.get_status_code() == 200
        global ATTACHMENT_1
        ATTACHMENT_1 = get_attachment_response.get_result()
        assert ATTACHMENT_1 is not None

        assert ATTACHMENT_1['account_id'] == self.ACCOUNT_ID
        assert ATTACHMENT_1['rule_id'] == RULE_ID_1
        assert ATTACHMENT_1['attachment_id'] == ATTACHMENT_ID_1
        assert ATTACHMENT_1['included_scope']['note'] == 'enterprise'
        assert len(ATTACHMENT_1['excluded_scopes']) == 1

        # Grab the Etag value from the response for use in the update operation.
        assert get_attachment_response.get_headers()['Etag'] is not None
        global ATTACHMENT_ETAG_1
        ATTACHMENT_ETAG_1 = get_attachment_response.get_headers()['Etag']
        assert ATTACHMENT_ETAG_1 is not None

    @needscredentials
    def test_get_attachment_invalid_attachment_id(self):
        try:
            assert RULE_ID_1 is not None
            assert ATTACHMENT_ID_1 is not None

            get_attachment_response = self.service.get_attachment(
                rule_id=RULE_ID_1,
                attachment_id="BOGUS_ID"
            )
            pytest.fail(msg="Invalid attachment id should not have succeeded!")
        except ApiException as e:
            assert e.code == 404
            assert e.message == "The requested resource was not found"

    @needscredentials
    def test_list_attachments(self):

        list_attachments_response = self.service.list_attachments(
            rule_id=RULE_ID_1,
            transaction_id=TRANSACTION_ID,
            limit=1000,
            offset=0
        )

        assert list_attachments_response.get_status_code() == 200
        attachment_list = list_attachments_response.get_result()
        assert attachment_list is not None

        assert attachment_list['offset'] == 0
        assert attachment_list['limit'] == 1000
        assert attachment_list['total_count'] == 2
        assert attachment_list['first'] is not None
        assert attachment_list['last'] is not None
        for att in attachment_list['attachments']:
            if att['attachment_id'] == ATTACHMENT_ID_1:
                assert att['included_scope']['note'] == 'enterprise'
                assert len(att['excluded_scopes']) == 1
            elif att['attachment_id'] == ATTACHMENT_ID_2:
                assert att['included_scope']['note'] == 'leaf account'
                assert len(att['excluded_scopes']) == 0
            else:
                pytest.fail(msg="Unrecognized attachmentId: " + att['attachment_id'])

    @needscredentials
    def test_update_attachment(self):

        assert RULE_ID_1 is not None
        assert ATTACHMENT_1 is not None
        assert ATTACHMENT_ETAG_1 is not None

        # Construct a dict representation of a RuleScope model
        rule_scope_model = {
            'note': "Updated: " + ATTACHMENT_1['included_scope']['note'],
            'scope_id': ATTACHMENT_1['included_scope']['scope_id'],
            'scope_type': ATTACHMENT_1['included_scope']['scope_type']
        }

        update_attachment_response = self.service.update_attachment(
            rule_id=ATTACHMENT_1['rule_id'],
            attachment_id=ATTACHMENT_1['attachment_id'],
            if_match=ATTACHMENT_ETAG_1,
            account_id=ATTACHMENT_1['account_id'],
            included_scope=rule_scope_model,
            excluded_scopes=ATTACHMENT_1['excluded_scopes'],
            transaction_id=TRANSACTION_ID
        )

        assert update_attachment_response.get_status_code() == 200
        attachment = update_attachment_response.get_result()
        assert attachment is not None

        assert attachment['included_scope'] is not None
        assert attachment['included_scope']['note'].startswith('Updated:')

    @needscredentials
    def test_update_attachment_invalid_etag(self):
        try:
            assert RULE_ID_1 is not None
            assert ATTACHMENT_1 is not None
            assert ATTACHMENT_ETAG_1 is not None

            # Construct a dict representation of a RuleScope model
            rule_scope_model = {
                'note': "Updated: " + ATTACHMENT_1['included_scope']['note'],
                'scope_id': ATTACHMENT_1['included_scope']['scope_id'],
                'scope_type': ATTACHMENT_1['included_scope']['scope_type']
            }

            update_attachment_response = self.service.update_attachment(
                rule_id=ATTACHMENT_1['rule_id'],
                attachment_id=ATTACHMENT_1['attachment_id'],
                if_match="BOGUS_ETAG",
                account_id=ATTACHMENT_1['account_id'],
                included_scope=rule_scope_model,
                excluded_scopes=ATTACHMENT_1['excluded_scopes'],
                transaction_id=TRANSACTION_ID
            )
            pytest.fail(msg="Invalid update should not have succeeded!")
        except ApiException as e:
            assert e.code == 400
            assert e.message == "The provided If-Match value is malformed"

    @needscredentials
    def test_delete_attachment(self):

        assert RULE_ID_1 is not None
        assert ATTACHMENT_ID_2 is not None

        delete_attachment_response = self.service.delete_attachment(
            rule_id=RULE_ID_1,
            attachment_id=ATTACHMENT_ID_2,
            transaction_id=TRANSACTION_ID
        )

        assert delete_attachment_response.get_status_code() == 204


        list_attachments_response = self.service.list_attachments(
            rule_id=RULE_ID_1,
            transaction_id=TRANSACTION_ID,
            limit=1000,
            offset=0
        )

        assert list_attachments_response.get_status_code() == 200
        attachment_list = list_attachments_response.get_result()
        assert attachment_list is not None

        assert attachment_list['total_count'] == 1

        try:
            attachment = self.get_attachment(RULE_ID_1, ATTACHMENT_ID_2)
            pytest.fail(msg="Getting a non-existant attachment should not have succeeded!")
        except ApiException as e:
            assert e.code == 404
            assert e.message == "The requested resource was not found"
