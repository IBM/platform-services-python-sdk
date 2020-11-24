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
Examples for ResourceControllerV2
"""

import os
import time
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.resource_controller_v2 import *

# Config file name
config_file = 'resource_controller.env'

#
# This file provides an example of how to use the Resource Controller service.
#
# The following configuration properties are assumed to be defined:
#
# RESOURCE_CONTROLLER_URL=<service url>
# RESOURCE_CONTROLLER_AUTH_TYPE=iam
# RESOURCE_CONTROLLER_AUTH_URL=<IAM Token Service url>
# RESOURCE_CONTROLLER_APIKEY=<User's IAM API Key>
# RESOURCE_CONTROLLER_RESOURCE_GROUP=<Short ID of the user's resource group>
# RESOURCE_CONTROLLER_PLAN_ID=<Unique ID of the plan associated with the offering>
# RESOURCE_CONTROLLER_ACCOUNT_ID=<User's account ID>
# RESOURCE_CONTROLLER_ALIAS_TARGET_CRN=<The CRN of target name(space) in a specific environment>
# RESOURCE_CONTROLLER_BINDING_TARGET_CRN=<The CRN of application to bind to in a specific environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a "credentials" file and then:
# export IBM_CREDENTIALS_FILE=<name of credentials file>
#

resource_controller_service = None

config = None

instanceGuid = None
aliasGuid = None
bindingGuid = None
instanceKeyGuid = None
resourceGroup = None
resourcePlanId = None
accountId = None
aliasTargetCRN = None
bindingTargetCRN = None
reclamationId = None
resourceInstanceName = 'RcSdkInstance1Python'
resourceInstanceUpdateName = 'RcSdkInstanceUpdate1Python'
aliasName = 'RcSdkAlias1Python'
aliasUpdateName = 'RcSdkAliasUpdate1Python'
bindingName = 'RcSdkBinding1Python'
bindingUpdateName = 'RcSdkBindingUpdate1Python'
keyName = 'RcSdkKey1Python'
keyUpdateName = 'RcSdkKeyUpdate1Python'
targetRegion = 'global'
reclaimAction = 'reclaim'

##############################################################################
# Start of Examples for Service: ResourceControllerV2
##############################################################################
# region
class TestResourceControllerV2Examples():
    """
    Example Test Class for ResourceControllerV2
    """

    @classmethod
    def setup_class(cls):
        global resource_controller_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            resource_controller_service = ResourceControllerV2.new_instance()

            # end-common
            assert resource_controller_service is not None

            # Load the configuration
            global config
            config = read_external_sources(
                ResourceControllerV2.DEFAULT_SERVICE_NAME)
            
            global resourceGroup
            resourceGroup = config['RESOURCE_GROUP']

            global resourcePlanId
            resourcePlanId = config['RECLAMATION_PLAN_ID']

            global accountId
            accountId = config['ACCOUNT_ID']

            global aliasTargetCRN
            aliasTargetCRN = config['ALIAS_TARGET_CRN']

            global bindingTargetCRN
            bindingTargetCRN = config['BINDING_TARGET_CRN']

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_resource_instance_example(self):
        """
        create_resource_instance request example
        """
        try:
            global instanceGuid, resourceInstanceName, targetRegion, resourceGroup, resourcePlanId
            # begin-create_resource_instance
            
            resource_instance = resource_controller_service.create_resource_instance(
                name=resourceInstanceName,
                target=targetRegion,
                resource_group=resourceGroup,
                resource_plan_id=resourcePlanId
            ).get_result()

            print(json.dumps(resource_instance, indent=2))

            instanceGuid = resource_instance.get('guid')
            # end-create_resource_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resource_instance_example(self):
        """
        get_resource_instance request example
        """
        try:
            global instanceGuid
            # begin-get_resource_instance

            resource_instance = resource_controller_service.get_resource_instance(
                id=instanceGuid
            ).get_result()

            print(json.dumps(resource_instance, indent=2))

            # end-get_resource_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_resource_instance_example(self):
        """
        update_resource_instance request example
        """
        try:
            global instanceGuid, resourceInstanceUpdateName
            # begin-update_resource_instance

            params = {}
            params['example'] = 'property'
            resource_instance = resource_controller_service.update_resource_instance(
                id=instanceGuid,
                name=resourceInstanceUpdateName,
                parameters=params
            ).get_result()

            print(json.dumps(resource_instance, indent=2))

            # end-update_resource_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_resource_instances_example(self):
        """
        list_resource_instances request example
        """
        try:
            global resourceInstanceName
            # begin-list_resource_instances

            resource_instances_list = resource_controller_service.list_resource_instances(
                name=resourceInstanceName
            ).get_result()

            print(json.dumps(resource_instances_list, indent=2))

            # end-list_resource_instances

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_resource_alias_example(self):
        """
        create_resource_alias request example
        """
        try:
            global instanceGuid, aliasName, aliasGuid, aliasTargetCRN
            # begin-create_resource_alias
            
            resource_alias = resource_controller_service.create_resource_alias(
                name=aliasName,
                source=instanceGuid,
                target=aliasTargetCRN
            ).get_result()

            aliasGuid = resource_alias.get('guid')
            print(json.dumps(resource_alias, indent=2))

            # end-create_resource_alias

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resource_alias_example(self):
        """
        get_resource_alias request example
        """
        try:
            global aliasGuid
            # begin-get_resource_alias

            resource_alias = resource_controller_service.get_resource_alias(
                id=aliasGuid
            ).get_result()

            print(json.dumps(resource_alias, indent=2))

            # end-get_resource_alias

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_resource_alias_example(self):
        """
        update_resource_alias request example
        """
        try:
            global aliasGuid, aliasUpdateName
            # begin-update_resource_alias
            
            resource_alias = resource_controller_service.update_resource_alias(
                id=aliasGuid,
                name=aliasUpdateName
            ).get_result()

            print(json.dumps(resource_alias, indent=2))

            # end-update_resource_alias

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_resource_aliases_example(self):
        """
        list_resource_aliases request example
        """
        try:
            # begin-list_resource_aliases
            
            resource_aliases_list = resource_controller_service.list_resource_aliases(
                name=aliasName
            ).get_result()

            print(json.dumps(resource_aliases_list, indent=2))

            # end-list_resource_aliases

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_create_resource_binding_example(self):
        """
        create_resource_binding request example
        """
        try:
            global aliasGuid, bindingGuid, bindingName, bindingTargetCRN
            # begin-create_resource_binding

            resource_binding = resource_controller_service.create_resource_binding(
                source=aliasGuid,
                target=bindingTargetCRN,
                name=bindingName
            ).get_result()

            bindingGuid = resource_binding.get('guid')
            print(json.dumps(resource_binding, indent=2))

            # end-create_resource_binding

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resource_binding_example(self):
        """
        get_resource_binding request example
        """
        try:
            global bindingGuid
            # begin-get_resource_binding

            resource_binding = resource_controller_service.get_resource_binding(
                id=bindingGuid
            ).get_result()

            print(json.dumps(resource_binding, indent=2))

            # end-get_resource_binding

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_resource_binding_example(self):
        """
        update_resource_binding request example
        """
        try:
            global bindingGuid, bindingUpdateName
            # begin-update_resource_binding
            
            resource_binding = resource_controller_service.update_resource_binding(
                id=bindingGuid,
                name=bindingUpdateName
            ).get_result()

            print(json.dumps(resource_binding, indent=2))

            # end-update_resource_binding

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_resource_bindings_example(self):
        """
        list_resource_bindings request example
        """
        try:
            # begin-list_resource_bindings

            resource_bindings_list = resource_controller_service.list_resource_bindings(
                name=bindingName
            ).get_result()

            print(json.dumps(resource_bindings_list, indent=2))

            # end-list_resource_bindings

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_resource_key_example(self):
        """
        create_resource_key request example
        """
        try:
            global instanceGuid, instanceKeyGuid, keyName
            # begin-create_resource_key

            resource_key = resource_controller_service.create_resource_key(
                name=keyName,
                source=instanceGuid
            ).get_result()

            instanceKeyGuid = resource_key.get('guid') 
            print(json.dumps(resource_key, indent=2))

            # end-create_resource_key

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resource_key_example(self):
        """
        get_resource_key request example
        """
        try:
            global instanceKeyGuid
            # begin-get_resource_key

            resource_key = resource_controller_service.get_resource_key(
                id=instanceKeyGuid
            ).get_result()

            print(json.dumps(resource_key, indent=2))

            # end-get_resource_key

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_resource_key_example(self):
        """
        update_resource_key request example
        """
        try:
            global instanceKeyGuid, keyUpdateName
            # begin-update_resource_key

            resource_key = resource_controller_service.update_resource_key(
                id=instanceKeyGuid,
                name=keyUpdateName
            ).get_result()

            print(json.dumps(resource_key, indent=2))

            # end-update_resource_key

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_resource_keys_example(self):
        """
        list_resource_keys request example
        """
        try:
            # begin-list_resource_keys

            resource_keys_list = resource_controller_service.list_resource_keys(
                name=keyName
            ).get_result()

            print(json.dumps(resource_keys_list, indent=2))

            # end-list_resource_keys

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_resource_binding_example(self):
        """
        delete_resource_binding request example
        """
        try:
            global bindingGuid
            # begin-delete_resource_binding

            response = resource_controller_service.delete_resource_binding(
                id=bindingGuid
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_resource_binding

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_resource_key_example(self):
        """
        delete_resource_key request example
        """
        try:
            global instanceKeyGuid
            # begin-delete_resource_key

            response = resource_controller_service.delete_resource_key(
                id=instanceKeyGuid
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_resource_key

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_resource_alias_example(self):
        """
        delete_resource_alias request example
        """
        try:
            global aliasGuid
            # begin-delete_resource_alias

            response = resource_controller_service.delete_resource_alias(
                id=aliasGuid
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_resource_alias

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_lock_resource_instance_example(self):
        """
        lock_resource_instance request example
        """
        try:
            global instanceGuid
            # begin-lock_resource_instance

            resource_instance = resource_controller_service.lock_resource_instance(
                id=instanceGuid
            ).get_result()

            print(json.dumps(resource_instance, indent=2))

            # end-lock_resource_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_unlock_resource_instance_example(self):
        """
        unlock_resource_instance request example
        """
        try:
            global instanceGuid
            # begin-unlock_resource_instance

            resource_instance = resource_controller_service.unlock_resource_instance(
                id=instanceGuid
            ).get_result()

            print(json.dumps(resource_instance, indent=2))

            # end-unlock_resource_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_resource_instance_example(self):
        """
        delete_resource_instance request example
        """
        try:
            global instanceGuid
            # begin-delete_resource_instance

            response = resource_controller_service.delete_resource_instance(
                id=instanceGuid
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_resource_instance

            #wait for reclamation object to be created
            time.sleep(20)

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_reclamations_example(self):
        """
        list_reclamations request example
        """
        try:
            global instanceGuid, reclamationId, accountId
            # begin-list_reclamations

            reclamations_list = resource_controller_service.list_reclamations(
                account_id=accountId
            ).get_result()

            for res in reclamations_list.get('resources'):
                if res.get('resource_instance_id') == instanceGuid:
                    reclamationId = res.get('id')

            print(json.dumps(reclamations_list, indent=2))

            # end-list_reclamations

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_run_reclamation_action_example(self):
        """
        run_reclamation_action request example
        """
        try:
            global reclamationId, reclaimAction
            # begin-run_reclamation_action
            
            reclamation = resource_controller_service.run_reclamation_action(
                id=reclamationId,
                action_name=reclaimAction
            ).get_result()

            print(json.dumps(reclamation, indent=2))

            # end-run_reclamation_action

        except ApiException as e:
            pytest.fail(str(e))
            # print(str(e))

# endregion
##############################################################################
# End of Examples for Service: ResourceControllerV2
##############################################################################
