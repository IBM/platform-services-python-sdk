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

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import requests
import responses
from platform_services.enterprise_usage_reports_v1 import *


service = EnterpriseUsageReportsV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://enterprise.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Default
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_resource_usage_report
#-----------------------------------------------------------------------------
class TestListResourceUsageReport():

    #--------------------------------------------------------
    # list_resource_usage_report()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resource_usage_report_all_params(self):
        # Set up mock
        url = base_url + '/v1/resource-usage-reports'
        mock_response = '{"limit": 5, "first": {"href": "href"}, "next": {"href": "href"}, "reports": [{"entity_id": "de129b787b86403db7d3a14be2ae5f76", "entity_type": "enterprise", "entity_crn": "crn:v1:bluemix:public:enterprise::a/e9a57260546c4b4aa9ebfa316a82e56e::enterprise:de129b787b86403db7d3a14be2ae5f76", "entity_name": "Platform-Services", "billing_unit_id": "65719a07280a4022a9efa2f6ff4c3369", "billing_unit_crn": "crn:v1:bluemix:public:billing::a/3f99f8accbc848ea96f3c61a0ae22c44::billing-unit:65719a07280a4022a9efa2f6ff4c3369", "billing_unit_name": "Operations", "country_code": "USA", "currency_code": "USD", "month": "2017-08", "billable_cost": 13, "non_billable_cost": 17, "billable_rated_cost": 19, "non_billable_rated_cost": 23, "resources": [{"resource_id": "resource_id", "billable_cost": 13, "billable_rated_cost": 19, "non_billable_cost": 17, "non_billable_rated_cost": 23, "plans": [{"plan_id": "plan_id", "pricing_region": "pricing_region", "pricing_plan_id": "pricing_plan_id", "billable": true, "cost": 4, "rated_cost": 10, "usage": [{"metric": "UP-TIME", "unit": "HOURS", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130, "price": [{"anyKey": "anyValue"}]}]}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        enterprise_id = 'testString'
        account_group_id = 'testString'
        account_id = 'testString'
        children = True
        month = 'testString'
        billing_unit_id = 'testString'

        # Invoke method
        response = service.list_resource_usage_report(
            enterprise_id=enterprise_id,
            account_group_id=account_group_id,
            account_id=account_id,
            children=children,
            month=month,
            billing_unit_id=billing_unit_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'enterprise_id={}'.format(enterprise_id) in query_string
        assert 'account_group_id={}'.format(account_group_id) in query_string
        assert 'account_id={}'.format(account_id) in query_string
        assert 'children={}'.format('true' if children else 'false') in query_string
        assert 'month={}'.format(month) in query_string
        assert 'billing_unit_id={}'.format(billing_unit_id) in query_string


    #--------------------------------------------------------
    # test_list_resource_usage_report_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_resource_usage_report_required_params(self):
        # Set up mock
        url = base_url + '/v1/resource-usage-reports'
        mock_response = '{"limit": 5, "first": {"href": "href"}, "next": {"href": "href"}, "reports": [{"entity_id": "de129b787b86403db7d3a14be2ae5f76", "entity_type": "enterprise", "entity_crn": "crn:v1:bluemix:public:enterprise::a/e9a57260546c4b4aa9ebfa316a82e56e::enterprise:de129b787b86403db7d3a14be2ae5f76", "entity_name": "Platform-Services", "billing_unit_id": "65719a07280a4022a9efa2f6ff4c3369", "billing_unit_crn": "crn:v1:bluemix:public:billing::a/3f99f8accbc848ea96f3c61a0ae22c44::billing-unit:65719a07280a4022a9efa2f6ff4c3369", "billing_unit_name": "Operations", "country_code": "USA", "currency_code": "USD", "month": "2017-08", "billable_cost": 13, "non_billable_cost": 17, "billable_rated_cost": 19, "non_billable_rated_cost": 23, "resources": [{"resource_id": "resource_id", "billable_cost": 13, "billable_rated_cost": 19, "non_billable_cost": 17, "non_billable_rated_cost": 23, "plans": [{"plan_id": "plan_id", "pricing_region": "pricing_region", "pricing_plan_id": "pricing_plan_id", "billable": true, "cost": 4, "rated_cost": 10, "usage": [{"metric": "UP-TIME", "unit": "HOURS", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130, "price": [{"anyKey": "anyValue"}]}]}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_resource_usage_report()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Default
##############################################################################

