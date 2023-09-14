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
Integration Tests for UsageReportsV4
"""

import os
import pytest
from ibm_cloud_sdk_core import *
from ibm_platform_services.usage_reports_v4 import *

# Config file name
config_file = 'usage_reports.env'


class TestUsageReportsV4:
    """
    Integration Test Class for UsageReportsV4
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.usage_reports_service = UsageReportsV4.new_instance()
            assert cls.usage_reports_service is not None

            cls.config = read_external_sources(UsageReportsV4.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            # Retrieve and verify some additional test-related config properties.
            cls.ACCOUNT_ID = cls.config.get("ACCOUNT_ID")
            cls.RESOURCE_GROUP_ID = cls.config.get("RESOURCE_GROUP_ID")
            cls.ORG_ID = cls.config.get("ORG_ID")
            cls.BILLING_MONTH = cls.config.get("BILLING_MONTH")
            cls.COS_BUCKET = cls.config.get("COS_BUCKET")
            cls.COS_LOCATION = cls.config.get("COS_LOCATION")
            cls.SNAPSHOT_DATE_FROM = cls.config.get("DATE_FROM")
            cls.SNAPSHOT_DATE_TO = cls.config.get("DATE_TO")
            assert cls.ACCOUNT_ID is not None
            assert cls.RESOURCE_GROUP_ID is not None
            assert cls.ORG_ID is not None
            assert cls.BILLING_MONTH is not None
            assert cls.COS_BUCKET is not None
            assert cls.COS_LOCATION is not None
            assert cls.SNAPSHOT_DATE_FROM is not None
            assert cls.SNAPSHOT_DATE_TO is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_account_summary(self):
        get_account_summary_response = self.usage_reports_service.get_account_summary(
            account_id=self.ACCOUNT_ID,
            billingmonth=self.BILLING_MONTH,
        )

        assert get_account_summary_response.get_status_code() == 200
        account_summary = get_account_summary_response.get_result()
        assert account_summary is not None
        assert account_summary['account_id'] == self.ACCOUNT_ID
        assert account_summary['month'] == self.BILLING_MONTH
        assert 'offers' in account_summary
        assert 'subscription' in account_summary

    @needscredentials
    def test_get_account_usage(self):
        get_account_usage_response = self.usage_reports_service.get_account_usage(
            account_id=self.ACCOUNT_ID, billingmonth=self.BILLING_MONTH, names=True, accept_language='English'
        )

        assert get_account_usage_response.get_status_code() == 200
        account_usage = get_account_usage_response.get_result()
        assert account_usage is not None
        assert account_usage['account_id'] == self.ACCOUNT_ID
        assert account_usage['month'] == self.BILLING_MONTH
        assert 'resources' in account_usage

    @needscredentials
    def test_get_resource_group_usage(self):
        get_resource_group_usage_response = self.usage_reports_service.get_resource_group_usage(
            account_id=self.ACCOUNT_ID,
            resource_group_id=self.RESOURCE_GROUP_ID,
            billingmonth=self.BILLING_MONTH,
            names=True,
        )

        assert get_resource_group_usage_response.get_status_code() == 200
        resource_group_usage = get_resource_group_usage_response.get_result()
        assert resource_group_usage is not None
        assert resource_group_usage['account_id'] == self.ACCOUNT_ID
        assert resource_group_usage['month'] == self.BILLING_MONTH
        assert 'resources' in resource_group_usage

    @needscredentials
    def test_get_org_usage(self):
        get_org_usage_response = self.usage_reports_service.get_org_usage(
            account_id=self.ACCOUNT_ID,
            organization_id=self.ORG_ID,
            billingmonth=self.BILLING_MONTH,
            names=True,
        )

        assert get_org_usage_response.get_status_code() == 200
        org_usage = get_org_usage_response.get_result()
        assert org_usage is not None
        assert org_usage['account_id'] == self.ACCOUNT_ID
        assert org_usage['month'] == self.BILLING_MONTH
        assert 'resources' in org_usage

    @needscredentials
    def test_get_resource_usage_account(self):
        resources = []
        offset = None

        while True:
            # Get next page of results
            response = self.usage_reports_service.get_resource_usage_account(
                account_id=self.ACCOUNT_ID,
                billingmonth=self.BILLING_MONTH,
                names=True,
                limit=50,
                start=offset,
            )

            assert response.get_status_code() == 200
            instances_usage = response.get_result()
            assert instances_usage is not None
            assert 'resources' in instances_usage

            resources.extend(instances_usage['resources'])

            next = instances_usage.get('next')
            if next is not None:
                offset = next['offset']
            else:
                break

        numResources = len(resources)
        print(f'get_resource_usage_account() response contained {numResources} total resources')
        assert numResources > 0

    @needscredentials
    def test_get_resource_usage_resource_group(self):
        resources = []
        offset = None

        while True:
            # Get next page of results
            response = self.usage_reports_service.get_resource_usage_resource_group(
                account_id=self.ACCOUNT_ID,
                resource_group_id=self.RESOURCE_GROUP_ID,
                billingmonth=self.BILLING_MONTH,
                names=True,
                limit=50,
                start=offset,
            )

            assert response.get_status_code() == 200
            instances_usage = response.get_result()
            assert instances_usage is not None
            assert 'resources' in instances_usage

            resources.extend(instances_usage['resources'])

            next = instances_usage.get('next')
            if next is not None:
                offset = next['offset']
            else:
                break

        numResources = len(resources)
        print(f'get_resource_usage_resource_group() response contained {numResources} total resources')
        assert numResources > 0

    @needscredentials
    def test_get_resource_usage_org(self):
        resources = []
        offset = None

        while True:
            # Get next page of results
            response = self.usage_reports_service.get_resource_usage_org(
                account_id=self.ACCOUNT_ID,
                organization_id=self.ORG_ID,
                billingmonth=self.BILLING_MONTH,
                names=True,
                limit=50,
                start=offset,
            )

            assert response.get_status_code() == 200
            instances_usage = response.get_result()
            assert instances_usage is not None
            assert 'resources' in instances_usage

            resources.extend(instances_usage['resources'])

            next = instances_usage.get('next')
            if next is not None:
                offset = next['offset']
            else:
                break

        numResources = len(resources)
        print(f'get_resource_usage_org() response contained {numResources} total resources')
        assert numResources > 0

    @needscredentials
    def test_create_reports_snapshot_config(self):
        response = self.usage_reports_service.create_reports_snapshot_config(
            account_id=self.ACCOUNT_ID,
            interval='daily',
            cos_bucket=self.COS_BUCKET,
            cos_location=self.COS_LOCATION,
            cos_reports_folder='IBMCloud-Billing-Reports',
            report_types=['account_summary', 'enterprise_summary', 'account_resource_instance_usage'],
            versioning='new',
        )

        assert response.get_status_code() == 201
        snapshot_config = response.get_result()
        assert snapshot_config is not None

    @needscredentials
    def test_get_reports_snapshot_config(self):
        response = self.usage_reports_service.get_reports_snapshot_config(
            account_id=self.ACCOUNT_ID,
        )

        assert response.get_status_code() == 200
        snapshot_config = response.get_result()
        assert snapshot_config is not None

    @needscredentials
    def test_update_reports_snapshot_config(self):
        response = self.usage_reports_service.update_reports_snapshot_config(
            account_id=self.ACCOUNT_ID,
            interval='daily',
            cos_bucket=self.COS_BUCKET,
            cos_location=self.COS_LOCATION,
            cos_reports_folder='IBMCloud-Billing-Reports',
            report_types=['account_summary', 'enterprise_summary'],
            versioning='new',
        )

        assert response.get_status_code() == 200
        snapshot_config = response.get_result()
        assert snapshot_config is not None

    @needscredentials
    def test_get_reports_snapshot(self):
        response = self.usage_reports_service.get_reports_snapshot(
            account_id=self.ACCOUNT_ID,
            month=self.BILLING_MONTH,
            date_from=self.SNAPSHOT_DATE_FROM,
            date_to=self.SNAPSHOT_DATE_TO,
        )

        assert response.get_status_code() == 200
        snapshot_list = response.get_result()
        assert snapshot_list is not None

    @needscredentials
    def test_delete_reports_snapshot_config(self):
        response = self.usage_reports_service.delete_reports_snapshot_config(
            account_id=self.ACCOUNT_ID,
        )

        assert response.get_status_code() == 204
