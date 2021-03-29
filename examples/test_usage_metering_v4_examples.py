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
Examples for UsageMeteringV4
"""

import os
import pytest
import time
from ibm_cloud_sdk_core import ApiException
from ibm_platform_services.usage_metering_v4 import *

#
# This file provides an example of how to use the Usage Metering service.
#
# The following configuration properties are assumed to be defined:
#
# USAGE_METERING_URL=<service url>
# USAGE_METERING_AUTHTYPE=iam
# USAGE_METERING_APIKEY=<your iam apikey>
# USAGE_METERING_AUTH_URL=<IAM token service URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'usage_metering.env'

usage_metering_service = None

config = None


##############################################################################
# Start of Examples for Service: UsageMeteringV4
##############################################################################
# region
class TestUsageMeteringV4Examples():
    """
    Example Test Class for UsageMeteringV4
    """
    @classmethod
    def setup_class(cls):
        global usage_metering_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            usage_metering_service = UsageMeteringV4.new_instance()

            # end-common
            assert usage_metering_service is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file),
        reason="External configuration not available, skipping...")

    @needscredentials
    def test_report_resource_usage_example(self):
        """
        report_resource_usage request example
        """
        try:
            # Get current time in ms since epoch.
            start_time = int(time.time() * 1000)
            end_time = start_time

            resource_id = 'cloudant'
            resource_instance_id = 'crn:v1:staging:public:cloudantnosqldb:us-south:a/f5086e3df886495991303628d21da513:3aafbbee-88e2-4d29-b144-9d267d97064c::'
            plan_id = 'cloudant-standard'
            region = 'us-south'

            # begin-report_resource_usage

            # Report usage for a mythical resource.
            # Use zero for quantities since this is only an example.
            measures = [
                {
                    'measure': 'LOOKUP',
                    'quantity': 0,
                },
                {
                    'measure': 'WRITE',
                    'quantity': 0,
                },
                {
                    'measure': 'QUERY',
                    'quantity': 0,
                },
                {
                    'measure': 'GIGABYTE',
                    'quantity': 0,
                },
            ]

            resource_instance_usage_model = {
                'resource_instance_id': resource_instance_id,
                'plan_id': plan_id,
                'region': region,
                'start': start_time,
                'end': end_time,
                'measured_usage': measures,
            }

            response_accepted = usage_metering_service.report_resource_usage(
                resource_id=resource_id,
                resource_usage=[resource_instance_usage_model]).get_result()

            print('\nreport_resource_usage() result:\n' + json.dumps(response_accepted, indent=2))

            # end-report_resource_usage

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: UsageMeteringV4
##############################################################################
