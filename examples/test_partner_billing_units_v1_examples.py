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
Examples for PartnerBillingUnitsV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from ibm_platform_services.partner_billing_units_v1 import *

#
# This file provides an example of how to use the Partner Billing Units service.
#
# The following configuration properties are assumed to be defined:
# PARTNER_BILLING_UNITS_URL=<service base url>
# PARTNER_BILLING_UNITS_AUTH_TYPE=iam
# PARTNER_BILLING_UNITS_APIKEY=<IAM apikey>
# PARTNER_BILLING_UNITS_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'partner_billing_units_v1.env'

partner_billing_units_service = None

config = None
partner_id = None
billing_month = None


##############################################################################
# Start of Examples for Service: PartnerBillingUnitsV1
##############################################################################
# region
class TestPartnerBillingUnitsV1Examples:
    """
    Example Test Class for PartnerBillingUnitsV1
    """

    @classmethod
    def setup_class(cls):
        global partner_billing_units_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            partner_billing_units_service = PartnerBillingUnitsV1.new_instance()

            # end-common
            assert partner_billing_units_service is not None

            # Load the configuration
            global config
            config = read_external_sources(PartnerBillingUnitsV1.DEFAULT_SERVICE_NAME)

            # Retrieve and verify some additional test-related config properties.
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
    def test_get_billing_options_example(self):
        """
        get_billing_options request example
        """
        try:
            print('\nget_billing_options() result:')
            # begin-get_billing_options

            response = partner_billing_units_service.get_billing_options(
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

            response = partner_billing_units_service.get_credit_pools_report(
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
# End of Examples for Service: PartnerBillingUnitsV1
##############################################################################
