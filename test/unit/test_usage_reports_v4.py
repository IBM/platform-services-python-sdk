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
Unit Tests for UsageReportsV4
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
from ibm_platform_services.usage_reports_v4 import *


_service = UsageReportsV4(authenticator=NoAuthAuthenticator())

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
# Start of Service: AccountOperations
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

        service = UsageReportsV4.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, UsageReportsV4)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = UsageReportsV4.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetAccountSummary:
    """
    Test Class for get_account_summary
    """

    @responses.activate
    def test_get_account_summary_all_params(self):
        """
        get_account_summary()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/summary/testString')
        mock_response = '{"account_id": "account_id", "account_resources": [{"resource_id": "resource_id", "resource_name": "resource_name", "billable_cost": 13, "billable_rated_cost": 19, "non_billable_cost": 17, "non_billable_rated_cost": 23, "plans": [{"plan_id": "plan_id", "plan_name": "plan_name", "pricing_region": "pricing_region", "pricing_plan_id": "pricing_plan_id", "billable": true, "cost": 4, "rated_cost": 10, "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}], "pending": true}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "month": "month", "billing_country_code": "billing_country_code", "billing_currency_code": "billing_currency_code", "resources": {"billable_cost": 13, "non_billable_cost": 17}, "offers": [{"offer_id": "offer_id", "credits_total": 13, "offer_template": "offer_template", "valid_from": "2019-01-01T12:00:00.000Z", "expires_on": "2019-01-01T12:00:00.000Z", "credits": {"starting_balance": 16, "used": 4, "balance": 7}}], "support": [{"cost": 4, "type": "type", "overage": 7}], "support_resources": ["anyValue"], "subscription": {"overage": 7, "subscriptions": [{"subscription_id": "subscription_id", "charge_agreement_number": "charge_agreement_number", "type": "type", "subscription_amount": 19, "start": "2019-01-01T12:00:00.000Z", "end": "2019-01-01T12:00:00.000Z", "credits_total": 13, "terms": [{"start": "2019-01-01T12:00:00.000Z", "end": "2019-01-01T12:00:00.000Z", "credits": {"total": 5, "starting_balance": 16, "used": 4, "balance": 7}}]}]}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = _service.get_account_summary(account_id, billingmonth, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_account_summary_all_params_with_retries(self):
        # Enable retries and run test_get_account_summary_all_params.
        _service.enable_retries()
        self.test_get_account_summary_all_params()

        # Disable retries and run test_get_account_summary_all_params.
        _service.disable_retries()
        self.test_get_account_summary_all_params()

    @responses.activate
    def test_get_account_summary_value_error(self):
        """
        test_get_account_summary_value_error()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/summary/testString')
        mock_response = '{"account_id": "account_id", "account_resources": [{"resource_id": "resource_id", "resource_name": "resource_name", "billable_cost": 13, "billable_rated_cost": 19, "non_billable_cost": 17, "non_billable_rated_cost": 23, "plans": [{"plan_id": "plan_id", "plan_name": "plan_name", "pricing_region": "pricing_region", "pricing_plan_id": "pricing_plan_id", "billable": true, "cost": 4, "rated_cost": 10, "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}], "pending": true}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "month": "month", "billing_country_code": "billing_country_code", "billing_currency_code": "billing_currency_code", "resources": {"billable_cost": 13, "non_billable_cost": 17}, "offers": [{"offer_id": "offer_id", "credits_total": 13, "offer_template": "offer_template", "valid_from": "2019-01-01T12:00:00.000Z", "expires_on": "2019-01-01T12:00:00.000Z", "credits": {"starting_balance": 16, "used": 4, "balance": 7}}], "support": [{"cost": 4, "type": "type", "overage": 7}], "support_resources": ["anyValue"], "subscription": {"overage": 7, "subscriptions": [{"subscription_id": "subscription_id", "charge_agreement_number": "charge_agreement_number", "type": "type", "subscription_amount": 19, "start": "2019-01-01T12:00:00.000Z", "end": "2019-01-01T12:00:00.000Z", "credits_total": 13, "terms": [{"start": "2019-01-01T12:00:00.000Z", "end": "2019-01-01T12:00:00.000Z", "credits": {"total": 5, "starting_balance": 16, "used": 4, "balance": 7}}]}]}}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        billingmonth = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "billingmonth": billingmonth,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_account_summary(**req_copy)

    def test_get_account_summary_value_error_with_retries(self):
        # Enable retries and run test_get_account_summary_value_error.
        _service.enable_retries()
        self.test_get_account_summary_value_error()

        # Disable retries and run test_get_account_summary_value_error.
        _service.disable_retries()
        self.test_get_account_summary_value_error()


