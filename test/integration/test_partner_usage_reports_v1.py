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
Integration Tests for PartnerUsageReportsV1
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_platform_services.partner_usage_reports_v1 import *

# Config file name
config_file = 'partner_usage_reports_v1.env'


class TestPartnerUsageReportsV1:
    """
    Integration Test Class for PartnerUsageReportsV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.partner_usage_reports_service = PartnerUsageReportsV1.new_instance()
            assert cls.partner_usage_reports_service is not None

            cls.config = read_external_sources(PartnerUsageReportsV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.partner_usage_reports_service.enable_retries()

            cls.PARTNER_ID = cls.config.get("PARTNER_ID")
            cls.RESELLER_ID = cls.config.get("RESELLER_ID")
            cls.CUSTOMER_ID = cls.config.get("CUSTOMER_ID")
            cls.BILLING_MONTH = cls.config.get("BILLING_MONTH")
            cls.VIEWPOINT = cls.config.get("VIEWPOINT")
            assert cls.PARTNER_ID is not None
            assert cls.RESELLER_ID is not None
            assert cls.CUSTOMER_ID is not None
            assert cls.BILLING_MONTH is not None
            assert cls.VIEWPOINT is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_resource_usage_report_partner(self):
        response = self.partner_usage_reports_service.get_resource_usage_report(
            partner_id=self.PARTNER_ID,
            month=self.BILLING_MONTH,
            limit=30,
        )

        assert response.get_status_code() == 200
        partner_usage_report_summary = response.get_result()
        assert partner_usage_report_summary is not None

    @needscredentials
    def test_get_resource_usage_report_with_pager_partner(self):
        all_results = []

        # Test get_next().
        pager = GetResourceUsageReportPager(
            client=self.partner_usage_reports_service,
            partner_id=self.PARTNER_ID,
            month=self.BILLING_MONTH,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = GetResourceUsageReportPager(
            client=self.partner_usage_reports_service,
            partner_id=self.PARTNER_ID,
            month=self.BILLING_MONTH,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(
            f'\nget_resource_usage_report() returned a total of {len(all_results)} items(s) using GetResourceUsageReportPager.'
        )

    @needscredentials
    def test_get_resource_usage_report_reseller_for_partner(self):
        response = self.partner_usage_reports_service.get_resource_usage_report(
            partner_id=self.PARTNER_ID,
            children=True,
            month=self.BILLING_MONTH,
            limit=30,
        )

        assert response.get_status_code() == 200
        partner_usage_report_summary = response.get_result()
        assert partner_usage_report_summary is not None

    @needscredentials
    def test_get_resource_usage_report_with_pager_reseller_for_partner(self):
        all_results = []

        # Test get_next().
        pager = GetResourceUsageReportPager(
            client=self.partner_usage_reports_service,
            partner_id=self.PARTNER_ID,
            children=True,
            month=self.BILLING_MONTH,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = GetResourceUsageReportPager(
            client=self.partner_usage_reports_service,
            partner_id=self.PARTNER_ID,
            children=True,
            month=self.BILLING_MONTH,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(
            f'\nget_resource_usage_report() returned a total of {len(all_results)} items(s) using GetResourceUsageReportPager.'
        )

    @needscredentials
    def test_get_resource_usage_report_specific_reseller(self):
        response = self.partner_usage_reports_service.get_resource_usage_report(
            partner_id=self.PARTNER_ID,
            reseller_id=self.RESELLER_ID,
            month=self.BILLING_MONTH,
            limit=30,
        )

        assert response.get_status_code() == 200
        partner_usage_report_summary = response.get_result()
        assert partner_usage_report_summary is not None

    @needscredentials
    def test_get_resource_usage_report_with_pager_specific_reseller(self):
        all_results = []

        # Test get_next().
        pager = GetResourceUsageReportPager(
            client=self.partner_usage_reports_service,
            partner_id=self.PARTNER_ID,
            reseller_id=self.RESELLER_ID,
            month=self.BILLING_MONTH,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = GetResourceUsageReportPager(
            client=self.partner_usage_reports_service,
            partner_id=self.PARTNER_ID,
            reseller_id=self.RESELLER_ID,
            month=self.BILLING_MONTH,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(
            f'\nget_resource_usage_report() returned a total of {len(all_results)} items(s) using GetResourceUsageReportPager.'
        )

    @needscredentials
    def test_get_resource_usage_report_specific_customer(self):
        response = self.partner_usage_reports_service.get_resource_usage_report(
            partner_id=self.PARTNER_ID,
            customer_id=self.CUSTOMER_ID,
            month=self.BILLING_MONTH,
            limit=30,
        )

        assert response.get_status_code() == 200
        partner_usage_report_summary = response.get_result()
        assert partner_usage_report_summary is not None

    @needscredentials
    def test_get_resource_usage_report_with_pager_specific_customer(self):
        all_results = []

        # Test get_next().
        pager = GetResourceUsageReportPager(
            client=self.partner_usage_reports_service,
            partner_id=self.PARTNER_ID,
            customer_id=self.CUSTOMER_ID,
            month=self.BILLING_MONTH,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = GetResourceUsageReportPager(
            client=self.partner_usage_reports_service,
            partner_id=self.PARTNER_ID,
            customer_id=self.CUSTOMER_ID,
            month=self.BILLING_MONTH,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(
            f'\nget_resource_usage_report() returned a total of {len(all_results)} items(s) using GetResourceUsageReportPager.'
        )

    @needscredentials
    def test_get_resource_usage_report_recursive(self):
        response = self.partner_usage_reports_service.get_resource_usage_report(
            partner_id=self.PARTNER_ID,
            month=self.BILLING_MONTH,
            recurse=True,
            limit=30,
        )

        assert response.get_status_code() == 200
        partner_usage_report_summary = response.get_result()
        assert partner_usage_report_summary is not None

    @needscredentials
    def test_get_resource_usage_report_with_pager_recursive(self):
        all_results = []

        # Test get_next().
        pager = GetResourceUsageReportPager(
            client=self.partner_usage_reports_service,
            partner_id=self.PARTNER_ID,
            month=self.BILLING_MONTH,
            recurse=True,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = GetResourceUsageReportPager(
            client=self.partner_usage_reports_service,
            partner_id=self.PARTNER_ID,
            month=self.BILLING_MONTH,
            recurse=True,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(
            f'\nget_resource_usage_report() returned a total of {len(all_results)} items(s) using GetResourceUsageReportPager.'
        )

    @needscredentials
    def test_get_resource_usage_report_viewpoint(self):
        response = self.partner_usage_reports_service.get_resource_usage_report(
            partner_id=self.PARTNER_ID,
            children=True,
            month=self.BILLING_MONTH,
            viewpoint=self.VIEWPOINT,
            limit=30,
        )

        assert response.get_status_code() == 200
        partner_usage_report_summary = response.get_result()
        assert partner_usage_report_summary is not None

    @needscredentials
    def test_get_resource_usage_report_with_pager_viewpoint(self):
        all_results = []

        # Test get_next().
        pager = GetResourceUsageReportPager(
            client=self.partner_usage_reports_service,
            partner_id=self.PARTNER_ID,
            children=True,
            month=self.BILLING_MONTH,
            viewpoint=self.VIEWPOINT,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = GetResourceUsageReportPager(
            client=self.partner_usage_reports_service,
            partner_id=self.PARTNER_ID,
            children=True,
            month=self.BILLING_MONTH,
            viewpoint=self.VIEWPOINT,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(
            f'\nget_resource_usage_report() returned a total of {len(all_results)} items(s) using GetResourceUsageReportPager.'
        )
