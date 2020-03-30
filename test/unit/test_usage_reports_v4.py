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

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import requests
import responses
from platform_services.usage_reports_v4 import *


service = UsageReportsV4(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://metering-reporting.ng.bluemix.net'
service.set_service_url(base_url)

##############################################################################
# Start of Service: UsageReports
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_account_summary
#-----------------------------------------------------------------------------
class TestGetAccountSummary():

    #--------------------------------------------------------
    # get_account_summary()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_summary_all_params(self):
        # Set up mock
        url = base_url + '/v4/accounts/testString/summary/testString'
        mock_response = '{"account_id": "account_id", "billing_month": "billing_month", "billing_country_code": "billing_country_code", "billing_currency_code": "billing_currency_code", "resources": {"billable_cost": 13, "non_billable_cost": 17}, "offers": [{"offer_id": "offer_id", "credits_total": 13, "offer_template": "offer_template", "valid_from": "2019-01-01T12:00:00", "expires_on": "2019-01-01T12:00:00", "credits": {"total": 5, "starting_balance": 16, "used": 4, "balance": 7}}], "subscription": {"overage": 7, "subscriptions": [{"subscription_id": "subscription_id", "charge_agreement_number": "charge_agreement_number", "type": "type", "subscription_amount": 19, "start": "2019-01-01T12:00:00", "end": "2019-01-01T12:00:00", "credits_total": 13, "terms": [{"start": "2019-01-01T12:00:00", "end": "2019-01-01T12:00:00", "credits": {"total": 5, "starting_balance": 16, "used": 4, "balance": 7}}]}]}, "support": [{"cost": 4, "type": "type", "overage": 7}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = service.get_account_summary(
            account_id,
            billingmonth
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_account_summary_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_summary_required_params(self):
        # Set up mock
        url = base_url + '/v4/accounts/testString/summary/testString'
        mock_response = '{"account_id": "account_id", "billing_month": "billing_month", "billing_country_code": "billing_country_code", "billing_currency_code": "billing_currency_code", "resources": {"billable_cost": 13, "non_billable_cost": 17}, "offers": [{"offer_id": "offer_id", "credits_total": 13, "offer_template": "offer_template", "valid_from": "2019-01-01T12:00:00", "expires_on": "2019-01-01T12:00:00", "credits": {"total": 5, "starting_balance": 16, "used": 4, "balance": 7}}], "subscription": {"overage": 7, "subscriptions": [{"subscription_id": "subscription_id", "charge_agreement_number": "charge_agreement_number", "type": "type", "subscription_amount": 19, "start": "2019-01-01T12:00:00", "end": "2019-01-01T12:00:00", "credits_total": 13, "terms": [{"start": "2019-01-01T12:00:00", "end": "2019-01-01T12:00:00", "credits": {"total": 5, "starting_balance": 16, "used": 4, "balance": 7}}]}]}, "support": [{"cost": 4, "type": "type", "overage": 7}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = service.get_account_summary(
            account_id,
            billingmonth
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_account_usage
#-----------------------------------------------------------------------------
class TestGetAccountUsage():

    #--------------------------------------------------------
    # get_account_usage()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_usage_all_params(self):
        # Set up mock
        url = base_url + '/v4/accounts/testString/usage/testString'
        mock_response = '{"account_id": "account_id", "pricing_country": "USA", "currency_code": "USD", "month": "2017-08", "resources": [{"resource_id": "resource_id", "billable_cost": 13, "non_billable_cost": 17, "plans": [{"plan_id": "plan_id", "pricing_region": "pricing_region", "billable": true, "cost": 4, "usage": [{"metric": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "price": [{"mapKey": {"anyKey": "anyValue"}}], "unit": "HOURS", "non_chargeable": true}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = service.get_account_usage(
            account_id,
            billingmonth
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_account_usage_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_usage_required_params(self):
        # Set up mock
        url = base_url + '/v4/accounts/testString/usage/testString'
        mock_response = '{"account_id": "account_id", "pricing_country": "USA", "currency_code": "USD", "month": "2017-08", "resources": [{"resource_id": "resource_id", "billable_cost": 13, "non_billable_cost": 17, "plans": [{"plan_id": "plan_id", "pricing_region": "pricing_region", "billable": true, "cost": 4, "usage": [{"metric": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "price": [{"mapKey": {"anyKey": "anyValue"}}], "unit": "HOURS", "non_chargeable": true}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = service.get_account_usage(
            account_id,
            billingmonth
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_resource_group_usage
#-----------------------------------------------------------------------------
class TestGetResourceGroupUsage():

    #--------------------------------------------------------
    # get_resource_group_usage()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_group_usage_all_params(self):
        # Set up mock
        url = base_url + '/v4/accounts/testString/resource_groups/testString/usage/testString'
        mock_response = '{"account_id": "account_id", "resource_group_id": "resource_group_id", "pricing_country": "USA", "currency_code": "USD", "month": "2017-08", "resources": [{"resource_id": "resource_id", "billable_cost": 13, "non_billable_cost": 17, "plans": [{"plan_id": "plan_id", "pricing_region": "pricing_region", "billable": true, "cost": 4, "usage": [{"metric": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "price": [{"mapKey": {"anyKey": "anyValue"}}], "unit": "HOURS", "non_chargeable": true}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_group_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = service.get_resource_group_usage(
            account_id,
            resource_group_id,
            billingmonth
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_resource_group_usage_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_group_usage_required_params(self):
        # Set up mock
        url = base_url + '/v4/accounts/testString/resource_groups/testString/usage/testString'
        mock_response = '{"account_id": "account_id", "resource_group_id": "resource_group_id", "pricing_country": "USA", "currency_code": "USD", "month": "2017-08", "resources": [{"resource_id": "resource_id", "billable_cost": 13, "non_billable_cost": 17, "plans": [{"plan_id": "plan_id", "pricing_region": "pricing_region", "billable": true, "cost": 4, "usage": [{"metric": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "price": [{"mapKey": {"anyKey": "anyValue"}}], "unit": "HOURS", "non_chargeable": true}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_group_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = service.get_resource_group_usage(
            account_id,
            resource_group_id,
            billingmonth
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_organization_usage
#-----------------------------------------------------------------------------
class TestGetOrganizationUsage():

    #--------------------------------------------------------
    # get_organization_usage()
    #--------------------------------------------------------
    @responses.activate
    def test_get_organization_usage_all_params(self):
        # Set up mock
        url = base_url + '/v4/accounts/testString/organizations/testString/usage/testString'
        mock_response = '{"account_id": "account_id", "organization_id": "organization_id", "pricing_country": "USA", "currency_code": "USD", "month": "2017-08", "resources": [{"resource_id": "resource_id", "billable_cost": 13, "non_billable_cost": 17, "plans": [{"plan_id": "plan_id", "pricing_region": "pricing_region", "billable": true, "cost": 4, "usage": [{"metric": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "price": [{"mapKey": {"anyKey": "anyValue"}}], "unit": "HOURS", "non_chargeable": true}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        organization_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = service.get_organization_usage(
            account_id,
            organization_id,
            billingmonth
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_organization_usage_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_organization_usage_required_params(self):
        # Set up mock
        url = base_url + '/v4/accounts/testString/organizations/testString/usage/testString'
        mock_response = '{"account_id": "account_id", "organization_id": "organization_id", "pricing_country": "USA", "currency_code": "USD", "month": "2017-08", "resources": [{"resource_id": "resource_id", "billable_cost": 13, "non_billable_cost": 17, "plans": [{"plan_id": "plan_id", "pricing_region": "pricing_region", "billable": true, "cost": 4, "usage": [{"metric": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "price": [{"mapKey": {"anyKey": "anyValue"}}], "unit": "HOURS", "non_chargeable": true}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        organization_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = service.get_organization_usage(
            account_id,
            organization_id,
            billingmonth
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_account_instances_usage
#-----------------------------------------------------------------------------
class TestGetAccountInstancesUsage():

    #--------------------------------------------------------
    # get_account_instances_usage()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_instances_usage_all_params(self):
        # Set up mock
        url = base_url + '/v4/accounts/testString/resource_instances/usage/testString'
        mock_response = '{"limit": 5, "count": 5, "first": {"href": "href", "offset": "offset"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"account_id": "account_id", "resource_instance_id": "resource_instance_id", "resource_id": "resource_id", "resource_group_id": "resource_group_id", "organization_id": "organization_id", "space": "space", "consumer_id": "consumer_id", "region": "region", "pricing_region": "pricing_region", "pricing_country": "USA", "currency_code": "USD", "billable": true, "plan_id": "plan_id", "month": "2017-08", "usage": [{"metric": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "price": [{"mapKey": {"anyKey": "anyValue"}}], "unit": "HOURS", "non_chargeable": true}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        billingmonth = 'testString'
        limit = 38
        start = 'testString'
        resource_group_id = 'testString'
        organization_id = 'testString'
        resource_instance_id = 'testString'
        resource_id = 'testString'
        plan_id = 'testString'
        region = 'testString'

        # Invoke method
        response = service.get_account_instances_usage(
            account_id,
            billingmonth,
            limit=limit,
            start=start,
            resource_group_id=resource_group_id,
            organization_id=organization_id,
            resource_instance_id=resource_instance_id,
            resource_id=resource_id,
            plan_id=plan_id,
            region=region
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert '_limit={}'.format(limit) in query_string
        assert '_start={}'.format(start) in query_string
        assert 'resource_group_id={}'.format(resource_group_id) in query_string
        assert 'organization_id={}'.format(organization_id) in query_string
        assert 'resource_instance_id={}'.format(resource_instance_id) in query_string
        assert 'resource_id={}'.format(resource_id) in query_string
        assert 'plan_id={}'.format(plan_id) in query_string
        assert 'region={}'.format(region) in query_string


    #--------------------------------------------------------
    # test_get_account_instances_usage_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_instances_usage_required_params(self):
        # Set up mock
        url = base_url + '/v4/accounts/testString/resource_instances/usage/testString'
        mock_response = '{"limit": 5, "count": 5, "first": {"href": "href", "offset": "offset"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"account_id": "account_id", "resource_instance_id": "resource_instance_id", "resource_id": "resource_id", "resource_group_id": "resource_group_id", "organization_id": "organization_id", "space": "space", "consumer_id": "consumer_id", "region": "region", "pricing_region": "pricing_region", "pricing_country": "USA", "currency_code": "USD", "billable": true, "plan_id": "plan_id", "month": "2017-08", "usage": [{"metric": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "price": [{"mapKey": {"anyKey": "anyValue"}}], "unit": "HOURS", "non_chargeable": true}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = service.get_account_instances_usage(
            account_id,
            billingmonth
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_resource_group_instances_usage
#-----------------------------------------------------------------------------
class TestGetResourceGroupInstancesUsage():

    #--------------------------------------------------------
    # get_resource_group_instances_usage()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_group_instances_usage_all_params(self):
        # Set up mock
        url = base_url + '/v4/accounts/testString/resource_groups/testString/resource_instances/usage/testString'
        mock_response = '{"limit": 5, "count": 5, "first": {"href": "href", "offset": "offset"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"account_id": "account_id", "resource_instance_id": "resource_instance_id", "resource_id": "resource_id", "resource_group_id": "resource_group_id", "organization_id": "organization_id", "space": "space", "consumer_id": "consumer_id", "region": "region", "pricing_region": "pricing_region", "pricing_country": "USA", "currency_code": "USD", "billable": true, "plan_id": "plan_id", "month": "2017-08", "usage": [{"metric": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "price": [{"mapKey": {"anyKey": "anyValue"}}], "unit": "HOURS", "non_chargeable": true}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_group_id = 'testString'
        billingmonth = 'testString'
        limit = 38
        start = 'testString'
        resource_instance_id = 'testString'
        resource_id = 'testString'
        plan_id = 'testString'
        region = 'testString'

        # Invoke method
        response = service.get_resource_group_instances_usage(
            account_id,
            resource_group_id,
            billingmonth,
            limit=limit,
            start=start,
            resource_instance_id=resource_instance_id,
            resource_id=resource_id,
            plan_id=plan_id,
            region=region
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert '_limit={}'.format(limit) in query_string
        assert '_start={}'.format(start) in query_string
        assert 'resource_instance_id={}'.format(resource_instance_id) in query_string
        assert 'resource_id={}'.format(resource_id) in query_string
        assert 'plan_id={}'.format(plan_id) in query_string
        assert 'region={}'.format(region) in query_string


    #--------------------------------------------------------
    # test_get_resource_group_instances_usage_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_group_instances_usage_required_params(self):
        # Set up mock
        url = base_url + '/v4/accounts/testString/resource_groups/testString/resource_instances/usage/testString'
        mock_response = '{"limit": 5, "count": 5, "first": {"href": "href", "offset": "offset"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"account_id": "account_id", "resource_instance_id": "resource_instance_id", "resource_id": "resource_id", "resource_group_id": "resource_group_id", "organization_id": "organization_id", "space": "space", "consumer_id": "consumer_id", "region": "region", "pricing_region": "pricing_region", "pricing_country": "USA", "currency_code": "USD", "billable": true, "plan_id": "plan_id", "month": "2017-08", "usage": [{"metric": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "price": [{"mapKey": {"anyKey": "anyValue"}}], "unit": "HOURS", "non_chargeable": true}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_group_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = service.get_resource_group_instances_usage(
            account_id,
            resource_group_id,
            billingmonth
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_organization_instances_usage
#-----------------------------------------------------------------------------
class TestGetOrganizationInstancesUsage():

    #--------------------------------------------------------
    # get_organization_instances_usage()
    #--------------------------------------------------------
    @responses.activate
    def test_get_organization_instances_usage_all_params(self):
        # Set up mock
        url = base_url + '/v4/accounts/testString/organizations/testString/resource_instances/usage/testString'
        mock_response = '{"limit": 5, "count": 5, "first": {"href": "href", "offset": "offset"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"account_id": "account_id", "resource_instance_id": "resource_instance_id", "resource_id": "resource_id", "resource_group_id": "resource_group_id", "organization_id": "organization_id", "space": "space", "consumer_id": "consumer_id", "region": "region", "pricing_region": "pricing_region", "pricing_country": "USA", "currency_code": "USD", "billable": true, "plan_id": "plan_id", "month": "2017-08", "usage": [{"metric": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "price": [{"mapKey": {"anyKey": "anyValue"}}], "unit": "HOURS", "non_chargeable": true}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        organization_id = 'testString'
        billingmonth = 'testString'
        limit = 38
        start = 'testString'
        resource_instance_id = 'testString'
        resource_id = 'testString'
        plan_id = 'testString'
        region = 'testString'

        # Invoke method
        response = service.get_organization_instances_usage(
            account_id,
            organization_id,
            billingmonth,
            limit=limit,
            start=start,
            resource_instance_id=resource_instance_id,
            resource_id=resource_id,
            plan_id=plan_id,
            region=region
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert '_limit={}'.format(limit) in query_string
        assert '_start={}'.format(start) in query_string
        assert 'resource_instance_id={}'.format(resource_instance_id) in query_string
        assert 'resource_id={}'.format(resource_id) in query_string
        assert 'plan_id={}'.format(plan_id) in query_string
        assert 'region={}'.format(region) in query_string


    #--------------------------------------------------------
    # test_get_organization_instances_usage_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_organization_instances_usage_required_params(self):
        # Set up mock
        url = base_url + '/v4/accounts/testString/organizations/testString/resource_instances/usage/testString'
        mock_response = '{"limit": 5, "count": 5, "first": {"href": "href", "offset": "offset"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"account_id": "account_id", "resource_instance_id": "resource_instance_id", "resource_id": "resource_id", "resource_group_id": "resource_group_id", "organization_id": "organization_id", "space": "space", "consumer_id": "consumer_id", "region": "region", "pricing_region": "pricing_region", "pricing_country": "USA", "currency_code": "USD", "billable": true, "plan_id": "plan_id", "month": "2017-08", "usage": [{"metric": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "price": [{"mapKey": {"anyKey": "anyValue"}}], "unit": "HOURS", "non_chargeable": true}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        organization_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = service.get_organization_instances_usage(
            account_id,
            organization_id,
            billingmonth
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UsageReports
##############################################################################