class TestGetAccountUsage:
    """
    Test Class for get_account_usage
    """

    @responses.activate
    def test_get_account_usage_all_params(self):
        """
        get_account_usage()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/usage/testString')
        mock_response = '{"account_id": "account_id", "pricing_country": "USA", "currency_code": "USD", "month": "2017-08", "resources": [{"resource_id": "resource_id", "resource_name": "resource_name", "billable_cost": 13, "billable_rated_cost": 19, "non_billable_cost": 17, "non_billable_rated_cost": 23, "plans": [{"plan_id": "plan_id", "plan_name": "plan_name", "pricing_region": "pricing_region", "pricing_plan_id": "pricing_plan_id", "billable": true, "cost": 4, "rated_cost": 10, "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}], "pending": true}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "currency_rate": 10.8716}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        billingmonth = 'testString'
        names = True
        accept_language = 'testString'

        # Invoke method
        response = _service.get_account_usage(
            account_id, billingmonth, names=names, accept_language=accept_language, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert '_names={}'.format('true' if names else 'false') in query_string

    def test_get_account_usage_all_params_with_retries(self):
        # Enable retries and run test_get_account_usage_all_params.
        _service.enable_retries()
        self.test_get_account_usage_all_params()

        # Disable retries and run test_get_account_usage_all_params.
        _service.disable_retries()
        self.test_get_account_usage_all_params()

    @responses.activate
    def test_get_account_usage_required_params(self):
        """
        test_get_account_usage_required_params()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/usage/testString')
        mock_response = '{"account_id": "account_id", "pricing_country": "USA", "currency_code": "USD", "month": "2017-08", "resources": [{"resource_id": "resource_id", "resource_name": "resource_name", "billable_cost": 13, "billable_rated_cost": 19, "non_billable_cost": 17, "non_billable_rated_cost": 23, "plans": [{"plan_id": "plan_id", "plan_name": "plan_name", "pricing_region": "pricing_region", "pricing_plan_id": "pricing_plan_id", "billable": true, "cost": 4, "rated_cost": 10, "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}], "pending": true}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "currency_rate": 10.8716}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = _service.get_account_usage(account_id, billingmonth, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_account_usage_required_params_with_retries(self):
        # Enable retries and run test_get_account_usage_required_params.
        _service.enable_retries()
        self.test_get_account_usage_required_params()

        # Disable retries and run test_get_account_usage_required_params.
        _service.disable_retries()
        self.test_get_account_usage_required_params()

    @responses.activate
    def test_get_account_usage_value_error(self):
        """
        test_get_account_usage_value_error()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/usage/testString')
        mock_response = '{"account_id": "account_id", "pricing_country": "USA", "currency_code": "USD", "month": "2017-08", "resources": [{"resource_id": "resource_id", "resource_name": "resource_name", "billable_cost": 13, "billable_rated_cost": 19, "non_billable_cost": 17, "non_billable_rated_cost": 23, "plans": [{"plan_id": "plan_id", "plan_name": "plan_name", "pricing_region": "pricing_region", "pricing_plan_id": "pricing_plan_id", "billable": true, "cost": 4, "rated_cost": 10, "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}], "pending": true}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "currency_rate": 10.8716}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        billingmonth = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "billingmonth": billingmonth,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_account_usage(**req_copy)

    def test_get_account_usage_value_error_with_retries(self):
        # Enable retries and run test_get_account_usage_value_error.
        _service.enable_retries()
        self.test_get_account_usage_value_error()

        # Disable retries and run test_get_account_usage_value_error.
        _service.disable_retries()
        self.test_get_account_usage_value_error()


# endregion
##############################################################################
# End of Service: AccountOperations
##############################################################################

##############################################################################
# Start of Service: ResourceOperations
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

        service = UsageReportsV4.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, UsageReportsV4)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = UsageReportsV4.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetResourceGroupUsage:
    """
    Test Class for get_resource_group_usage
    """

    @responses.activate
    def test_get_resource_group_usage_all_params(self):
        """
        get_resource_group_usage()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/resource_groups/testString/usage/testString')
        mock_response = '{"account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_name": "resource_group_name", "pricing_country": "USA", "currency_code": "USD", "month": "2017-08", "resources": [{"resource_id": "resource_id", "resource_name": "resource_name", "billable_cost": 13, "billable_rated_cost": 19, "non_billable_cost": 17, "non_billable_rated_cost": 23, "plans": [{"plan_id": "plan_id", "plan_name": "plan_name", "pricing_region": "pricing_region", "pricing_plan_id": "pricing_plan_id", "billable": true, "cost": 4, "rated_cost": 10, "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}], "pending": true}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "currency_rate": 10.8716}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_group_id = 'testString'
        billingmonth = 'testString'
        names = True
        accept_language = 'testString'

        # Invoke method
        response = _service.get_resource_group_usage(
            account_id, resource_group_id, billingmonth, names=names, accept_language=accept_language, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert '_names={}'.format('true' if names else 'false') in query_string

    def test_get_resource_group_usage_all_params_with_retries(self):
        # Enable retries and run test_get_resource_group_usage_all_params.
        _service.enable_retries()
        self.test_get_resource_group_usage_all_params()

        # Disable retries and run test_get_resource_group_usage_all_params.
        _service.disable_retries()
        self.test_get_resource_group_usage_all_params()

    @responses.activate
    def test_get_resource_group_usage_required_params(self):
        """
        test_get_resource_group_usage_required_params()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/resource_groups/testString/usage/testString')
        mock_response = '{"account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_name": "resource_group_name", "pricing_country": "USA", "currency_code": "USD", "month": "2017-08", "resources": [{"resource_id": "resource_id", "resource_name": "resource_name", "billable_cost": 13, "billable_rated_cost": 19, "non_billable_cost": 17, "non_billable_rated_cost": 23, "plans": [{"plan_id": "plan_id", "plan_name": "plan_name", "pricing_region": "pricing_region", "pricing_plan_id": "pricing_plan_id", "billable": true, "cost": 4, "rated_cost": 10, "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}], "pending": true}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "currency_rate": 10.8716}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_group_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = _service.get_resource_group_usage(account_id, resource_group_id, billingmonth, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_resource_group_usage_required_params_with_retries(self):
        # Enable retries and run test_get_resource_group_usage_required_params.
        _service.enable_retries()
        self.test_get_resource_group_usage_required_params()

        # Disable retries and run test_get_resource_group_usage_required_params.
        _service.disable_retries()
        self.test_get_resource_group_usage_required_params()

    @responses.activate
    def test_get_resource_group_usage_value_error(self):
        """
        test_get_resource_group_usage_value_error()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/resource_groups/testString/usage/testString')
        mock_response = '{"account_id": "account_id", "resource_group_id": "resource_group_id", "resource_group_name": "resource_group_name", "pricing_country": "USA", "currency_code": "USD", "month": "2017-08", "resources": [{"resource_id": "resource_id", "resource_name": "resource_name", "billable_cost": 13, "billable_rated_cost": 19, "non_billable_cost": 17, "non_billable_rated_cost": 23, "plans": [{"plan_id": "plan_id", "plan_name": "plan_name", "pricing_region": "pricing_region", "pricing_plan_id": "pricing_plan_id", "billable": true, "cost": 4, "rated_cost": 10, "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}], "pending": true}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "currency_rate": 10.8716}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_group_id = 'testString'
        billingmonth = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "resource_group_id": resource_group_id,
            "billingmonth": billingmonth,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_resource_group_usage(**req_copy)

    def test_get_resource_group_usage_value_error_with_retries(self):
        # Enable retries and run test_get_resource_group_usage_value_error.
        _service.enable_retries()
        self.test_get_resource_group_usage_value_error()

        # Disable retries and run test_get_resource_group_usage_value_error.
        _service.disable_retries()
        self.test_get_resource_group_usage_value_error()


class TestGetResourceUsageAccount:
    """
    Test Class for get_resource_usage_account
    """

    @responses.activate
    def test_get_resource_usage_account_all_params(self):
        """
        get_resource_usage_account()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/resource_instances/usage/testString')
        mock_response = '{"limit": 5, "count": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"account_id": "account_id", "resource_instance_id": "resource_instance_id", "resource_instance_name": "resource_instance_name", "resource_id": "resource_id", "resource_name": "resource_name", "resource_group_id": "resource_group_id", "resource_group_name": "resource_group_name", "organization_id": "organization_id", "organization_name": "organization_name", "space_id": "space_id", "space_name": "space_name", "consumer_id": "consumer_id", "region": "region", "pricing_region": "pricing_region", "pricing_country": "USA", "currency_code": "USD", "billable": true, "plan_id": "plan_id", "plan_name": "plan_name", "month": "2017-08", "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "pending": true, "currency_rate": 10.8716}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        billingmonth = 'testString'
        names = True
        accept_language = 'testString'
        limit = 1
        start = 'testString'
        resource_group_id = 'testString'
        organization_id = 'testString'
        resource_instance_id = 'testString'
        resource_id = 'testString'
        plan_id = 'testString'
        region = 'testString'

        # Invoke method
        response = _service.get_resource_usage_account(
            account_id,
            billingmonth,
            names=names,
            accept_language=accept_language,
            limit=limit,
            start=start,
            resource_group_id=resource_group_id,
            organization_id=organization_id,
            resource_instance_id=resource_instance_id,
            resource_id=resource_id,
            plan_id=plan_id,
            region=region,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert '_names={}'.format('true' if names else 'false') in query_string
        assert '_limit={}'.format(limit) in query_string
        assert '_start={}'.format(start) in query_string
        assert 'resource_group_id={}'.format(resource_group_id) in query_string
        assert 'organization_id={}'.format(organization_id) in query_string
        assert 'resource_instance_id={}'.format(resource_instance_id) in query_string
        assert 'resource_id={}'.format(resource_id) in query_string
        assert 'plan_id={}'.format(plan_id) in query_string
        assert 'region={}'.format(region) in query_string

    def test_get_resource_usage_account_all_params_with_retries(self):
        # Enable retries and run test_get_resource_usage_account_all_params.
        _service.enable_retries()
        self.test_get_resource_usage_account_all_params()

        # Disable retries and run test_get_resource_usage_account_all_params.
        _service.disable_retries()
        self.test_get_resource_usage_account_all_params()

    @responses.activate
    def test_get_resource_usage_account_required_params(self):
        """
        test_get_resource_usage_account_required_params()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/resource_instances/usage/testString')
        mock_response = '{"limit": 5, "count": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"account_id": "account_id", "resource_instance_id": "resource_instance_id", "resource_instance_name": "resource_instance_name", "resource_id": "resource_id", "resource_name": "resource_name", "resource_group_id": "resource_group_id", "resource_group_name": "resource_group_name", "organization_id": "organization_id", "organization_name": "organization_name", "space_id": "space_id", "space_name": "space_name", "consumer_id": "consumer_id", "region": "region", "pricing_region": "pricing_region", "pricing_country": "USA", "currency_code": "USD", "billable": true, "plan_id": "plan_id", "plan_name": "plan_name", "month": "2017-08", "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "pending": true, "currency_rate": 10.8716}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = _service.get_resource_usage_account(account_id, billingmonth, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_resource_usage_account_required_params_with_retries(self):
        # Enable retries and run test_get_resource_usage_account_required_params.
        _service.enable_retries()
        self.test_get_resource_usage_account_required_params()

        # Disable retries and run test_get_resource_usage_account_required_params.
        _service.disable_retries()
        self.test_get_resource_usage_account_required_params()

    @responses.activate
    def test_get_resource_usage_account_value_error(self):
        """
        test_get_resource_usage_account_value_error()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/resource_instances/usage/testString')
        mock_response = '{"limit": 5, "count": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"account_id": "account_id", "resource_instance_id": "resource_instance_id", "resource_instance_name": "resource_instance_name", "resource_id": "resource_id", "resource_name": "resource_name", "resource_group_id": "resource_group_id", "resource_group_name": "resource_group_name", "organization_id": "organization_id", "organization_name": "organization_name", "space_id": "space_id", "space_name": "space_name", "consumer_id": "consumer_id", "region": "region", "pricing_region": "pricing_region", "pricing_country": "USA", "currency_code": "USD", "billable": true, "plan_id": "plan_id", "plan_name": "plan_name", "month": "2017-08", "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "pending": true, "currency_rate": 10.8716}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        billingmonth = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "billingmonth": billingmonth,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_resource_usage_account(**req_copy)

    def test_get_resource_usage_account_value_error_with_retries(self):
        # Enable retries and run test_get_resource_usage_account_value_error.
        _service.enable_retries()
        self.test_get_resource_usage_account_value_error()

        # Disable retries and run test_get_resource_usage_account_value_error.
        _service.disable_retries()
        self.test_get_resource_usage_account_value_error()

    @responses.activate
    def test_get_resource_usage_account_with_pager_get_next(self):
        """
        test_get_resource_usage_account_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v4/accounts/testString/resource_instances/usage/testString')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?_start=1"},"total_count":2,"limit":1,"resources":[{"account_id":"account_id","resource_instance_id":"resource_instance_id","resource_instance_name":"resource_instance_name","resource_id":"resource_id","resource_name":"resource_name","resource_group_id":"resource_group_id","resource_group_name":"resource_group_name","organization_id":"organization_id","organization_name":"organization_name","space_id":"space_id","space_name":"space_name","consumer_id":"consumer_id","region":"region","pricing_region":"pricing_region","pricing_country":"USA","currency_code":"USD","billable":true,"plan_id":"plan_id","plan_name":"plan_name","month":"2017-08","usage":[{"metric":"UP-TIME","metric_name":"UP-TIME","quantity":711.11,"rateable_quantity":700,"cost":123.45,"rated_cost":130.0,"price":["anyValue"],"unit":"HOURS","unit_name":"HOURS","non_chargeable":true,"discounts":[{"ref":"Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9","name":"platform-discount","display_name":"Platform Service Discount","discount":5}]}],"pending":true,"currency_rate":10.8716}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"account_id":"account_id","resource_instance_id":"resource_instance_id","resource_instance_name":"resource_instance_name","resource_id":"resource_id","resource_name":"resource_name","resource_group_id":"resource_group_id","resource_group_name":"resource_group_name","organization_id":"organization_id","organization_name":"organization_name","space_id":"space_id","space_name":"space_name","consumer_id":"consumer_id","region":"region","pricing_region":"pricing_region","pricing_country":"USA","currency_code":"USD","billable":true,"plan_id":"plan_id","plan_name":"plan_name","month":"2017-08","usage":[{"metric":"UP-TIME","metric_name":"UP-TIME","quantity":711.11,"rateable_quantity":700,"cost":123.45,"rated_cost":130.0,"price":["anyValue"],"unit":"HOURS","unit_name":"HOURS","non_chargeable":true,"discounts":[{"ref":"Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9","name":"platform-discount","display_name":"Platform Service Discount","discount":5}]}],"pending":true,"currency_rate":10.8716}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = GetResourceUsageAccountPager(
            client=_service,
            account_id='testString',
            billingmonth='testString',
            names=True,
            accept_language='testString',
            limit=1,
            resource_group_id='testString',
            organization_id='testString',
            resource_instance_id='testString',
            resource_id='testString',
            plan_id='testString',
            region='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_get_resource_usage_account_with_pager_get_all(self):
        """
        test_get_resource_usage_account_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v4/accounts/testString/resource_instances/usage/testString')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?_start=1"},"total_count":2,"limit":1,"resources":[{"account_id":"account_id","resource_instance_id":"resource_instance_id","resource_instance_name":"resource_instance_name","resource_id":"resource_id","resource_name":"resource_name","resource_group_id":"resource_group_id","resource_group_name":"resource_group_name","organization_id":"organization_id","organization_name":"organization_name","space_id":"space_id","space_name":"space_name","consumer_id":"consumer_id","region":"region","pricing_region":"pricing_region","pricing_country":"USA","currency_code":"USD","billable":true,"plan_id":"plan_id","plan_name":"plan_name","month":"2017-08","usage":[{"metric":"UP-TIME","metric_name":"UP-TIME","quantity":711.11,"rateable_quantity":700,"cost":123.45,"rated_cost":130.0,"price":["anyValue"],"unit":"HOURS","unit_name":"HOURS","non_chargeable":true,"discounts":[{"ref":"Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9","name":"platform-discount","display_name":"Platform Service Discount","discount":5}]}],"pending":true,"currency_rate":10.8716}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"account_id":"account_id","resource_instance_id":"resource_instance_id","resource_instance_name":"resource_instance_name","resource_id":"resource_id","resource_name":"resource_name","resource_group_id":"resource_group_id","resource_group_name":"resource_group_name","organization_id":"organization_id","organization_name":"organization_name","space_id":"space_id","space_name":"space_name","consumer_id":"consumer_id","region":"region","pricing_region":"pricing_region","pricing_country":"USA","currency_code":"USD","billable":true,"plan_id":"plan_id","plan_name":"plan_name","month":"2017-08","usage":[{"metric":"UP-TIME","metric_name":"UP-TIME","quantity":711.11,"rateable_quantity":700,"cost":123.45,"rated_cost":130.0,"price":["anyValue"],"unit":"HOURS","unit_name":"HOURS","non_chargeable":true,"discounts":[{"ref":"Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9","name":"platform-discount","display_name":"Platform Service Discount","discount":5}]}],"pending":true,"currency_rate":10.8716}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = GetResourceUsageAccountPager(
            client=_service,
            account_id='testString',
            billingmonth='testString',
            names=True,
            accept_language='testString',
            limit=1,
            resource_group_id='testString',
            organization_id='testString',
            resource_instance_id='testString',
            resource_id='testString',
            plan_id='testString',
            region='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetResourceUsageResourceGroup:
    """
    Test Class for get_resource_usage_resource_group
    """

    @responses.activate
    def test_get_resource_usage_resource_group_all_params(self):
        """
        get_resource_usage_resource_group()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/resource_groups/testString/resource_instances/usage/testString')
        mock_response = '{"limit": 5, "count": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"account_id": "account_id", "resource_instance_id": "resource_instance_id", "resource_instance_name": "resource_instance_name", "resource_id": "resource_id", "resource_name": "resource_name", "resource_group_id": "resource_group_id", "resource_group_name": "resource_group_name", "organization_id": "organization_id", "organization_name": "organization_name", "space_id": "space_id", "space_name": "space_name", "consumer_id": "consumer_id", "region": "region", "pricing_region": "pricing_region", "pricing_country": "USA", "currency_code": "USD", "billable": true, "plan_id": "plan_id", "plan_name": "plan_name", "month": "2017-08", "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "pending": true, "currency_rate": 10.8716}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_group_id = 'testString'
        billingmonth = 'testString'
        names = True
        accept_language = 'testString'
        limit = 1
        start = 'testString'
        resource_instance_id = 'testString'
        resource_id = 'testString'
        plan_id = 'testString'
        region = 'testString'

        # Invoke method
        response = _service.get_resource_usage_resource_group(
            account_id,
            resource_group_id,
            billingmonth,
            names=names,
            accept_language=accept_language,
            limit=limit,
            start=start,
            resource_instance_id=resource_instance_id,
            resource_id=resource_id,
            plan_id=plan_id,
            region=region,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert '_names={}'.format('true' if names else 'false') in query_string
        assert '_limit={}'.format(limit) in query_string
        assert '_start={}'.format(start) in query_string
        assert 'resource_instance_id={}'.format(resource_instance_id) in query_string
        assert 'resource_id={}'.format(resource_id) in query_string
        assert 'plan_id={}'.format(plan_id) in query_string
        assert 'region={}'.format(region) in query_string

    def test_get_resource_usage_resource_group_all_params_with_retries(self):
        # Enable retries and run test_get_resource_usage_resource_group_all_params.
        _service.enable_retries()
        self.test_get_resource_usage_resource_group_all_params()

        # Disable retries and run test_get_resource_usage_resource_group_all_params.
        _service.disable_retries()
        self.test_get_resource_usage_resource_group_all_params()

    @responses.activate
    def test_get_resource_usage_resource_group_required_params(self):
        """
        test_get_resource_usage_resource_group_required_params()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/resource_groups/testString/resource_instances/usage/testString')
        mock_response = '{"limit": 5, "count": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"account_id": "account_id", "resource_instance_id": "resource_instance_id", "resource_instance_name": "resource_instance_name", "resource_id": "resource_id", "resource_name": "resource_name", "resource_group_id": "resource_group_id", "resource_group_name": "resource_group_name", "organization_id": "organization_id", "organization_name": "organization_name", "space_id": "space_id", "space_name": "space_name", "consumer_id": "consumer_id", "region": "region", "pricing_region": "pricing_region", "pricing_country": "USA", "currency_code": "USD", "billable": true, "plan_id": "plan_id", "plan_name": "plan_name", "month": "2017-08", "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "pending": true, "currency_rate": 10.8716}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_group_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = _service.get_resource_usage_resource_group(account_id, resource_group_id, billingmonth, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_resource_usage_resource_group_required_params_with_retries(self):
        # Enable retries and run test_get_resource_usage_resource_group_required_params.
        _service.enable_retries()
        self.test_get_resource_usage_resource_group_required_params()

        # Disable retries and run test_get_resource_usage_resource_group_required_params.
        _service.disable_retries()
        self.test_get_resource_usage_resource_group_required_params()

    @responses.activate
    def test_get_resource_usage_resource_group_value_error(self):
        """
        test_get_resource_usage_resource_group_value_error()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/resource_groups/testString/resource_instances/usage/testString')
        mock_response = '{"limit": 5, "count": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"account_id": "account_id", "resource_instance_id": "resource_instance_id", "resource_instance_name": "resource_instance_name", "resource_id": "resource_id", "resource_name": "resource_name", "resource_group_id": "resource_group_id", "resource_group_name": "resource_group_name", "organization_id": "organization_id", "organization_name": "organization_name", "space_id": "space_id", "space_name": "space_name", "consumer_id": "consumer_id", "region": "region", "pricing_region": "pricing_region", "pricing_country": "USA", "currency_code": "USD", "billable": true, "plan_id": "plan_id", "plan_name": "plan_name", "month": "2017-08", "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "pending": true, "currency_rate": 10.8716}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        resource_group_id = 'testString'
        billingmonth = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "resource_group_id": resource_group_id,
            "billingmonth": billingmonth,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_resource_usage_resource_group(**req_copy)

    def test_get_resource_usage_resource_group_value_error_with_retries(self):
        # Enable retries and run test_get_resource_usage_resource_group_value_error.
        _service.enable_retries()
        self.test_get_resource_usage_resource_group_value_error()

        # Disable retries and run test_get_resource_usage_resource_group_value_error.
        _service.disable_retries()
        self.test_get_resource_usage_resource_group_value_error()

    @responses.activate
    def test_get_resource_usage_resource_group_with_pager_get_next(self):
        """
        test_get_resource_usage_resource_group_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v4/accounts/testString/resource_groups/testString/resource_instances/usage/testString')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?_start=1"},"total_count":2,"limit":1,"resources":[{"account_id":"account_id","resource_instance_id":"resource_instance_id","resource_instance_name":"resource_instance_name","resource_id":"resource_id","resource_name":"resource_name","resource_group_id":"resource_group_id","resource_group_name":"resource_group_name","organization_id":"organization_id","organization_name":"organization_name","space_id":"space_id","space_name":"space_name","consumer_id":"consumer_id","region":"region","pricing_region":"pricing_region","pricing_country":"USA","currency_code":"USD","billable":true,"plan_id":"plan_id","plan_name":"plan_name","month":"2017-08","usage":[{"metric":"UP-TIME","metric_name":"UP-TIME","quantity":711.11,"rateable_quantity":700,"cost":123.45,"rated_cost":130.0,"price":["anyValue"],"unit":"HOURS","unit_name":"HOURS","non_chargeable":true,"discounts":[{"ref":"Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9","name":"platform-discount","display_name":"Platform Service Discount","discount":5}]}],"pending":true,"currency_rate":10.8716}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"account_id":"account_id","resource_instance_id":"resource_instance_id","resource_instance_name":"resource_instance_name","resource_id":"resource_id","resource_name":"resource_name","resource_group_id":"resource_group_id","resource_group_name":"resource_group_name","organization_id":"organization_id","organization_name":"organization_name","space_id":"space_id","space_name":"space_name","consumer_id":"consumer_id","region":"region","pricing_region":"pricing_region","pricing_country":"USA","currency_code":"USD","billable":true,"plan_id":"plan_id","plan_name":"plan_name","month":"2017-08","usage":[{"metric":"UP-TIME","metric_name":"UP-TIME","quantity":711.11,"rateable_quantity":700,"cost":123.45,"rated_cost":130.0,"price":["anyValue"],"unit":"HOURS","unit_name":"HOURS","non_chargeable":true,"discounts":[{"ref":"Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9","name":"platform-discount","display_name":"Platform Service Discount","discount":5}]}],"pending":true,"currency_rate":10.8716}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = GetResourceUsageResourceGroupPager(
            client=_service,
            account_id='testString',
            resource_group_id='testString',
            billingmonth='testString',
            names=True,
            accept_language='testString',
            limit=1,
            resource_instance_id='testString',
            resource_id='testString',
            plan_id='testString',
            region='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_get_resource_usage_resource_group_with_pager_get_all(self):
        """
        test_get_resource_usage_resource_group_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v4/accounts/testString/resource_groups/testString/resource_instances/usage/testString')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?_start=1"},"total_count":2,"limit":1,"resources":[{"account_id":"account_id","resource_instance_id":"resource_instance_id","resource_instance_name":"resource_instance_name","resource_id":"resource_id","resource_name":"resource_name","resource_group_id":"resource_group_id","resource_group_name":"resource_group_name","organization_id":"organization_id","organization_name":"organization_name","space_id":"space_id","space_name":"space_name","consumer_id":"consumer_id","region":"region","pricing_region":"pricing_region","pricing_country":"USA","currency_code":"USD","billable":true,"plan_id":"plan_id","plan_name":"plan_name","month":"2017-08","usage":[{"metric":"UP-TIME","metric_name":"UP-TIME","quantity":711.11,"rateable_quantity":700,"cost":123.45,"rated_cost":130.0,"price":["anyValue"],"unit":"HOURS","unit_name":"HOURS","non_chargeable":true,"discounts":[{"ref":"Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9","name":"platform-discount","display_name":"Platform Service Discount","discount":5}]}],"pending":true,"currency_rate":10.8716}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"account_id":"account_id","resource_instance_id":"resource_instance_id","resource_instance_name":"resource_instance_name","resource_id":"resource_id","resource_name":"resource_name","resource_group_id":"resource_group_id","resource_group_name":"resource_group_name","organization_id":"organization_id","organization_name":"organization_name","space_id":"space_id","space_name":"space_name","consumer_id":"consumer_id","region":"region","pricing_region":"pricing_region","pricing_country":"USA","currency_code":"USD","billable":true,"plan_id":"plan_id","plan_name":"plan_name","month":"2017-08","usage":[{"metric":"UP-TIME","metric_name":"UP-TIME","quantity":711.11,"rateable_quantity":700,"cost":123.45,"rated_cost":130.0,"price":["anyValue"],"unit":"HOURS","unit_name":"HOURS","non_chargeable":true,"discounts":[{"ref":"Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9","name":"platform-discount","display_name":"Platform Service Discount","discount":5}]}],"pending":true,"currency_rate":10.8716}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = GetResourceUsageResourceGroupPager(
            client=_service,
            account_id='testString',
            resource_group_id='testString',
            billingmonth='testString',
            names=True,
            accept_language='testString',
            limit=1,
            resource_instance_id='testString',
            resource_id='testString',
            plan_id='testString',
            region='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetResourceUsageOrg:
    """
    Test Class for get_resource_usage_org
    """

    @responses.activate
    def test_get_resource_usage_org_all_params(self):
        """
        get_resource_usage_org()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/organizations/testString/resource_instances/usage/testString')
        mock_response = '{"limit": 5, "count": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"account_id": "account_id", "resource_instance_id": "resource_instance_id", "resource_instance_name": "resource_instance_name", "resource_id": "resource_id", "resource_name": "resource_name", "resource_group_id": "resource_group_id", "resource_group_name": "resource_group_name", "organization_id": "organization_id", "organization_name": "organization_name", "space_id": "space_id", "space_name": "space_name", "consumer_id": "consumer_id", "region": "region", "pricing_region": "pricing_region", "pricing_country": "USA", "currency_code": "USD", "billable": true, "plan_id": "plan_id", "plan_name": "plan_name", "month": "2017-08", "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "pending": true, "currency_rate": 10.8716}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        organization_id = 'testString'
        billingmonth = 'testString'
        names = True
        accept_language = 'testString'
        limit = 1
        start = 'testString'
        resource_instance_id = 'testString'
        resource_id = 'testString'
        plan_id = 'testString'
        region = 'testString'

        # Invoke method
        response = _service.get_resource_usage_org(
            account_id,
            organization_id,
            billingmonth,
            names=names,
            accept_language=accept_language,
            limit=limit,
            start=start,
            resource_instance_id=resource_instance_id,
            resource_id=resource_id,
            plan_id=plan_id,
            region=region,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert '_names={}'.format('true' if names else 'false') in query_string
        assert '_limit={}'.format(limit) in query_string
        assert '_start={}'.format(start) in query_string
        assert 'resource_instance_id={}'.format(resource_instance_id) in query_string
        assert 'resource_id={}'.format(resource_id) in query_string
        assert 'plan_id={}'.format(plan_id) in query_string
        assert 'region={}'.format(region) in query_string

    def test_get_resource_usage_org_all_params_with_retries(self):
        # Enable retries and run test_get_resource_usage_org_all_params.
        _service.enable_retries()
        self.test_get_resource_usage_org_all_params()

        # Disable retries and run test_get_resource_usage_org_all_params.
        _service.disable_retries()
        self.test_get_resource_usage_org_all_params()

    @responses.activate
    def test_get_resource_usage_org_required_params(self):
        """
        test_get_resource_usage_org_required_params()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/organizations/testString/resource_instances/usage/testString')
        mock_response = '{"limit": 5, "count": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"account_id": "account_id", "resource_instance_id": "resource_instance_id", "resource_instance_name": "resource_instance_name", "resource_id": "resource_id", "resource_name": "resource_name", "resource_group_id": "resource_group_id", "resource_group_name": "resource_group_name", "organization_id": "organization_id", "organization_name": "organization_name", "space_id": "space_id", "space_name": "space_name", "consumer_id": "consumer_id", "region": "region", "pricing_region": "pricing_region", "pricing_country": "USA", "currency_code": "USD", "billable": true, "plan_id": "plan_id", "plan_name": "plan_name", "month": "2017-08", "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "pending": true, "currency_rate": 10.8716}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        organization_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = _service.get_resource_usage_org(account_id, organization_id, billingmonth, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_resource_usage_org_required_params_with_retries(self):
        # Enable retries and run test_get_resource_usage_org_required_params.
        _service.enable_retries()
        self.test_get_resource_usage_org_required_params()

        # Disable retries and run test_get_resource_usage_org_required_params.
        _service.disable_retries()
        self.test_get_resource_usage_org_required_params()

    @responses.activate
    def test_get_resource_usage_org_value_error(self):
        """
        test_get_resource_usage_org_value_error()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/organizations/testString/resource_instances/usage/testString')
        mock_response = '{"limit": 5, "count": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"account_id": "account_id", "resource_instance_id": "resource_instance_id", "resource_instance_name": "resource_instance_name", "resource_id": "resource_id", "resource_name": "resource_name", "resource_group_id": "resource_group_id", "resource_group_name": "resource_group_name", "organization_id": "organization_id", "organization_name": "organization_name", "space_id": "space_id", "space_name": "space_name", "consumer_id": "consumer_id", "region": "region", "pricing_region": "pricing_region", "pricing_country": "USA", "currency_code": "USD", "billable": true, "plan_id": "plan_id", "plan_name": "plan_name", "month": "2017-08", "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "pending": true, "currency_rate": 10.8716}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        organization_id = 'testString'
        billingmonth = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "organization_id": organization_id,
            "billingmonth": billingmonth,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_resource_usage_org(**req_copy)

    def test_get_resource_usage_org_value_error_with_retries(self):
        # Enable retries and run test_get_resource_usage_org_value_error.
        _service.enable_retries()
        self.test_get_resource_usage_org_value_error()

        # Disable retries and run test_get_resource_usage_org_value_error.
        _service.disable_retries()
        self.test_get_resource_usage_org_value_error()

    @responses.activate
    def test_get_resource_usage_org_with_pager_get_next(self):
        """
        test_get_resource_usage_org_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v4/accounts/testString/organizations/testString/resource_instances/usage/testString')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?_start=1"},"total_count":2,"limit":1,"resources":[{"account_id":"account_id","resource_instance_id":"resource_instance_id","resource_instance_name":"resource_instance_name","resource_id":"resource_id","resource_name":"resource_name","resource_group_id":"resource_group_id","resource_group_name":"resource_group_name","organization_id":"organization_id","organization_name":"organization_name","space_id":"space_id","space_name":"space_name","consumer_id":"consumer_id","region":"region","pricing_region":"pricing_region","pricing_country":"USA","currency_code":"USD","billable":true,"plan_id":"plan_id","plan_name":"plan_name","month":"2017-08","usage":[{"metric":"UP-TIME","metric_name":"UP-TIME","quantity":711.11,"rateable_quantity":700,"cost":123.45,"rated_cost":130.0,"price":["anyValue"],"unit":"HOURS","unit_name":"HOURS","non_chargeable":true,"discounts":[{"ref":"Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9","name":"platform-discount","display_name":"Platform Service Discount","discount":5}]}],"pending":true,"currency_rate":10.8716}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"account_id":"account_id","resource_instance_id":"resource_instance_id","resource_instance_name":"resource_instance_name","resource_id":"resource_id","resource_name":"resource_name","resource_group_id":"resource_group_id","resource_group_name":"resource_group_name","organization_id":"organization_id","organization_name":"organization_name","space_id":"space_id","space_name":"space_name","consumer_id":"consumer_id","region":"region","pricing_region":"pricing_region","pricing_country":"USA","currency_code":"USD","billable":true,"plan_id":"plan_id","plan_name":"plan_name","month":"2017-08","usage":[{"metric":"UP-TIME","metric_name":"UP-TIME","quantity":711.11,"rateable_quantity":700,"cost":123.45,"rated_cost":130.0,"price":["anyValue"],"unit":"HOURS","unit_name":"HOURS","non_chargeable":true,"discounts":[{"ref":"Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9","name":"platform-discount","display_name":"Platform Service Discount","discount":5}]}],"pending":true,"currency_rate":10.8716}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = GetResourceUsageOrgPager(
            client=_service,
            account_id='testString',
            organization_id='testString',
            billingmonth='testString',
            names=True,
            accept_language='testString',
            limit=1,
            resource_instance_id='testString',
            resource_id='testString',
            plan_id='testString',
            region='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_get_resource_usage_org_with_pager_get_all(self):
        """
        test_get_resource_usage_org_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v4/accounts/testString/organizations/testString/resource_instances/usage/testString')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?_start=1"},"total_count":2,"limit":1,"resources":[{"account_id":"account_id","resource_instance_id":"resource_instance_id","resource_instance_name":"resource_instance_name","resource_id":"resource_id","resource_name":"resource_name","resource_group_id":"resource_group_id","resource_group_name":"resource_group_name","organization_id":"organization_id","organization_name":"organization_name","space_id":"space_id","space_name":"space_name","consumer_id":"consumer_id","region":"region","pricing_region":"pricing_region","pricing_country":"USA","currency_code":"USD","billable":true,"plan_id":"plan_id","plan_name":"plan_name","month":"2017-08","usage":[{"metric":"UP-TIME","metric_name":"UP-TIME","quantity":711.11,"rateable_quantity":700,"cost":123.45,"rated_cost":130.0,"price":["anyValue"],"unit":"HOURS","unit_name":"HOURS","non_chargeable":true,"discounts":[{"ref":"Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9","name":"platform-discount","display_name":"Platform Service Discount","discount":5}]}],"pending":true,"currency_rate":10.8716}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"account_id":"account_id","resource_instance_id":"resource_instance_id","resource_instance_name":"resource_instance_name","resource_id":"resource_id","resource_name":"resource_name","resource_group_id":"resource_group_id","resource_group_name":"resource_group_name","organization_id":"organization_id","organization_name":"organization_name","space_id":"space_id","space_name":"space_name","consumer_id":"consumer_id","region":"region","pricing_region":"pricing_region","pricing_country":"USA","currency_code":"USD","billable":true,"plan_id":"plan_id","plan_name":"plan_name","month":"2017-08","usage":[{"metric":"UP-TIME","metric_name":"UP-TIME","quantity":711.11,"rateable_quantity":700,"cost":123.45,"rated_cost":130.0,"price":["anyValue"],"unit":"HOURS","unit_name":"HOURS","non_chargeable":true,"discounts":[{"ref":"Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9","name":"platform-discount","display_name":"Platform Service Discount","discount":5}]}],"pending":true,"currency_rate":10.8716}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = GetResourceUsageOrgPager(
            client=_service,
            account_id='testString',
            organization_id='testString',
            billingmonth='testString',
            names=True,
            accept_language='testString',
            limit=1,
            resource_instance_id='testString',
            resource_id='testString',
            plan_id='testString',
            region='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


# endregion
##############################################################################
# End of Service: ResourceOperations
##############################################################################

##############################################################################
# Start of Service: OrganizationOperations
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

        service = UsageReportsV4.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, UsageReportsV4)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = UsageReportsV4.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetOrgUsage:
    """
    Test Class for get_org_usage
    """

    @responses.activate
    def test_get_org_usage_all_params(self):
        """
        get_org_usage()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/organizations/testString/usage/testString')
        mock_response = '{"account_id": "account_id", "organization_id": "organization_id", "organization_name": "organization_name", "pricing_country": "USA", "currency_code": "USD", "month": "2017-08", "resources": [{"resource_id": "resource_id", "resource_name": "resource_name", "billable_cost": 13, "billable_rated_cost": 19, "non_billable_cost": 17, "non_billable_rated_cost": 23, "plans": [{"plan_id": "plan_id", "plan_name": "plan_name", "pricing_region": "pricing_region", "pricing_plan_id": "pricing_plan_id", "billable": true, "cost": 4, "rated_cost": 10, "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}], "pending": true}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "currency_rate": 10.8716}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        organization_id = 'testString'
        billingmonth = 'testString'
        names = True
        accept_language = 'testString'

        # Invoke method
        response = _service.get_org_usage(
            account_id, organization_id, billingmonth, names=names, accept_language=accept_language, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert '_names={}'.format('true' if names else 'false') in query_string

    def test_get_org_usage_all_params_with_retries(self):
        # Enable retries and run test_get_org_usage_all_params.
        _service.enable_retries()
        self.test_get_org_usage_all_params()

        # Disable retries and run test_get_org_usage_all_params.
        _service.disable_retries()
        self.test_get_org_usage_all_params()

    @responses.activate
    def test_get_org_usage_required_params(self):
        """
        test_get_org_usage_required_params()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/organizations/testString/usage/testString')
        mock_response = '{"account_id": "account_id", "organization_id": "organization_id", "organization_name": "organization_name", "pricing_country": "USA", "currency_code": "USD", "month": "2017-08", "resources": [{"resource_id": "resource_id", "resource_name": "resource_name", "billable_cost": 13, "billable_rated_cost": 19, "non_billable_cost": 17, "non_billable_rated_cost": 23, "plans": [{"plan_id": "plan_id", "plan_name": "plan_name", "pricing_region": "pricing_region", "pricing_plan_id": "pricing_plan_id", "billable": true, "cost": 4, "rated_cost": 10, "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}], "pending": true}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "currency_rate": 10.8716}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        organization_id = 'testString'
        billingmonth = 'testString'

        # Invoke method
        response = _service.get_org_usage(account_id, organization_id, billingmonth, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_org_usage_required_params_with_retries(self):
        # Enable retries and run test_get_org_usage_required_params.
        _service.enable_retries()
        self.test_get_org_usage_required_params()

        # Disable retries and run test_get_org_usage_required_params.
        _service.disable_retries()
        self.test_get_org_usage_required_params()

    @responses.activate
    def test_get_org_usage_value_error(self):
        """
        test_get_org_usage_value_error()
        """
        # Set up mock
        url = preprocess_url('/v4/accounts/testString/organizations/testString/usage/testString')
        mock_response = '{"account_id": "account_id", "organization_id": "organization_id", "organization_name": "organization_name", "pricing_country": "USA", "currency_code": "USD", "month": "2017-08", "resources": [{"resource_id": "resource_id", "resource_name": "resource_name", "billable_cost": 13, "billable_rated_cost": 19, "non_billable_cost": 17, "non_billable_rated_cost": 23, "plans": [{"plan_id": "plan_id", "plan_name": "plan_name", "pricing_region": "pricing_region", "pricing_plan_id": "pricing_plan_id", "billable": true, "cost": 4, "rated_cost": 10, "usage": [{"metric": "UP-TIME", "metric_name": "UP-TIME", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130.0, "price": ["anyValue"], "unit": "HOURS", "unit_name": "HOURS", "non_chargeable": true, "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}], "pending": true}], "discounts": [{"ref": "Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9", "name": "platform-discount", "display_name": "Platform Service Discount", "discount": 5}]}], "currency_rate": 10.8716}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'
        organization_id = 'testString'
        billingmonth = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "organization_id": organization_id,
            "billingmonth": billingmonth,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_org_usage(**req_copy)

    def test_get_org_usage_value_error_with_retries(self):
        # Enable retries and run test_get_org_usage_value_error.
        _service.enable_retries()
        self.test_get_org_usage_value_error()

        # Disable retries and run test_get_org_usage_value_error.
        _service.disable_retries()
        self.test_get_org_usage_value_error()


# endregion
##############################################################################
# End of Service: OrganizationOperations
##############################################################################

##############################################################################
# Start of Service: BillingReportsSnapshot
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

        service = UsageReportsV4.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, UsageReportsV4)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = UsageReportsV4.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateReportsSnapshotConfig:
    """
    Test Class for create_reports_snapshot_config
    """

    @responses.activate
    def test_create_reports_snapshot_config_all_params(self):
        """
        create_reports_snapshot_config()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-reports-snapshot-config')
        mock_response = '{"account_id": "abc", "state": "enabled", "account_type": "account", "interval": "daily", "versioning": "new", "report_types": ["account_summary"], "compression": "GZIP", "content_type": "text/csv", "cos_reports_folder": "IBMCloud-Billing-Reports", "cos_bucket": "bucket_name", "cos_location": "us-south", "cos_endpoint": "https://s3.us-west.cloud-object-storage.test.appdomain.cloud", "created_at": 1687469854342, "last_updated_at": 1687469989326, "history": [{"start_time": 1687469854342, "end_time": 1687469989326, "updated_by": "IBMid-506PR16K14", "account_id": "abc", "state": "enabled", "account_type": "account", "interval": "daily", "versioning": "new", "report_types": ["account_summary"], "compression": "GZIP", "content_type": "text/csv", "cos_reports_folder": "IBMCloud-Billing-Reports", "cos_bucket": "bucket_name", "cos_location": "us-south", "cos_endpoint": "https://s3.us-west.cloud-object-storage.test.appdomain.cloud"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        account_id = 'abc'
        interval = 'daily'
        cos_bucket = 'bucket_name'
        cos_location = 'us-south'
        cos_reports_folder = 'IBMCloud-Billing-Reports'
        report_types = ['account_summary', 'enterprise_summary', 'account_resource_instance_usage']
        versioning = 'new'

        # Invoke method
        response = _service.create_reports_snapshot_config(
            account_id,
            interval,
            cos_bucket,
            cos_location,
            cos_reports_folder=cos_reports_folder,
            report_types=report_types,
            versioning=versioning,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == 'abc'
        assert req_body['interval'] == 'daily'
        assert req_body['cos_bucket'] == 'bucket_name'
        assert req_body['cos_location'] == 'us-south'
        assert req_body['cos_reports_folder'] == 'IBMCloud-Billing-Reports'
        assert req_body['report_types'] == ['account_summary', 'enterprise_summary', 'account_resource_instance_usage']
        assert req_body['versioning'] == 'new'

    def test_create_reports_snapshot_config_all_params_with_retries(self):
        # Enable retries and run test_create_reports_snapshot_config_all_params.
        _service.enable_retries()
        self.test_create_reports_snapshot_config_all_params()

        # Disable retries and run test_create_reports_snapshot_config_all_params.
        _service.disable_retries()
        self.test_create_reports_snapshot_config_all_params()

    @responses.activate
    def test_create_reports_snapshot_config_value_error(self):
        """
        test_create_reports_snapshot_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-reports-snapshot-config')
        mock_response = '{"account_id": "abc", "state": "enabled", "account_type": "account", "interval": "daily", "versioning": "new", "report_types": ["account_summary"], "compression": "GZIP", "content_type": "text/csv", "cos_reports_folder": "IBMCloud-Billing-Reports", "cos_bucket": "bucket_name", "cos_location": "us-south", "cos_endpoint": "https://s3.us-west.cloud-object-storage.test.appdomain.cloud", "created_at": 1687469854342, "last_updated_at": 1687469989326, "history": [{"start_time": 1687469854342, "end_time": 1687469989326, "updated_by": "IBMid-506PR16K14", "account_id": "abc", "state": "enabled", "account_type": "account", "interval": "daily", "versioning": "new", "report_types": ["account_summary"], "compression": "GZIP", "content_type": "text/csv", "cos_reports_folder": "IBMCloud-Billing-Reports", "cos_bucket": "bucket_name", "cos_location": "us-south", "cos_endpoint": "https://s3.us-west.cloud-object-storage.test.appdomain.cloud"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        account_id = 'abc'
        interval = 'daily'
        cos_bucket = 'bucket_name'
        cos_location = 'us-south'
        cos_reports_folder = 'IBMCloud-Billing-Reports'
        report_types = ['account_summary', 'enterprise_summary', 'account_resource_instance_usage']
        versioning = 'new'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "interval": interval,
            "cos_bucket": cos_bucket,
            "cos_location": cos_location,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_reports_snapshot_config(**req_copy)

    def test_create_reports_snapshot_config_value_error_with_retries(self):
        # Enable retries and run test_create_reports_snapshot_config_value_error.
        _service.enable_retries()
        self.test_create_reports_snapshot_config_value_error()

        # Disable retries and run test_create_reports_snapshot_config_value_error.
        _service.disable_retries()
        self.test_create_reports_snapshot_config_value_error()


class TestGetReportsSnapshotConfig:
    """
    Test Class for get_reports_snapshot_config
    """

    @responses.activate
    def test_get_reports_snapshot_config_all_params(self):
        """
        get_reports_snapshot_config()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-reports-snapshot-config')
        mock_response = '{"account_id": "abc", "state": "enabled", "account_type": "account", "interval": "daily", "versioning": "new", "report_types": ["account_summary"], "compression": "GZIP", "content_type": "text/csv", "cos_reports_folder": "IBMCloud-Billing-Reports", "cos_bucket": "bucket_name", "cos_location": "us-south", "cos_endpoint": "https://s3.us-west.cloud-object-storage.test.appdomain.cloud", "created_at": 1687469854342, "last_updated_at": 1687469989326, "history": [{"start_time": 1687469854342, "end_time": 1687469989326, "updated_by": "IBMid-506PR16K14", "account_id": "abc", "state": "enabled", "account_type": "account", "interval": "daily", "versioning": "new", "report_types": ["account_summary"], "compression": "GZIP", "content_type": "text/csv", "cos_reports_folder": "IBMCloud-Billing-Reports", "cos_bucket": "bucket_name", "cos_location": "us-south", "cos_endpoint": "https://s3.us-west.cloud-object-storage.test.appdomain.cloud"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'abc'

        # Invoke method
        response = _service.get_reports_snapshot_config(
            account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_get_reports_snapshot_config_all_params_with_retries(self):
        # Enable retries and run test_get_reports_snapshot_config_all_params.
        _service.enable_retries()
        self.test_get_reports_snapshot_config_all_params()

        # Disable retries and run test_get_reports_snapshot_config_all_params.
        _service.disable_retries()
        self.test_get_reports_snapshot_config_all_params()

    @responses.activate
    def test_get_reports_snapshot_config_value_error(self):
        """
        test_get_reports_snapshot_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-reports-snapshot-config')
        mock_response = '{"account_id": "abc", "state": "enabled", "account_type": "account", "interval": "daily", "versioning": "new", "report_types": ["account_summary"], "compression": "GZIP", "content_type": "text/csv", "cos_reports_folder": "IBMCloud-Billing-Reports", "cos_bucket": "bucket_name", "cos_location": "us-south", "cos_endpoint": "https://s3.us-west.cloud-object-storage.test.appdomain.cloud", "created_at": 1687469854342, "last_updated_at": 1687469989326, "history": [{"start_time": 1687469854342, "end_time": 1687469989326, "updated_by": "IBMid-506PR16K14", "account_id": "abc", "state": "enabled", "account_type": "account", "interval": "daily", "versioning": "new", "report_types": ["account_summary"], "compression": "GZIP", "content_type": "text/csv", "cos_reports_folder": "IBMCloud-Billing-Reports", "cos_bucket": "bucket_name", "cos_location": "us-south", "cos_endpoint": "https://s3.us-west.cloud-object-storage.test.appdomain.cloud"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'abc'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_reports_snapshot_config(**req_copy)

    def test_get_reports_snapshot_config_value_error_with_retries(self):
        # Enable retries and run test_get_reports_snapshot_config_value_error.
        _service.enable_retries()
        self.test_get_reports_snapshot_config_value_error()

        # Disable retries and run test_get_reports_snapshot_config_value_error.
        _service.disable_retries()
        self.test_get_reports_snapshot_config_value_error()


class TestUpdateReportsSnapshotConfig:
    """
    Test Class for update_reports_snapshot_config
    """

    @responses.activate
    def test_update_reports_snapshot_config_all_params(self):
        """
        update_reports_snapshot_config()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-reports-snapshot-config')
        mock_response = '{"account_id": "abc", "state": "enabled", "account_type": "account", "interval": "daily", "versioning": "new", "report_types": ["account_summary"], "compression": "GZIP", "content_type": "text/csv", "cos_reports_folder": "IBMCloud-Billing-Reports", "cos_bucket": "bucket_name", "cos_location": "us-south", "cos_endpoint": "https://s3.us-west.cloud-object-storage.test.appdomain.cloud", "created_at": 1687469854342, "last_updated_at": 1687469989326, "history": [{"start_time": 1687469854342, "end_time": 1687469989326, "updated_by": "IBMid-506PR16K14", "account_id": "abc", "state": "enabled", "account_type": "account", "interval": "daily", "versioning": "new", "report_types": ["account_summary"], "compression": "GZIP", "content_type": "text/csv", "cos_reports_folder": "IBMCloud-Billing-Reports", "cos_bucket": "bucket_name", "cos_location": "us-south", "cos_endpoint": "https://s3.us-west.cloud-object-storage.test.appdomain.cloud"}]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'abc'
        interval = 'daily'
        cos_bucket = 'bucket_name'
        cos_location = 'us-south'
        cos_reports_folder = 'IBMCloud-Billing-Reports'
        report_types = ['account_summary', 'enterprise_summary', 'account_resource_instance_usage']
        versioning = 'new'

        # Invoke method
        response = _service.update_reports_snapshot_config(
            account_id,
            interval=interval,
            cos_bucket=cos_bucket,
            cos_location=cos_location,
            cos_reports_folder=cos_reports_folder,
            report_types=report_types,
            versioning=versioning,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == 'abc'
        assert req_body['interval'] == 'daily'
        assert req_body['cos_bucket'] == 'bucket_name'
        assert req_body['cos_location'] == 'us-south'
        assert req_body['cos_reports_folder'] == 'IBMCloud-Billing-Reports'
        assert req_body['report_types'] == ['account_summary', 'enterprise_summary', 'account_resource_instance_usage']
        assert req_body['versioning'] == 'new'

    def test_update_reports_snapshot_config_all_params_with_retries(self):
        # Enable retries and run test_update_reports_snapshot_config_all_params.
        _service.enable_retries()
        self.test_update_reports_snapshot_config_all_params()

        # Disable retries and run test_update_reports_snapshot_config_all_params.
        _service.disable_retries()
        self.test_update_reports_snapshot_config_all_params()

    @responses.activate
    def test_update_reports_snapshot_config_value_error(self):
        """
        test_update_reports_snapshot_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-reports-snapshot-config')
        mock_response = '{"account_id": "abc", "state": "enabled", "account_type": "account", "interval": "daily", "versioning": "new", "report_types": ["account_summary"], "compression": "GZIP", "content_type": "text/csv", "cos_reports_folder": "IBMCloud-Billing-Reports", "cos_bucket": "bucket_name", "cos_location": "us-south", "cos_endpoint": "https://s3.us-west.cloud-object-storage.test.appdomain.cloud", "created_at": 1687469854342, "last_updated_at": 1687469989326, "history": [{"start_time": 1687469854342, "end_time": 1687469989326, "updated_by": "IBMid-506PR16K14", "account_id": "abc", "state": "enabled", "account_type": "account", "interval": "daily", "versioning": "new", "report_types": ["account_summary"], "compression": "GZIP", "content_type": "text/csv", "cos_reports_folder": "IBMCloud-Billing-Reports", "cos_bucket": "bucket_name", "cos_location": "us-south", "cos_endpoint": "https://s3.us-west.cloud-object-storage.test.appdomain.cloud"}]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'abc'
        interval = 'daily'
        cos_bucket = 'bucket_name'
        cos_location = 'us-south'
        cos_reports_folder = 'IBMCloud-Billing-Reports'
        report_types = ['account_summary', 'enterprise_summary', 'account_resource_instance_usage']
        versioning = 'new'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_reports_snapshot_config(**req_copy)

    def test_update_reports_snapshot_config_value_error_with_retries(self):
        # Enable retries and run test_update_reports_snapshot_config_value_error.
        _service.enable_retries()
        self.test_update_reports_snapshot_config_value_error()

        # Disable retries and run test_update_reports_snapshot_config_value_error.
        _service.disable_retries()
        self.test_update_reports_snapshot_config_value_error()


class TestDeleteReportsSnapshotConfig:
    """
    Test Class for delete_reports_snapshot_config
    """

    @responses.activate
    def test_delete_reports_snapshot_config_all_params(self):
        """
        delete_reports_snapshot_config()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-reports-snapshot-config')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        account_id = 'abc'

        # Invoke method
        response = _service.delete_reports_snapshot_config(
            account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_delete_reports_snapshot_config_all_params_with_retries(self):
        # Enable retries and run test_delete_reports_snapshot_config_all_params.
        _service.enable_retries()
        self.test_delete_reports_snapshot_config_all_params()

        # Disable retries and run test_delete_reports_snapshot_config_all_params.
        _service.disable_retries()
        self.test_delete_reports_snapshot_config_all_params()

    @responses.activate
    def test_delete_reports_snapshot_config_value_error(self):
        """
        test_delete_reports_snapshot_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-reports-snapshot-config')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        account_id = 'abc'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_reports_snapshot_config(**req_copy)

    def test_delete_reports_snapshot_config_value_error_with_retries(self):
        # Enable retries and run test_delete_reports_snapshot_config_value_error.
        _service.enable_retries()
        self.test_delete_reports_snapshot_config_value_error()

        # Disable retries and run test_delete_reports_snapshot_config_value_error.
        _service.disable_retries()
        self.test_delete_reports_snapshot_config_value_error()


class TestValidateReportsSnapshotConfig:
    """
    Test Class for validate_reports_snapshot_config
    """

    @responses.activate
    def test_validate_reports_snapshot_config_all_params(self):
        """
        validate_reports_snapshot_config()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-reports-snapshot-config/validate')
        mock_response = '{"account_id": "abc", "cos_bucket": "bucket_name", "cos_location": "us-south"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'abc'
        interval = 'daily'
        cos_bucket = 'bucket_name'
        cos_location = 'us-south'
        cos_reports_folder = 'IBMCloud-Billing-Reports'
        report_types = ['account_summary', 'enterprise_summary', 'account_resource_instance_usage']
        versioning = 'new'

        # Invoke method
        response = _service.validate_reports_snapshot_config(
            account_id,
            interval=interval,
            cos_bucket=cos_bucket,
            cos_location=cos_location,
            cos_reports_folder=cos_reports_folder,
            report_types=report_types,
            versioning=versioning,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == 'abc'
        assert req_body['interval'] == 'daily'
        assert req_body['cos_bucket'] == 'bucket_name'
        assert req_body['cos_location'] == 'us-south'
        assert req_body['cos_reports_folder'] == 'IBMCloud-Billing-Reports'
        assert req_body['report_types'] == ['account_summary', 'enterprise_summary', 'account_resource_instance_usage']
        assert req_body['versioning'] == 'new'

    def test_validate_reports_snapshot_config_all_params_with_retries(self):
        # Enable retries and run test_validate_reports_snapshot_config_all_params.
        _service.enable_retries()
        self.test_validate_reports_snapshot_config_all_params()

        # Disable retries and run test_validate_reports_snapshot_config_all_params.
        _service.disable_retries()
        self.test_validate_reports_snapshot_config_all_params()

    @responses.activate
    def test_validate_reports_snapshot_config_value_error(self):
        """
        test_validate_reports_snapshot_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-reports-snapshot-config/validate')
        mock_response = '{"account_id": "abc", "cos_bucket": "bucket_name", "cos_location": "us-south"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'abc'
        interval = 'daily'
        cos_bucket = 'bucket_name'
        cos_location = 'us-south'
        cos_reports_folder = 'IBMCloud-Billing-Reports'
        report_types = ['account_summary', 'enterprise_summary', 'account_resource_instance_usage']
        versioning = 'new'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.validate_reports_snapshot_config(**req_copy)

    def test_validate_reports_snapshot_config_value_error_with_retries(self):
        # Enable retries and run test_validate_reports_snapshot_config_value_error.
        _service.enable_retries()
        self.test_validate_reports_snapshot_config_value_error()

        # Disable retries and run test_validate_reports_snapshot_config_value_error.
        _service.disable_retries()
        self.test_validate_reports_snapshot_config_value_error()


class TestGetReportsSnapshot:
    """
    Test Class for get_reports_snapshot
    """

    @responses.activate
    def test_get_reports_snapshot_all_params(self):
        """
        get_reports_snapshot()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-reports-snapshots')
        mock_response = '{"count": 3, "first": {"href": "/v1/billing-reports-snapshots?_limit=10&account_id=272b9a4f73e11030d0ba037daee47a35&date_from=-Infinity&date_to=Infinity&month=2023-06"}, "next": {"href": "/v1/billing-reports-snapshots?_limit=10&account_id=272b9a4f73e11030d0ba037daee47a35&date_from=-Infinity&date_to=Infinity&month=2023-06", "offset": "g1AAAAHyeJzLYWBgYMtgTmHQSklKzi9KdUhJMtRLytVNTtZNSU3JTE4sSU0xMjTUS87JL01JzCvRy0styQHqYUpSAJJJ-v___88C892cKtZ"}, "snapshots": [{"account_id": "abc", "month": "2023-06", "account_type": "account", "expected_processed_at": 1687470383610, "state": "enabled", "billing_period": {"start": "2023-06-01T00:00:00.000Z", "end": "2023-06-30T23:59:59.999Z"}, "snapshot_id": "1685577600000", "charset": "UTF-8", "compression": "GZIP", "content_type": "text/csv", "bucket": "bucket_name", "version": "1.0", "created_on": "2023-06-22T21:47:28.297Z", "report_types": [{"type": "account_summary", "version": "1.0"}], "files": [{"report_types": "account_summary", "location": "june/2023-06/1685577600000/2023-06-account-summary-272b9a4f73e11030d0ba037daee47a35.csv.gz", "account_id": "abc"}], "processed_at": 1687470448297}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'abc'
        month = '2023-02'
        date_from = 1675209600000
        date_to = 1675987200000
        limit = 30
        start = 'testString'

        # Invoke method
        response = _service.get_reports_snapshot(
            account_id,
            month,
            date_from=date_from,
            date_to=date_to,
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
        assert 'month={}'.format(month) in query_string
        assert 'date_from={}'.format(date_from) in query_string
        assert 'date_to={}'.format(date_to) in query_string
        assert '_limit={}'.format(limit) in query_string
        assert '_start={}'.format(start) in query_string

    def test_get_reports_snapshot_all_params_with_retries(self):
        # Enable retries and run test_get_reports_snapshot_all_params.
        _service.enable_retries()
        self.test_get_reports_snapshot_all_params()

        # Disable retries and run test_get_reports_snapshot_all_params.
        _service.disable_retries()
        self.test_get_reports_snapshot_all_params()

    @responses.activate
    def test_get_reports_snapshot_required_params(self):
        """
        test_get_reports_snapshot_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-reports-snapshots')
        mock_response = '{"count": 3, "first": {"href": "/v1/billing-reports-snapshots?_limit=10&account_id=272b9a4f73e11030d0ba037daee47a35&date_from=-Infinity&date_to=Infinity&month=2023-06"}, "next": {"href": "/v1/billing-reports-snapshots?_limit=10&account_id=272b9a4f73e11030d0ba037daee47a35&date_from=-Infinity&date_to=Infinity&month=2023-06", "offset": "g1AAAAHyeJzLYWBgYMtgTmHQSklKzi9KdUhJMtRLytVNTtZNSU3JTE4sSU0xMjTUS87JL01JzCvRy0styQHqYUpSAJJJ-v___88C892cKtZ"}, "snapshots": [{"account_id": "abc", "month": "2023-06", "account_type": "account", "expected_processed_at": 1687470383610, "state": "enabled", "billing_period": {"start": "2023-06-01T00:00:00.000Z", "end": "2023-06-30T23:59:59.999Z"}, "snapshot_id": "1685577600000", "charset": "UTF-8", "compression": "GZIP", "content_type": "text/csv", "bucket": "bucket_name", "version": "1.0", "created_on": "2023-06-22T21:47:28.297Z", "report_types": [{"type": "account_summary", "version": "1.0"}], "files": [{"report_types": "account_summary", "location": "june/2023-06/1685577600000/2023-06-account-summary-272b9a4f73e11030d0ba037daee47a35.csv.gz", "account_id": "abc"}], "processed_at": 1687470448297}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'abc'
        month = '2023-02'

        # Invoke method
        response = _service.get_reports_snapshot(
            account_id,
            month,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'month={}'.format(month) in query_string

    def test_get_reports_snapshot_required_params_with_retries(self):
        # Enable retries and run test_get_reports_snapshot_required_params.
        _service.enable_retries()
        self.test_get_reports_snapshot_required_params()

        # Disable retries and run test_get_reports_snapshot_required_params.
        _service.disable_retries()
        self.test_get_reports_snapshot_required_params()

    @responses.activate
    def test_get_reports_snapshot_value_error(self):
        """
        test_get_reports_snapshot_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-reports-snapshots')
        mock_response = '{"count": 3, "first": {"href": "/v1/billing-reports-snapshots?_limit=10&account_id=272b9a4f73e11030d0ba037daee47a35&date_from=-Infinity&date_to=Infinity&month=2023-06"}, "next": {"href": "/v1/billing-reports-snapshots?_limit=10&account_id=272b9a4f73e11030d0ba037daee47a35&date_from=-Infinity&date_to=Infinity&month=2023-06", "offset": "g1AAAAHyeJzLYWBgYMtgTmHQSklKzi9KdUhJMtRLytVNTtZNSU3JTE4sSU0xMjTUS87JL01JzCvRy0styQHqYUpSAJJJ-v___88C892cKtZ"}, "snapshots": [{"account_id": "abc", "month": "2023-06", "account_type": "account", "expected_processed_at": 1687470383610, "state": "enabled", "billing_period": {"start": "2023-06-01T00:00:00.000Z", "end": "2023-06-30T23:59:59.999Z"}, "snapshot_id": "1685577600000", "charset": "UTF-8", "compression": "GZIP", "content_type": "text/csv", "bucket": "bucket_name", "version": "1.0", "created_on": "2023-06-22T21:47:28.297Z", "report_types": [{"type": "account_summary", "version": "1.0"}], "files": [{"report_types": "account_summary", "location": "june/2023-06/1685577600000/2023-06-account-summary-272b9a4f73e11030d0ba037daee47a35.csv.gz", "account_id": "abc"}], "processed_at": 1687470448297}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        account_id = 'abc'
        month = '2023-02'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "month": month,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_reports_snapshot(**req_copy)

    def test_get_reports_snapshot_value_error_with_retries(self):
        # Enable retries and run test_get_reports_snapshot_value_error.
        _service.enable_retries()
        self.test_get_reports_snapshot_value_error()

        # Disable retries and run test_get_reports_snapshot_value_error.
        _service.disable_retries()
        self.test_get_reports_snapshot_value_error()

    @responses.activate
    def test_get_reports_snapshot_with_pager_get_next(self):
        """
        test_get_reports_snapshot_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/billing-reports-snapshots')
        mock_response1 = '{"snapshots":[{"account_id":"abc","month":"2023-06","account_type":"account","expected_processed_at":1687470383610,"state":"enabled","billing_period":{"start":"2023-06-01T00:00:00.000Z","end":"2023-06-30T23:59:59.999Z"},"snapshot_id":"1685577600000","charset":"UTF-8","compression":"GZIP","content_type":"text/csv","bucket":"bucket_name","version":"1.0","created_on":"2023-06-22T21:47:28.297Z","report_types":[{"type":"account_summary","version":"1.0"}],"files":[{"report_types":"account_summary","location":"june/2023-06/1685577600000/2023-06-account-summary-272b9a4f73e11030d0ba037daee47a35.csv.gz","account_id":"abc"}],"processed_at":1687470448297}],"next":{"href":"https://myhost.com/somePath?_start=1"},"total_count":2,"limit":1}'
        mock_response2 = '{"snapshots":[{"account_id":"abc","month":"2023-06","account_type":"account","expected_processed_at":1687470383610,"state":"enabled","billing_period":{"start":"2023-06-01T00:00:00.000Z","end":"2023-06-30T23:59:59.999Z"},"snapshot_id":"1685577600000","charset":"UTF-8","compression":"GZIP","content_type":"text/csv","bucket":"bucket_name","version":"1.0","created_on":"2023-06-22T21:47:28.297Z","report_types":[{"type":"account_summary","version":"1.0"}],"files":[{"report_types":"account_summary","location":"june/2023-06/1685577600000/2023-06-account-summary-272b9a4f73e11030d0ba037daee47a35.csv.gz","account_id":"abc"}],"processed_at":1687470448297}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = GetReportsSnapshotPager(
            client=_service,
            account_id='abc',
            month='2023-02',
            date_from=1675209600000,
            date_to=1675987200000,
            limit=30,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_get_reports_snapshot_with_pager_get_all(self):
        """
        test_get_reports_snapshot_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/billing-reports-snapshots')
        mock_response1 = '{"snapshots":[{"account_id":"abc","month":"2023-06","account_type":"account","expected_processed_at":1687470383610,"state":"enabled","billing_period":{"start":"2023-06-01T00:00:00.000Z","end":"2023-06-30T23:59:59.999Z"},"snapshot_id":"1685577600000","charset":"UTF-8","compression":"GZIP","content_type":"text/csv","bucket":"bucket_name","version":"1.0","created_on":"2023-06-22T21:47:28.297Z","report_types":[{"type":"account_summary","version":"1.0"}],"files":[{"report_types":"account_summary","location":"june/2023-06/1685577600000/2023-06-account-summary-272b9a4f73e11030d0ba037daee47a35.csv.gz","account_id":"abc"}],"processed_at":1687470448297}],"next":{"href":"https://myhost.com/somePath?_start=1"},"total_count":2,"limit":1}'
        mock_response2 = '{"snapshots":[{"account_id":"abc","month":"2023-06","account_type":"account","expected_processed_at":1687470383610,"state":"enabled","billing_period":{"start":"2023-06-01T00:00:00.000Z","end":"2023-06-30T23:59:59.999Z"},"snapshot_id":"1685577600000","charset":"UTF-8","compression":"GZIP","content_type":"text/csv","bucket":"bucket_name","version":"1.0","created_on":"2023-06-22T21:47:28.297Z","report_types":[{"type":"account_summary","version":"1.0"}],"files":[{"report_types":"account_summary","location":"june/2023-06/1685577600000/2023-06-account-summary-272b9a4f73e11030d0ba037daee47a35.csv.gz","account_id":"abc"}],"processed_at":1687470448297}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = GetReportsSnapshotPager(
            client=_service,
            account_id='abc',
            month='2023-02',
            date_from=1675209600000,
            date_to=1675987200000,
            limit=30,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


# endregion
##############################################################################
# End of Service: BillingReportsSnapshot
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AccountSummary:
    """
    Test Class for AccountSummary
    """

    def test_account_summary_serialization(self):
        """
        Test serialization/deserialization for AccountSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        discount_model = {}  # Discount
        discount_model['ref'] = 'Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9'
        discount_model['name'] = 'platform-discount'
        discount_model['display_name'] = 'Platform Service Discount'
        discount_model['discount'] = 5

        metric_model = {}  # Metric
        metric_model['metric'] = 'UP-TIME'
        metric_model['metric_name'] = 'UP-TIME'
        metric_model['quantity'] = 711.11
        metric_model['rateable_quantity'] = 700
        metric_model['cost'] = 123.45
        metric_model['rated_cost'] = 130.0
        metric_model['price'] = ['testString']
        metric_model['unit'] = 'HOURS'
        metric_model['unit_name'] = 'HOURS'
        metric_model['non_chargeable'] = True
        metric_model['discounts'] = [discount_model]

        plan_model = {}  # Plan
        plan_model['plan_id'] = 'testString'
        plan_model['plan_name'] = 'testString'
        plan_model['pricing_region'] = 'testString'
        plan_model['pricing_plan_id'] = 'testString'
        plan_model['billable'] = True
        plan_model['cost'] = 72.5
        plan_model['rated_cost'] = 72.5
        plan_model['usage'] = [metric_model]
        plan_model['discounts'] = [discount_model]
        plan_model['pending'] = True

        resource_model = {}  # Resource
        resource_model['resource_id'] = 'testString'
        resource_model['resource_name'] = 'testString'
        resource_model['billable_cost'] = 72.5
        resource_model['billable_rated_cost'] = 72.5
        resource_model['non_billable_cost'] = 72.5
        resource_model['non_billable_rated_cost'] = 72.5
        resource_model['plans'] = [plan_model]
        resource_model['discounts'] = [discount_model]

        resources_summary_model = {}  # ResourcesSummary
        resources_summary_model['billable_cost'] = 72.5
        resources_summary_model['non_billable_cost'] = 72.5

        offer_credits_model = {}  # OfferCredits
        offer_credits_model['starting_balance'] = 72.5
        offer_credits_model['used'] = 72.5
        offer_credits_model['balance'] = 72.5

        offer_model = {}  # Offer
        offer_model['offer_id'] = 'testString'
        offer_model['credits_total'] = 72.5
        offer_model['offer_template'] = 'testString'
        offer_model['valid_from'] = '2019-01-01T12:00:00Z'
        offer_model['expires_on'] = '2019-01-01T12:00:00Z'
        offer_model['credits'] = offer_credits_model

        support_summary_model = {}  # SupportSummary
        support_summary_model['cost'] = 72.5
        support_summary_model['type'] = 'testString'
        support_summary_model['overage'] = 72.5

        subscription_term_credits_model = {}  # SubscriptionTermCredits
        subscription_term_credits_model['total'] = 72.5
        subscription_term_credits_model['starting_balance'] = 72.5
        subscription_term_credits_model['used'] = 72.5
        subscription_term_credits_model['balance'] = 72.5

        subscription_term_model = {}  # SubscriptionTerm
        subscription_term_model['start'] = '2019-01-01T12:00:00Z'
        subscription_term_model['end'] = '2019-01-01T12:00:00Z'
        subscription_term_model['credits'] = subscription_term_credits_model

        subscription_model = {}  # Subscription
        subscription_model['subscription_id'] = 'testString'
        subscription_model['charge_agreement_number'] = 'testString'
        subscription_model['type'] = 'testString'
        subscription_model['subscription_amount'] = 72.5
        subscription_model['start'] = '2019-01-01T12:00:00Z'
        subscription_model['end'] = '2019-01-01T12:00:00Z'
        subscription_model['credits_total'] = 72.5
        subscription_model['terms'] = [subscription_term_model]

        subscription_summary_model = {}  # SubscriptionSummary
        subscription_summary_model['overage'] = 72.5
        subscription_summary_model['subscriptions'] = [subscription_model]

        # Construct a json representation of a AccountSummary model
        account_summary_model_json = {}
        account_summary_model_json['account_id'] = 'testString'
        account_summary_model_json['account_resources'] = [resource_model]
        account_summary_model_json['month'] = 'testString'
        account_summary_model_json['billing_country_code'] = 'testString'
        account_summary_model_json['billing_currency_code'] = 'testString'
        account_summary_model_json['resources'] = resources_summary_model
        account_summary_model_json['offers'] = [offer_model]
        account_summary_model_json['support'] = [support_summary_model]
        account_summary_model_json['support_resources'] = ['testString']
        account_summary_model_json['subscription'] = subscription_summary_model

        # Construct a model instance of AccountSummary by calling from_dict on the json representation
        account_summary_model = AccountSummary.from_dict(account_summary_model_json)
        assert account_summary_model != False

        # Construct a model instance of AccountSummary by calling from_dict on the json representation
        account_summary_model_dict = AccountSummary.from_dict(account_summary_model_json).__dict__
        account_summary_model2 = AccountSummary(**account_summary_model_dict)

        # Verify the model instances are equivalent
        assert account_summary_model == account_summary_model2

        # Convert model instance back to dict and verify no loss of data
        account_summary_model_json2 = account_summary_model.to_dict()
        assert account_summary_model_json2 == account_summary_model_json


class TestModel_AccountUsage:
    """
    Test Class for AccountUsage
    """

    def test_account_usage_serialization(self):
        """
        Test serialization/deserialization for AccountUsage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        discount_model = {}  # Discount
        discount_model['ref'] = 'Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9'
        discount_model['name'] = 'platform-discount'
        discount_model['display_name'] = 'Platform Service Discount'
        discount_model['discount'] = 5

        metric_model = {}  # Metric
        metric_model['metric'] = 'UP-TIME'
        metric_model['metric_name'] = 'UP-TIME'
        metric_model['quantity'] = 711.11
        metric_model['rateable_quantity'] = 700
        metric_model['cost'] = 123.45
        metric_model['rated_cost'] = 130.0
        metric_model['price'] = ['testString']
        metric_model['unit'] = 'HOURS'
        metric_model['unit_name'] = 'HOURS'
        metric_model['non_chargeable'] = True
        metric_model['discounts'] = [discount_model]

        plan_model = {}  # Plan
        plan_model['plan_id'] = 'testString'
        plan_model['plan_name'] = 'testString'
        plan_model['pricing_region'] = 'testString'
        plan_model['pricing_plan_id'] = 'testString'
        plan_model['billable'] = True
        plan_model['cost'] = 72.5
        plan_model['rated_cost'] = 72.5
        plan_model['usage'] = [metric_model]
        plan_model['discounts'] = [discount_model]
        plan_model['pending'] = True

        resource_model = {}  # Resource
        resource_model['resource_id'] = 'testString'
        resource_model['resource_name'] = 'testString'
        resource_model['billable_cost'] = 72.5
        resource_model['billable_rated_cost'] = 72.5
        resource_model['non_billable_cost'] = 72.5
        resource_model['non_billable_rated_cost'] = 72.5
        resource_model['plans'] = [plan_model]
        resource_model['discounts'] = [discount_model]

        # Construct a json representation of a AccountUsage model
        account_usage_model_json = {}
        account_usage_model_json['account_id'] = 'testString'
        account_usage_model_json['pricing_country'] = 'USA'
        account_usage_model_json['currency_code'] = 'USD'
        account_usage_model_json['month'] = '2017-08'
        account_usage_model_json['resources'] = [resource_model]
        account_usage_model_json['currency_rate'] = 10.8716

        # Construct a model instance of AccountUsage by calling from_dict on the json representation
        account_usage_model = AccountUsage.from_dict(account_usage_model_json)
        assert account_usage_model != False

        # Construct a model instance of AccountUsage by calling from_dict on the json representation
        account_usage_model_dict = AccountUsage.from_dict(account_usage_model_json).__dict__
        account_usage_model2 = AccountUsage(**account_usage_model_dict)

        # Verify the model instances are equivalent
        assert account_usage_model == account_usage_model2

        # Convert model instance back to dict and verify no loss of data
        account_usage_model_json2 = account_usage_model.to_dict()
        assert account_usage_model_json2 == account_usage_model_json


class TestModel_Discount:
    """
    Test Class for Discount
    """

    def test_discount_serialization(self):
        """
        Test serialization/deserialization for Discount
        """

        # Construct a json representation of a Discount model
        discount_model_json = {}
        discount_model_json['ref'] = 'Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9'
        discount_model_json['name'] = 'platform-discount'
        discount_model_json['display_name'] = 'Platform Service Discount'
        discount_model_json['discount'] = 5

        # Construct a model instance of Discount by calling from_dict on the json representation
        discount_model = Discount.from_dict(discount_model_json)
        assert discount_model != False

        # Construct a model instance of Discount by calling from_dict on the json representation
        discount_model_dict = Discount.from_dict(discount_model_json).__dict__
        discount_model2 = Discount(**discount_model_dict)

        # Verify the model instances are equivalent
        assert discount_model == discount_model2

        # Convert model instance back to dict and verify no loss of data
        discount_model_json2 = discount_model.to_dict()
        assert discount_model_json2 == discount_model_json


class TestModel_InstanceUsage:
    """
    Test Class for InstanceUsage
    """

    def test_instance_usage_serialization(self):
        """
        Test serialization/deserialization for InstanceUsage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        discount_model = {}  # Discount
        discount_model['ref'] = 'Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9'
        discount_model['name'] = 'platform-discount'
        discount_model['display_name'] = 'Platform Service Discount'
        discount_model['discount'] = 5

        metric_model = {}  # Metric
        metric_model['metric'] = 'UP-TIME'
        metric_model['metric_name'] = 'UP-TIME'
        metric_model['quantity'] = 711.11
        metric_model['rateable_quantity'] = 700
        metric_model['cost'] = 123.45
        metric_model['rated_cost'] = 130.0
        metric_model['price'] = ['testString']
        metric_model['unit'] = 'HOURS'
        metric_model['unit_name'] = 'HOURS'
        metric_model['non_chargeable'] = True
        metric_model['discounts'] = [discount_model]

        # Construct a json representation of a InstanceUsage model
        instance_usage_model_json = {}
        instance_usage_model_json['account_id'] = 'testString'
        instance_usage_model_json['resource_instance_id'] = 'testString'
        instance_usage_model_json['resource_instance_name'] = 'testString'
        instance_usage_model_json['resource_id'] = 'testString'
        instance_usage_model_json['resource_name'] = 'testString'
        instance_usage_model_json['resource_group_id'] = 'testString'
        instance_usage_model_json['resource_group_name'] = 'testString'
        instance_usage_model_json['organization_id'] = 'testString'
        instance_usage_model_json['organization_name'] = 'testString'
        instance_usage_model_json['space_id'] = 'testString'
        instance_usage_model_json['space_name'] = 'testString'
        instance_usage_model_json['consumer_id'] = 'testString'
        instance_usage_model_json['region'] = 'testString'
        instance_usage_model_json['pricing_region'] = 'testString'
        instance_usage_model_json['pricing_country'] = 'USA'
        instance_usage_model_json['currency_code'] = 'USD'
        instance_usage_model_json['billable'] = True
        instance_usage_model_json['plan_id'] = 'testString'
        instance_usage_model_json['plan_name'] = 'testString'
        instance_usage_model_json['month'] = '2017-08'
        instance_usage_model_json['usage'] = [metric_model]
        instance_usage_model_json['pending'] = True
        instance_usage_model_json['currency_rate'] = 10.8716

        # Construct a model instance of InstanceUsage by calling from_dict on the json representation
        instance_usage_model = InstanceUsage.from_dict(instance_usage_model_json)
        assert instance_usage_model != False

        # Construct a model instance of InstanceUsage by calling from_dict on the json representation
        instance_usage_model_dict = InstanceUsage.from_dict(instance_usage_model_json).__dict__
        instance_usage_model2 = InstanceUsage(**instance_usage_model_dict)

        # Verify the model instances are equivalent
        assert instance_usage_model == instance_usage_model2

        # Convert model instance back to dict and verify no loss of data
        instance_usage_model_json2 = instance_usage_model.to_dict()
        assert instance_usage_model_json2 == instance_usage_model_json


class TestModel_InstancesUsageFirst:
    """
    Test Class for InstancesUsageFirst
    """

    def test_instances_usage_first_serialization(self):
        """
        Test serialization/deserialization for InstancesUsageFirst
        """

        # Construct a json representation of a InstancesUsageFirst model
        instances_usage_first_model_json = {}
        instances_usage_first_model_json['href'] = 'testString'

        # Construct a model instance of InstancesUsageFirst by calling from_dict on the json representation
        instances_usage_first_model = InstancesUsageFirst.from_dict(instances_usage_first_model_json)
        assert instances_usage_first_model != False

        # Construct a model instance of InstancesUsageFirst by calling from_dict on the json representation
        instances_usage_first_model_dict = InstancesUsageFirst.from_dict(instances_usage_first_model_json).__dict__
        instances_usage_first_model2 = InstancesUsageFirst(**instances_usage_first_model_dict)

        # Verify the model instances are equivalent
        assert instances_usage_first_model == instances_usage_first_model2

        # Convert model instance back to dict and verify no loss of data
        instances_usage_first_model_json2 = instances_usage_first_model.to_dict()
        assert instances_usage_first_model_json2 == instances_usage_first_model_json


class TestModel_InstancesUsageNext:
    """
    Test Class for InstancesUsageNext
    """

    def test_instances_usage_next_serialization(self):
        """
        Test serialization/deserialization for InstancesUsageNext
        """

        # Construct a json representation of a InstancesUsageNext model
        instances_usage_next_model_json = {}
        instances_usage_next_model_json['href'] = 'testString'
        instances_usage_next_model_json['offset'] = 'testString'

        # Construct a model instance of InstancesUsageNext by calling from_dict on the json representation
        instances_usage_next_model = InstancesUsageNext.from_dict(instances_usage_next_model_json)
        assert instances_usage_next_model != False

        # Construct a model instance of InstancesUsageNext by calling from_dict on the json representation
        instances_usage_next_model_dict = InstancesUsageNext.from_dict(instances_usage_next_model_json).__dict__
        instances_usage_next_model2 = InstancesUsageNext(**instances_usage_next_model_dict)

        # Verify the model instances are equivalent
        assert instances_usage_next_model == instances_usage_next_model2

        # Convert model instance back to dict and verify no loss of data
        instances_usage_next_model_json2 = instances_usage_next_model.to_dict()
        assert instances_usage_next_model_json2 == instances_usage_next_model_json


class TestModel_InstancesUsage:
    """
    Test Class for InstancesUsage
    """

    def test_instances_usage_serialization(self):
        """
        Test serialization/deserialization for InstancesUsage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        instances_usage_first_model = {}  # InstancesUsageFirst
        instances_usage_first_model['href'] = 'testString'

        instances_usage_next_model = {}  # InstancesUsageNext
        instances_usage_next_model['href'] = 'testString'
        instances_usage_next_model['offset'] = 'testString'

        discount_model = {}  # Discount
        discount_model['ref'] = 'Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9'
        discount_model['name'] = 'platform-discount'
        discount_model['display_name'] = 'Platform Service Discount'
        discount_model['discount'] = 5

        metric_model = {}  # Metric
        metric_model['metric'] = 'UP-TIME'
        metric_model['metric_name'] = 'UP-TIME'
        metric_model['quantity'] = 711.11
        metric_model['rateable_quantity'] = 700
        metric_model['cost'] = 123.45
        metric_model['rated_cost'] = 130.0
        metric_model['price'] = ['testString']
        metric_model['unit'] = 'HOURS'
        metric_model['unit_name'] = 'HOURS'
        metric_model['non_chargeable'] = True
        metric_model['discounts'] = [discount_model]

        instance_usage_model = {}  # InstanceUsage
        instance_usage_model['account_id'] = 'testString'
        instance_usage_model['resource_instance_id'] = 'testString'
        instance_usage_model['resource_instance_name'] = 'testString'
        instance_usage_model['resource_id'] = 'testString'
        instance_usage_model['resource_name'] = 'testString'
        instance_usage_model['resource_group_id'] = 'testString'
        instance_usage_model['resource_group_name'] = 'testString'
        instance_usage_model['organization_id'] = 'testString'
        instance_usage_model['organization_name'] = 'testString'
        instance_usage_model['space_id'] = 'testString'
        instance_usage_model['space_name'] = 'testString'
        instance_usage_model['consumer_id'] = 'testString'
        instance_usage_model['region'] = 'testString'
        instance_usage_model['pricing_region'] = 'testString'
        instance_usage_model['pricing_country'] = 'USA'
        instance_usage_model['currency_code'] = 'USD'
        instance_usage_model['billable'] = True
        instance_usage_model['plan_id'] = 'testString'
        instance_usage_model['plan_name'] = 'testString'
        instance_usage_model['month'] = '2017-08'
        instance_usage_model['usage'] = [metric_model]
        instance_usage_model['pending'] = True
        instance_usage_model['currency_rate'] = 10.8716

        # Construct a json representation of a InstancesUsage model
        instances_usage_model_json = {}
        instances_usage_model_json['limit'] = 38
        instances_usage_model_json['count'] = 38
        instances_usage_model_json['first'] = instances_usage_first_model
        instances_usage_model_json['next'] = instances_usage_next_model
        instances_usage_model_json['resources'] = [instance_usage_model]

        # Construct a model instance of InstancesUsage by calling from_dict on the json representation
        instances_usage_model = InstancesUsage.from_dict(instances_usage_model_json)
        assert instances_usage_model != False

        # Construct a model instance of InstancesUsage by calling from_dict on the json representation
        instances_usage_model_dict = InstancesUsage.from_dict(instances_usage_model_json).__dict__
        instances_usage_model2 = InstancesUsage(**instances_usage_model_dict)

        # Verify the model instances are equivalent
        assert instances_usage_model == instances_usage_model2

        # Convert model instance back to dict and verify no loss of data
        instances_usage_model_json2 = instances_usage_model.to_dict()
        assert instances_usage_model_json2 == instances_usage_model_json


class TestModel_Metric:
    """
    Test Class for Metric
    """

    def test_metric_serialization(self):
        """
        Test serialization/deserialization for Metric
        """

        # Construct dict forms of any model objects needed in order to build this model.

        discount_model = {}  # Discount
        discount_model['ref'] = 'Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9'
        discount_model['name'] = 'platform-discount'
        discount_model['display_name'] = 'Platform Service Discount'
        discount_model['discount'] = 5

        # Construct a json representation of a Metric model
        metric_model_json = {}
        metric_model_json['metric'] = 'UP-TIME'
        metric_model_json['metric_name'] = 'UP-TIME'
        metric_model_json['quantity'] = 711.11
        metric_model_json['rateable_quantity'] = 700
        metric_model_json['cost'] = 123.45
        metric_model_json['rated_cost'] = 130.0
        metric_model_json['price'] = ['testString']
        metric_model_json['unit'] = 'HOURS'
        metric_model_json['unit_name'] = 'HOURS'
        metric_model_json['non_chargeable'] = True
        metric_model_json['discounts'] = [discount_model]

        # Construct a model instance of Metric by calling from_dict on the json representation
        metric_model = Metric.from_dict(metric_model_json)
        assert metric_model != False

        # Construct a model instance of Metric by calling from_dict on the json representation
        metric_model_dict = Metric.from_dict(metric_model_json).__dict__
        metric_model2 = Metric(**metric_model_dict)

        # Verify the model instances are equivalent
        assert metric_model == metric_model2

        # Convert model instance back to dict and verify no loss of data
        metric_model_json2 = metric_model.to_dict()
        assert metric_model_json2 == metric_model_json


class TestModel_Offer:
    """
    Test Class for Offer
    """

    def test_offer_serialization(self):
        """
        Test serialization/deserialization for Offer
        """

        # Construct dict forms of any model objects needed in order to build this model.

        offer_credits_model = {}  # OfferCredits
        offer_credits_model['starting_balance'] = 72.5
        offer_credits_model['used'] = 72.5
        offer_credits_model['balance'] = 72.5

        # Construct a json representation of a Offer model
        offer_model_json = {}
        offer_model_json['offer_id'] = 'testString'
        offer_model_json['credits_total'] = 72.5
        offer_model_json['offer_template'] = 'testString'
        offer_model_json['valid_from'] = '2019-01-01T12:00:00Z'
        offer_model_json['expires_on'] = '2019-01-01T12:00:00Z'
        offer_model_json['credits'] = offer_credits_model

        # Construct a model instance of Offer by calling from_dict on the json representation
        offer_model = Offer.from_dict(offer_model_json)
        assert offer_model != False

        # Construct a model instance of Offer by calling from_dict on the json representation
        offer_model_dict = Offer.from_dict(offer_model_json).__dict__
        offer_model2 = Offer(**offer_model_dict)

        # Verify the model instances are equivalent
        assert offer_model == offer_model2

        # Convert model instance back to dict and verify no loss of data
        offer_model_json2 = offer_model.to_dict()
        assert offer_model_json2 == offer_model_json


class TestModel_OfferCredits:
    """
    Test Class for OfferCredits
    """

    def test_offer_credits_serialization(self):
        """
        Test serialization/deserialization for OfferCredits
        """

        # Construct a json representation of a OfferCredits model
        offer_credits_model_json = {}
        offer_credits_model_json['starting_balance'] = 72.5
        offer_credits_model_json['used'] = 72.5
        offer_credits_model_json['balance'] = 72.5

        # Construct a model instance of OfferCredits by calling from_dict on the json representation
        offer_credits_model = OfferCredits.from_dict(offer_credits_model_json)
        assert offer_credits_model != False

        # Construct a model instance of OfferCredits by calling from_dict on the json representation
        offer_credits_model_dict = OfferCredits.from_dict(offer_credits_model_json).__dict__
        offer_credits_model2 = OfferCredits(**offer_credits_model_dict)

        # Verify the model instances are equivalent
        assert offer_credits_model == offer_credits_model2

        # Convert model instance back to dict and verify no loss of data
        offer_credits_model_json2 = offer_credits_model.to_dict()
        assert offer_credits_model_json2 == offer_credits_model_json


class TestModel_OrgUsage:
    """
    Test Class for OrgUsage
    """

    def test_org_usage_serialization(self):
        """
        Test serialization/deserialization for OrgUsage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        discount_model = {}  # Discount
        discount_model['ref'] = 'Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9'
        discount_model['name'] = 'platform-discount'
        discount_model['display_name'] = 'Platform Service Discount'
        discount_model['discount'] = 5

        metric_model = {}  # Metric
        metric_model['metric'] = 'UP-TIME'
        metric_model['metric_name'] = 'UP-TIME'
        metric_model['quantity'] = 711.11
        metric_model['rateable_quantity'] = 700
        metric_model['cost'] = 123.45
        metric_model['rated_cost'] = 130.0
        metric_model['price'] = ['testString']
        metric_model['unit'] = 'HOURS'
        metric_model['unit_name'] = 'HOURS'
        metric_model['non_chargeable'] = True
        metric_model['discounts'] = [discount_model]

        plan_model = {}  # Plan
        plan_model['plan_id'] = 'testString'
        plan_model['plan_name'] = 'testString'
        plan_model['pricing_region'] = 'testString'
        plan_model['pricing_plan_id'] = 'testString'
        plan_model['billable'] = True
        plan_model['cost'] = 72.5
        plan_model['rated_cost'] = 72.5
        plan_model['usage'] = [metric_model]
        plan_model['discounts'] = [discount_model]
        plan_model['pending'] = True

        resource_model = {}  # Resource
        resource_model['resource_id'] = 'testString'
        resource_model['resource_name'] = 'testString'
        resource_model['billable_cost'] = 72.5
        resource_model['billable_rated_cost'] = 72.5
        resource_model['non_billable_cost'] = 72.5
        resource_model['non_billable_rated_cost'] = 72.5
        resource_model['plans'] = [plan_model]
        resource_model['discounts'] = [discount_model]

        # Construct a json representation of a OrgUsage model
        org_usage_model_json = {}
        org_usage_model_json['account_id'] = 'testString'
        org_usage_model_json['organization_id'] = 'testString'
        org_usage_model_json['organization_name'] = 'testString'
        org_usage_model_json['pricing_country'] = 'USA'
        org_usage_model_json['currency_code'] = 'USD'
        org_usage_model_json['month'] = '2017-08'
        org_usage_model_json['resources'] = [resource_model]
        org_usage_model_json['currency_rate'] = 10.8716

        # Construct a model instance of OrgUsage by calling from_dict on the json representation
        org_usage_model = OrgUsage.from_dict(org_usage_model_json)
        assert org_usage_model != False

        # Construct a model instance of OrgUsage by calling from_dict on the json representation
        org_usage_model_dict = OrgUsage.from_dict(org_usage_model_json).__dict__
        org_usage_model2 = OrgUsage(**org_usage_model_dict)

        # Verify the model instances are equivalent
        assert org_usage_model == org_usage_model2

        # Convert model instance back to dict and verify no loss of data
        org_usage_model_json2 = org_usage_model.to_dict()
        assert org_usage_model_json2 == org_usage_model_json


class TestModel_Plan:
    """
    Test Class for Plan
    """

    def test_plan_serialization(self):
        """
        Test serialization/deserialization for Plan
        """

        # Construct dict forms of any model objects needed in order to build this model.

        discount_model = {}  # Discount
        discount_model['ref'] = 'Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9'
        discount_model['name'] = 'platform-discount'
        discount_model['display_name'] = 'Platform Service Discount'
        discount_model['discount'] = 5

        metric_model = {}  # Metric
        metric_model['metric'] = 'UP-TIME'
        metric_model['metric_name'] = 'UP-TIME'
        metric_model['quantity'] = 711.11
        metric_model['rateable_quantity'] = 700
        metric_model['cost'] = 123.45
        metric_model['rated_cost'] = 130.0
        metric_model['price'] = ['testString']
        metric_model['unit'] = 'HOURS'
        metric_model['unit_name'] = 'HOURS'
        metric_model['non_chargeable'] = True
        metric_model['discounts'] = [discount_model]

        # Construct a json representation of a Plan model
        plan_model_json = {}
        plan_model_json['plan_id'] = 'testString'
        plan_model_json['plan_name'] = 'testString'
        plan_model_json['pricing_region'] = 'testString'
        plan_model_json['pricing_plan_id'] = 'testString'
        plan_model_json['billable'] = True
        plan_model_json['cost'] = 72.5
        plan_model_json['rated_cost'] = 72.5
        plan_model_json['usage'] = [metric_model]
        plan_model_json['discounts'] = [discount_model]
        plan_model_json['pending'] = True

        # Construct a model instance of Plan by calling from_dict on the json representation
        plan_model = Plan.from_dict(plan_model_json)
        assert plan_model != False

        # Construct a model instance of Plan by calling from_dict on the json representation
        plan_model_dict = Plan.from_dict(plan_model_json).__dict__
        plan_model2 = Plan(**plan_model_dict)

        # Verify the model instances are equivalent
        assert plan_model == plan_model2

        # Convert model instance back to dict and verify no loss of data
        plan_model_json2 = plan_model.to_dict()
        assert plan_model_json2 == plan_model_json


class TestModel_Resource:
    """
    Test Class for Resource
    """

    def test_resource_serialization(self):
        """
        Test serialization/deserialization for Resource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        discount_model = {}  # Discount
        discount_model['ref'] = 'Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9'
        discount_model['name'] = 'platform-discount'
        discount_model['display_name'] = 'Platform Service Discount'
        discount_model['discount'] = 5

        metric_model = {}  # Metric
        metric_model['metric'] = 'UP-TIME'
        metric_model['metric_name'] = 'UP-TIME'
        metric_model['quantity'] = 711.11
        metric_model['rateable_quantity'] = 700
        metric_model['cost'] = 123.45
        metric_model['rated_cost'] = 130.0
        metric_model['price'] = ['testString']
        metric_model['unit'] = 'HOURS'
        metric_model['unit_name'] = 'HOURS'
        metric_model['non_chargeable'] = True
        metric_model['discounts'] = [discount_model]

        plan_model = {}  # Plan
        plan_model['plan_id'] = 'testString'
        plan_model['plan_name'] = 'testString'
        plan_model['pricing_region'] = 'testString'
        plan_model['pricing_plan_id'] = 'testString'
        plan_model['billable'] = True
        plan_model['cost'] = 72.5
        plan_model['rated_cost'] = 72.5
        plan_model['usage'] = [metric_model]
        plan_model['discounts'] = [discount_model]
        plan_model['pending'] = True

        # Construct a json representation of a Resource model
        resource_model_json = {}
        resource_model_json['resource_id'] = 'testString'
        resource_model_json['resource_name'] = 'testString'
        resource_model_json['billable_cost'] = 72.5
        resource_model_json['billable_rated_cost'] = 72.5
        resource_model_json['non_billable_cost'] = 72.5
        resource_model_json['non_billable_rated_cost'] = 72.5
        resource_model_json['plans'] = [plan_model]
        resource_model_json['discounts'] = [discount_model]

        # Construct a model instance of Resource by calling from_dict on the json representation
        resource_model = Resource.from_dict(resource_model_json)
        assert resource_model != False

        # Construct a model instance of Resource by calling from_dict on the json representation
        resource_model_dict = Resource.from_dict(resource_model_json).__dict__
        resource_model2 = Resource(**resource_model_dict)

        # Verify the model instances are equivalent
        assert resource_model == resource_model2

        # Convert model instance back to dict and verify no loss of data
        resource_model_json2 = resource_model.to_dict()
        assert resource_model_json2 == resource_model_json


class TestModel_ResourceGroupUsage:
    """
    Test Class for ResourceGroupUsage
    """

    def test_resource_group_usage_serialization(self):
        """
        Test serialization/deserialization for ResourceGroupUsage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        discount_model = {}  # Discount
        discount_model['ref'] = 'Discount-d27beddb-111b-4bbf-8cb1-b770f531c1a9'
        discount_model['name'] = 'platform-discount'
        discount_model['display_name'] = 'Platform Service Discount'
        discount_model['discount'] = 5

        metric_model = {}  # Metric
        metric_model['metric'] = 'UP-TIME'
        metric_model['metric_name'] = 'UP-TIME'
        metric_model['quantity'] = 711.11
        metric_model['rateable_quantity'] = 700
        metric_model['cost'] = 123.45
        metric_model['rated_cost'] = 130.0
        metric_model['price'] = ['testString']
        metric_model['unit'] = 'HOURS'
        metric_model['unit_name'] = 'HOURS'
        metric_model['non_chargeable'] = True
        metric_model['discounts'] = [discount_model]

        plan_model = {}  # Plan
        plan_model['plan_id'] = 'testString'
        plan_model['plan_name'] = 'testString'
        plan_model['pricing_region'] = 'testString'
        plan_model['pricing_plan_id'] = 'testString'
        plan_model['billable'] = True
        plan_model['cost'] = 72.5
        plan_model['rated_cost'] = 72.5
        plan_model['usage'] = [metric_model]
        plan_model['discounts'] = [discount_model]
        plan_model['pending'] = True

        resource_model = {}  # Resource
        resource_model['resource_id'] = 'testString'
        resource_model['resource_name'] = 'testString'
        resource_model['billable_cost'] = 72.5
        resource_model['billable_rated_cost'] = 72.5
        resource_model['non_billable_cost'] = 72.5
        resource_model['non_billable_rated_cost'] = 72.5
        resource_model['plans'] = [plan_model]
        resource_model['discounts'] = [discount_model]

        # Construct a json representation of a ResourceGroupUsage model
        resource_group_usage_model_json = {}
        resource_group_usage_model_json['account_id'] = 'testString'
        resource_group_usage_model_json['resource_group_id'] = 'testString'
        resource_group_usage_model_json['resource_group_name'] = 'testString'
        resource_group_usage_model_json['pricing_country'] = 'USA'
        resource_group_usage_model_json['currency_code'] = 'USD'
        resource_group_usage_model_json['month'] = '2017-08'
        resource_group_usage_model_json['resources'] = [resource_model]
        resource_group_usage_model_json['currency_rate'] = 10.8716

        # Construct a model instance of ResourceGroupUsage by calling from_dict on the json representation
        resource_group_usage_model = ResourceGroupUsage.from_dict(resource_group_usage_model_json)
        assert resource_group_usage_model != False

        # Construct a model instance of ResourceGroupUsage by calling from_dict on the json representation
        resource_group_usage_model_dict = ResourceGroupUsage.from_dict(resource_group_usage_model_json).__dict__
        resource_group_usage_model2 = ResourceGroupUsage(**resource_group_usage_model_dict)

        # Verify the model instances are equivalent
        assert resource_group_usage_model == resource_group_usage_model2

        # Convert model instance back to dict and verify no loss of data
        resource_group_usage_model_json2 = resource_group_usage_model.to_dict()
        assert resource_group_usage_model_json2 == resource_group_usage_model_json


class TestModel_ResourcesSummary:
    """
    Test Class for ResourcesSummary
    """

    def test_resources_summary_serialization(self):
        """
        Test serialization/deserialization for ResourcesSummary
        """

        # Construct a json representation of a ResourcesSummary model
        resources_summary_model_json = {}
        resources_summary_model_json['billable_cost'] = 72.5
        resources_summary_model_json['non_billable_cost'] = 72.5

        # Construct a model instance of ResourcesSummary by calling from_dict on the json representation
        resources_summary_model = ResourcesSummary.from_dict(resources_summary_model_json)
        assert resources_summary_model != False

        # Construct a model instance of ResourcesSummary by calling from_dict on the json representation
        resources_summary_model_dict = ResourcesSummary.from_dict(resources_summary_model_json).__dict__
        resources_summary_model2 = ResourcesSummary(**resources_summary_model_dict)

        # Verify the model instances are equivalent
        assert resources_summary_model == resources_summary_model2

        # Convert model instance back to dict and verify no loss of data
        resources_summary_model_json2 = resources_summary_model.to_dict()
        assert resources_summary_model_json2 == resources_summary_model_json


class TestModel_SnapshotConfigHistoryItem:
    """
    Test Class for SnapshotConfigHistoryItem
    """

    def test_snapshot_config_history_item_serialization(self):
        """
        Test serialization/deserialization for SnapshotConfigHistoryItem
        """

        # Construct a json representation of a SnapshotConfigHistoryItem model
        snapshot_config_history_item_model_json = {}
        snapshot_config_history_item_model_json['start_time'] = 1687469854342
        snapshot_config_history_item_model_json['end_time'] = 1687469989326
        snapshot_config_history_item_model_json['updated_by'] = 'IBMid-506PR16K14'
        snapshot_config_history_item_model_json['account_id'] = 'abc'
        snapshot_config_history_item_model_json['state'] = 'enabled'
        snapshot_config_history_item_model_json['account_type'] = 'account'
        snapshot_config_history_item_model_json['interval'] = 'daily'
        snapshot_config_history_item_model_json['versioning'] = 'new'
        snapshot_config_history_item_model_json['report_types'] = [
            'account_summary',
            'enterprise_summary',
            'account_resource_instance_usage',
        ]
        snapshot_config_history_item_model_json['compression'] = 'GZIP'
        snapshot_config_history_item_model_json['content_type'] = 'text/csv'
        snapshot_config_history_item_model_json['cos_reports_folder'] = 'IBMCloud-Billing-Reports'
        snapshot_config_history_item_model_json['cos_bucket'] = 'bucket_name'
        snapshot_config_history_item_model_json['cos_location'] = 'us-south'
        snapshot_config_history_item_model_json['cos_endpoint'] = (
            'https://s3.us-west.cloud-object-storage.test.appdomain.cloud'
        )

        # Construct a model instance of SnapshotConfigHistoryItem by calling from_dict on the json representation
        snapshot_config_history_item_model = SnapshotConfigHistoryItem.from_dict(
            snapshot_config_history_item_model_json
        )
        assert snapshot_config_history_item_model != False

        # Construct a model instance of SnapshotConfigHistoryItem by calling from_dict on the json representation
        snapshot_config_history_item_model_dict = SnapshotConfigHistoryItem.from_dict(
            snapshot_config_history_item_model_json
        ).__dict__
        snapshot_config_history_item_model2 = SnapshotConfigHistoryItem(**snapshot_config_history_item_model_dict)

        # Verify the model instances are equivalent
        assert snapshot_config_history_item_model == snapshot_config_history_item_model2

        # Convert model instance back to dict and verify no loss of data
        snapshot_config_history_item_model_json2 = snapshot_config_history_item_model.to_dict()
        assert snapshot_config_history_item_model_json2 == snapshot_config_history_item_model_json


class TestModel_SnapshotList:
    """
    Test Class for SnapshotList
    """

    def test_snapshot_list_serialization(self):
        """
        Test serialization/deserialization for SnapshotList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        snapshot_list_first_model = {}  # SnapshotListFirst
        snapshot_list_first_model['href'] = (
            '/v1/billing-reports-snapshots?_limit=10&account_id=272b9a4f73e11030d0ba037daee47a35&date_from=-Infinity&date_to=Infinity&month=2023-06'
        )

        snapshot_list_next_model = {}  # SnapshotListNext
        snapshot_list_next_model['href'] = (
            '/v1/billing-reports-snapshots?_limit=10&account_id=272b9a4f73e11030d0ba037daee47a35&date_from=-Infinity&date_to=Infinity&month=2023-06'
        )
        snapshot_list_next_model['offset'] = (
            'g1AAAAHyeJzLYWBgYMtgTmHQSklKzi9KdUhJMtRLytVNTtZNSU3JTE4sSU0xMjTUS87JL01JzCvRy0styQHqYUpSAJJJ-v___88C892cKtZ'
        )

        snapshot_list_snapshots_item_billing_period_model = {}  # SnapshotListSnapshotsItemBillingPeriod
        snapshot_list_snapshots_item_billing_period_model['start'] = '2023-06-01T00:00:00.000Z'
        snapshot_list_snapshots_item_billing_period_model['end'] = '2023-06-30T23:59:59.999Z'

        snapshot_list_snapshots_item_report_types_item_model = {}  # SnapshotListSnapshotsItemReportTypesItem
        snapshot_list_snapshots_item_report_types_item_model['type'] = 'account_summary'
        snapshot_list_snapshots_item_report_types_item_model['version'] = '1.0'

        snapshot_list_snapshots_item_files_item_model = {}  # SnapshotListSnapshotsItemFilesItem
        snapshot_list_snapshots_item_files_item_model['report_types'] = 'account_summary'
        snapshot_list_snapshots_item_files_item_model['location'] = (
            'june/2023-06/1685577600000/2023-06-account-summary-272b9a4f73e11030d0ba037daee47a35.csv.gz'
        )
        snapshot_list_snapshots_item_files_item_model['account_id'] = 'abc'

        snapshot_list_snapshots_item_model = {}  # SnapshotListSnapshotsItem
        snapshot_list_snapshots_item_model['account_id'] = 'abc'
        snapshot_list_snapshots_item_model['month'] = '2023-06'
        snapshot_list_snapshots_item_model['account_type'] = 'account'
        snapshot_list_snapshots_item_model['expected_processed_at'] = 1687470383610
        snapshot_list_snapshots_item_model['state'] = 'enabled'
        snapshot_list_snapshots_item_model['billing_period'] = snapshot_list_snapshots_item_billing_period_model
        snapshot_list_snapshots_item_model['snapshot_id'] = '1685577600000'
        snapshot_list_snapshots_item_model['charset'] = 'UTF-8'
        snapshot_list_snapshots_item_model['compression'] = 'GZIP'
        snapshot_list_snapshots_item_model['content_type'] = 'text/csv'
        snapshot_list_snapshots_item_model['bucket'] = 'bucket_name'
        snapshot_list_snapshots_item_model['version'] = '1.0'
        snapshot_list_snapshots_item_model['created_on'] = '2023-06-22T21:47:28.297Z'
        snapshot_list_snapshots_item_model['report_types'] = [snapshot_list_snapshots_item_report_types_item_model]
        snapshot_list_snapshots_item_model['files'] = [snapshot_list_snapshots_item_files_item_model]
        snapshot_list_snapshots_item_model['processed_at'] = 1687470448297

        # Construct a json representation of a SnapshotList model
        snapshot_list_model_json = {}
        snapshot_list_model_json['count'] = 3
        snapshot_list_model_json['first'] = snapshot_list_first_model
        snapshot_list_model_json['next'] = snapshot_list_next_model
        snapshot_list_model_json['snapshots'] = [snapshot_list_snapshots_item_model]

        # Construct a model instance of SnapshotList by calling from_dict on the json representation
        snapshot_list_model = SnapshotList.from_dict(snapshot_list_model_json)
        assert snapshot_list_model != False

        # Construct a model instance of SnapshotList by calling from_dict on the json representation
        snapshot_list_model_dict = SnapshotList.from_dict(snapshot_list_model_json).__dict__
        snapshot_list_model2 = SnapshotList(**snapshot_list_model_dict)

        # Verify the model instances are equivalent
        assert snapshot_list_model == snapshot_list_model2

        # Convert model instance back to dict and verify no loss of data
        snapshot_list_model_json2 = snapshot_list_model.to_dict()
        assert snapshot_list_model_json2 == snapshot_list_model_json


class TestModel_SnapshotListFirst:
    """
    Test Class for SnapshotListFirst
    """

    def test_snapshot_list_first_serialization(self):
        """
        Test serialization/deserialization for SnapshotListFirst
        """

        # Construct a json representation of a SnapshotListFirst model
        snapshot_list_first_model_json = {}
        snapshot_list_first_model_json['href'] = (
            '/v1/billing-reports-snapshots?_limit=10&account_id=272b9a4f73e11030d0ba037daee47a35&date_from=-Infinity&date_to=Infinity&month=2023-06'
        )

        # Construct a model instance of SnapshotListFirst by calling from_dict on the json representation
        snapshot_list_first_model = SnapshotListFirst.from_dict(snapshot_list_first_model_json)
        assert snapshot_list_first_model != False

        # Construct a model instance of SnapshotListFirst by calling from_dict on the json representation
        snapshot_list_first_model_dict = SnapshotListFirst.from_dict(snapshot_list_first_model_json).__dict__
        snapshot_list_first_model2 = SnapshotListFirst(**snapshot_list_first_model_dict)

        # Verify the model instances are equivalent
        assert snapshot_list_first_model == snapshot_list_first_model2

        # Convert model instance back to dict and verify no loss of data
        snapshot_list_first_model_json2 = snapshot_list_first_model.to_dict()
        assert snapshot_list_first_model_json2 == snapshot_list_first_model_json


class TestModel_SnapshotListNext:
    """
    Test Class for SnapshotListNext
    """

    def test_snapshot_list_next_serialization(self):
        """
        Test serialization/deserialization for SnapshotListNext
        """

        # Construct a json representation of a SnapshotListNext model
        snapshot_list_next_model_json = {}
        snapshot_list_next_model_json['href'] = (
            '/v1/billing-reports-snapshots?_limit=10&account_id=272b9a4f73e11030d0ba037daee47a35&date_from=-Infinity&date_to=Infinity&month=2023-06'
        )
        snapshot_list_next_model_json['offset'] = (
            'g1AAAAHyeJzLYWBgYMtgTmHQSklKzi9KdUhJMtRLytVNTtZNSU3JTE4sSU0xMjTUS87JL01JzCvRy0styQHqYUpSAJJJ-v___88C892cKtZ'
        )

        # Construct a model instance of SnapshotListNext by calling from_dict on the json representation
        snapshot_list_next_model = SnapshotListNext.from_dict(snapshot_list_next_model_json)
        assert snapshot_list_next_model != False

        # Construct a model instance of SnapshotListNext by calling from_dict on the json representation
        snapshot_list_next_model_dict = SnapshotListNext.from_dict(snapshot_list_next_model_json).__dict__
        snapshot_list_next_model2 = SnapshotListNext(**snapshot_list_next_model_dict)

        # Verify the model instances are equivalent
        assert snapshot_list_next_model == snapshot_list_next_model2

        # Convert model instance back to dict and verify no loss of data
        snapshot_list_next_model_json2 = snapshot_list_next_model.to_dict()
        assert snapshot_list_next_model_json2 == snapshot_list_next_model_json


class TestModel_SnapshotListSnapshotsItem:
    """
    Test Class for SnapshotListSnapshotsItem
    """

    def test_snapshot_list_snapshots_item_serialization(self):
        """
        Test serialization/deserialization for SnapshotListSnapshotsItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        snapshot_list_snapshots_item_billing_period_model = {}  # SnapshotListSnapshotsItemBillingPeriod
        snapshot_list_snapshots_item_billing_period_model['start'] = '2023-06-01T00:00:00.000Z'
        snapshot_list_snapshots_item_billing_period_model['end'] = '2023-06-30T23:59:59.999Z'

        snapshot_list_snapshots_item_report_types_item_model = {}  # SnapshotListSnapshotsItemReportTypesItem
        snapshot_list_snapshots_item_report_types_item_model['type'] = 'account_summary'
        snapshot_list_snapshots_item_report_types_item_model['version'] = '1.0'

        snapshot_list_snapshots_item_files_item_model = {}  # SnapshotListSnapshotsItemFilesItem
        snapshot_list_snapshots_item_files_item_model['report_types'] = 'account_summary'
        snapshot_list_snapshots_item_files_item_model['location'] = (
            'june/2023-06/1685577600000/2023-06-account-summary-272b9a4f73e11030d0ba037daee47a35.csv.gz'
        )
        snapshot_list_snapshots_item_files_item_model['account_id'] = 'abc'

        # Construct a json representation of a SnapshotListSnapshotsItem model
        snapshot_list_snapshots_item_model_json = {}
        snapshot_list_snapshots_item_model_json['account_id'] = 'abc'
        snapshot_list_snapshots_item_model_json['month'] = '2023-06'
        snapshot_list_snapshots_item_model_json['account_type'] = 'account'
        snapshot_list_snapshots_item_model_json['expected_processed_at'] = 1687470383610
        snapshot_list_snapshots_item_model_json['state'] = 'enabled'
        snapshot_list_snapshots_item_model_json['billing_period'] = snapshot_list_snapshots_item_billing_period_model
        snapshot_list_snapshots_item_model_json['snapshot_id'] = '1685577600000'
        snapshot_list_snapshots_item_model_json['charset'] = 'UTF-8'
        snapshot_list_snapshots_item_model_json['compression'] = 'GZIP'
        snapshot_list_snapshots_item_model_json['content_type'] = 'text/csv'
        snapshot_list_snapshots_item_model_json['bucket'] = 'bucket_name'
        snapshot_list_snapshots_item_model_json['version'] = '1.0'
        snapshot_list_snapshots_item_model_json['created_on'] = '2023-06-22T21:47:28.297Z'
        snapshot_list_snapshots_item_model_json['report_types'] = [snapshot_list_snapshots_item_report_types_item_model]
        snapshot_list_snapshots_item_model_json['files'] = [snapshot_list_snapshots_item_files_item_model]
        snapshot_list_snapshots_item_model_json['processed_at'] = 1687470448297

        # Construct a model instance of SnapshotListSnapshotsItem by calling from_dict on the json representation
        snapshot_list_snapshots_item_model = SnapshotListSnapshotsItem.from_dict(
            snapshot_list_snapshots_item_model_json
        )
        assert snapshot_list_snapshots_item_model != False

        # Construct a model instance of SnapshotListSnapshotsItem by calling from_dict on the json representation
        snapshot_list_snapshots_item_model_dict = SnapshotListSnapshotsItem.from_dict(
            snapshot_list_snapshots_item_model_json
        ).__dict__
        snapshot_list_snapshots_item_model2 = SnapshotListSnapshotsItem(**snapshot_list_snapshots_item_model_dict)

        # Verify the model instances are equivalent
        assert snapshot_list_snapshots_item_model == snapshot_list_snapshots_item_model2

        # Convert model instance back to dict and verify no loss of data
        snapshot_list_snapshots_item_model_json2 = snapshot_list_snapshots_item_model.to_dict()
        assert snapshot_list_snapshots_item_model_json2 == snapshot_list_snapshots_item_model_json


class TestModel_SnapshotListSnapshotsItemBillingPeriod:
    """
    Test Class for SnapshotListSnapshotsItemBillingPeriod
    """

    def test_snapshot_list_snapshots_item_billing_period_serialization(self):
        """
        Test serialization/deserialization for SnapshotListSnapshotsItemBillingPeriod
        """

        # Construct a json representation of a SnapshotListSnapshotsItemBillingPeriod model
        snapshot_list_snapshots_item_billing_period_model_json = {}
        snapshot_list_snapshots_item_billing_period_model_json['start'] = '2023-06-01T00:00:00.000Z'
        snapshot_list_snapshots_item_billing_period_model_json['end'] = '2023-06-30T23:59:59.999Z'

        # Construct a model instance of SnapshotListSnapshotsItemBillingPeriod by calling from_dict on the json representation
        snapshot_list_snapshots_item_billing_period_model = SnapshotListSnapshotsItemBillingPeriod.from_dict(
            snapshot_list_snapshots_item_billing_period_model_json
        )
        assert snapshot_list_snapshots_item_billing_period_model != False

        # Construct a model instance of SnapshotListSnapshotsItemBillingPeriod by calling from_dict on the json representation
        snapshot_list_snapshots_item_billing_period_model_dict = SnapshotListSnapshotsItemBillingPeriod.from_dict(
            snapshot_list_snapshots_item_billing_period_model_json
        ).__dict__
        snapshot_list_snapshots_item_billing_period_model2 = SnapshotListSnapshotsItemBillingPeriod(
            **snapshot_list_snapshots_item_billing_period_model_dict
        )

        # Verify the model instances are equivalent
        assert snapshot_list_snapshots_item_billing_period_model == snapshot_list_snapshots_item_billing_period_model2

        # Convert model instance back to dict and verify no loss of data
        snapshot_list_snapshots_item_billing_period_model_json2 = (
            snapshot_list_snapshots_item_billing_period_model.to_dict()
        )
        assert (
            snapshot_list_snapshots_item_billing_period_model_json2
            == snapshot_list_snapshots_item_billing_period_model_json
        )


class TestModel_SnapshotListSnapshotsItemFilesItem:
    """
    Test Class for SnapshotListSnapshotsItemFilesItem
    """

    def test_snapshot_list_snapshots_item_files_item_serialization(self):
        """
        Test serialization/deserialization for SnapshotListSnapshotsItemFilesItem
        """

        # Construct a json representation of a SnapshotListSnapshotsItemFilesItem model
        snapshot_list_snapshots_item_files_item_model_json = {}
        snapshot_list_snapshots_item_files_item_model_json['report_types'] = 'account_summary'
        snapshot_list_snapshots_item_files_item_model_json['location'] = (
            'june/2023-06/1685577600000/2023-06-account-summary-272b9a4f73e11030d0ba037daee47a35.csv.gz'
        )
        snapshot_list_snapshots_item_files_item_model_json['account_id'] = 'abc'

        # Construct a model instance of SnapshotListSnapshotsItemFilesItem by calling from_dict on the json representation
        snapshot_list_snapshots_item_files_item_model = SnapshotListSnapshotsItemFilesItem.from_dict(
            snapshot_list_snapshots_item_files_item_model_json
        )
        assert snapshot_list_snapshots_item_files_item_model != False

        # Construct a model instance of SnapshotListSnapshotsItemFilesItem by calling from_dict on the json representation
        snapshot_list_snapshots_item_files_item_model_dict = SnapshotListSnapshotsItemFilesItem.from_dict(
            snapshot_list_snapshots_item_files_item_model_json
        ).__dict__
        snapshot_list_snapshots_item_files_item_model2 = SnapshotListSnapshotsItemFilesItem(
            **snapshot_list_snapshots_item_files_item_model_dict
        )

        # Verify the model instances are equivalent
        assert snapshot_list_snapshots_item_files_item_model == snapshot_list_snapshots_item_files_item_model2

        # Convert model instance back to dict and verify no loss of data
        snapshot_list_snapshots_item_files_item_model_json2 = snapshot_list_snapshots_item_files_item_model.to_dict()
        assert snapshot_list_snapshots_item_files_item_model_json2 == snapshot_list_snapshots_item_files_item_model_json


class TestModel_SnapshotListSnapshotsItemReportTypesItem:
    """
    Test Class for SnapshotListSnapshotsItemReportTypesItem
    """

    def test_snapshot_list_snapshots_item_report_types_item_serialization(self):
        """
        Test serialization/deserialization for SnapshotListSnapshotsItemReportTypesItem
        """

        # Construct a json representation of a SnapshotListSnapshotsItemReportTypesItem model
        snapshot_list_snapshots_item_report_types_item_model_json = {}
        snapshot_list_snapshots_item_report_types_item_model_json['type'] = 'account_summary'
        snapshot_list_snapshots_item_report_types_item_model_json['version'] = '1.0'

        # Construct a model instance of SnapshotListSnapshotsItemReportTypesItem by calling from_dict on the json representation
        snapshot_list_snapshots_item_report_types_item_model = SnapshotListSnapshotsItemReportTypesItem.from_dict(
            snapshot_list_snapshots_item_report_types_item_model_json
        )
        assert snapshot_list_snapshots_item_report_types_item_model != False

        # Construct a model instance of SnapshotListSnapshotsItemReportTypesItem by calling from_dict on the json representation
        snapshot_list_snapshots_item_report_types_item_model_dict = SnapshotListSnapshotsItemReportTypesItem.from_dict(
            snapshot_list_snapshots_item_report_types_item_model_json
        ).__dict__
        snapshot_list_snapshots_item_report_types_item_model2 = SnapshotListSnapshotsItemReportTypesItem(
            **snapshot_list_snapshots_item_report_types_item_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            snapshot_list_snapshots_item_report_types_item_model
            == snapshot_list_snapshots_item_report_types_item_model2
        )

        # Convert model instance back to dict and verify no loss of data
        snapshot_list_snapshots_item_report_types_item_model_json2 = (
            snapshot_list_snapshots_item_report_types_item_model.to_dict()
        )
        assert (
            snapshot_list_snapshots_item_report_types_item_model_json2
            == snapshot_list_snapshots_item_report_types_item_model_json
        )


class TestModel_SnapshotConfig:
    """
    Test Class for SnapshotConfig
    """

    def test_snapshot_config_serialization(self):
        """
        Test serialization/deserialization for SnapshotConfig
        """

        # Construct dict forms of any model objects needed in order to build this model.

        snapshot_config_history_item_model = {}  # SnapshotConfigHistoryItem
        snapshot_config_history_item_model['start_time'] = 1687469854342
        snapshot_config_history_item_model['end_time'] = 1687469989326
        snapshot_config_history_item_model['updated_by'] = 'IBMid-506PR16K14'
        snapshot_config_history_item_model['account_id'] = 'abc'
        snapshot_config_history_item_model['state'] = 'enabled'
        snapshot_config_history_item_model['account_type'] = 'account'
        snapshot_config_history_item_model['interval'] = 'daily'
        snapshot_config_history_item_model['versioning'] = 'new'
        snapshot_config_history_item_model['report_types'] = [
            'account_summary',
            'enterprise_summary',
            'account_resource_instance_usage',
        ]
        snapshot_config_history_item_model['compression'] = 'GZIP'
        snapshot_config_history_item_model['content_type'] = 'text/csv'
        snapshot_config_history_item_model['cos_reports_folder'] = 'IBMCloud-Billing-Reports'
        snapshot_config_history_item_model['cos_bucket'] = 'bucket_name'
        snapshot_config_history_item_model['cos_location'] = 'us-south'
        snapshot_config_history_item_model['cos_endpoint'] = (
            'https://s3.us-west.cloud-object-storage.test.appdomain.cloud'
        )

        # Construct a json representation of a SnapshotConfig model
        snapshot_config_model_json = {}
        snapshot_config_model_json['account_id'] = 'abc'
        snapshot_config_model_json['state'] = 'enabled'
        snapshot_config_model_json['account_type'] = 'account'
        snapshot_config_model_json['interval'] = 'daily'
        snapshot_config_model_json['versioning'] = 'new'
        snapshot_config_model_json['report_types'] = [
            'account_summary',
            'enterprise_summary',
            'account_resource_instance_usage',
        ]
        snapshot_config_model_json['compression'] = 'GZIP'
        snapshot_config_model_json['content_type'] = 'text/csv'
        snapshot_config_model_json['cos_reports_folder'] = 'IBMCloud-Billing-Reports'
        snapshot_config_model_json['cos_bucket'] = 'bucket_name'
        snapshot_config_model_json['cos_location'] = 'us-south'
        snapshot_config_model_json['cos_endpoint'] = 'https://s3.us-west.cloud-object-storage.test.appdomain.cloud'
        snapshot_config_model_json['created_at'] = 1687469854342
        snapshot_config_model_json['last_updated_at'] = 1687469989326
        snapshot_config_model_json['history'] = [snapshot_config_history_item_model]

        # Construct a model instance of SnapshotConfig by calling from_dict on the json representation
        snapshot_config_model = SnapshotConfig.from_dict(snapshot_config_model_json)
        assert snapshot_config_model != False

        # Construct a model instance of SnapshotConfig by calling from_dict on the json representation
        snapshot_config_model_dict = SnapshotConfig.from_dict(snapshot_config_model_json).__dict__
        snapshot_config_model2 = SnapshotConfig(**snapshot_config_model_dict)

        # Verify the model instances are equivalent
        assert snapshot_config_model == snapshot_config_model2

        # Convert model instance back to dict and verify no loss of data
        snapshot_config_model_json2 = snapshot_config_model.to_dict()
        assert snapshot_config_model_json2 == snapshot_config_model_json


class TestModel_SnapshotConfigValidateResponse:
    """
    Test Class for SnapshotConfigValidateResponse
    """

    def test_snapshot_config_validate_response_serialization(self):
        """
        Test serialization/deserialization for SnapshotConfigValidateResponse
        """

        # Construct a json representation of a SnapshotConfigValidateResponse model
        snapshot_config_validate_response_model_json = {}
        snapshot_config_validate_response_model_json['account_id'] = 'abc'
        snapshot_config_validate_response_model_json['cos_bucket'] = 'bucket_name'
        snapshot_config_validate_response_model_json['cos_location'] = 'us-south'

        # Construct a model instance of SnapshotConfigValidateResponse by calling from_dict on the json representation
        snapshot_config_validate_response_model = SnapshotConfigValidateResponse.from_dict(
            snapshot_config_validate_response_model_json
        )
        assert snapshot_config_validate_response_model != False

        # Construct a model instance of SnapshotConfigValidateResponse by calling from_dict on the json representation
        snapshot_config_validate_response_model_dict = SnapshotConfigValidateResponse.from_dict(
            snapshot_config_validate_response_model_json
        ).__dict__
        snapshot_config_validate_response_model2 = SnapshotConfigValidateResponse(
            **snapshot_config_validate_response_model_dict
        )

        # Verify the model instances are equivalent
        assert snapshot_config_validate_response_model == snapshot_config_validate_response_model2

        # Convert model instance back to dict and verify no loss of data
        snapshot_config_validate_response_model_json2 = snapshot_config_validate_response_model.to_dict()
        assert snapshot_config_validate_response_model_json2 == snapshot_config_validate_response_model_json


class TestModel_Subscription:
    """
    Test Class for Subscription
    """

    def test_subscription_serialization(self):
        """
        Test serialization/deserialization for Subscription
        """

        # Construct dict forms of any model objects needed in order to build this model.

        subscription_term_credits_model = {}  # SubscriptionTermCredits
        subscription_term_credits_model['total'] = 72.5
        subscription_term_credits_model['starting_balance'] = 72.5
        subscription_term_credits_model['used'] = 72.5
        subscription_term_credits_model['balance'] = 72.5

        subscription_term_model = {}  # SubscriptionTerm
        subscription_term_model['start'] = '2019-01-01T12:00:00Z'
        subscription_term_model['end'] = '2019-01-01T12:00:00Z'
        subscription_term_model['credits'] = subscription_term_credits_model

        # Construct a json representation of a Subscription model
        subscription_model_json = {}
        subscription_model_json['subscription_id'] = 'testString'
        subscription_model_json['charge_agreement_number'] = 'testString'
        subscription_model_json['type'] = 'testString'
        subscription_model_json['subscription_amount'] = 72.5
        subscription_model_json['start'] = '2019-01-01T12:00:00Z'
        subscription_model_json['end'] = '2019-01-01T12:00:00Z'
        subscription_model_json['credits_total'] = 72.5
        subscription_model_json['terms'] = [subscription_term_model]

        # Construct a model instance of Subscription by calling from_dict on the json representation
        subscription_model = Subscription.from_dict(subscription_model_json)
        assert subscription_model != False

        # Construct a model instance of Subscription by calling from_dict on the json representation
        subscription_model_dict = Subscription.from_dict(subscription_model_json).__dict__
        subscription_model2 = Subscription(**subscription_model_dict)

        # Verify the model instances are equivalent
        assert subscription_model == subscription_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_model_json2 = subscription_model.to_dict()
        assert subscription_model_json2 == subscription_model_json


class TestModel_SubscriptionSummary:
    """
    Test Class for SubscriptionSummary
    """

    def test_subscription_summary_serialization(self):
        """
        Test serialization/deserialization for SubscriptionSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        subscription_term_credits_model = {}  # SubscriptionTermCredits
        subscription_term_credits_model['total'] = 72.5
        subscription_term_credits_model['starting_balance'] = 72.5
        subscription_term_credits_model['used'] = 72.5
        subscription_term_credits_model['balance'] = 72.5

        subscription_term_model = {}  # SubscriptionTerm
        subscription_term_model['start'] = '2019-01-01T12:00:00Z'
        subscription_term_model['end'] = '2019-01-01T12:00:00Z'
        subscription_term_model['credits'] = subscription_term_credits_model

        subscription_model = {}  # Subscription
        subscription_model['subscription_id'] = 'testString'
        subscription_model['charge_agreement_number'] = 'testString'
        subscription_model['type'] = 'testString'
        subscription_model['subscription_amount'] = 72.5
        subscription_model['start'] = '2019-01-01T12:00:00Z'
        subscription_model['end'] = '2019-01-01T12:00:00Z'
        subscription_model['credits_total'] = 72.5
        subscription_model['terms'] = [subscription_term_model]

        # Construct a json representation of a SubscriptionSummary model
        subscription_summary_model_json = {}
        subscription_summary_model_json['overage'] = 72.5
        subscription_summary_model_json['subscriptions'] = [subscription_model]

        # Construct a model instance of SubscriptionSummary by calling from_dict on the json representation
        subscription_summary_model = SubscriptionSummary.from_dict(subscription_summary_model_json)
        assert subscription_summary_model != False

        # Construct a model instance of SubscriptionSummary by calling from_dict on the json representation
        subscription_summary_model_dict = SubscriptionSummary.from_dict(subscription_summary_model_json).__dict__
        subscription_summary_model2 = SubscriptionSummary(**subscription_summary_model_dict)

        # Verify the model instances are equivalent
        assert subscription_summary_model == subscription_summary_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_summary_model_json2 = subscription_summary_model.to_dict()
        assert subscription_summary_model_json2 == subscription_summary_model_json


class TestModel_SubscriptionTerm:
    """
    Test Class for SubscriptionTerm
    """

    def test_subscription_term_serialization(self):
        """
        Test serialization/deserialization for SubscriptionTerm
        """

        # Construct dict forms of any model objects needed in order to build this model.

        subscription_term_credits_model = {}  # SubscriptionTermCredits
        subscription_term_credits_model['total'] = 72.5
        subscription_term_credits_model['starting_balance'] = 72.5
        subscription_term_credits_model['used'] = 72.5
        subscription_term_credits_model['balance'] = 72.5

        # Construct a json representation of a SubscriptionTerm model
        subscription_term_model_json = {}
        subscription_term_model_json['start'] = '2019-01-01T12:00:00Z'
        subscription_term_model_json['end'] = '2019-01-01T12:00:00Z'
        subscription_term_model_json['credits'] = subscription_term_credits_model

        # Construct a model instance of SubscriptionTerm by calling from_dict on the json representation
        subscription_term_model = SubscriptionTerm.from_dict(subscription_term_model_json)
        assert subscription_term_model != False

        # Construct a model instance of SubscriptionTerm by calling from_dict on the json representation
        subscription_term_model_dict = SubscriptionTerm.from_dict(subscription_term_model_json).__dict__
        subscription_term_model2 = SubscriptionTerm(**subscription_term_model_dict)

        # Verify the model instances are equivalent
        assert subscription_term_model == subscription_term_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_term_model_json2 = subscription_term_model.to_dict()
        assert subscription_term_model_json2 == subscription_term_model_json


class TestModel_SubscriptionTermCredits:
    """
    Test Class for SubscriptionTermCredits
    """

    def test_subscription_term_credits_serialization(self):
        """
        Test serialization/deserialization for SubscriptionTermCredits
        """

        # Construct a json representation of a SubscriptionTermCredits model
        subscription_term_credits_model_json = {}
        subscription_term_credits_model_json['total'] = 72.5
        subscription_term_credits_model_json['starting_balance'] = 72.5
        subscription_term_credits_model_json['used'] = 72.5
        subscription_term_credits_model_json['balance'] = 72.5

        # Construct a model instance of SubscriptionTermCredits by calling from_dict on the json representation
        subscription_term_credits_model = SubscriptionTermCredits.from_dict(subscription_term_credits_model_json)
        assert subscription_term_credits_model != False

        # Construct a model instance of SubscriptionTermCredits by calling from_dict on the json representation
        subscription_term_credits_model_dict = SubscriptionTermCredits.from_dict(
            subscription_term_credits_model_json
        ).__dict__
        subscription_term_credits_model2 = SubscriptionTermCredits(**subscription_term_credits_model_dict)

        # Verify the model instances are equivalent
        assert subscription_term_credits_model == subscription_term_credits_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_term_credits_model_json2 = subscription_term_credits_model.to_dict()
        assert subscription_term_credits_model_json2 == subscription_term_credits_model_json


class TestModel_SupportSummary:
    """
    Test Class for SupportSummary
    """

    def test_support_summary_serialization(self):
        """
        Test serialization/deserialization for SupportSummary
        """

        # Construct a json representation of a SupportSummary model
        support_summary_model_json = {}
        support_summary_model_json['cost'] = 72.5
        support_summary_model_json['type'] = 'testString'
        support_summary_model_json['overage'] = 72.5

        # Construct a model instance of SupportSummary by calling from_dict on the json representation
        support_summary_model = SupportSummary.from_dict(support_summary_model_json)
        assert support_summary_model != False

        # Construct a model instance of SupportSummary by calling from_dict on the json representation
        support_summary_model_dict = SupportSummary.from_dict(support_summary_model_json).__dict__
        support_summary_model2 = SupportSummary(**support_summary_model_dict)

        # Verify the model instances are equivalent
        assert support_summary_model == support_summary_model2

        # Convert model instance back to dict and verify no loss of data
        support_summary_model_json2 = support_summary_model.to_dict()
        assert support_summary_model_json2 == support_summary_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
