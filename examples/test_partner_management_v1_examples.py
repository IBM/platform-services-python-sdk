# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2024.
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
Examples for PartnerManagementV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from ibm_platform_services.partner_management_v1 import *

#
# This file provides an example of how to use the Partner Management service.
#
# The following configuration properties are assumed to be defined:
# PARTNER_MANAGEMENT_URL=<service base url>
# PARTNER_MANAGEMENT_AUTH_TYPE=iam
# PARTNER_MANAGEMENT_APIKEY=<IAM apikey>
# PARTNER_MANAGEMENT_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'partner_management_v1.env'

partner_management_service = None

config = None
partner_id = None
billing_month = None


##############################################################################
# Start of Examples for Service: PartnerManagementV1
##############################################################################
# region
class TestPartnerManagementV1Examples:
    """
    Example Test Class for PartnerManagementV1
    """

    @classmethod
    def setup_class(cls):
        global partner_management_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            partner_management_service = PartnerManagementV1.new_instance()

            # end-common
            assert partner_management_service is not None

            # Load the configuration
            global config
            config = read_external_sources(PartnerManagementV1.DEFAULT_SERVICE_NAME)

            global partner_id
            partner_id = config.get("PARTNER_ID")

            global billing_month
            billing_month = config.get("BILLING_MONTH")

            assert partner_id is not None
            assert billing_month is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_resource_usage_report_example(self):
        """
        get_resource_usage_report request example
        """
        try:
            print('\nget_resource_usage_report() result:')

            # begin-get_resource_usage_report

            all_results = []
            pager = GetResourceUsageReportPager(
                client=partner_management_service,
                partner_id=partner_id,
                month=billing_month,
                limit=10,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-get_resource_usage_report
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_billing_options_example(self):
        """
        get_billing_options request example
        """
        try:
            print('\nget_billing_options() result:')

            # begin-get_billing_options

            response = partner_management_service.get_billing_options(
                partner_id=partner_id,
                date=billing_month,
            )
            billing_options_summary = response.get_result()

            print(json.dumps(billing_options_summary, indent=2))

            # end-get_billing_options

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_credit_pools_report_example(self):
        """
        get_credit_pools_report request example
        """
        try:
            print('\nget_credit_pools_report() result:')

            # begin-get_credit_pools_report

            response = partner_management_service.get_credit_pools_report(
                partner_id=partner_id,
                date=billing_month,
            )
            credit_pools_report_summary = response.get_result()

            print(json.dumps(credit_pools_report_summary, indent=2))

            # end-get_credit_pools_report

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: PartnerManagementV1
##############################################################################
