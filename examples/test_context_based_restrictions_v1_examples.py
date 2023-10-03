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
# CONTEXT_BASED_RESTRICTIONS_TEST_ACCOUNT_ID=<the id of the account under which test CBR zones and rules are created>
# CONTEXT_BASED_RESTRICTIONS_TEST_SERVICE_NAME=<the name of the service to be associated with the test CBR rules>
# CONTEXT_BASED_RESTRICTIONS_TEST_VPC_CRN=<the CRN of the vpc instance to be associated with the test CBR rules>
#
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'context_based_restrictions_v1.env'

context_based_restrictions_service = None

config = None

account_id = None
service_name = None
vpc_crn = None
zone_id = None
zone_rev = None
rule_id = None
rule_rev = None


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

            global account_id
            account_id = config['TEST_ACCOUNT_ID']

            global service_name
            service_name = config['TEST_SERVICE_NAME']

            global vpc_crn
            vpc_crn = config['TEST_VPC_CRN']

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

            ip_address_model = {
                'type': 'ipAddress',
                'value': '169.23.56.234',
            }
            ip_range_address_model = {
                'type': 'ipRange',
                'value': '169.23.22.0-169.23.22.255',
            }
            subnet_address_model = {
                'type': 'subnet',
                'value': '192.0.2.0/24',
            }
            vpc_address_model = {
                'type': 'vpc',
                'value': vpc_crn,
            }
            service_ref_address_model = {
                'type': 'serviceRef',
                'ref': {
                    'account_id': account_id,
                    'service_name': 'cloud-object-storage',
                },
            }
            excluded_ip_address_model = {
                'type': 'ipAddress',
                'value': '169.23.22.127',
            }

            response = context_based_restrictions_service.create_zone(
                name='an example of zone',
                account_id=account_id,
                addresses=[
                    ip_address_model,
                    ip_range_address_model,
                    subnet_address_model,
                    vpc_address_model,
                    service_ref_address_model,
                ],
                description='this is an example of zone',
                excluded=[excluded_ip_address_model],
            )
            zone = response.get_result()

            print(json.dumps(zone, indent=2))

            # end-create_zone
            global zone_id
            zone_id = zone['id']

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
                account_id=account_id,
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
                zone_id=zone_id,
            )
            zone = response.get_result()

            print(json.dumps(zone, indent=2))

            # end-get_zone
            global zone_rev
            zone_rev = response.headers.get("ETag")

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
                zone_id=zone_id,
                if_match=zone_rev,
                name='an example of zone',
                account_id=account_id,
                addresses=[address_model],
                description='this is an example of zone',
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
                'value': zone_id,
            }

            rule_context_model = {
                'attributes': [rule_context_attribute_model],
            }

            resource_attribute_model = {
                'name': 'accountId',
                'value': account_id,
            }

            resource_attribute_service_name_model = {
                'name': 'serviceName',
                'value': service_name,
            }

            resource_model = {
                'attributes': [resource_attribute_model, resource_attribute_service_name_model],
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
            global rule_id
            rule_id = rule['id']

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
                account_id=account_id,
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
                rule_id=rule_id,
            )
            rule = response.get_result()

            print(json.dumps(rule, indent=2))

            # end-get_rule
            global rule_rev
            rule_rev = response.headers.get("ETag")

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
                'value': zone_id,
            }

            rule_context_model = {
                'attributes': [rule_context_attribute_model],
            }

            resource_attribute_model = {
                'name': 'accountId',
                'value': account_id,
            }

            resource_attribute_service_name_model = {
                'name': 'serviceName',
                'value': service_name,
            }

            resource_tag_attribute_model = {
                'name': 'tagName',
                'value': 'tagValue',
            }

            resource_model = {
                'attributes': [resource_attribute_model, resource_attribute_service_name_model],
                'tags': [resource_tag_attribute_model],
            }

            response = context_based_restrictions_service.replace_rule(
                rule_id=rule_id,
                if_match=rule_rev,
                contexts=[rule_context_model],
                resources=[resource_model],
                description='this is an example of updated rule',
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
                account_id=account_id,
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
    def test_delete_rule_example(self):
        """
        delete_rule request example
        """
        try:
            # begin-delete_rule

            response = context_based_restrictions_service.delete_rule(
                rule_id=rule_id,
            )

            # end-delete_rule
            print('\ndelete_rule() response status code: ', response.get_status_code())

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
                zone_id=zone_id,
            )

            # end-delete_zone
            print('\ndelete_zone() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: ContextBasedRestrictionsV1
##############################################################################
