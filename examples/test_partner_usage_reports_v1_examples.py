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
Examples for PartnerUsageReportsV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from ibm_platform_services.partner_usage_reports_v1 import *

#
# This file provides an example of how to use the Partner Usage Reports service.
#
# The following configuration properties are assumed to be defined:
# PARTNER_USAGE_REPORTS_URL=<service base url>
# PARTNER_USAGE_REPORTS_AUTH_TYPE=iam
# PARTNER_USAGE_REPORTS_APIKEY=<IAM apikey>
# PARTNER_USAGE_REPORTS_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
# PARTNER_USAGE_REPORTS_PARTNER_ID=<Enterprise ID of the distributor or reseller for which the report is requested>
# PARTNER_USAGE_REPORTS_CUSTOMER_ID=<Enterprise ID of the child customer for which the report is requested>
# PARTNER_USAGE_REPORTS_RESELLER_ID=<Enterprise ID of the reseller for which the report is requested>
# PARTNER_USAGE_REPORTS_BILLING_MONTH=<The billing month for which the usage report is requested. Format is `yyyy-mm`>
# PARTNER_USAGE_REPORTS_VIEWPOINT=<Enables partner to view the cost of provisioned services as applicable at each level of the hierarchy>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'partner_usage_reports_v1.env'

partner_usage_reports_service = None

config = None
partner_id = None
billing_month = None


##############################################################################
# Start of Examples for Service: PartnerUsageReportsV1
##############################################################################
# region
class TestPartnerUsageReportsV1Examples:
    """
    Example Test Class for PartnerUsageReportsV1
    """

    @classmethod
    def setup_class(cls):
        global partner_usage_reports_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            partner_usage_reports_service = PartnerUsageReportsV1.new_instance()

            # end-common
            assert partner_usage_reports_service is not None

            # Load the configuration
            global config
            config = read_external_sources(PartnerUsageReportsV1.DEFAULT_SERVICE_NAME)

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
                client=partner_usage_reports_service,
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


# endregion
##############################################################################
# End of Examples for Service: PartnerUsageReportsV1
##############################################################################
