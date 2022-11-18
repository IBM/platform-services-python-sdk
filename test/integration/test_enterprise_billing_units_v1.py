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
Integration Tests for EnterpriseBillingUnitsV1
"""

import os
import json
import pytest
from ibm_cloud_sdk_core import *
from ibm_platform_services.enterprise_billing_units_v1 import *

# Config file name
config_file = 'enterprise_billing_units.env'


class TestEnterpriseBillingUnitsV1:
    """
    Integration Test Class for EnterpriseBillingUnitsV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.enterprise_billing_units_service = EnterpriseBillingUnitsV1.new_instance()
            assert cls.enterprise_billing_units_service is not None

            cls.config = read_external_sources(EnterpriseBillingUnitsV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.ENTERPRISE_ID = cls.config.get("ENTERPRISE_ID")
            cls.ACCOUNT_ID = cls.config.get("ACCOUNT_ID")
            cls.ACCOUNT_GROUP_ID = cls.config.get("ACCOUNT_GROUP_ID")
            cls.BILLING_UNIT_ID = cls.config.get("BILLING_UNIT_ID")
            assert cls.ENTERPRISE_ID is not None
            assert cls.ACCOUNT_ID is not None
            assert cls.ACCOUNT_GROUP_ID is not None
            assert cls.BILLING_UNIT_ID is not None

        print('\nService URL: ', cls.enterprise_billing_units_service.service_url)
        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_billing_unit(self):

        get_billing_unit_response = self.enterprise_billing_units_service.get_billing_unit(
            billing_unit_id=self.BILLING_UNIT_ID
        )

        assert get_billing_unit_response.get_status_code() == 200
        billing_unit = get_billing_unit_response.get_result()
        assert billing_unit is not None
        print('get_billing_unit() result: ', json.dumps(billing_unit))

    @needscredentials
    def test_list_billing_units_1(self):

        list_billing_units_response = self.enterprise_billing_units_service.list_billing_units(
            enterprise_id=self.ENTERPRISE_ID
        )

        assert list_billing_units_response.get_status_code() == 200
        billing_units_list = list_billing_units_response.get_result()
        assert billing_units_list is not None
        print('list_billing_units(enterprise id) result: ', json.dumps(billing_units_list))

    @needscredentials
    def test_list_billing_units_2(self):

        list_billing_units_response = self.enterprise_billing_units_service.list_billing_units(
            account_id=self.ACCOUNT_ID
        )

        assert list_billing_units_response.get_status_code() == 200
        billing_units_list = list_billing_units_response.get_result()
        assert billing_units_list is not None
        print('list_billing_units(account id) result: ', json.dumps(billing_units_list))

    @needscredentials
    def test_list_billing_units_3(self):

        list_billing_units_response = self.enterprise_billing_units_service.list_billing_units(
            account_group_id=self.ACCOUNT_GROUP_ID
        )

        assert list_billing_units_response.get_status_code() == 200
        billing_units_list = list_billing_units_response.get_result()
        assert billing_units_list is not None
        print('list_billing_units(account group id) result: ', json.dumps(billing_units_list))

    @needscredentials
    def test_list_billing_options(self):

        list_billing_options_response = self.enterprise_billing_units_service.list_billing_options(
            billing_unit_id=self.BILLING_UNIT_ID
        )

        assert list_billing_options_response.get_status_code() == 200
        billing_options_list = list_billing_options_response.get_result()
        assert billing_options_list is not None
        print('list_billing_options() result: ', json.dumps(billing_options_list))

    @needscredentials
    def test_get_credit_pools(self):

        get_credit_pools_response = self.enterprise_billing_units_service.get_credit_pools(
            billing_unit_id=self.BILLING_UNIT_ID, type='PLATFORM'
        )

        assert get_credit_pools_response.get_status_code() == 200
        credit_pools_list = get_credit_pools_response.get_result()
        assert credit_pools_list is not None
        print('get_credit_pools() result: ', json.dumps(credit_pools_list))
