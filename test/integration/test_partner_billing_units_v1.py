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
Integration Tests for PartnerBillingUnitsV1
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_platform_services.partner_billing_units_v1 import *

# Config file name
config_file = 'partner_billing_units_v1.env'


class TestPartnerBillingUnitsV1:
    """
    Integration Test Class for PartnerBillingUnitsV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.partner_billing_units_service = PartnerBillingUnitsV1.new_instance()
            assert cls.partner_billing_units_service is not None

            cls.config = read_external_sources(PartnerBillingUnitsV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.PARTNER_ID = cls.config.get("PARTNER_ID")
            cls.CUSTOMER_ID = cls.config.get("CUSTOMER_ID")
            cls.RESELLER_ID = cls.config.get("RESELLER_ID")
            cls.BILLING_MONTH = cls.config.get("BILLING_MONTH")
            assert cls.PARTNER_ID is not None
            assert cls.CUSTOMER_ID is not None
            assert cls.RESELLER_ID is not None
            assert cls.BILLING_MONTH is not None

            cls.partner_billing_units_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_billing_options(self):
        response = self.partner_billing_units_service.get_billing_options(
            partner_id=self.PARTNER_ID,
            date=self.BILLING_MONTH,
            limit=30,
        )

        assert response.get_status_code() == 200
        billing_options_summary = response.get_result()
        assert billing_options_summary is not None

    @needscredentials
    def test_get_billing_options_reseller_for_partner(self):
        response = self.partner_billing_units_service.get_billing_options(
            partner_id=self.PARTNER_ID,
            reseller_id=self.RESELLER_ID,
            date=self.BILLING_MONTH,
            limit=30,
        )

        assert response.get_status_code() == 200
        billing_options_summary = response.get_result()
        assert billing_options_summary is not None

    @needscredentials
    def test_get_billing_options_customer_for_partner(self):
        response = self.partner_billing_units_service.get_billing_options(
            partner_id=self.PARTNER_ID,
            customer_id=self.CUSTOMER_ID,
            date=self.BILLING_MONTH,
            limit=30,
        )

        assert response.get_status_code() == 200
        billing_options_summary = response.get_result()
        assert billing_options_summary is not None

    @needscredentials
    def test_get_credit_pools_report(self):
        response = self.partner_billing_units_service.get_credit_pools_report(
            partner_id=self.PARTNER_ID,
            date=self.BILLING_MONTH,
            limit=30,
        )

        assert response.get_status_code() == 200
        credit_pools_report_summary = response.get_result()
        assert credit_pools_report_summary is not None

    @needscredentials
    def test_get_credit_pools_report_reseller_for_partner(self):
        response = self.partner_billing_units_service.get_credit_pools_report(
            partner_id=self.PARTNER_ID,
            reseller_id=self.RESELLER_ID,
            date=self.BILLING_MONTH,
            limit=30,
        )

        assert response.get_status_code() == 200
        credit_pools_report_summary = response.get_result()
        assert credit_pools_report_summary is not None

    @needscredentials
    def test_get_credit_pools_report_customer_for_partner(self):
        response = self.partner_billing_units_service.get_credit_pools_report(
            partner_id=self.PARTNER_ID,
            customer_id=self.CUSTOMER_ID,
            date=self.BILLING_MONTH,
            limit=30,
        )

        assert response.get_status_code() == 200
        credit_pools_report_summary = response.get_result()
        assert credit_pools_report_summary is not None
