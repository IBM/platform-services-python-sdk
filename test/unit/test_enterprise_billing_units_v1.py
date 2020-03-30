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
from platform_services.enterprise_billing_units_v1 import *


service = EnterpriseBillingUnitsV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://billing.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: BillingOptions
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_billing_option_by_query
#-----------------------------------------------------------------------------
class TestGetBillingOptionByQuery():

    #--------------------------------------------------------
    # get_billing_option_by_query()
    #--------------------------------------------------------
    @responses.activate
    def test_get_billing_option_by_query_all_params(self):
        # Set up mock
        url = base_url + '/v1/billing-options'
        mock_response = '{"id": "id", "billing_unit_id": "billing_unit_id", "start_date": "2019-05-01T00:00:00.000Z", "end_date": "2020-05-01T00:00:00.000Z", "state": "ACTIVE", "type": "SUBSCRIPTION", "category": "PLATFORM", "payment_instrument": {"anyKey": "anyValue"}, "duration_in_months": 11, "line_item_id": 10, "billing_system": {"anyKey": "anyValue"}, "renewal_mode_code": "renewal_mode_code", "updated_at": "2019-06-01T00:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        billing_unit_id = 'testString'

        # Invoke method
        response = service.get_billing_option_by_query(
            billing_unit_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'billing_unit_id={}'.format(billing_unit_id) in query_string


    #--------------------------------------------------------
    # test_get_billing_option_by_query_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_billing_option_by_query_required_params(self):
        # Set up mock
        url = base_url + '/v1/billing-options'
        mock_response = '{"id": "id", "billing_unit_id": "billing_unit_id", "start_date": "2019-05-01T00:00:00.000Z", "end_date": "2020-05-01T00:00:00.000Z", "state": "ACTIVE", "type": "SUBSCRIPTION", "category": "PLATFORM", "payment_instrument": {"anyKey": "anyValue"}, "duration_in_months": 11, "line_item_id": 10, "billing_system": {"anyKey": "anyValue"}, "renewal_mode_code": "renewal_mode_code", "updated_at": "2019-06-01T00:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        billing_unit_id = 'testString'

        # Invoke method
        response = service.get_billing_option_by_query(
            billing_unit_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'billing_unit_id={}'.format(billing_unit_id) in query_string


# endregion
##############################################################################
# End of Service: BillingOptions
##############################################################################

##############################################################################
# Start of Service: BillingUnits
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_billing_unit_by_id
#-----------------------------------------------------------------------------
class TestGetBillingUnitById():

    #--------------------------------------------------------
    # get_billing_unit_by_id()
    #--------------------------------------------------------
    @responses.activate
    def test_get_billing_unit_by_id_all_params(self):
        # Set up mock
        url = base_url + '/v1/billing-units/testString'
        mock_response = '{"id": "id", "crn": "crn:v1:bluemix:public:billing::a/<<enterprise_account_id>>::billing-unit:<<billing_unit_id>>", "name": "name", "enterprise_id": "enterprise_id", "currency_code": "USD", "country_code": "USA", "master": true, "created_at": "2019-05-01T00:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        billing_unit_id = 'testString'

        # Invoke method
        response = service.get_billing_unit_by_id(
            billing_unit_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_billing_unit_by_id_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_billing_unit_by_id_required_params(self):
        # Set up mock
        url = base_url + '/v1/billing-units/testString'
        mock_response = '{"id": "id", "crn": "crn:v1:bluemix:public:billing::a/<<enterprise_account_id>>::billing-unit:<<billing_unit_id>>", "name": "name", "enterprise_id": "enterprise_id", "currency_code": "USD", "country_code": "USA", "master": true, "created_at": "2019-05-01T00:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        billing_unit_id = 'testString'

        # Invoke method
        response = service.get_billing_unit_by_id(
            billing_unit_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_billing_unit_by_query
#-----------------------------------------------------------------------------
class TestGetBillingUnitByQuery():

    #--------------------------------------------------------
    # get_billing_unit_by_query()
    #--------------------------------------------------------
    @responses.activate
    def test_get_billing_unit_by_query_all_params(self):
        # Set up mock
        url = base_url + '/v1/billing-units'
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "crn": "crn:v1:bluemix:public:billing::a/<<enterprise_account_id>>::billing-unit:<<billing_unit_id>>", "name": "name", "enterprise_id": "enterprise_id", "currency_code": "USD", "country_code": "USA", "master": true, "created_at": "2019-05-01T00:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        enterprise_id = 'testString'
        account_group_id = 'testString'

        # Invoke method
        response = service.get_billing_unit_by_query(
            account_id=account_id,
            enterprise_id=enterprise_id,
            account_group_id=account_group_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'enterprise_id={}'.format(enterprise_id) in query_string
        assert 'account_group_id={}'.format(account_group_id) in query_string


    #--------------------------------------------------------
    # test_get_billing_unit_by_query_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_billing_unit_by_query_required_params(self):
        # Set up mock
        url = base_url + '/v1/billing-units'
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "crn": "crn:v1:bluemix:public:billing::a/<<enterprise_account_id>>::billing-unit:<<billing_unit_id>>", "name": "name", "enterprise_id": "enterprise_id", "currency_code": "USD", "country_code": "USA", "master": true, "created_at": "2019-05-01T00:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_billing_unit_by_query()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: BillingUnits
##############################################################################

##############################################################################
# Start of Service: CreditPools
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_credit_pools
#-----------------------------------------------------------------------------
class TestGetCreditPools():

    #--------------------------------------------------------
    # get_credit_pools()
    #--------------------------------------------------------
    @responses.activate
    def test_get_credit_pools_all_params(self):
        # Set up mock
        url = base_url + '/v1/credit-pools'
        mock_response = '{"rows_count": 2, "next_url": "next_url", "resources": [{"type": "type", "currency_code": "USD", "billing_unit_id": "billing_unit_id", "term_credits": [{"billing_option_id": "JWX986YRGFSHACQUEFOI", "category": "PLATFORM", "start_date": "2019-05-01T00:00:00.000Z", "end_date": "2020-04-30T23:59:29.999Z", "total_credits": 10000, "starting_balance": 9000, "used_credits": 9500, "current_balance": 0, "resources": [{"anyKey": "anyValue"}]}], "overage": {"cost": 500, "resources": [{"anyKey": "anyValue"}]}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        billing_unit_id = 'testString'
        date = 'testString'
        type = 'testString'

        # Invoke method
        response = service.get_credit_pools(
            billing_unit_id,
            date=date,
            type=type
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'billing_unit_id={}'.format(billing_unit_id) in query_string
        assert 'date={}'.format(date) in query_string
        assert 'type={}'.format(type) in query_string


    #--------------------------------------------------------
    # test_get_credit_pools_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_credit_pools_required_params(self):
        # Set up mock
        url = base_url + '/v1/credit-pools'
        mock_response = '{"rows_count": 2, "next_url": "next_url", "resources": [{"type": "type", "currency_code": "USD", "billing_unit_id": "billing_unit_id", "term_credits": [{"billing_option_id": "JWX986YRGFSHACQUEFOI", "category": "PLATFORM", "start_date": "2019-05-01T00:00:00.000Z", "end_date": "2020-04-30T23:59:29.999Z", "total_credits": 10000, "starting_balance": 9000, "used_credits": 9500, "current_balance": 0, "resources": [{"anyKey": "anyValue"}]}], "overage": {"cost": 500, "resources": [{"anyKey": "anyValue"}]}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        billing_unit_id = 'testString'

        # Invoke method
        response = service.get_credit_pools(
            billing_unit_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'billing_unit_id={}'.format(billing_unit_id) in query_string


# endregion
##############################################################################
# End of Service: CreditPools
##############################################################################

