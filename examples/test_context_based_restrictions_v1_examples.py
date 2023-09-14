# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2023.
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
Examples for ContextBasedRestrictionsV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from ibm_platform_services.context_based_restrictions_v1 import *

#
# This file provides an example of how to use the Context Based Restrictions service.
#
# The following configuration properties are assumed to be defined:
# CONTEXT_BASED_RESTRICTIONS_URL=<service base url>
# CONTEXT_BASED_RESTRICTIONS_AUTH_TYPE=iam
# CONTEXT_BASED_RESTRICTIONS_APIKEY=<IAM apikey>
# CONTEXT_BASED_RESTRICTIONS_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'context_based_restrictions_v1.env'

context_based_restrictions_service = None

config = None


##############################################################################
# Start of Examples for Service: ContextBasedRestrictionsV1
##############################################################################
# region
class TestContextBasedRestrictionsV1Examples:
    """
    Example Test Class for ContextBasedRestrictionsV1
    """

    @classmethod
    def setup_class(cls):
        global context_based_restrictions_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            context_based_restrictions_service = ContextBasedRestrictionsV1.new_instance()

            # end-common
            assert context_based_restrictions_service is not None

            # Load the configuration
            global config
            config = read_external_sources(ContextBasedRestrictionsV1.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_zone_example(self):
        """
        create_zone request example
        """
        try:
            print('\ncreate_zone() result:')
            # begin-create_zone

            address_model = {
                'type': 'ipAddress',
                'value': '169.23.56.234',
            }

            response = context_based_restrictions_service.create_zone(
                name='an example of zone',
                account_id='12ab34cd56ef78ab90cd12ef34ab56cd',
                addresses=[address_model],
                description='this is an example of zone',
                excluded=[address_model],
            )
            zone = response.get_result()

            print(json.dumps(zone, indent=2))

            # end-create_zone

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_zones_example(self):
        """
        list_zones request example
        """
        try:
            print('\nlist_zones() result:')
            # begin-list_zones

            response = context_based_restrictions_service.list_zones(
                account_id='testString',
            )
            zone_list = response.get_result()

            print(json.dumps(zone_list, indent=2))

            # end-list_zones

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_zone_example(self):
        """
        get_zone request example
        """
        try:
            print('\nget_zone() result:')
            # begin-get_zone

            response = context_based_restrictions_service.get_zone(
                zone_id='testString',
            )
            zone = response.get_result()

            print(json.dumps(zone, indent=2))

            # end-get_zone

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_zone_example(self):
        """
        replace_zone request example
        """
        try:
            print('\nreplace_zone() result:')
            # begin-replace_zone

            address_model = {
                'type': 'ipAddress',
                'value': '169.23.56.234',
            }

            response = context_based_restrictions_service.replace_zone(
                zone_id='testString',
                if_match='testString',
                name='an example of zone',
                account_id='12ab34cd56ef78ab90cd12ef34ab56cd',
                addresses=[address_model],
                description='this is an example of zone',
                excluded=[address_model],
            )
            zone = response.get_result()

            print(json.dumps(zone, indent=2))

            # end-replace_zone

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_available_serviceref_targets_example(self):
        """
        list_available_serviceref_targets request example
        """
        try:
            print('\nlist_available_serviceref_targets() result:')
            # begin-list_available_serviceref_targets

            response = context_based_restrictions_service.list_available_serviceref_targets()
            service_ref_target_list = response.get_result()

            print(json.dumps(service_ref_target_list, indent=2))

            # end-list_available_serviceref_targets

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_rule_example(self):
        """
        create_rule request example
        """
        try:
            print('\ncreate_rule() result:')
            # begin-create_rule

            rule_context_attribute_model = {
                'name': 'networkZoneId',
                'value': '65810ac762004f22ac19f8f8edf70a34',
            }

            rule_context_model = {
                'attributes': [rule_context_attribute_model],
            }

            resource_attribute_model = {
                'name': 'accountId',
                'value': '12ab34cd56ef78ab90cd12ef34ab56cd',
            }

            resource_model = {
                'attributes': [resource_attribute_model],
            }

            response = context_based_restrictions_service.create_rule(
                contexts=[rule_context_model],
                resources=[resource_model],
                description='this is an example of rule',
                enforcement_mode='enabled',
            )
            rule = response.get_result()

            print(json.dumps(rule, indent=2))

            # end-create_rule

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_rules_example(self):
        """
        list_rules request example
        """
        try:
            print('\nlist_rules() result:')
            # begin-list_rules

            response = context_based_restrictions_service.list_rules(
                account_id='testString',
            )
            rule_list = response.get_result()

            print(json.dumps(rule_list, indent=2))

            # end-list_rules

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_rule_example(self):
        """
        get_rule request example
        """
        try:
            print('\nget_rule() result:')
            # begin-get_rule

            response = context_based_restrictions_service.get_rule(
                rule_id='testString',
            )
            rule = response.get_result()

            print(json.dumps(rule, indent=2))

            # end-get_rule

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_rule_example(self):
        """
        replace_rule request example
        """
        try:
            print('\nreplace_rule() result:')
            # begin-replace_rule

            rule_context_attribute_model = {
                'name': 'networkZoneId',
                'value': '76921bd873115033bd2a0909fe081b45',
            }

            rule_context_model = {
                'attributes': [rule_context_attribute_model],
            }

            resource_attribute_model = {
                'name': 'accountId',
                'value': '12ab34cd56ef78ab90cd12ef34ab56cd',
            }

            resource_model = {
                'attributes': [resource_attribute_model],
            }

            response = context_based_restrictions_service.replace_rule(
                rule_id='testString',
                if_match='testString',
                contexts=[rule_context_model],
                resources=[resource_model],
                description='this is an example of rule',
                enforcement_mode='disabled',
            )
            rule = response.get_result()

            print(json.dumps(rule, indent=2))

            # end-replace_rule

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_account_settings_example(self):
        """
        get_account_settings request example
        """
        try:
            print('\nget_account_settings() result:')
            # begin-get_account_settings

            response = context_based_restrictions_service.get_account_settings(
                account_id='testString',
            )
            account_settings = response.get_result()

            print(json.dumps(account_settings, indent=2))

            # end-get_account_settings

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_available_service_operations_example(self):
        """
        list_available_service_operations request example
        """
        try:
            print('\nlist_available_service_operations() result:')
            # begin-list_available_service_operations

            operations_list = context_based_restrictions_service.list_available_service_operations(
                service_name='containers-kubernetes'
            ).get_result()

            print(json.dumps(operations_list, indent=2))

            # end-list_available_service_operations

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_zone_example(self):
        """
        delete_zone request example
        """
        try:
            # begin-delete_zone

            response = context_based_restrictions_service.delete_zone(
                zone_id='testString',
            )

            # end-delete_zone
            print('\ndelete_zone() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_rule_example(self):
        """
        delete_rule request example
        """
        try:
            # begin-delete_rule

            response = context_based_restrictions_service.delete_rule(
                rule_id='testString',
            )

            # end-delete_rule
            print('\ndelete_rule() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: ContextBasedRestrictionsV1
##############################################################################
