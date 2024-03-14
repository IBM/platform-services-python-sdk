# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2023.
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
Unit Tests for EnterpriseBillingUnitsV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_platform_services.enterprise_billing_units_v1 import *


_service = EnterpriseBillingUnitsV1(authenticator=NoAuthAuthenticator())

_base_url = 'https://billing.cloud.ibm.com'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if not request_url.endswith('/'):
        return request_url
    return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: BillingUnits
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = EnterpriseBillingUnitsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, EnterpriseBillingUnitsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = EnterpriseBillingUnitsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetBillingUnit:
    """
    Test Class for get_billing_unit
    """

    @responses.activate
    def test_get_billing_unit_all_params(self):
        """
        get_billing_unit()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-units/testString')
        mock_response = '{"id": "id", "crn": "crn:v1:bluemix:public:billing::a/<<enterprise_account_id>>::billing-unit:<<billing_unit_id>>", "name": "name", "enterprise_id": "enterprise_id", "currency_code": "USD", "country_code": "USA", "master": true, "created_at": "2019-05-01T00:00:00.000Z"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        billing_unit_id = 'testString'

        # Invoke method
        response = _service.get_billing_unit(billing_unit_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_billing_unit_all_params_with_retries(self):
        # Enable retries and run test_get_billing_unit_all_params.
        _service.enable_retries()
        self.test_get_billing_unit_all_params()

        # Disable retries and run test_get_billing_unit_all_params.
        _service.disable_retries()
        self.test_get_billing_unit_all_params()

    @responses.activate
    def test_get_billing_unit_value_error(self):
        """
        test_get_billing_unit_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-units/testString')
        mock_response = '{"id": "id", "crn": "crn:v1:bluemix:public:billing::a/<<enterprise_account_id>>::billing-unit:<<billing_unit_id>>", "name": "name", "enterprise_id": "enterprise_id", "currency_code": "USD", "country_code": "USA", "master": true, "created_at": "2019-05-01T00:00:00.000Z"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        billing_unit_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "billing_unit_id": billing_unit_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_billing_unit(**req_copy)

    def test_get_billing_unit_value_error_with_retries(self):
        # Enable retries and run test_get_billing_unit_value_error.
        _service.enable_retries()
        self.test_get_billing_unit_value_error()

        # Disable retries and run test_get_billing_unit_value_error.
        _service.disable_retries()
        self.test_get_billing_unit_value_error()


