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

#
# This file provides an example of how to use the Open Service Broker service.
#
# The following configuration properties are assumed to be defined:
#
# OPEN_SERVICE_BROKER_URL=<Service broker's URL>
# OPEN_SERVICE_BROKER_AUTH_TYPE=basic
# OPEN_SERVICE_BROKER_USERNAME=<username>
# OPEN_SERVICE_BROKER_PASSWORD=<password>
# OPEN_SERVICE_BROKER_PLAN_ID=<The ID of the plan associated with the service offering>
# OPEN_SERVICE_BROKER_RESOURCE_INSTANCE_ID=<The ID of a previously provisioned service instance>
# OPEN_SERVICE_BROKER_SERVICE_ID=<The ID of the service being offered>
# OPEN_SERVICE_BROKER_ACCOUNT_ID=<User's account ID>
# OPEN_SERVICE_BROKER_BINDING_ID=<The ID of a previously provisioned binding for that service instance>
# OPEN_SERVICE_BROKER_SPACE_GUID=<The identifier for the project space within the IBM Cloud platform organization>
# OPEN_SERVICE_BROKER_APPLICATION_GUID=<GUID of an application associated with the binding>
# OPEN_SERVICE_BROKER_ORGANIZATION_GUID=<The IBM Cloud platform GUID for the organization under which the service instance is to be provisioned>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'open_service_broker.env'

open_service_broker_service = None

config = None

instanceId = None
orgGuid = None
planId = None
serviceId = None
spaceGuid = None
accountId = None
bindingId = None
appGuid = None
initiatorId = 'null'
reasonCode = 'IBMCLOUD_ACCT_SUSPEND'
operation = 'Provision_45'


##############################################################################
# Start of Examples for Service: OpenServiceBrokerV1
##############################################################################
# region
class TestOpenServiceBrokerV1Examples:
    """
    Example Test Class for OpenServiceBrokerV1
    """

    @classmethod
    def setup_class(cls):
        global open_service_broker_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            open_service_broker_service = OpenServiceBrokerV1.new_instance()

            # end-common
            assert open_service_broker_service is not None

            # Load the configuration
            global config
            config = read_external_sources(OpenServiceBrokerV1.DEFAULT_SERVICE_NAME)

            global instanceId
            instanceId = config['RESOURCE_INSTANCE_ID']

            global orgGuid
            orgGuid = config['ORGANIZATION_GUID']

            global planId
            planId = config['PLAN_ID']

            global serviceId
            serviceId = config['SERVICE_ID']

            global spaceGuid
            spaceGuid = config['SPACE_GUID']

            global accountId
            accountId = config['ACCOUNT_ID']

            global bindingId
            bindingId = config['BINDING_ID']

            global appGuid
            appGuid = config['APPLICATION_GUID']

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
            print('\nget_service_instance_state() result:')
            # begin-get_service_instance_state

            response = open_service_broker_service.get_service_instance_state(instance_id=instanceId).get_result()

            print(json.dumps(response, indent=2))

            # end-get_service_instance_state

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_service_instance_state_example(self):
        """
        replace_service_instance_state request example
        """
        try:
            print('\nreplace_service_instance_state() result:')
            # begin-replace_service_instance_state

            response = open_service_broker_service.replace_service_instance_state(
                instance_id=instanceId, enabled=False, initiator_id=initiatorId, reason_code=reasonCode
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-replace_service_instance_state

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_service_instance_example(self):
        """
        replace_service_instance request example
        """
        try:
            print('\nreplace_service_instance() result:')
            # begin-replace_service_instance

            context = Context(account_id=accountId, crn=instanceId, platform='ibmcloud')
            pars = {}
            response = open_service_broker_service.replace_service_instance(
                instance_id=instanceId,
                organization_guid=orgGuid,
                plan_id=planId,
                service_id=serviceId,
                space_guid=spaceGuid,
                context=context,
                parameters=pars,
                accepts_incomplete=True,
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-replace_service_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_service_instance_example(self):
        """
        update_service_instance request example
        """
        try:
            print('\nupdate_service_instance() result:')
            # begin-update_service_instance

            context = Context(account_id=accountId, crn=instanceId, platform='ibmcloud')
            pars = {}
            prevValues = {}
            response = open_service_broker_service.update_service_instance(
                instance_id=instanceId,
                plan_id=planId,
                service_id=serviceId,
                context=context,
                parameters=pars,
                previous_values=prevValues,
                accepts_incomplete=True,
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-update_service_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_catalog_example(self):
        """
        list_catalog request example
        """
        try:
            print('\nlist_catalog() result:')
            # begin-list_catalog

            response = open_service_broker_service.list_catalog().get_result()

            print(json.dumps(response, indent=2))

            # end-list_catalog

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_last_operation_example(self):
        """
        get_last_operation request example
        """
        try:
            print('\nget_last_operation() result:')
            # begin-get_last_operation

            response = open_service_broker_service.get_last_operation(
                instance_id=instanceId, operation=operation, plan_id=planId, service_id=serviceId
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-get_last_operation

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_service_binding_example(self):
        """
        replace_service_binding request example
        """
        try:
            print('\nreplace_service_binding() result:')
            # begin-replace_service_binding

            bindResource = BindResource(account_id=accountId, serviceid_crn=appGuid)
            pars = {}
            response = open_service_broker_service.replace_service_binding(
                binding_id=bindingId,
                instance_id=instanceId,
                plan_id=planId,
                service_id=serviceId,
                bind_resource=bindResource,
                parameters=pars,
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-replace_service_binding

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_service_instance_example(self):
        """
        delete_service_instance request example
        """
        try:
            print('\ndelete_service_instance() result:')
            # begin-delete_service_instance

            response = open_service_broker_service.delete_service_instance(
                instance_id=instanceId,
                plan_id=planId,
                service_id=serviceId,
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_service_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_service_binding_example(self):
        """
        delete_service_binding request example
        """
        try:
            print('\ndelete_service_binding() result:')
            # begin-delete_service_binding

            response = open_service_broker_service.delete_service_binding(
                binding_id=bindingId,
                instance_id=instanceId,
                plan_id=planId,
                service_id=serviceId,
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_service_binding

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: OpenServiceBrokerV1
##############################################################################
