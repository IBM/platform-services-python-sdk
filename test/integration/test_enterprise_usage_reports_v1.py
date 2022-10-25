# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020, 2022.
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
Integration Tests for EnterpriseUsageReportsV1
"""

import os
import pytest
from ibm_cloud_sdk_core import *
from ibm_platform_services.enterprise_usage_reports_v1 import *

# Config file name
config_file = 'enterprise_usage_reports.env'


class TestEnterpriseUsageReportsV1():
    """
    Integration Test Class for EnterpriseUsageReportsV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.enterprise_usage_reports_service = EnterpriseUsageReportsV1.new_instance(
            )
            assert cls.enterprise_usage_reports_service is not None

            cls.config = read_external_sources(
                EnterpriseUsageReportsV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            # Retrieve and verify some additional test-related config properties.
            cls.ACCOUNT_ID = cls.config.get("ACCOUNT_ID")
            cls.ACCOUNT_GROUP_ID = cls.config.get("ACCOUNT_GROUP_ID")
            cls.ENTERPRISE_ID = cls.config.get("ENTERPRISE_ID")
            cls.BILLING_MONTH = cls.config.get("BILLING_MONTH")
            assert cls.ACCOUNT_ID is not None
            assert cls.ACCOUNT_GROUP_ID is not None
            assert cls.ENTERPRISE_ID is not None
            assert cls.BILLING_MONTH is not None
        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_resource_usage_report_enterprise(self):
        results = []
        offset = None

        while True:
            get_resource_usage_report_response = self.enterprise_usage_reports_service.get_resource_usage_report(
                enterprise_id=self.ENTERPRISE_ID,
                month=self.BILLING_MONTH,
                limit=1,
                offset=offset,
            )

            assert get_resource_usage_report_response.get_status_code() == 200
            reports = get_resource_usage_report_response.get_result()
            assert reports is not None
            assert 'reports' in reports

            results.extend(reports['reports'])

            next = reports.get('next')
            offset = None
            if next is not None and 'href' in next:
                offset = get_query_param(next['href'], 'offset')

            if offset is None:
                break

        numReports = len(results)
        print(
            f'get_resource_usage_report()/enterprise response contained {numReports} total reports.')
        assert numReports > 0

    @needscredentials
    def test_get_resource_usage_report_account(self):
        results = []
        offset = None

        while True:
            get_resource_usage_report_response = self.enterprise_usage_reports_service.get_resource_usage_report(
                account_id=self.ACCOUNT_ID,
                month=self.BILLING_MONTH,
                limit=1,
                offset=offset,
            )

            assert get_resource_usage_report_response.get_status_code() == 200
            reports = get_resource_usage_report_response.get_result()
            assert reports is not None
            assert 'reports' in reports

            results.extend(reports['reports'])

            next = reports.get('next')
            offset = None
            if next is not None and 'href' in next:
                offset = get_query_param(next['href'], 'offset')

            if offset is None:
                break

        numReports = len(results)
        print(
            f'get_resource_usage_report()/account response contained {numReports} total reports.')
        assert numReports > 0

    @needscredentials
    def test_get_resource_usage_report_account_group(self):
        results = []
        offset = None

        while True:
            get_resource_usage_report_response = self.enterprise_usage_reports_service.get_resource_usage_report(
                account_group_id=self.ACCOUNT_GROUP_ID,
                month=self.BILLING_MONTH,
                limit=1,
                offset=offset,
            )

            assert get_resource_usage_report_response.get_status_code() == 200
            reports = get_resource_usage_report_response.get_result()
            assert reports is not None
            assert 'reports' in reports

            results.extend(reports['reports'])

            next = reports.get('next')
            offset = None
            if next is not None and 'href' in next:
                offset = get_query_param(next['href'], 'offset')

            if offset is None:
                break

        numReports = len(results)
        print(
            f'get_resource_usage_report()/account-group response contained {numReports} total reports.')
        assert numReports > 0

    @needscredentials
    def test_get_resource_usage_report_with_pager(self):
        all_results = []

        # Test get_next().
        pager = GetResourceUsageReportPager(
            client=self.enterprise_usage_reports_service,
            account_group_id=self.ACCOUNT_GROUP_ID,
            month=self.BILLING_MONTH,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = GetResourceUsageReportPager(
            client=self.enterprise_usage_reports_service,
            account_group_id=self.ACCOUNT_GROUP_ID,
            month=self.BILLING_MONTH,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nget_resource_usage_report() returned a total of {len(all_results)} items(s) using GetResourceUsageReportPager.')
