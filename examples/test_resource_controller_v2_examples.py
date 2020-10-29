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
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.resource_controller_v2 import *

# Config file name
config_file = 'resource_controller.env'

resource_controller_service = None

config = None


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

            resource_controller_service = ResourceControllerV2.new_instance(
            )

            # end-common
            assert resource_controller_service is not None

            # Load the configuration
            global config
            config = read_external_sources(
                ResourceControllerV2.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_list_resource_instances_example(self):
        """
        list_resource_instances request example
        """
        try:
            # begin-list_resource_instances

            resource_instances_list = resource_controller_service.list_resource_instances(
                updated_from='2019-01-08T00:00:00.000Z',
                updated_to='2019-01-08T00:00:00.000Z'
            ).get_result()

            print(json.dumps(resource_instances_list, indent=2))

            # end-list_resource_instances

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_resource_instance_example(self):
        """
        create_resource_instance request example
        """
        try:
            # begin-create_resource_instance

            resource_instance = resource_controller_service.create_resource_instance(
                name='my-instance',
                target='bluemix-us-south',
                resource_group='5c49eabc-f5e8-5881-a37e-2d100a33b3df',
                resource_plan_id='cloudant-standard'
            ).get_result()

            print(json.dumps(resource_instance, indent=2))

            # end-create_resource_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resource_instance_example(self):
        """
        get_resource_instance request example
        """
        try:
            # begin-get_resource_instance

            resource_instance = resource_controller_service.get_resource_instance(
                id='testString'
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
            # begin-update_resource_instance

            resource_instance = resource_controller_service.update_resource_instance(
                id='testString',
            ).get_result()

            print(json.dumps(resource_instance, indent=2))

            # end-update_resource_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_lock_resource_instance_example(self):
        """
        lock_resource_instance request example
        """
        try:
            # begin-lock_resource_instance

            resource_instance = resource_controller_service.lock_resource_instance(
                id='testString'
            ).get_result()

            print(json.dumps(resource_instance, indent=2))

            # end-lock_resource_instance

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
                updated_from='2019-01-08T00:00:00.000Z',
                updated_to='2019-01-08T00:00:00.000Z'
            ).get_result()

            print(json.dumps(resource_keys_list, indent=2))

            # end-list_resource_keys

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_resource_key_example(self):
        """
        create_resource_key request example
        """
        try:
            # begin-create_resource_key

            resource_key = resource_controller_service.create_resource_key(
                name='my-key',
                source='25eba2a9-beef-450b-82cf-f5ad5e36c6dd'
            ).get_result()

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
            # begin-get_resource_key

            resource_key = resource_controller_service.get_resource_key(
                id='testString'
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
            # begin-update_resource_key

            resource_key = resource_controller_service.update_resource_key(
                id='testString',
                name='my-new-key-name'
            ).get_result()

            print(json.dumps(resource_key, indent=2))

            # end-update_resource_key

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
                updated_from='2019-01-08T00:00:00.000Z',
                updated_to='2019-01-08T00:00:00.000Z'
            ).get_result()

            print(json.dumps(resource_bindings_list, indent=2))

            # end-list_resource_bindings

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_resource_binding_example(self):
        """
        create_resource_binding request example
        """
        try:
            # begin-create_resource_binding

            resource_binding = resource_controller_service.create_resource_binding(
                source='25eba2a9-beef-450b-82cf-f5ad5e36c6dd',
                target='crn:v1:cf:public:cf:us-south:s/0ba4dba0-a120-4a1e-a124-5a249a904b76::cf-application:a1caa40b-2c24-4da8-8267-ac2c1a42ad0c'
            ).get_result()

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
            # begin-get_resource_binding

            resource_binding = resource_controller_service.get_resource_binding(
                id='testString'
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
            # begin-update_resource_binding

            resource_binding = resource_controller_service.update_resource_binding(
                id='testString',
                name='my-new-binding-name'
            ).get_result()

            print(json.dumps(resource_binding, indent=2))

            # end-update_resource_binding

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
                updated_from='2019-01-08T00:00:00.000Z',
                updated_to='2019-01-08T00:00:00.000Z'
            ).get_result()

            print(json.dumps(resource_aliases_list, indent=2))

            # end-list_resource_aliases

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_resource_alias_example(self):
        """
        create_resource_alias request example
        """
        try:
            # begin-create_resource_alias

            resource_alias = resource_controller_service.create_resource_alias(
                name='my-alias',
                source='a8dff6d3-d287-4668-a81d-c87c55c2656d',
                target='crn:v1:cf:public:cf:us-south:o/5e939cd5-6377-4383-b9e0-9db22cd11753::cf-space:66c8b915-101a-406c-a784-e6636676e4f5'
            ).get_result()

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
            # begin-get_resource_alias

            resource_alias = resource_controller_service.get_resource_alias(
                id='testString'
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
            # begin-update_resource_alias

            resource_alias = resource_controller_service.update_resource_alias(
                id='testString',
                name='my-new-alias-name'
            ).get_result()

            print(json.dumps(resource_alias, indent=2))

            # end-update_resource_alias

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_reclamations_example(self):
        """
        list_reclamations request example
        """
        try:
            # begin-list_reclamations

            reclamations_list = resource_controller_service.list_reclamations().get_result()

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
            # begin-run_reclamation_action

            reclamation = resource_controller_service.run_reclamation_action(
                id='testString',
                action_name='testString'
            ).get_result()

            print(json.dumps(reclamation, indent=2))

            # end-run_reclamation_action

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_unlock_resource_instance_example(self):
        """
        unlock_resource_instance request example
        """
        try:
            # begin-unlock_resource_instance

            resource_instance = resource_controller_service.unlock_resource_instance(
                id='testString'
            ).get_result()

            print(json.dumps(resource_instance, indent=2))

            # end-unlock_resource_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_resource_key_example(self):
        """
        delete_resource_key request example
        """
        try:
            # begin-delete_resource_key

            response = resource_controller_service.delete_resource_key(
                id='testString'
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_resource_key

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_resource_instance_example(self):
        """
        delete_resource_instance request example
        """
        try:
            # begin-delete_resource_instance

            response = resource_controller_service.delete_resource_instance(
                id='testString'
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_resource_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_resource_binding_example(self):
        """
        delete_resource_binding request example
        """
        try:
            # begin-delete_resource_binding

            response = resource_controller_service.delete_resource_binding(
                id='testString'
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_resource_binding

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_resource_alias_example(self):
        """
        delete_resource_alias request example
        """
        try:
            # begin-delete_resource_alias

            response = resource_controller_service.delete_resource_alias(
                id='testString'
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_resource_alias

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: ResourceControllerV2
##############################################################################
