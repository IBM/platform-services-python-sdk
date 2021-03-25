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
Examples for EnterpriseUsageReportsV1
"""

import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.enterprise_usage_reports_v1 import *

#
# This file provides an example of how to use the Enterprise Usage Reports service.
#
# The following configuration properties are assumed to be defined:
# ENTERPRISE_USAGE_REPORTS_URL=<service url>
# ENTERPRISE_USAGE_REPORTS_AUTHTYPE=iam
# ENTERPRISE_USAGE_REPORTS_APIKEY=<IAM api key of user with authority to create rules>
# ENTERPRISE_USAGE_REPORTS_AUTH_URL=<IAM token service URL - omit this if using the production environment>
# ENTERPRISE_USAGE_REPORTS_ENTERPRISE_ID=<the id of the enterprise whose usage info will be retrieved>
# ENTERPRISE_USAGE_REPORTS_ACCOUNT_ID=<the id of the account whose usage info will be retrieved>
# ENTERPRISE_USAGE_REPORTS_ACCOUNT_GROUP_ID=<the id of the account group whose usage info will be retrieved>
# ENTERPRISE_USAGE_REPORTS_BILLING_MONTH=<the billing month (yyyy-mm) for which usage info will be retrieved>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'enterprise_usage_reports.env'

enterprise_usage_reports_service = None

config = None

enterprise_id = None
billing_month = None

##############################################################################
# Start of Examples for Service: EnterpriseUsageReportsV1
##############################################################################
# region


class TestEnterpriseUsageReportsV1Examples():
    """
    Example Test Class for EnterpriseUsageReportsV1
    """

    @classmethod
    def setup_class(cls):
        global enterprise_usage_reports_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            enterprise_usage_reports_service = EnterpriseUsageReportsV1.new_instance()

            # end-common
            assert enterprise_usage_reports_service is not None

            # Load the configuration
            global config
            config = read_external_sources(
                EnterpriseUsageReportsV1.DEFAULT_SERVICE_NAME)

            global enterprise_id
            enterprise_id = config.get("ENTERPRISE_ID")

            global billing_month
            billing_month = config.get("BILLING_MONTH")

            assert enterprise_id is not None
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
            global enterprise_id, billing_month
            # begin-get_resource_usage_report

            reports = enterprise_usage_reports_service.get_resource_usage_report(
                enterprise_id=enterprise_id,
                month=billing_month,
                limit=10
            ).get_result()

            print('\nget_resource_usage_report() result:\n' + json.dumps(reports, indent=2))

            # end-get_resource_usage_report

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: EnterpriseUsageReportsV1
##############################################################################
