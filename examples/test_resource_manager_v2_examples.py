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
Examples for ResourceManagerV2
"""

import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.resource_manager_v2 import *

#
# This file provides an example of how to use the Resource Manager service.
#
# The following configuration properties are assumed to be defined:
# RESOURCE_MANAGER_URL=<service base url>
# RESOURCE_MANAGER_AUTH_TYPE=iam
# RESOURCE_MANAGER_APIKEY=<IAM apikey>
# RESOURCE_MANAGER_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'resource_manager_v2.env'

resource_manager_service = None

config = None


##############################################################################
# Start of Examples for Service: ResourceManagerV2
##############################################################################
# region
class TestResourceManagerV2Examples():
    """
    Example Test Class for ResourceManagerV2
    """

    @classmethod
    def setup_class(cls):
        global resource_manager_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            resource_manager_service = ResourceManagerV2.new_instance(
            )

            # end-common
            assert resource_manager_service is not None

            # Load the configuration
            global config
            config = read_external_sources(ResourceManagerV2.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_list_resource_groups_example(self):
        """
        list_resource_groups request example
        """
        try:
            # begin-list_resource_groups

            resource_group_list = resource_manager_service.list_resource_groups().get_result()

            print(json.dumps(resource_group_list, indent=2))

            # end-list_resource_groups

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_resource_group_example(self):
        """
        create_resource_group request example
        """
        try:
            # begin-create_resource_group

            res_create_resource_group = resource_manager_service.create_resource_group().get_result()

            print(json.dumps(res_create_resource_group, indent=2))

            # end-create_resource_group

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resource_group_example(self):
        """
        get_resource_group request example
        """
        try:
            # begin-get_resource_group

            resource_group = resource_manager_service.get_resource_group(
                id='testString'
            ).get_result()

            print(json.dumps(resource_group, indent=2))

            # end-get_resource_group

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_resource_group_example(self):
        """
        update_resource_group request example
        """
        try:
            # begin-update_resource_group

            resource_group = resource_manager_service.update_resource_group(
                id='testString'
            ).get_result()

            print(json.dumps(resource_group, indent=2))

            # end-update_resource_group

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_quota_definitions_example(self):
        """
        list_quota_definitions request example
        """
        try:
            # begin-list_quota_definitions

            quota_definition_list = resource_manager_service.list_quota_definitions().get_result()

            print(json.dumps(quota_definition_list, indent=2))

            # end-list_quota_definitions

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_quota_definition_example(self):
        """
        get_quota_definition request example
        """
        try:
            # begin-get_quota_definition

            quota_definition = resource_manager_service.get_quota_definition(
                id='testString'
            ).get_result()

            print(json.dumps(quota_definition, indent=2))

            # end-get_quota_definition

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_resource_group_example(self):
        """
        delete_resource_group request example
        """
        try:
            # begin-delete_resource_group

            response = resource_manager_service.delete_resource_group(
                id='testString'
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_resource_group

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: ResourceManagerV2
##############################################################################
