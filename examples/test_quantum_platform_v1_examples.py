# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.
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
Examples for QuantumPlatformV1
"""

import json
import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.global_catalog_v1 import GlobalCatalogV1
from ibm_platform_services.quantum_platform_v1 import *
from ibm_platform_services.resource_controller_v2 import ResourceControllerV2, ResourceInstancesPager

#
# This file provides examples of how to use the IBM Quantum Platform REST service.
#
# The following configuration properties are assumed to be defined:
#
# QUANTUM_PLATFORM_URL=<service url, optional>
# QUANTUM_PLATFORM_AUTH_TYPE=iam
# QUANTUM_PLATFORM_AUTH_URL=<IAM token service URL - omit this if using the production environment>
# QUANTUM_PLATFORM_APIKEY=<IBM Cloud API key>
# QUANTUM_PLATFORM_INSTANCE_CRN=<IBM Quantum Platform instance CRN>
# QUANTUM_PLATFORM_API_VERSION=2026-03-15
#
# RESOURCE_CONTROLLER_URL=<service url, optional>
# RESOURCE_CONTROLLER_AUTH_TYPE=iam
# RESOURCE_CONTROLLER_APIKEY=<IBM Cloud API key>
#
# GLOBAL_CATALOG_URL=<service url, optional>
# GLOBAL_CATALOG_AUTH_TYPE=iam
# GLOBAL_CATALOG_APIKEY=<IBM Cloud API key>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
# Qiskit credentials stored in ~/.qiskit/qiskit-ibm.json are not read automatically
# by this SDK. If qiskit-ibm-runtime is installed, callers can read saved accounts
# and use the saved token as an IBM Cloud API key:
#
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, BearerTokenAuthenticator
# from qiskit_ibm_runtime import QiskitRuntimeService
#
# account = QiskitRuntimeService.saved_accounts(channel='ibm_cloud')['default-ibm-cloud']
# authenticator = IAMAuthenticator(account['token'])
# quantum_platform_service = QuantumPlatformV1(
#     authenticator=authenticator,
#     instance_crn=account['instance'],
# )
# resource_controller_service = ResourceControllerV2(authenticator=authenticator)
#
# Use BearerTokenAuthenticator only when you already have an issued bearer/access token,
# not for qiskit-ibm-runtime saved account tokens.
#
config_file = 'quantum_platform.env'

quantum_platform_service = None
resource_controller_service = None
global_catalog_service = None
config = None


class TestQuantumPlatformV1Examples:
    """
    Example Test Class for QuantumPlatformV1
    """

    @classmethod
    def setup_class(cls):
        global quantum_platform_service
        global resource_controller_service
        global global_catalog_service
        global config

        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            quantum_platform_service = QuantumPlatformV1.new_instance()
            resource_controller_service = ResourceControllerV2.new_instance()
            global_catalog_service = GlobalCatalogV1.new_instance()

            # end-common
            assert quantum_platform_service is not None
            assert resource_controller_service is not None
            assert global_catalog_service is not None

            config = read_external_sources(QuantumPlatformV1.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_discover_quantum_instance_crns_example(self):
        """
        discover quantum instance CRNs request example
        """
        try:
            print('\ndiscover quantum instance CRNs result:')
            # begin-discover_quantum_instance_crns

            catalog_entries = global_catalog_service.list_catalog_entries(
                q='name:quantum-computing kind:service',
                limit=10,
            ).get_result()
            quantum_service = next(
                entry
                for entry in catalog_entries['resources']
                if entry.get('name') == 'quantum-computing'
            )

            all_results = []
            pager = ResourceInstancesPager(
                client=resource_controller_service,
                type='service_instance',
                resource_id=quantum_service['id'],
                limit=50,
            )

            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            for instance in all_results:
                print(
                    json.dumps(
                        {
                            'name': instance.get('name'),
                            'crn': instance.get('crn'),
                            'region_id': instance.get('region_id'),
                            'resource_plan_id': instance.get('resource_plan_id'),
                        },
                        indent=2,
                    )
                )

            # end-discover_quantum_instance_crns
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_backends_example(self):
        """
        list_backends request example
        """
        try:
            print('\nlist_backends() result:')
            # begin-list_backends

            response = quantum_platform_service.list_backends()
            backends = response.get_result()

            print(json.dumps(backends, indent=2))

            # end-list_backends
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_usage_example(self):
        """
        get_usage request example
        """
        try:
            print('\nget_usage() result:')
            # begin-get_usage

            response = quantum_platform_service.get_usage()
            usage = response.get_result()

            print(json.dumps(usage, indent=2))

            # end-get_usage
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_find_instance_workloads_example(self):
        """
        find_instance_workloads request example
        """
        try:
            print('\nfind_instance_workloads() result:')
            # begin-find_instance_workloads

            response = quantum_platform_service.find_instance_workloads(limit=10)
            workloads = response.get_result()

            print(json.dumps(workloads, indent=2))

            # end-find_instance_workloads
        except ApiException as e:
            pytest.fail(str(e))
