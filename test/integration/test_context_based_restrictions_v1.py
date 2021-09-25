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
Integration Tests for ContextBasedRestrictionsV1
"""

import os
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
        address_model = {
            'type': 'ipAddress',
            'value': '169.23.56.234',
        }

        create_zone_response = self.context_based_restrictions_service.create_zone(
            name='SDK TEST - an example of zone',
            account_id=TestContextBasedRestrictionsV1.test_account_id,
            addresses=[address_model],
            description='SDK TEST - this is an example of zone',
            transaction_id='testString'
        )

        assert create_zone_response.get_status_code() == 201
        zone = create_zone_response.get_result()
        assert zone is not None
        TestContextBasedRestrictionsV1.zone_id = zone['id']

    @needscredentials
    def test_list_zones(self):
        list_zones_response = self.context_based_restrictions_service.list_zones(
            account_id=TestContextBasedRestrictionsV1.test_account_id,
            transaction_id='testString',
        )

        assert list_zones_response.get_status_code() == 200
        zone_list = list_zones_response.get_result()
        assert zone_list is not None

    @needscredentials
    def test_get_zone(self):
        get_zone_response = self.context_based_restrictions_service.get_zone(
            zone_id=TestContextBasedRestrictionsV1.zone_id,
            transaction_id='testString'
        )

        assert get_zone_response.get_status_code() == 200
        zone = get_zone_response.get_result()
        assert zone is not None
        TestContextBasedRestrictionsV1.zone_rev = get_zone_response.headers.get('ETag')

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
            transaction_id='testString'
        )

        assert replace_zone_response.get_status_code() == 200
        zone = replace_zone_response.get_result()
        assert zone is not None

    @needscredentials
    def test_list_available_serviceref_targets(self):
        list_available_serviceref_targets_response = self.context_based_restrictions_service.list_available_serviceref_targets(
            type='all'
        )

        assert list_available_serviceref_targets_response.get_status_code() == 200
        service_ref_target_list = list_available_serviceref_targets_response.get_result()
        assert service_ref_target_list is not None

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
            transaction_id='testString'
        )

        assert create_rule_response.get_status_code() == 201
        rule = create_rule_response.get_result()
        assert rule is not None
        TestContextBasedRestrictionsV1.rule_id = rule['id']

    @needscredentials
    def test_list_rules(self):
        list_rules_response = self.context_based_restrictions_service.list_rules(
            account_id=TestContextBasedRestrictionsV1.test_account_id,
            transaction_id='testString',
        )

        assert list_rules_response.get_status_code() == 200
        rule_list = list_rules_response.get_result()
        assert rule_list is not None

    @needscredentials
    def test_get_rule(self):
        get_rule_response = self.context_based_restrictions_service.get_rule(
            rule_id=TestContextBasedRestrictionsV1.rule_id,
            transaction_id='testString'
        )

        assert get_rule_response.get_status_code() == 200
        rule = get_rule_response.get_result()
        assert rule is not None
        TestContextBasedRestrictionsV1.rule_rev = get_rule_response.headers.get("ETag")

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
            transaction_id='testString'
        )

        assert replace_rule_response.get_status_code() == 200
        rule = replace_rule_response.get_result()
        assert rule is not None

    @needscredentials
    def test_get_account_settings(self):
        get_account_settings_response = self.context_based_restrictions_service.get_account_settings(
            account_id=TestContextBasedRestrictionsV1.test_account_id,
            transaction_id='testString'
        )

        assert get_account_settings_response.get_status_code() == 200
        account_settings = get_account_settings_response.get_result()
        assert account_settings is not None

    @needscredentials
    def test_delete_rule(self):
        delete_rule_response = self.context_based_restrictions_service.delete_rule(
            rule_id=TestContextBasedRestrictionsV1.rule_id,
            transaction_id='testString'
        )

        assert delete_rule_response.get_status_code() == 204

    @needscredentials
    def test_delete_zone(self):
        delete_zone_response = self.context_based_restrictions_service.delete_zone(
            zone_id=TestContextBasedRestrictionsV1.zone_id,
            transaction_id='testString'
        )

        assert delete_zone_response.get_status_code() == 204


