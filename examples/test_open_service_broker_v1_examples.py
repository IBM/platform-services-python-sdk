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
Examples for OpenServiceBrokerV1
"""

import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.open_service_broker_v1 import *

# Config file name
config_file = 'open_service_broker.env'

open_service_broker_service = None

config = None


##############################################################################
# Start of Examples for Service: OpenServiceBrokerV1
##############################################################################
# region
class TestOpenServiceBrokerV1Examples():
    """
    Example Test Class for OpenServiceBrokerV1
    """

    @classmethod
    def setup_class(cls):
        global open_service_broker_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            open_service_broker_service = OpenServiceBrokerV1.new_instance(
            )

            # end-common
            assert open_service_broker_service is not None

            # Load the configuration
            global config
            config = read_external_sources(
                OpenServiceBrokerV1.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_service_instance_state_example(self):
        """
        get_service_instance_state request example
        """
        try:
            # begin-get_service_instance_state

            resp1874644_root = open_service_broker_service.get_service_instance_state(
                instance_id='testString'
            ).get_result()

            print(json.dumps(resp1874644_root, indent=2))

            # end-get_service_instance_state

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_service_instance_state_example(self):
        """
        replace_service_instance_state request example
        """
        try:
            # begin-replace_service_instance_state

            resp2448145_root = open_service_broker_service.replace_service_instance_state(
                instance_id='testString'
            ).get_result()

            print(json.dumps(resp2448145_root, indent=2))

            # end-replace_service_instance_state

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_service_instance_example(self):
        """
        replace_service_instance request example
        """
        try:
            # begin-replace_service_instance

            resp2079872_root = open_service_broker_service.replace_service_instance(
                instance_id='testString'
            ).get_result()

            print(json.dumps(resp2079872_root, indent=2))

            # end-replace_service_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_service_instance_example(self):
        """
        update_service_instance request example
        """
        try:
            # begin-update_service_instance

            resp2079874_root = open_service_broker_service.update_service_instance(
                instance_id='testString'
            ).get_result()

            print(json.dumps(resp2079874_root, indent=2))

            # end-update_service_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_catalog_example(self):
        """
        list_catalog request example
        """
        try:
            # begin-list_catalog

            resp1874650_root = open_service_broker_service.list_catalog().get_result()

            print(json.dumps(resp1874650_root, indent=2))

            # end-list_catalog

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_last_operation_example(self):
        """
        get_last_operation request example
        """
        try:
            # begin-get_last_operation

            resp2079894_root = open_service_broker_service.get_last_operation(
                instance_id='testString'
            ).get_result()

            print(json.dumps(resp2079894_root, indent=2))

            # end-get_last_operation

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_service_binding_example(self):
        """
        replace_service_binding request example
        """
        try:
            # begin-replace_service_binding

            resp2079876_root = open_service_broker_service.replace_service_binding(
                binding_id='testString',
                instance_id='testString'
            ).get_result()

            print(json.dumps(resp2079876_root, indent=2))

            # end-replace_service_binding

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_service_instance_example(self):
        """
        delete_service_instance request example
        """
        try:
            # begin-delete_service_instance

            resp2079874_root = open_service_broker_service.delete_service_instance(
                service_id='testString',
                plan_id='testString',
                instance_id='testString'
            ).get_result()

            print(json.dumps(resp2079874_root, indent=2))

            # end-delete_service_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_service_binding_example(self):
        """
        delete_service_binding request example
        """
        try:
            # begin-delete_service_binding

            response = open_service_broker_service.delete_service_binding(
                binding_id='testString',
                instance_id='testString',
                plan_id='testString',
                service_id='testString'
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_service_binding

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: OpenServiceBrokerV1
##############################################################################
