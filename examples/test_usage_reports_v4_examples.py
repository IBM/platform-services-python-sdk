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
Examples for UsageReportsV4
"""

import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.usage_reports_v4 import *

#
# This file provides an example of how to use the Usage Reports service.
#
# The following configuration properties are assumed to be defined:
# USAGE_REPORTS_URL=<service url>
# USAGE_REPORTS_AUTHTYPE=iam
# USAGE_REPORTS_APIKEY=<IAM api key of user with authority to create rules>
# USAGE_REPORTS_AUTH_URL=<IAM token service URL - omit this if using the production environment>
# USAGE_REPORTS_ACCOUNT_ID=<the id of the account whose usage info will be retrieved>
# USAGE_REPORTS_RESOURCE_GROUP_ID=<the id of the resource group whose usage info will be retrieved>
# USAGE_REPORTS_ORG_ID=<the id of the organization whose usage info will be retrieved>
# USAGE_REPORTS_BILLING_MONTH=<the billing month (yyyy-mm) for which usage info will be retrieved>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'usage_reports.env'

usage_reports_service = None

config = None

account_id = None
resource_group_id = None
org_id = None
billing_month = None

##############################################################################
# Start of Examples for Service: UsageReportsV4
##############################################################################
# region


class TestUsageReportsV4Examples():
    """
    Example Test Class for UsageReportsV4
    """

    @classmethod
    def setup_class(cls):
        global usage_reports_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            usage_reports_service = UsageReportsV4.new_instance(
            )

            # end-common
            assert usage_reports_service is not None

            # Load the configuration
            global config
            config = read_external_sources(UsageReportsV4.DEFAULT_SERVICE_NAME)

            # Retrieve and verify some additional test-related config properties.
            global account_id
            account_id = config.get("ACCOUNT_ID")

            global resource_group_id
            resource_group_id = config.get("RESOURCE_GROUP_ID")

            global org_id
            org_id = config.get("ORG_ID")

            global billing_month
            billing_month = config.get("BILLING_MONTH")

            assert account_id is not None
            assert resource_group_id is not None
            assert org_id is not None
            assert billing_month is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_account_summary_example(self):
        """
        get_account_summary request example
        """
        try:
            global account_id, billing_month

            print('\nget_account_summary() result:')
            # begin-get_account_summary

            account_summary = usage_reports_service.get_account_summary(
                account_id=account_id,
                billingmonth=billing_month
            ).get_result()

            print(json.dumps(account_summary, indent=2))

            # end-get_account_summary

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_account_usage_example(self):
        """
        get_account_usage request example
        """
        try:
            global account_id, billing_month

            print('\nget_account_usage() result:')
            # begin-get_account_usage

            account_usage = usage_reports_service.get_account_usage(
                account_id=account_id,
                billingmonth=billing_month
            ).get_result()

            print(json.dumps(account_usage, indent=2))

            # end-get_account_usage

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resource_group_usage_example(self):
        """
        get_resource_group_usage request example
        """
        try:
            global account_id, resource_group_id, billing_month

            print('\nget_resource_group_usage() result:')
            # begin-get_resource_group_usage

            resource_group_usage = usage_reports_service.get_resource_group_usage(
                account_id=account_id,
                resource_group_id=resource_group_id,
                billingmonth=billing_month
            ).get_result()

            print(json.dumps(resource_group_usage, indent=2))

            # end-get_resource_group_usage

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_org_usage_example(self):
        """
        get_org_usage request example
        """
        try:
            global account_id, org_id, billing_month

            print('\nget_org_usage() result:')
            # begin-get_org_usage

            org_usage = usage_reports_service.get_org_usage(
                account_id=account_id,
                organization_id=org_id,
                billingmonth=billing_month
            ).get_result()

            print(json.dumps(org_usage, indent=2))

            # end-get_org_usage

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resource_usage_account_example(self):
        """
        get_resource_usage_account request example
        """
        try:
            global account_id, billing_month

            print('\nget_resource_usage_account() result:')
            # begin-get_resource_usage_account

            instances_usage = usage_reports_service.get_resource_usage_account(
                account_id=account_id,
                billingmonth=billing_month
            ).get_result()

            print(json.dumps(instances_usage, indent=2))

            # end-get_resource_usage_account

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resource_usage_resource_group_example(self):
        """
        get_resource_usage_resource_group request example
        """
        try:
            global account_id, resource_group_id, billing_month

            print('\nget_resource_usage_resource_group() result:')
            # begin-get_resource_usage_resource_group

            instances_usage = usage_reports_service.get_resource_usage_resource_group(
                account_id=account_id,
                resource_group_id=resource_group_id,
                billingmonth=billing_month
            ).get_result()

            print(json.dumps(instances_usage, indent=2))

            # end-get_resource_usage_resource_group

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resource_usage_org_example(self):
        """
        get_resource_usage_org request example
        """
        try:
            global account_id, org_id, billing_month

            print('\nget_resource_usage_org() result:')
            # begin-get_resource_usage_org

            instances_usage = usage_reports_service.get_resource_usage_org(
                account_id=account_id,
                organization_id=org_id,
                billingmonth=billing_month
            ).get_result()

            print(json.dumps(instances_usage, indent=2))

            # end-get_resource_usage_org

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: UsageReportsV4
##############################################################################
