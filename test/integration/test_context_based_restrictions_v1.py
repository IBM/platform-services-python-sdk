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

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.context_based_restrictions_service = ContextBasedRestrictionsV1.new_instance(
            )
            assert cls.context_based_restrictions_service is not None

            cls.config = read_external_sources(
                ContextBasedRestrictionsV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.context_based_restrictions_service.enable_retries()

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
            name='an example of zone',
            account_id='12ab34cd56ef78ab90cd12ef34ab56cd',
            addresses=[address_model],
            description='this is an example of zone',
            excluded=[address_model],
            transaction_id='testString'
        )

        assert create_zone_response.get_status_code() == 201
        out_zone = create_zone_response.get_result()
        assert out_zone is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 409
        # 429
        # 503
        #

    @needscredentials
    def test_list_zones(self):

        list_zones_response = self.context_based_restrictions_service.list_zones(
            account_id='testString',
            transaction_id='testString',
            name='testString',
            sort='testString'
        )

        assert list_zones_response.get_status_code() == 200
        out_zone_page = list_zones_response.get_result()
        assert out_zone_page is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 429
        # 503
        #

    @needscredentials
    def test_get_zone(self):

        get_zone_response = self.context_based_restrictions_service.get_zone(
            zone_id='testString',
            transaction_id='testString'
        )

        assert get_zone_response.get_status_code() == 200
        out_zone = get_zone_response.get_result()
        assert out_zone is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 429
        # 503
        #

    @needscredentials
    def test_replace_zone(self):

        # Construct a dict representation of a AddressIPAddress model
        address_model = {
            'type': 'ipAddress',
            'value': '169.23.56.234',
        }

        replace_zone_response = self.context_based_restrictions_service.replace_zone(
            zone_id='testString',
            if_match='testString',
            name='an example of zone',
            account_id='12ab34cd56ef78ab90cd12ef34ab56cd',
            addresses=[address_model],
            description='this is an example of zone',
            excluded=[address_model],
            transaction_id='testString'
        )

        assert replace_zone_response.get_status_code() == 200
        out_zone = replace_zone_response.get_result()
        assert out_zone is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 412
        # 429
        # 503
        #

    @needscredentials
    def test_list_available_serviceref_targets(self):

        list_available_serviceref_targets_response = self.context_based_restrictions_service.list_available_serviceref_targets(
            type='all'
        )

        assert list_available_serviceref_targets_response.get_status_code() == 200
        service_ref_target_page = list_available_serviceref_targets_response.get_result()
        assert service_ref_target_page is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 429
        # 503
        #

    @needscredentials
    def test_create_rule(self):

        # Construct a dict representation of a RuleContextAttribute model
        rule_context_attribute_model = {
            'name': 'networkZoneId',
            'value': '65810ac762004f22ac19f8f8edf70a34',
        }

        # Construct a dict representation of a RuleContext model
        rule_context_model = {
            'attributes': [rule_context_attribute_model],
        }

        # Construct a dict representation of a ResourceAttribute model
        resource_attribute_model = {
            'name': 'accountId',
            'value': '12ab34cd56ef78ab90cd12ef34ab56cd',
            'operator': 'testString',
        }

        # Construct a dict representation of a ResourceTagAttribute model
        resource_tag_attribute_model = {
            'name': 'testString',
            'value': 'testString',
            'operator': 'testString',
        }

        # Construct a dict representation of a Resource model
        resource_model = {
            'attributes': [resource_attribute_model],
            'tags': [resource_tag_attribute_model],
        }

        create_rule_response = self.context_based_restrictions_service.create_rule(
            contexts=[rule_context_model],
            resources=[resource_model],
            description='this is an example of rule',
            transaction_id='testString'
        )

        assert create_rule_response.get_status_code() == 201
        out_rule = create_rule_response.get_result()
        assert out_rule is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 429
        # 503
        #

    @needscredentials
    def test_list_rules(self):

        list_rules_response = self.context_based_restrictions_service.list_rules(
            account_id='testString',
            transaction_id='testString',
            region='testString',
            resource='testString',
            resource_type='testString',
            service_instance='testString',
            service_name='testString',
            service_type='testString',
            zone_id='testString',
            sort='testString'
        )

        assert list_rules_response.get_status_code() == 200
        out_rule_page = list_rules_response.get_result()
        assert out_rule_page is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 429
        # 503
        #

    @needscredentials
    def test_get_rule(self):

        get_rule_response = self.context_based_restrictions_service.get_rule(
            rule_id='testString',
            transaction_id='testString'
        )

        assert get_rule_response.get_status_code() == 200
        out_rule = get_rule_response.get_result()
        assert out_rule is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 429
        # 503
        #

    @needscredentials
    def test_replace_rule(self):

        # Construct a dict representation of a RuleContextAttribute model
        rule_context_attribute_model = {
            'name': 'networkZoneId',
            'value': '76921bd873115033bd2a0909fe081b45',
        }

        # Construct a dict representation of a RuleContext model
        rule_context_model = {
            'attributes': [rule_context_attribute_model],
        }

        # Construct a dict representation of a ResourceAttribute model
        resource_attribute_model = {
            'name': 'accountId',
            'value': '12ab34cd56ef78ab90cd12ef34ab56cd',
            'operator': 'testString',
        }

        # Construct a dict representation of a ResourceTagAttribute model
        resource_tag_attribute_model = {
            'name': 'testString',
            'value': 'testString',
            'operator': 'testString',
        }

        # Construct a dict representation of a Resource model
        resource_model = {
            'attributes': [resource_attribute_model],
            'tags': [resource_tag_attribute_model],
        }

        replace_rule_response = self.context_based_restrictions_service.replace_rule(
            rule_id='testString',
            if_match='testString',
            contexts=[rule_context_model],
            resources=[resource_model],
            description='this is an example of rule',
            transaction_id='testString'
        )

        assert replace_rule_response.get_status_code() == 200
        out_rule = replace_rule_response.get_result()
        assert out_rule is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 412
        # 429
        # 503
        #

    @needscredentials
    def test_get_account_settings(self):

        get_account_settings_response = self.context_based_restrictions_service.get_account_settings(
            account_id='testString',
            transaction_id='testString'
        )

        assert get_account_settings_response.get_status_code() == 200
        out_account_settings = get_account_settings_response.get_result()
        assert out_account_settings is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 429
        # 503
        #

    @needscredentials
    def test_delete_zone(self):

        delete_zone_response = self.context_based_restrictions_service.delete_zone(
            zone_id='testString',
            transaction_id='testString'
        )

        assert delete_zone_response.get_status_code() == 204

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 412
        # 429
        # 503
        #

    @needscredentials
    def test_delete_rule(self):

        delete_rule_response = self.context_based_restrictions_service.delete_rule(
            rule_id='testString',
            transaction_id='testString'
        )

        assert delete_rule_response.get_status_code() == 204

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 429
        # 503
        #