class TestListBillingUnits:
    """
    Test Class for list_billing_units
    """

    @responses.activate
    def test_list_billing_units_all_params(self):
        """
        list_billing_units()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-units')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "crn": "crn:v1:bluemix:public:billing::a/<<enterprise_account_id>>::billing-unit:<<billing_unit_id>>", "name": "name", "enterprise_id": "enterprise_id", "currency_code": "USD", "country_code": "USA", "master": true, "created_at": "2019-05-01T00:00:00.000Z"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        enterprise_id = 'testString'
        account_group_id = 'testString'
        limit = 1
        start = 'testString'

        # Invoke method
        response = _service.list_billing_units(
            account_id=account_id,
            enterprise_id=enterprise_id,
            account_group_id=account_group_id,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'enterprise_id={}'.format(enterprise_id) in query_string
        assert 'account_group_id={}'.format(account_group_id) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_billing_units_all_params_with_retries(self):
        # Enable retries and run test_list_billing_units_all_params.
        _service.enable_retries()
        self.test_list_billing_units_all_params()

        # Disable retries and run test_list_billing_units_all_params.
        _service.disable_retries()
        self.test_list_billing_units_all_params()

    @responses.activate
    def test_list_billing_units_required_params(self):
        """
        test_list_billing_units_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-units')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "crn": "crn:v1:bluemix:public:billing::a/<<enterprise_account_id>>::billing-unit:<<billing_unit_id>>", "name": "name", "enterprise_id": "enterprise_id", "currency_code": "USD", "country_code": "USA", "master": true, "created_at": "2019-05-01T00:00:00.000Z"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Invoke method
        response = _service.list_billing_units()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_billing_units_required_params_with_retries(self):
        # Enable retries and run test_list_billing_units_required_params.
        _service.enable_retries()
        self.test_list_billing_units_required_params()

        # Disable retries and run test_list_billing_units_required_params.
        _service.disable_retries()
        self.test_list_billing_units_required_params()

    @responses.activate
    def test_list_billing_units_with_pager_get_next(self):
        """
        test_list_billing_units_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/billing-units')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","crn":"crn:v1:bluemix:public:billing::a/<<enterprise_account_id>>::billing-unit:<<billing_unit_id>>","name":"name","enterprise_id":"enterprise_id","currency_code":"USD","country_code":"USA","master":true,"created_at":"2019-05-01T00:00:00.000Z"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","crn":"crn:v1:bluemix:public:billing::a/<<enterprise_account_id>>::billing-unit:<<billing_unit_id>>","name":"name","enterprise_id":"enterprise_id","currency_code":"USD","country_code":"USA","master":true,"created_at":"2019-05-01T00:00:00.000Z"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = BillingUnitsPager(
            client=_service,
            account_id='testString',
            enterprise_id='testString',
            account_group_id='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_billing_units_with_pager_get_all(self):
        """
        test_list_billing_units_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/billing-units')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","crn":"crn:v1:bluemix:public:billing::a/<<enterprise_account_id>>::billing-unit:<<billing_unit_id>>","name":"name","enterprise_id":"enterprise_id","currency_code":"USD","country_code":"USA","master":true,"created_at":"2019-05-01T00:00:00.000Z"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","crn":"crn:v1:bluemix:public:billing::a/<<enterprise_account_id>>::billing-unit:<<billing_unit_id>>","name":"name","enterprise_id":"enterprise_id","currency_code":"USD","country_code":"USA","master":true,"created_at":"2019-05-01T00:00:00.000Z"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = BillingUnitsPager(
            client=_service,
            account_id='testString',
            enterprise_id='testString',
            account_group_id='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


# endregion
##############################################################################
# End of Service: BillingUnits
##############################################################################

