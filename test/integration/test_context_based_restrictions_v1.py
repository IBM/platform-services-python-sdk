# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2022.
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
Integration Tests for ContextBasedRestrictionsV1
"""

import os
import uuid

import pytest
from ibm_cloud_sdk_core import *
from ibm_platform_services.context_based_restrictions_v1 import *

# Config file name
config_file = 'context_based_restrictions_v1.env'


class TestContextBasedRestrictionsV1():
    """
    Integration Test Class for ContextBasedRestrictionsV1
    """

    test_account_id = None
    service_name = None
    zone_id = None
    zone_rev = None
    rule_id = None
    rule_rev = None

    NonExistentID = "1234567890abcdef1234567890abcdef"
    InvalidID = "this_is_an_invalid_id"

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.context_based_restrictions_service = ContextBasedRestrictionsV1.new_instance()
            assert cls.context_based_restrictions_service is not None

            cls.config = read_external_sources(
                ContextBasedRestrictionsV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.context_based_restrictions_service.enable_retries()

            TestContextBasedRestrictionsV1.test_account_id = cls.config['TEST_ACCOUNT_ID']
            TestContextBasedRestrictionsV1.service_name = cls.config['TEST_SERVICE_NAME']

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_zone(self):
        # Construct a dict representation of a AddressIPAddress model
        ip_address_model = {
            'type': 'ipAddress',
            'value': '169.23.56.234',
        }

        # Construct a dict representation of a AddressServiceRef model
        service_ref_address_model = {
            'type': 'serviceRef',
            'ref': {
                'account_id': TestContextBasedRestrictionsV1.test_account_id,
                'service_name': 'containers-kubernetes',
                'location': 'us-south',
            },
        }

        create_zone_response = self.context_based_restrictions_service.create_zone(
            name='SDK TEST - an example of zone',
            account_id=TestContextBasedRestrictionsV1.test_account_id,
            addresses=[ip_address_model, service_ref_address_model],
            description='SDK TEST - this is an example of zone',
            transaction_id=self.getTransactionID()
        )

        assert create_zone_response.get_status_code() == 201
        zone = create_zone_response.get_result()
        assert zone is not None
        TestContextBasedRestrictionsV1.zone_id = zone['id']

    @needscredentials
    def test_create_zone_with_duplicated_name_error(self):
        # Construct a dict representation of a AddressIPAddress model
        address_model = {
            'type': 'ipAddress',
            'value': '169.23.56.234',
        }

        with pytest.raises(ApiException, match="409"):
            self.context_based_restrictions_service.create_zone(
                name='SDK TEST - an example of zone',
                account_id=TestContextBasedRestrictionsV1.test_account_id,
                addresses=[address_model],
                description='SDK TEST - this is an example of zone',
                transaction_id=self.getTransactionID()
                 )


    @needscredentials
    def test_create_zone_with_invalid_ip_address_format_error(self):
        # Construct a dict representation of a AddressIPAddress model
        address_model = {
            'type': 'ipAddress',
            'value': '16.923.562.34',
        }
        with pytest.raises(ApiException, match="400"):
             self.context_based_restrictions_service.create_zone(
                name='SDK TEST - an example of zone',
                account_id=TestContextBasedRestrictionsV1.test_account_id,
                addresses=[address_model],
                description='SDK TEST - this is an example of zone',
                transaction_id=self.getTransactionID()
            )



    @needscredentials
    def test_list_zones(self):
        list_zones_response = self.context_based_restrictions_service.list_zones(
            account_id=TestContextBasedRestrictionsV1.test_account_id,
            transaction_id=self.getTransactionID(),
        )

        assert list_zones_response.get_status_code() == 200
        zone_list = list_zones_response.get_result()
        assert zone_list is not None

    @needscredentials
    def test_list_zones_with_invalid_account_id_parameter_error(self):
        with pytest.raises(ApiException, match="400"):
             self.context_based_restrictions_service.list_zones(
                account_id= self.InvalidID,
                transaction_id=self.getTransactionID(),
            )

    @needscredentials
    def test_get_zone(self):
        get_zone_response = self.context_based_restrictions_service.get_zone(
            zone_id=TestContextBasedRestrictionsV1.zone_id,
            transaction_id=self.getTransactionID()
        )

        assert get_zone_response.get_status_code() == 200
        zone = get_zone_response.get_result()
        assert zone is not None
        TestContextBasedRestrictionsV1.zone_rev = get_zone_response.headers.get('ETag')

    @needscredentials
    def test_get_zone_with_zone_not_found_error(self):
        with pytest.raises(ApiException, match="404"):
             self.context_based_restrictions_service.get_zone(
                zone_id=self.NonExistentID,
                transaction_id=self.getTransactionID()
            )


    @needscredentials
    def test_replace_zone(self):
        # Construct a dict representation of a AddressIPAddress model
        address_model = {
            'type': 'ipAddress',
            'value': '169.23.56.234',
        }

        replace_zone_response = self.context_based_restrictions_service.replace_zone(
            zone_id=TestContextBasedRestrictionsV1.zone_id,
            if_match=TestContextBasedRestrictionsV1.zone_rev,
            name='SDK TEST - an example of updated zone',
            account_id=TestContextBasedRestrictionsV1.test_account_id,
            addresses=[address_model],
            description='SDK TEST - this is an example of updated zone',
            transaction_id=self.getTransactionID()
        )

        assert replace_zone_response.get_status_code() == 200
        zone = replace_zone_response.get_result()
        assert zone is not None

    @needscredentials
    def test_replace_zone_update_zone_with_zone_not_found_error(self):
        # Construct a dict representation of a AddressIPAddress model
        address_model = {
            'type': 'ipAddress',
            'value': '169.23.56.234',
        }

        with pytest.raises(ApiException, match="404"):
             self.context_based_restrictions_service.replace_zone(
                zone_id=self.NonExistentID,
                if_match=TestContextBasedRestrictionsV1.zone_rev,
                name='SDK TEST - an example of updated zone',
                account_id=TestContextBasedRestrictionsV1.test_account_id,
                addresses=[address_model],
                description='SDK TEST - this is an example of updated zone',
                transaction_id=self.getTransactionID()
            )

    @needscredentials
    def test_replace_zone_update_zone_with_invalid_if_match_parameter_error(self):
        # Construct a dict representation of a AddressIPAddress model
        address_model = {
            'type': 'ipAddress',
            'value': '169.23.56.234',
        }

        with pytest.raises(ApiException, match="412"):
            self.context_based_restrictions_service.replace_zone(
                zone_id=TestContextBasedRestrictionsV1.zone_id,
                if_match="abc",
                name='SDK TEST - an example of updated zone',
                account_id=TestContextBasedRestrictionsV1.test_account_id,
                addresses=[address_model],
                description='SDK TEST - this is an example of updated zone',
                transaction_id=self.getTransactionID()
            )

    @needscredentials
    def test_list_available_serviceref_targets(self):
        list_available_serviceref_targets_response = self.context_based_restrictions_service.list_available_serviceref_targets(
            type='all'
        )

        assert list_available_serviceref_targets_response.get_status_code() == 200
        service_ref_target_list = list_available_serviceref_targets_response.get_result()
        assert service_ref_target_list is not None

    @needscredentials
    def test_list_available_serviceref_targets_list_with_invalid_type_parameter_error(self):
        with pytest.raises(ApiException, match="400"):
         self.context_based_restrictions_service.list_available_serviceref_targets(
            type='invalid-type'
        )

    @needscredentials
    def test_create_rule(self):
        # Construct a dict representation of a RuleContextAttribute model
        rule_context_attribute_model = {
            'name': 'networkZoneId',
            'value': TestContextBasedRestrictionsV1.zone_id,
        }

        # Construct a dict representation of a RuleContext model
        rule_context_model = {
            'attributes': [rule_context_attribute_model],
        }

        # Construct a dict representation of a ResourceAttribute model
        account_id_resource_attribute_model = {
            'name': 'accountId',
            'value': TestContextBasedRestrictionsV1.test_account_id,
        }

        service_name_resource_attribute_model = {
            'name': 'serviceName',
            'value': TestContextBasedRestrictionsV1.service_name,
        }

        # Construct a dict representation of a Resource model
        resource_model = {
            'attributes': [account_id_resource_attribute_model, service_name_resource_attribute_model],
        }

        create_rule_response = self.context_based_restrictions_service.create_rule(
            contexts=[rule_context_model],
            resources=[resource_model],
            description='SDK TEST - this is an example of rule',
            enforcement_mode='enabled',
            transaction_id=self.getTransactionID()
        )

        assert create_rule_response.get_status_code() == 201
        rule = create_rule_response.get_result()
        assert rule is not None
        TestContextBasedRestrictionsV1.rule_id = rule['id']

    @needscredentials
    def test_create_rule_with_api_types(self):
        # Construct a dict representation of a RuleContextAttribute model
        rule_context_attribute_model = {
            'name': 'networkZoneId',
            'value': TestContextBasedRestrictionsV1.zone_id,
        }

        # Construct a dict representation of a RuleContext model
        rule_context_model = {
            'attributes': [rule_context_attribute_model],
        }

        # Construct a dict representation of a ResourceAttribute model
        account_id_resource_attribute_model = {
            'name': 'accountId',
            'value': TestContextBasedRestrictionsV1.test_account_id,
        }

        service_name_resource_attribute_model = {
            'name': 'serviceName',
            'value': 'containers-kubernetes',
        }

        # Construct a dict representation of a Resource model
        resource_model = {
            'attributes': [account_id_resource_attribute_model, service_name_resource_attribute_model],
        }

        # Construct a dict representation of a NewRuleOperationsApiTypesItem model
        api_type_model = {
            'api_type_id': 'crn:v1:bluemix:public:containers-kubernetes::::api-type:management'
        }

        # Construct a dict representation of a NewRuleOperations model
        operations_model = {
            'api_types': [api_type_model]
        }

        create_rule_response = self.context_based_restrictions_service.create_rule(
            contexts=[rule_context_model],
            resources=[resource_model],
            operations=operations_model,
            description='SDK TEST - this is an example of rule',
            enforcement_mode='enabled',
            transaction_id=self.getTransactionID()
        )

        assert create_rule_response.get_status_code() == 201
        rule = create_rule_response.get_result()
        assert rule is not None

        # cleanup
        delete_rule_response = self.context_based_restrictions_service.delete_rule(
            rule_id=rule['id'],
            # Using the standard X-Correlation-Id header in this case
            x_correlation_id=self.getTransactionID()
        )

        assert delete_rule_response.get_status_code() == 204

    @needscredentials
    def test_create_rule_with_service_not_cbr_enabled_error(self):
        # Construct a dict representation of a RuleContextAttribute model
        rule_context_attribute_model = {
            'name': 'networkZoneId',
            'value': TestContextBasedRestrictionsV1.zone_id,
        }

        # Construct a dict representation of a RuleContext model
        rule_context_model = {
            'attributes': [rule_context_attribute_model],
        }

        # Construct a dict representation of a ResourceAttribute model
        account_id_resource_attribute_model = {
            'name': 'accountId',
            'value': TestContextBasedRestrictionsV1.test_account_id,
        }

        service_name_resource_attribute_model = {
            'name': 'serviceName',
            'value': "cbr-not-enabled",
        }

        # Construct a dict representation of a Resource model
        resource_model = {
            'attributes': [account_id_resource_attribute_model, service_name_resource_attribute_model],
        }

        with pytest.raises(ApiException, match="400"):
            self.context_based_restrictions_service.create_rule(
                contexts=[rule_context_model],
                resources=[resource_model],
                description='SDK TEST - this is an example of rule',
                enforcement_mode='enabled',
                transaction_id=self.getTransactionID()
            )


    @needscredentials
    def test_list_rules(self):
        list_rules_response = self.context_based_restrictions_service.list_rules(
            account_id=TestContextBasedRestrictionsV1.test_account_id,
            transaction_id=self.getTransactionID(),
        )

        assert list_rules_response.get_status_code() == 200
        rule_list = list_rules_response.get_result()
        assert rule_list is not None

    @needscredentials
    def list_rules_with_missing_required_account_id_parameter_error(self):
        with pytest.raises(ApiException, match="404"):
            self.context_based_restrictions_service.list_rules(
                transaction_id=self.getTransactionID(),
            )

    @needscredentials
    def list_rules_with_invalid_account_id_parameter_error(self):
        with pytest.raises(ApiException, match="400"):
             self.context_based_restrictions_service.list_rules(
                account_id=self.InvalidID,
                transaction_id=self.getTransactionID(),
            )
            
    @needscredentials
    def test_list_rule_with_service_group_id(self):
        # Construct a dict representation of a RuleContextAttribute model
        rule_context_attribute_model = {
            'name': 'networkZoneId',
            'value': TestContextBasedRestrictionsV1.zone_id,
        }

        # Construct a dict representation of a RuleContext model
        rule_context_model = {
            'attributes': [rule_context_attribute_model],
        }

        # Construct a dict representation of a ResourceAttribute model
        account_id_resource_attribute_model = {
            'name': 'accountId',
            'value': TestContextBasedRestrictionsV1.test_account_id,
        }

        service_group_id_resource_attribute_model = {
            'name': 'service_group_id',
            'value': 'IAM',
        }

        # Construct a dict representation of a Resource model
        resource_model = {
            'attributes': [account_id_resource_attribute_model, service_group_id_resource_attribute_model],
        }

        create_rule_response = self.context_based_restrictions_service.create_rule(
            contexts=[rule_context_model],
            resources=[resource_model],
            description='SDK TEST - this is an example of rule with a service group id',
            enforcement_mode='enabled',
            transaction_id=self.getTransactionID()
        )

        assert create_rule_response.get_status_code() == 201
        rule = create_rule_response.get_result()
        assert rule is not None
        TestContextBasedRestrictionsV1.rule_id = rule['id']

        list_rules_response = self.context_based_restrictions_service.list_rules(
            service_group_id='IAM',
            transaction_id=self.getTransactionID(),
        )

        assert list_rules_response.get_status_code() == 200
        rule_list = list_rules_response.get_result()
        assert rule_list is not None
        assert rule_list['total_count'] == 1
        assert rule['id'] == rule_list['first'].id

        delete_rule_response = self.context_based_restrictions_service.delete_rule(
            rule_id=TestContextBasedRestrictionsV1.rule_id,
            # Using the standard X-Correlation-Id header in this case
            x_correlation_id=self.getTransactionID()
        )

        assert delete_rule_response.get_status_code() == 204

    @needscredentials
    def test_get_rule(self):
        get_rule_response = self.context_based_restrictions_service.get_rule(
            rule_id=TestContextBasedRestrictionsV1.rule_id,
            transaction_id=self.getTransactionID()
        )

        assert get_rule_response.get_status_code() == 200
        rule = get_rule_response.get_result()
        assert rule is not None
        TestContextBasedRestrictionsV1.rule_rev = get_rule_response.headers.get("ETag")

    @needscredentials
    def test_get_rule_with_rule_not_found_error(self):
        with pytest.raises(ApiException, match="404"):
             self.context_based_restrictions_service.get_rule(
                rule_id=self.NonExistentID,
                transaction_id=self.getTransactionID()
            )

    @needscredentials
    def test_replace_rule(self):
        # Construct a dict representation of a RuleContextAttribute model
        rule_context_attribute_model = {
            'name': 'networkZoneId',
            'value': TestContextBasedRestrictionsV1.zone_id,
        }

        # Construct a dict representation of a RuleContext model
        rule_context_model = {
            'attributes': [rule_context_attribute_model],
        }

        # Construct a dict representation of a ResourceAttribute model
        account_id_resource_attribute_model = {
            'name': 'accountId',
            'value': TestContextBasedRestrictionsV1.test_account_id,
        }

        service_name_resource_attribute_model = {
            'name': 'serviceName',
            'value': TestContextBasedRestrictionsV1.service_name,
        }

        # Construct a dict representation of a ResourceTagAttribute model
        resource_tag_attribute_model = {
            'name': 'tagName',
            'value': 'tagValue',
        }

        # Construct a dict representation of a Resource model
        resource_model = {
            'attributes': [account_id_resource_attribute_model, service_name_resource_attribute_model],
            'tags': [resource_tag_attribute_model],
        }

        replace_rule_response = self.context_based_restrictions_service.replace_rule(
            rule_id=TestContextBasedRestrictionsV1.rule_id,
            if_match=TestContextBasedRestrictionsV1.rule_rev,
            contexts=[rule_context_model],
            resources=[resource_model],
            description='SDK TEST - this is an example of updated rule',
            enforcement_mode='disabled',
            transaction_id=self.getTransactionID()
        )

        assert replace_rule_response.get_status_code() == 200
        rule = replace_rule_response.get_result()
        assert rule is not None

    @needscredentials
    def test_replace_rule_update_rule_with_rule_not_found_error(self):
        # Construct a dict representation of a RuleContextAttribute model
        rule_context_attribute_model = {
            'name': 'networkZoneId',
            'value': TestContextBasedRestrictionsV1.zone_id,
        }

        # Construct a dict representation of a RuleContext model
        rule_context_model = {
            'attributes': [rule_context_attribute_model],
        }

        # Construct a dict representation of a ResourceAttribute model
        account_id_resource_attribute_model = {
            'name': 'accountId',
            'value': TestContextBasedRestrictionsV1.test_account_id,
        }

        service_name_resource_attribute_model = {
            'name': 'serviceName',
            'value': TestContextBasedRestrictionsV1.service_name,
        }

        # Construct a dict representation of a ResourceTagAttribute model
        resource_tag_attribute_model = {
            'name': 'tagName',
            'value': 'tagValue',
        }

        # Construct a dict representation of a Resource model
        resource_model = {
            'attributes': [account_id_resource_attribute_model, service_name_resource_attribute_model],
            'tags': [resource_tag_attribute_model],
        }

        with pytest.raises(ApiException, match="404"):
            self.context_based_restrictions_service.replace_rule(
                rule_id=self.NonExistentID,
                if_match=TestContextBasedRestrictionsV1.rule_rev,
                contexts=[rule_context_model],
                resources=[resource_model],
                description='SDK TEST - this is an example of updated rule',
                enforcement_mode='disabled',
                transaction_id=self.getTransactionID()
            )

    @needscredentials
    def test_replace_rule_update_rule_with_invalid_if_match_parameter_error(self):
        # Construct a dict representation of a RuleContextAttribute model
        rule_context_attribute_model = {
            'name': 'networkZoneId',
            'value': TestContextBasedRestrictionsV1.zone_id,
        }

        # Construct a dict representation of a RuleContext model
        rule_context_model = {
            'attributes': [rule_context_attribute_model],
        }

        # Construct a dict representation of a ResourceAttribute model
        account_id_resource_attribute_model = {
            'name': 'accountId',
            'value': TestContextBasedRestrictionsV1.test_account_id,
        }

        service_name_resource_attribute_model = {
            'name': 'serviceName',
            'value': TestContextBasedRestrictionsV1.service_name,
        }

        # Construct a dict representation of a ResourceTagAttribute model
        resource_tag_attribute_model = {
            'name': 'tagName',
            'value': 'tagValue',
        }

        # Construct a dict representation of a Resource model
        resource_model = {
            'attributes': [account_id_resource_attribute_model, service_name_resource_attribute_model],
            'tags': [resource_tag_attribute_model],
        }

        with pytest.raises(ApiException, match="412"):
            self.context_based_restrictions_service.replace_rule(
                rule_id=TestContextBasedRestrictionsV1.rule_id,
                if_match="abc",
                contexts=[rule_context_model],
                resources=[resource_model],
                description='SDK TEST - this is an example of updated rule',
                enforcement_mode='disabled',
                transaction_id=self.getTransactionID()
            )

    @needscredentials
    def test_get_account_settings(self):
        get_account_settings_response = self.context_based_restrictions_service.get_account_settings(
            account_id=TestContextBasedRestrictionsV1.test_account_id,
            transaction_id=self.getTransactionID()
        )

        assert get_account_settings_response.get_status_code() == 200
        account_settings = get_account_settings_response.get_result()
        assert account_settings is not None

    @needscredentials
    def test_get_account_settings_with_invalid_account_id_parameter(self):
        with pytest.raises(ApiException, match="400"):
            self.context_based_restrictions_service.get_account_settings(
                account_id=self.InvalidID,
                transaction_id=self.getTransactionID()
            )

    @needscredentials
    def test_list_available_service_operations(self):

        list_available_service_operations_response = self.context_based_restrictions_service.list_available_service_operations(
            service_name='containers-kubernetes',
            transaction_id=self.getTransactionID()
        )

        assert list_available_service_operations_response.get_status_code() == 200
        operations_list = list_available_service_operations_response.get_result()
        assert operations_list is not None

    @needscredentials
    def test_delete_rule(self):
        delete_rule_response = self.context_based_restrictions_service.delete_rule(
            rule_id=TestContextBasedRestrictionsV1.rule_id,
            # Using the standard X-Correlation-Id header in this case
            x_correlation_id=self.getTransactionID()
        )

        assert delete_rule_response.get_status_code() == 204

    @needscredentials
    def test_delete_rule_with_rule_not_found_error(self):
        with pytest.raises(ApiException, match="404"):
            self.context_based_restrictions_service.delete_rule(
                rule_id=self.NonExistentID,
                transaction_id=self.getTransactionID()
            )


    @needscredentials
    def test_delete_zone(self):
        delete_zone_response = self.context_based_restrictions_service.delete_zone(
            zone_id=TestContextBasedRestrictionsV1.zone_id,
            transaction_id=self.getTransactionID()
        )

        assert delete_zone_response.get_status_code() == 204

    @needscredentials
    def test_delete_zone_with_zone_not_found_error(self):
        with pytest.raises(ApiException, match="404"):
             self.context_based_restrictions_service.delete_zone(
                zone_id=self.NonExistentID,
                transaction_id=self.getTransactionID()
            )

    def getTransactionID(self):
        return "sdk-test-" + str(uuid.uuid4())