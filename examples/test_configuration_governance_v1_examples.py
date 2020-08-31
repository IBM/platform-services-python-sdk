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
Examples for ConfigurationGovernanceV1
"""

import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.configuration_governance_v1 import *

# Config file name
config_file = 'configuration_governance.env'

configuration_governance_service = None

config = None

# Variables to hold link values
attachment_etag_link = None
attachment_id_link = None
rule_etag_link = None
rule_id_link = None

# Additional configuration settings
test_label = 'PythonSDKExamples'
account_id = None
service_name = None
enterprise_scope_id = None
subacct_scope_id = None

##############################################################################
# Start of Examples for Service: ConfigurationGovernanceV1
##############################################################################
# region
class TestConfigurationGovernanceV1Examples():
    """
    Example Test Class for ConfigurationGovernanceV1
    """

    @classmethod
    def setup_class(cls):
        global configuration_governance_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            configuration_governance_service = ConfigurationGovernanceV1.new_instance(
            )

            # end-common
            assert configuration_governance_service is not None

            # Load the configuration
            global config, account_id, service_name, enterprise_scope_id, subacct_scope_id
            config = read_external_sources(ConfigurationGovernanceV1.DEFAULT_SERVICE_NAME)

            account_id = config['ACCOUNT_ID']
            service_name = config['EXAMPLE_SERVICE_NAME']
            enterprise_scope_id = config['ENTERPRISE_SCOPE_ID']
            subacct_scope_id = config['SUBACCT_SCOPE_ID']

            cls.clean_rules()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_rules_example(self):
        """
        create_rules request example
        """
        try:
            # begin-create_rules

            target_resource_model = {
                'service_name': service_name,
                'resource_kind': 'service'
            }

            rule_required_config_model = {
                'description': 'Public access check',
                'property': 'public_access_enabled',
                'operator': 'is_true'
            }

            enforcement_action_model = {
                'action': 'disallow'
            }

            rule_request_model = {
                'account_id': account_id,
                'name': 'Disable public access',
                'description': 'Ensure that public access to account resources is disabled.',
                'target': {'service_name':service_name,'resource_kind':'service'},
                'required_config': {'description':'Public access check','and':[{'property':'public_access_enabled','operator':'is_false'}]},
                'enforcement_actions': [enforcement_action_model],
                'labels': [test_label]
            }

            create_rule_request_model = {
                'request_id': '3cebc877-58e7-44a5-a292-32114fa73558',
                'rule': {'account_id':account_id,'name':'Disable public access','description':'Ensure that public access to account resources is disabled.','labels':[test_label],'target':{'service_name':service_name,'resource_kind':'service'},'required_config':{'description':'Public access check','and':[{'property':'public_access_enabled','operator':'is_false'}]},'enforcement_actions':[{'action':'disallow'},{'action':'audit_log'}]}
            }

            create_rules_response = configuration_governance_service.create_rules(
                rules=[create_rule_request_model]
            ).get_result()

            print(json.dumps(create_rules_response, indent=2))

            # end-create_rules

            global rule_id_link
            rule_id_link = create_rules_response['rules'][0]['rule']['rule_id'];
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_attachments_example(self):
        """
        create_attachments request example
        """
        try:
            # begin-create_attachments

            excluded_scope_model = {
                'note': 'Development account',
                'scope_id': subacct_scope_id,
                'scope_type': 'enterprise.account'
            }

            attachment_request_model = {
                'account_id': account_id,
                'included_scope': {'note':'My enterprise','scope_id':enterprise_scope_id,'scope_type':'enterprise'},
                'excluded_scopes': [excluded_scope_model]
            }

            create_attachments_response = configuration_governance_service.create_attachments(
                rule_id=rule_id_link,
                attachments=[attachment_request_model]
            ).get_result()

            print(json.dumps(create_attachments_response, indent=2))

            # end-create_attachments

            global attachment_id_link
            attachment_id_link = create_attachments_response['attachments'][0]['attachment_id'];
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_attachment_example(self):
        """
        get_attachment request example
        """
        try:
            # begin-get_attachment

            attachment = configuration_governance_service.get_attachment(
                rule_id=rule_id_link,
                attachment_id=attachment_id_link
            ).get_result()

            print(json.dumps(attachment, indent=2))

            # end-get_attachment

            global attachment_etag_link
            attachment_etag_link = configuration_governance_service.get_attachment(
                rule_id=rule_id_link, attachment_id=attachment_id_link).get_headers().get('Etag')
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_rule_example(self):
        """
        get_rule request example
        """
        try:
            # begin-get_rule

            rule = configuration_governance_service.get_rule(
                rule_id=rule_id_link
            ).get_result()

            print(json.dumps(rule, indent=2))

            # end-get_rule

            global rule_etag_link
            rule_etag_link = configuration_governance_service.get_rule(rule_id=rule_id_link).get_headers().get('etag')
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_rules_example(self):
        """
        list_rules request example
        """
        try:
            # begin-list_rules

            rule_list = configuration_governance_service.list_rules(
                account_id=account_id
            ).get_result()

            print(json.dumps(rule_list, indent=2))

            # end-list_rules

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_rule_example(self):
        """
        update_rule request example
        """
        try:
            # begin-update_rule

            rule_target_attribute_model = {
                'name': 'testString',
                'operator': 'string_equals'
            }

            target_resource_model = {
                'service_name': service_name,
                'resource_kind': 'service',
                'additional_target_attributes': [rule_target_attribute_model]
            }

            rule_required_config_model = {
                'property': 'public_access_enabled',
                'operator': 'is_false'
            }

            enforcement_action_model = {
                'action': 'audit_log'
            }

            rule = configuration_governance_service.update_rule(
                rule_id=rule_id_link,
                if_match=rule_etag_link,
                name='Disable public access',
                description='Ensure that public access to account resources is disabled.',
                target={'service_name':service_name,'resource_kind':'service','additional_target_attributes':[]},
                required_config={'property':'public_access_enabled','operator':'is_false'},
                enforcement_actions=[enforcement_action_model],
                account_id=account_id,
                rule_type='user_defined',
                labels=['testString']
            ).get_result()

            print(json.dumps(rule, indent=2))

            # end-update_rule

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_attachments_example(self):
        """
        list_attachments request example
        """
        try:
            # begin-list_attachments

            attachment_list = configuration_governance_service.list_attachments(
                rule_id=rule_id_link
            ).get_result()

            print(json.dumps(attachment_list, indent=2))

            # end-list_attachments

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_attachment_example(self):
        """
        update_attachment request example
        """
        try:
            # begin-update_attachment

            excluded_scope_model = {
                'note': 'Development account',
                'scope_id': subacct_scope_id,
                'scope_type': 'enterprise.account'
            }

            attachment = configuration_governance_service.update_attachment(
                rule_id=rule_id_link,
                attachment_id=attachment_id_link,
                if_match=attachment_etag_link,
                account_id=account_id,
                included_scope={'note':'My enterprise','scope_id':enterprise_scope_id,'scope_type':'enterprise'},
                excluded_scopes=[excluded_scope_model]
            ).get_result()

            print(json.dumps(attachment, indent=2))

            # end-update_attachment

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_attachment_example(self):
        """
        delete_attachment request example
        """
        try:
            # begin-delete_attachment

            response = configuration_governance_service.delete_attachment(
                rule_id=rule_id_link,
                attachment_id=attachment_id_link
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_attachment

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_rule_example(self):
        """
        delete_rule request example
        """
        try:
            # begin-delete_rule

            response = configuration_governance_service.delete_rule(
                rule_id=rule_id_link
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_rule

        except ApiException as e:
            pytest.fail(str(e))

    @classmethod
    def clean_rules(cls):
        """
        Clean up rules from prior test runs
        """
        try:
            rule_list = configuration_governance_service.list_rules(
                account_id=account_id,
                labels=test_label
            ).get_result()

            for rule in rule_list['rules']:
                rule_id = rule['rule_id']
                print(f'deleting rule {rule_id}')
                configuration_governance_service.delete_rule(rule_id)

        except ApiException as e:
            print(str(e))

# endregion
##############################################################################
# End of Examples for Service: ConfigurationGovernanceV1
##############################################################################