##############################################################################
# Start of Service: BillingOptions
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = EnterpriseBillingUnitsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, EnterpriseBillingUnitsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = EnterpriseBillingUnitsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListBillingOptions:
    """
    Test Class for list_billing_options
    """

    @responses.activate
    def test_list_billing_options_all_params(self):
        """
        list_billing_options()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-options')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "billing_unit_id": "billing_unit_id", "start_date": "2019-05-01T00:00:00.000Z", "end_date": "2020-05-01T00:00:00.000Z", "state": "ACTIVE", "type": "SUBSCRIPTION", "category": "PLATFORM", "payment_instrument": {"anyKey": "anyValue"}, "duration_in_months": 11, "line_item_id": 10, "billing_system": {"anyKey": "anyValue"}, "renewal_mode_code": "renewal_mode_code", "updated_at": "2019-06-01T00:00:00.000Z"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        billing_unit_id = 'testString'
        limit = 1
        start = 'testString'

        # Invoke method
        response = _service.list_billing_options(billing_unit_id, limit=limit, start=start, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'billing_unit_id={}'.format(billing_unit_id) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_billing_options_all_params_with_retries(self):
        # Enable retries and run test_list_billing_options_all_params.
        _service.enable_retries()
        self.test_list_billing_options_all_params()

        # Disable retries and run test_list_billing_options_all_params.
        _service.disable_retries()
        self.test_list_billing_options_all_params()

    @responses.activate
    def test_list_billing_options_required_params(self):
        """
        test_list_billing_options_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-options')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "billing_unit_id": "billing_unit_id", "start_date": "2019-05-01T00:00:00.000Z", "end_date": "2020-05-01T00:00:00.000Z", "state": "ACTIVE", "type": "SUBSCRIPTION", "category": "PLATFORM", "payment_instrument": {"anyKey": "anyValue"}, "duration_in_months": 11, "line_item_id": 10, "billing_system": {"anyKey": "anyValue"}, "renewal_mode_code": "renewal_mode_code", "updated_at": "2019-06-01T00:00:00.000Z"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        billing_unit_id = 'testString'

        # Invoke method
        response = _service.list_billing_options(billing_unit_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'billing_unit_id={}'.format(billing_unit_id) in query_string

    def test_list_billing_options_required_params_with_retries(self):
        # Enable retries and run test_list_billing_options_required_params.
        _service.enable_retries()
        self.test_list_billing_options_required_params()

        # Disable retries and run test_list_billing_options_required_params.
        _service.disable_retries()
        self.test_list_billing_options_required_params()

    @responses.activate
    def test_list_billing_options_value_error(self):
        """
        test_list_billing_options_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-options')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"id": "id", "billing_unit_id": "billing_unit_id", "start_date": "2019-05-01T00:00:00.000Z", "end_date": "2020-05-01T00:00:00.000Z", "state": "ACTIVE", "type": "SUBSCRIPTION", "category": "PLATFORM", "payment_instrument": {"anyKey": "anyValue"}, "duration_in_months": 11, "line_item_id": 10, "billing_system": {"anyKey": "anyValue"}, "renewal_mode_code": "renewal_mode_code", "updated_at": "2019-06-01T00:00:00.000Z"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        billing_unit_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "billing_unit_id": billing_unit_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_billing_options(**req_copy)

    def test_list_billing_options_value_error_with_retries(self):
        # Enable retries and run test_list_billing_options_value_error.
        _service.enable_retries()
        self.test_list_billing_options_value_error()

        # Disable retries and run test_list_billing_options_value_error.
        _service.disable_retries()
        self.test_list_billing_options_value_error()

    @responses.activate
    def test_list_billing_options_with_pager_get_next(self):
        """
        test_list_billing_options_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/billing-options')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","billing_unit_id":"billing_unit_id","start_date":"2019-05-01T00:00:00.000Z","end_date":"2020-05-01T00:00:00.000Z","state":"ACTIVE","type":"SUBSCRIPTION","category":"PLATFORM","payment_instrument":{"anyKey":"anyValue"},"duration_in_months":11,"line_item_id":10,"billing_system":{"anyKey":"anyValue"},"renewal_mode_code":"renewal_mode_code","updated_at":"2019-06-01T00:00:00.000Z"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","billing_unit_id":"billing_unit_id","start_date":"2019-05-01T00:00:00.000Z","end_date":"2020-05-01T00:00:00.000Z","state":"ACTIVE","type":"SUBSCRIPTION","category":"PLATFORM","payment_instrument":{"anyKey":"anyValue"},"duration_in_months":11,"line_item_id":10,"billing_system":{"anyKey":"anyValue"},"renewal_mode_code":"renewal_mode_code","updated_at":"2019-06-01T00:00:00.000Z"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = BillingOptionsPager(
            client=_service,
            billing_unit_id='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_billing_options_with_pager_get_all(self):
        """
        test_list_billing_options_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/billing-options')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?start=1","resources":[{"id":"id","billing_unit_id":"billing_unit_id","start_date":"2019-05-01T00:00:00.000Z","end_date":"2020-05-01T00:00:00.000Z","state":"ACTIVE","type":"SUBSCRIPTION","category":"PLATFORM","payment_instrument":{"anyKey":"anyValue"},"duration_in_months":11,"line_item_id":10,"billing_system":{"anyKey":"anyValue"},"renewal_mode_code":"renewal_mode_code","updated_at":"2019-06-01T00:00:00.000Z"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"id":"id","billing_unit_id":"billing_unit_id","start_date":"2019-05-01T00:00:00.000Z","end_date":"2020-05-01T00:00:00.000Z","state":"ACTIVE","type":"SUBSCRIPTION","category":"PLATFORM","payment_instrument":{"anyKey":"anyValue"},"duration_in_months":11,"line_item_id":10,"billing_system":{"anyKey":"anyValue"},"renewal_mode_code":"renewal_mode_code","updated_at":"2019-06-01T00:00:00.000Z"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = BillingOptionsPager(
            client=_service,
            billing_unit_id='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


# endregion
##############################################################################
# End of Service: BillingOptions
##############################################################################

##############################################################################
# Start of Service: CreditPools
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = EnterpriseBillingUnitsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, EnterpriseBillingUnitsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = EnterpriseBillingUnitsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetCreditPools:
    """
    Test Class for get_credit_pools
    """

    @responses.activate
    def test_get_credit_pools_all_params(self):
        """
        get_credit_pools()
        """
        # Set up mock
        url = preprocess_url('/v1/credit-pools')
        mock_response = '{"rows_count": 2, "next_url": "next_url", "resources": [{"type": "PLATFORM", "currency_code": "USD", "billing_unit_id": "billing_unit_id", "term_credits": [{"billing_option_id": "JWX986YRGFSHACQUEFOI", "category": "PLATFORM", "start_date": "2019-05-01T00:00:00.000Z", "end_date": "2020-04-30T23:59:29.999Z", "total_credits": 10000, "starting_balance": 9000, "used_credits": 9500, "current_balance": 0, "resources": [{"anyKey": "anyValue"}]}], "overage": {"cost": 500, "resources": [{"anyKey": "anyValue"}]}}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        billing_unit_id = 'testString'
        date = 'testString'
        type = 'testString'
        limit = 1
        start = 'testString'

        # Invoke method
        response = _service.get_credit_pools(
            billing_unit_id, date=date, type=type, limit=limit, start=start, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'billing_unit_id={}'.format(billing_unit_id) in query_string
        assert 'date={}'.format(date) in query_string
        assert 'type={}'.format(type) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_get_credit_pools_all_params_with_retries(self):
        # Enable retries and run test_get_credit_pools_all_params.
        _service.enable_retries()
        self.test_get_credit_pools_all_params()

        # Disable retries and run test_get_credit_pools_all_params.
        _service.disable_retries()
        self.test_get_credit_pools_all_params()

    @responses.activate
    def test_get_credit_pools_required_params(self):
        """
        test_get_credit_pools_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/credit-pools')
        mock_response = '{"rows_count": 2, "next_url": "next_url", "resources": [{"type": "PLATFORM", "currency_code": "USD", "billing_unit_id": "billing_unit_id", "term_credits": [{"billing_option_id": "JWX986YRGFSHACQUEFOI", "category": "PLATFORM", "start_date": "2019-05-01T00:00:00.000Z", "end_date": "2020-04-30T23:59:29.999Z", "total_credits": 10000, "starting_balance": 9000, "used_credits": 9500, "current_balance": 0, "resources": [{"anyKey": "anyValue"}]}], "overage": {"cost": 500, "resources": [{"anyKey": "anyValue"}]}}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        billing_unit_id = 'testString'

        # Invoke method
        response = _service.get_credit_pools(billing_unit_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'billing_unit_id={}'.format(billing_unit_id) in query_string

    def test_get_credit_pools_required_params_with_retries(self):
        # Enable retries and run test_get_credit_pools_required_params.
        _service.enable_retries()
        self.test_get_credit_pools_required_params()

        # Disable retries and run test_get_credit_pools_required_params.
        _service.disable_retries()
        self.test_get_credit_pools_required_params()

    @responses.activate
    def test_get_credit_pools_value_error(self):
        """
        test_get_credit_pools_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/credit-pools')
        mock_response = '{"rows_count": 2, "next_url": "next_url", "resources": [{"type": "PLATFORM", "currency_code": "USD", "billing_unit_id": "billing_unit_id", "term_credits": [{"billing_option_id": "JWX986YRGFSHACQUEFOI", "category": "PLATFORM", "start_date": "2019-05-01T00:00:00.000Z", "end_date": "2020-04-30T23:59:29.999Z", "total_credits": 10000, "starting_balance": 9000, "used_credits": 9500, "current_balance": 0, "resources": [{"anyKey": "anyValue"}]}], "overage": {"cost": 500, "resources": [{"anyKey": "anyValue"}]}}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        billing_unit_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "billing_unit_id": billing_unit_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_credit_pools(**req_copy)

    def test_get_credit_pools_value_error_with_retries(self):
        # Enable retries and run test_get_credit_pools_value_error.
        _service.enable_retries()
        self.test_get_credit_pools_value_error()

        # Disable retries and run test_get_credit_pools_value_error.
        _service.disable_retries()
        self.test_get_credit_pools_value_error()


# endregion
##############################################################################
# End of Service: CreditPools
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_BillingOption:
    """
    Test Class for BillingOption
    """

    def test_billing_option_serialization(self):
        """
        Test serialization/deserialization for BillingOption
        """

        # Construct a json representation of a BillingOption model
        billing_option_model_json = {}
        billing_option_model_json['id'] = 'testString'
        billing_option_model_json['billing_unit_id'] = 'testString'
        billing_option_model_json['start_date'] = '2019-05-01T00:00:00Z'
        billing_option_model_json['end_date'] = '2020-05-01T00:00:00Z'
        billing_option_model_json['state'] = 'ACTIVE'
        billing_option_model_json['type'] = 'SUBSCRIPTION'
        billing_option_model_json['category'] = 'PLATFORM'
        billing_option_model_json['payment_instrument'] = {'foo': 'bar'}
        billing_option_model_json['duration_in_months'] = 11
        billing_option_model_json['line_item_id'] = 10
        billing_option_model_json['billing_system'] = {'foo': 'bar'}
        billing_option_model_json['renewal_mode_code'] = 'testString'
        billing_option_model_json['updated_at'] = '2019-06-01T00:00:00Z'

        # Construct a model instance of BillingOption by calling from_dict on the json representation
        billing_option_model = BillingOption.from_dict(billing_option_model_json)
        assert billing_option_model != False

        # Construct a model instance of BillingOption by calling from_dict on the json representation
        billing_option_model_dict = BillingOption.from_dict(billing_option_model_json).__dict__
        billing_option_model2 = BillingOption(**billing_option_model_dict)

        # Verify the model instances are equivalent
        assert billing_option_model == billing_option_model2

        # Convert model instance back to dict and verify no loss of data
        billing_option_model_json2 = billing_option_model.to_dict()
        assert billing_option_model_json2 == billing_option_model_json


class TestModel_BillingOptionsList:
    """
    Test Class for BillingOptionsList
    """

    def test_billing_options_list_serialization(self):
        """
        Test serialization/deserialization for BillingOptionsList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        billing_option_model = {}  # BillingOption
        billing_option_model['id'] = 'CFL_JJKLVZ2I0JE-_MGU'
        billing_option_model['billing_unit_id'] = 'e19fa97c9bb34963a31a2008044d8b59'
        billing_option_model['start_date'] = '2019-05-02T07:00:00Z'
        billing_option_model['end_date'] = '2019-11-30T08:00:00Z'
        billing_option_model['state'] = 'ACTIVE'
        billing_option_model['type'] = 'SUBSCRIPTION'
        billing_option_model['category'] = 'PLATFORM'
        billing_option_model['payment_instrument'] = {'foo': 'bar'}
        billing_option_model['duration_in_months'] = 6
        billing_option_model['line_item_id'] = 10
        billing_option_model['billing_system'] = {'foo': 'bar'}
        billing_option_model['renewal_mode_code'] = 'T'
        billing_option_model['updated_at'] = '2019-05-02T07:00:00Z'

        # Construct a json representation of a BillingOptionsList model
        billing_options_list_model_json = {}
        billing_options_list_model_json['rows_count'] = 38
        billing_options_list_model_json['next_url'] = 'testString'
        billing_options_list_model_json['resources'] = [billing_option_model]

        # Construct a model instance of BillingOptionsList by calling from_dict on the json representation
        billing_options_list_model = BillingOptionsList.from_dict(billing_options_list_model_json)
        assert billing_options_list_model != False

        # Construct a model instance of BillingOptionsList by calling from_dict on the json representation
        billing_options_list_model_dict = BillingOptionsList.from_dict(billing_options_list_model_json).__dict__
        billing_options_list_model2 = BillingOptionsList(**billing_options_list_model_dict)

        # Verify the model instances are equivalent
        assert billing_options_list_model == billing_options_list_model2

        # Convert model instance back to dict and verify no loss of data
        billing_options_list_model_json2 = billing_options_list_model.to_dict()
        assert billing_options_list_model_json2 == billing_options_list_model_json


class TestModel_BillingUnit:
    """
    Test Class for BillingUnit
    """

    def test_billing_unit_serialization(self):
        """
        Test serialization/deserialization for BillingUnit
        """

        # Construct a json representation of a BillingUnit model
        billing_unit_model_json = {}
        billing_unit_model_json['id'] = 'testString'
        billing_unit_model_json['crn'] = (
            'crn:v1:bluemix:public:billing::a/<<enterprise_account_id>>::billing-unit:<<billing_unit_id>>'
        )
        billing_unit_model_json['name'] = 'testString'
        billing_unit_model_json['enterprise_id'] = 'testString'
        billing_unit_model_json['currency_code'] = 'USD'
        billing_unit_model_json['country_code'] = 'USA'
        billing_unit_model_json['master'] = True
        billing_unit_model_json['created_at'] = '2019-05-01T00:00:00Z'

        # Construct a model instance of BillingUnit by calling from_dict on the json representation
        billing_unit_model = BillingUnit.from_dict(billing_unit_model_json)
        assert billing_unit_model != False

        # Construct a model instance of BillingUnit by calling from_dict on the json representation
        billing_unit_model_dict = BillingUnit.from_dict(billing_unit_model_json).__dict__
        billing_unit_model2 = BillingUnit(**billing_unit_model_dict)

        # Verify the model instances are equivalent
        assert billing_unit_model == billing_unit_model2

        # Convert model instance back to dict and verify no loss of data
        billing_unit_model_json2 = billing_unit_model.to_dict()
        assert billing_unit_model_json2 == billing_unit_model_json


class TestModel_BillingUnitsList:
    """
    Test Class for BillingUnitsList
    """

    def test_billing_units_list_serialization(self):
        """
        Test serialization/deserialization for BillingUnitsList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        billing_unit_model = {}  # BillingUnit
        billing_unit_model['id'] = '$BILLING_UNIT_ID'
        billing_unit_model['crn'] = (
            'crn:v1:bluemix:public:billing::a/$ENTERPRISE_ACCOUNT_ID::billing-unit:$BILLING_UNIT_ID'
        )
        billing_unit_model['name'] = 'Sample Billing Unit'
        billing_unit_model['enterprise_id'] = '$ENTERPRISE_ID'
        billing_unit_model['currency_code'] = 'USD'
        billing_unit_model['country_code'] = 'USA'
        billing_unit_model['master'] = True
        billing_unit_model['created_at'] = '2019-07-01T00:00:00Z'

        # Construct a json representation of a BillingUnitsList model
        billing_units_list_model_json = {}
        billing_units_list_model_json['rows_count'] = 38
        billing_units_list_model_json['next_url'] = 'testString'
        billing_units_list_model_json['resources'] = [billing_unit_model]

        # Construct a model instance of BillingUnitsList by calling from_dict on the json representation
        billing_units_list_model = BillingUnitsList.from_dict(billing_units_list_model_json)
        assert billing_units_list_model != False

        # Construct a model instance of BillingUnitsList by calling from_dict on the json representation
        billing_units_list_model_dict = BillingUnitsList.from_dict(billing_units_list_model_json).__dict__
        billing_units_list_model2 = BillingUnitsList(**billing_units_list_model_dict)

        # Verify the model instances are equivalent
        assert billing_units_list_model == billing_units_list_model2

        # Convert model instance back to dict and verify no loss of data
        billing_units_list_model_json2 = billing_units_list_model.to_dict()
        assert billing_units_list_model_json2 == billing_units_list_model_json


class TestModel_CreditPool:
    """
    Test Class for CreditPool
    """

    def test_credit_pool_serialization(self):
        """
        Test serialization/deserialization for CreditPool
        """

        # Construct dict forms of any model objects needed in order to build this model.

        term_credits_model = {}  # TermCredits
        term_credits_model['billing_option_id'] = '$BILLING_OPTION_ID'
        term_credits_model['category'] = 'PLATFORM'
        term_credits_model['start_date'] = '2019-07-01T01:00:00Z'
        term_credits_model['end_date'] = '2020-06-30T23:59:59.999000Z'
        term_credits_model['total_credits'] = 7000
        term_credits_model['starting_balance'] = 6000
        term_credits_model['used_credits'] = 1000
        term_credits_model['current_balance'] = 5000
        term_credits_model['resources'] = []

        credit_pool_overage_model = {}  # CreditPoolOverage
        credit_pool_overage_model['cost'] = 0
        credit_pool_overage_model['resources'] = []

        # Construct a json representation of a CreditPool model
        credit_pool_model_json = {}
        credit_pool_model_json['type'] = 'PLATFORM'
        credit_pool_model_json['currency_code'] = 'USD'
        credit_pool_model_json['billing_unit_id'] = 'testString'
        credit_pool_model_json['term_credits'] = [term_credits_model]
        credit_pool_model_json['overage'] = credit_pool_overage_model

        # Construct a model instance of CreditPool by calling from_dict on the json representation
        credit_pool_model = CreditPool.from_dict(credit_pool_model_json)
        assert credit_pool_model != False

        # Construct a model instance of CreditPool by calling from_dict on the json representation
        credit_pool_model_dict = CreditPool.from_dict(credit_pool_model_json).__dict__
        credit_pool_model2 = CreditPool(**credit_pool_model_dict)

        # Verify the model instances are equivalent
        assert credit_pool_model == credit_pool_model2

        # Convert model instance back to dict and verify no loss of data
        credit_pool_model_json2 = credit_pool_model.to_dict()
        assert credit_pool_model_json2 == credit_pool_model_json


class TestModel_CreditPoolOverage:
    """
    Test Class for CreditPoolOverage
    """

    def test_credit_pool_overage_serialization(self):
        """
        Test serialization/deserialization for CreditPoolOverage
        """

        # Construct a json representation of a CreditPoolOverage model
        credit_pool_overage_model_json = {}
        credit_pool_overage_model_json['cost'] = 500
        credit_pool_overage_model_json['resources'] = [{'foo': 'bar'}]

        # Construct a model instance of CreditPoolOverage by calling from_dict on the json representation
        credit_pool_overage_model = CreditPoolOverage.from_dict(credit_pool_overage_model_json)
        assert credit_pool_overage_model != False

        # Construct a model instance of CreditPoolOverage by calling from_dict on the json representation
        credit_pool_overage_model_dict = CreditPoolOverage.from_dict(credit_pool_overage_model_json).__dict__
        credit_pool_overage_model2 = CreditPoolOverage(**credit_pool_overage_model_dict)

        # Verify the model instances are equivalent
        assert credit_pool_overage_model == credit_pool_overage_model2

        # Convert model instance back to dict and verify no loss of data
        credit_pool_overage_model_json2 = credit_pool_overage_model.to_dict()
        assert credit_pool_overage_model_json2 == credit_pool_overage_model_json


class TestModel_CreditPoolsList:
    """
    Test Class for CreditPoolsList
    """

    def test_credit_pools_list_serialization(self):
        """
        Test serialization/deserialization for CreditPoolsList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        term_credits_model = {}  # TermCredits
        term_credits_model['billing_option_id'] = '$BILLING_OPTION_ID'
        term_credits_model['category'] = 'PLATFORM'
        term_credits_model['start_date'] = '2019-07-01T01:00:00Z'
        term_credits_model['end_date'] = '2020-06-30T23:59:59.999000Z'
        term_credits_model['total_credits'] = 7000
        term_credits_model['starting_balance'] = 6000
        term_credits_model['used_credits'] = 1000
        term_credits_model['current_balance'] = 5000
        term_credits_model['resources'] = []

        credit_pool_overage_model = {}  # CreditPoolOverage
        credit_pool_overage_model['cost'] = 0
        credit_pool_overage_model['resources'] = []

        credit_pool_model = {}  # CreditPool
        credit_pool_model['type'] = 'PLATFORM'
        credit_pool_model['currency_code'] = 'USD'
        credit_pool_model['billing_unit_id'] = '$BILLING_UNIT_ID'
        credit_pool_model['term_credits'] = [term_credits_model]
        credit_pool_model['overage'] = credit_pool_overage_model

        # Construct a json representation of a CreditPoolsList model
        credit_pools_list_model_json = {}
        credit_pools_list_model_json['rows_count'] = 2
        credit_pools_list_model_json['next_url'] = 'testString'
        credit_pools_list_model_json['resources'] = [credit_pool_model]

        # Construct a model instance of CreditPoolsList by calling from_dict on the json representation
        credit_pools_list_model = CreditPoolsList.from_dict(credit_pools_list_model_json)
        assert credit_pools_list_model != False

        # Construct a model instance of CreditPoolsList by calling from_dict on the json representation
        credit_pools_list_model_dict = CreditPoolsList.from_dict(credit_pools_list_model_json).__dict__
        credit_pools_list_model2 = CreditPoolsList(**credit_pools_list_model_dict)

        # Verify the model instances are equivalent
        assert credit_pools_list_model == credit_pools_list_model2

        # Convert model instance back to dict and verify no loss of data
        credit_pools_list_model_json2 = credit_pools_list_model.to_dict()
        assert credit_pools_list_model_json2 == credit_pools_list_model_json


class TestModel_TermCredits:
    """
    Test Class for TermCredits
    """

    def test_term_credits_serialization(self):
        """
        Test serialization/deserialization for TermCredits
        """

        # Construct a json representation of a TermCredits model
        term_credits_model_json = {}
        term_credits_model_json['billing_option_id'] = 'JWX986YRGFSHACQUEFOI'
        term_credits_model_json['category'] = 'PLATFORM'
        term_credits_model_json['start_date'] = '2019-05-01T00:00:00Z'
        term_credits_model_json['end_date'] = '2020-04-30T23:59:29.999000Z'
        term_credits_model_json['total_credits'] = 10000
        term_credits_model_json['starting_balance'] = 9000
        term_credits_model_json['used_credits'] = 9500
        term_credits_model_json['current_balance'] = 0
        term_credits_model_json['resources'] = [{'foo': 'bar'}]

        # Construct a model instance of TermCredits by calling from_dict on the json representation
        term_credits_model = TermCredits.from_dict(term_credits_model_json)
        assert term_credits_model != False

        # Construct a model instance of TermCredits by calling from_dict on the json representation
        term_credits_model_dict = TermCredits.from_dict(term_credits_model_json).__dict__
        term_credits_model2 = TermCredits(**term_credits_model_dict)

        # Verify the model instances are equivalent
        assert term_credits_model == term_credits_model2

        # Convert model instance back to dict and verify no loss of data
        term_credits_model_json2 = term_credits_model.to_dict()
        assert term_credits_model_json2 == term_credits_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
