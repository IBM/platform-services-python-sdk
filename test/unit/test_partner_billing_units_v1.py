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
Unit Tests for PartnerBillingUnitsV1
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
from ibm_platform_services.partner_billing_units_v1 import *


_service = PartnerBillingUnitsV1(authenticator=NoAuthAuthenticator())

_base_url = 'https://partner.cloud.ibm.com'
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
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    else:
        return re.compile(request_url.rstrip('/') + '/+')


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

        service = PartnerBillingUnitsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, PartnerBillingUnitsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = PartnerBillingUnitsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetBillingOptions:
    """
    Test Class for get_billing_options
    """

    @responses.activate
    def test_get_billing_options_all_params(self):
        """
        get_billing_options()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-options')
        mock_response = '{"limit": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"id": "CFL_JJKLVZ2I0JE-_MGU", "billing_unit_id": "e19fa97c9bb34963a31a2008044d8b59", "customer_id": "<ford_account_id>", "customer_type": "ACCOUNT", "customer_name": "Ford", "reseller_id": "<techdata_enterprise_id>", "reseller_name": "TechData", "month": "2022-04", "errors": [{"anyKey": "anyValue"}], "type": "SUBSCRIPTION", "start_date": "2019-05-01T00:00:00.000Z", "end_date": "2020-05-01T00:00:00.000Z", "state": "ACTIVE", "category": "PLATFORM", "payment_instrument": {"anyKey": "anyValue"}, "part_number": "<PART_NUMBER_1>", "catalog_id": "ibmcloud-platform-payg-commit", "order_id": "23wzpnpmh8", "po_number": "<PO_NUMBER_1>", "subscription_model": "4.0", "duration_in_months": 11, "monthly_amount": 8333.333333333334, "billing_system": {"anyKey": "anyValue"}, "country_code": "USA", "currency_code": "USD"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        partner_id = 'testString'
        customer_id = 'testString'
        reseller_id = 'testString'
        date = '2022-04'
        limit = 30

        # Invoke method
        response = _service.get_billing_options(
            partner_id,
            customer_id=customer_id,
            reseller_id=reseller_id,
            date=date,
            limit=limit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'partner_id={}'.format(partner_id) in query_string
        assert 'customer_id={}'.format(customer_id) in query_string
        assert 'reseller_id={}'.format(reseller_id) in query_string
        assert 'date={}'.format(date) in query_string
        assert '_limit={}'.format(limit) in query_string

    def test_get_billing_options_all_params_with_retries(self):
        # Enable retries and run test_get_billing_options_all_params.
        _service.enable_retries()
        self.test_get_billing_options_all_params()

        # Disable retries and run test_get_billing_options_all_params.
        _service.disable_retries()
        self.test_get_billing_options_all_params()

    @responses.activate
    def test_get_billing_options_required_params(self):
        """
        test_get_billing_options_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-options')
        mock_response = '{"limit": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"id": "CFL_JJKLVZ2I0JE-_MGU", "billing_unit_id": "e19fa97c9bb34963a31a2008044d8b59", "customer_id": "<ford_account_id>", "customer_type": "ACCOUNT", "customer_name": "Ford", "reseller_id": "<techdata_enterprise_id>", "reseller_name": "TechData", "month": "2022-04", "errors": [{"anyKey": "anyValue"}], "type": "SUBSCRIPTION", "start_date": "2019-05-01T00:00:00.000Z", "end_date": "2020-05-01T00:00:00.000Z", "state": "ACTIVE", "category": "PLATFORM", "payment_instrument": {"anyKey": "anyValue"}, "part_number": "<PART_NUMBER_1>", "catalog_id": "ibmcloud-platform-payg-commit", "order_id": "23wzpnpmh8", "po_number": "<PO_NUMBER_1>", "subscription_model": "4.0", "duration_in_months": 11, "monthly_amount": 8333.333333333334, "billing_system": {"anyKey": "anyValue"}, "country_code": "USA", "currency_code": "USD"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        partner_id = 'testString'

        # Invoke method
        response = _service.get_billing_options(
            partner_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'partner_id={}'.format(partner_id) in query_string

    def test_get_billing_options_required_params_with_retries(self):
        # Enable retries and run test_get_billing_options_required_params.
        _service.enable_retries()
        self.test_get_billing_options_required_params()

        # Disable retries and run test_get_billing_options_required_params.
        _service.disable_retries()
        self.test_get_billing_options_required_params()

    @responses.activate
    def test_get_billing_options_value_error(self):
        """
        test_get_billing_options_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/billing-options')
        mock_response = '{"limit": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"id": "CFL_JJKLVZ2I0JE-_MGU", "billing_unit_id": "e19fa97c9bb34963a31a2008044d8b59", "customer_id": "<ford_account_id>", "customer_type": "ACCOUNT", "customer_name": "Ford", "reseller_id": "<techdata_enterprise_id>", "reseller_name": "TechData", "month": "2022-04", "errors": [{"anyKey": "anyValue"}], "type": "SUBSCRIPTION", "start_date": "2019-05-01T00:00:00.000Z", "end_date": "2020-05-01T00:00:00.000Z", "state": "ACTIVE", "category": "PLATFORM", "payment_instrument": {"anyKey": "anyValue"}, "part_number": "<PART_NUMBER_1>", "catalog_id": "ibmcloud-platform-payg-commit", "order_id": "23wzpnpmh8", "po_number": "<PO_NUMBER_1>", "subscription_model": "4.0", "duration_in_months": 11, "monthly_amount": 8333.333333333334, "billing_system": {"anyKey": "anyValue"}, "country_code": "USA", "currency_code": "USD"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        partner_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "partner_id": partner_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_billing_options(**req_copy)

    def test_get_billing_options_value_error_with_retries(self):
        # Enable retries and run test_get_billing_options_value_error.
        _service.enable_retries()
        self.test_get_billing_options_value_error()

        # Disable retries and run test_get_billing_options_value_error.
        _service.disable_retries()
        self.test_get_billing_options_value_error()


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

        service = PartnerBillingUnitsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, PartnerBillingUnitsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = PartnerBillingUnitsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetCreditPoolsReport:
    """
    Test Class for get_credit_pools_report
    """

    @responses.activate
    def test_get_credit_pools_report_all_params(self):
        """
        get_credit_pools_report()
        """
        # Set up mock
        url = preprocess_url('/v1/credit-pools')
        mock_response = '{"limit": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"type": "PLATFORM", "billing_unit_id": "e19fa97c9bb34963a31a2008044d8b59", "customer_id": "<ford_account_id>", "customer_type": "ACCOUNT", "customer_name": "Ford", "reseller_id": "<techdata_enterprise_id>", "reseller_name": "TechData", "month": "2022-04", "currency_code": "USD", "term_credits": [{"billing_option_id": "JWX986YRGFSHACQUEFOI", "billing_option_model": "4.0", "category": "PLATFORM", "start_date": "2019-07-01T00:00:00.000Z", "end_date": "2019-08-31T23:59:59.999Z", "total_credits": 100000, "starting_balance": 100000, "used_credits": 0, "current_balance": 100000, "resources": [{"anyKey": "anyValue"}]}], "overage": {"cost": 500, "resources": [{"anyKey": "anyValue"}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        partner_id = 'testString'
        customer_id = 'testString'
        reseller_id = 'testString'
        date = '2022-04'
        limit = 30

        # Invoke method
        response = _service.get_credit_pools_report(
            partner_id,
            customer_id=customer_id,
            reseller_id=reseller_id,
            date=date,
            limit=limit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'partner_id={}'.format(partner_id) in query_string
        assert 'customer_id={}'.format(customer_id) in query_string
        assert 'reseller_id={}'.format(reseller_id) in query_string
        assert 'date={}'.format(date) in query_string
        assert '_limit={}'.format(limit) in query_string

    def test_get_credit_pools_report_all_params_with_retries(self):
        # Enable retries and run test_get_credit_pools_report_all_params.
        _service.enable_retries()
        self.test_get_credit_pools_report_all_params()

        # Disable retries and run test_get_credit_pools_report_all_params.
        _service.disable_retries()
        self.test_get_credit_pools_report_all_params()

    @responses.activate
    def test_get_credit_pools_report_required_params(self):
        """
        test_get_credit_pools_report_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/credit-pools')
        mock_response = '{"limit": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"type": "PLATFORM", "billing_unit_id": "e19fa97c9bb34963a31a2008044d8b59", "customer_id": "<ford_account_id>", "customer_type": "ACCOUNT", "customer_name": "Ford", "reseller_id": "<techdata_enterprise_id>", "reseller_name": "TechData", "month": "2022-04", "currency_code": "USD", "term_credits": [{"billing_option_id": "JWX986YRGFSHACQUEFOI", "billing_option_model": "4.0", "category": "PLATFORM", "start_date": "2019-07-01T00:00:00.000Z", "end_date": "2019-08-31T23:59:59.999Z", "total_credits": 100000, "starting_balance": 100000, "used_credits": 0, "current_balance": 100000, "resources": [{"anyKey": "anyValue"}]}], "overage": {"cost": 500, "resources": [{"anyKey": "anyValue"}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        partner_id = 'testString'

        # Invoke method
        response = _service.get_credit_pools_report(
            partner_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'partner_id={}'.format(partner_id) in query_string

    def test_get_credit_pools_report_required_params_with_retries(self):
        # Enable retries and run test_get_credit_pools_report_required_params.
        _service.enable_retries()
        self.test_get_credit_pools_report_required_params()

        # Disable retries and run test_get_credit_pools_report_required_params.
        _service.disable_retries()
        self.test_get_credit_pools_report_required_params()

    @responses.activate
    def test_get_credit_pools_report_value_error(self):
        """
        test_get_credit_pools_report_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/credit-pools')
        mock_response = '{"limit": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "resources": [{"type": "PLATFORM", "billing_unit_id": "e19fa97c9bb34963a31a2008044d8b59", "customer_id": "<ford_account_id>", "customer_type": "ACCOUNT", "customer_name": "Ford", "reseller_id": "<techdata_enterprise_id>", "reseller_name": "TechData", "month": "2022-04", "currency_code": "USD", "term_credits": [{"billing_option_id": "JWX986YRGFSHACQUEFOI", "billing_option_model": "4.0", "category": "PLATFORM", "start_date": "2019-07-01T00:00:00.000Z", "end_date": "2019-08-31T23:59:59.999Z", "total_credits": 100000, "starting_balance": 100000, "used_credits": 0, "current_balance": 100000, "resources": [{"anyKey": "anyValue"}]}], "overage": {"cost": 500, "resources": [{"anyKey": "anyValue"}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        partner_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "partner_id": partner_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_credit_pools_report(**req_copy)

    def test_get_credit_pools_report_value_error_with_retries(self):
        # Enable retries and run test_get_credit_pools_report_value_error.
        _service.enable_retries()
        self.test_get_credit_pools_report_value_error()

        # Disable retries and run test_get_credit_pools_report_value_error.
        _service.disable_retries()
        self.test_get_credit_pools_report_value_error()


# endregion
##############################################################################
# End of Service: CreditPools
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_BillingOptionsSummaryFirst:
    """
    Test Class for BillingOptionsSummaryFirst
    """

    def test_billing_options_summary_first_serialization(self):
        """
        Test serialization/deserialization for BillingOptionsSummaryFirst
        """

        # Construct a json representation of a BillingOptionsSummaryFirst model
        billing_options_summary_first_model_json = {}
        billing_options_summary_first_model_json['href'] = 'testString'

        # Construct a model instance of BillingOptionsSummaryFirst by calling from_dict on the json representation
        billing_options_summary_first_model = BillingOptionsSummaryFirst.from_dict(
            billing_options_summary_first_model_json
        )
        assert billing_options_summary_first_model != False

        # Construct a model instance of BillingOptionsSummaryFirst by calling from_dict on the json representation
        billing_options_summary_first_model_dict = BillingOptionsSummaryFirst.from_dict(
            billing_options_summary_first_model_json
        ).__dict__
        billing_options_summary_first_model2 = BillingOptionsSummaryFirst(**billing_options_summary_first_model_dict)

        # Verify the model instances are equivalent
        assert billing_options_summary_first_model == billing_options_summary_first_model2

        # Convert model instance back to dict and verify no loss of data
        billing_options_summary_first_model_json2 = billing_options_summary_first_model.to_dict()
        assert billing_options_summary_first_model_json2 == billing_options_summary_first_model_json


class TestModel_BillingOptionsSummaryNext:
    """
    Test Class for BillingOptionsSummaryNext
    """

    def test_billing_options_summary_next_serialization(self):
        """
        Test serialization/deserialization for BillingOptionsSummaryNext
        """

        # Construct a json representation of a BillingOptionsSummaryNext model
        billing_options_summary_next_model_json = {}
        billing_options_summary_next_model_json['href'] = 'testString'
        billing_options_summary_next_model_json['offset'] = 'testString'

        # Construct a model instance of BillingOptionsSummaryNext by calling from_dict on the json representation
        billing_options_summary_next_model = BillingOptionsSummaryNext.from_dict(
            billing_options_summary_next_model_json
        )
        assert billing_options_summary_next_model != False

        # Construct a model instance of BillingOptionsSummaryNext by calling from_dict on the json representation
        billing_options_summary_next_model_dict = BillingOptionsSummaryNext.from_dict(
            billing_options_summary_next_model_json
        ).__dict__
        billing_options_summary_next_model2 = BillingOptionsSummaryNext(**billing_options_summary_next_model_dict)

        # Verify the model instances are equivalent
        assert billing_options_summary_next_model == billing_options_summary_next_model2

        # Convert model instance back to dict and verify no loss of data
        billing_options_summary_next_model_json2 = billing_options_summary_next_model.to_dict()
        assert billing_options_summary_next_model_json2 == billing_options_summary_next_model_json


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
        billing_option_model_json['id'] = 'CFL_JJKLVZ2I0JE-_MGU'
        billing_option_model_json['billing_unit_id'] = 'e19fa97c9bb34963a31a2008044d8b59'
        billing_option_model_json['customer_id'] = '<ford_account_id>'
        billing_option_model_json['customer_type'] = 'ACCOUNT'
        billing_option_model_json['customer_name'] = 'Ford'
        billing_option_model_json['reseller_id'] = '<techdata_enterprise_id>'
        billing_option_model_json['reseller_name'] = 'TechData'
        billing_option_model_json['month'] = '2022-04'
        billing_option_model_json['errors'] = [{'anyKey': 'anyValue'}]
        billing_option_model_json['type'] = 'SUBSCRIPTION'
        billing_option_model_json['start_date'] = '2019-05-01T00:00:00Z'
        billing_option_model_json['end_date'] = '2020-05-01T00:00:00Z'
        billing_option_model_json['state'] = 'ACTIVE'
        billing_option_model_json['category'] = 'PLATFORM'
        billing_option_model_json['payment_instrument'] = {'anyKey': 'anyValue'}
        billing_option_model_json['part_number'] = '<PART_NUMBER_1>'
        billing_option_model_json['catalog_id'] = 'ibmcloud-platform-payg-commit'
        billing_option_model_json['order_id'] = '23wzpnpmh8'
        billing_option_model_json['po_number'] = '<PO_NUMBER_1>'
        billing_option_model_json['subscription_model'] = '4.0'
        billing_option_model_json['duration_in_months'] = 11
        billing_option_model_json['monthly_amount'] = 8333.333333333334
        billing_option_model_json['billing_system'] = {'anyKey': 'anyValue'}
        billing_option_model_json['country_code'] = 'USA'
        billing_option_model_json['currency_code'] = 'USD'

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


class TestModel_BillingOptionsSummary:
    """
    Test Class for BillingOptionsSummary
    """

    def test_billing_options_summary_serialization(self):
        """
        Test serialization/deserialization for BillingOptionsSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        billing_options_summary_first_model = {}  # BillingOptionsSummaryFirst
        billing_options_summary_first_model['href'] = 'testString'

        billing_options_summary_next_model = {}  # BillingOptionsSummaryNext
        billing_options_summary_next_model['href'] = 'testString'
        billing_options_summary_next_model['offset'] = 'testString'

        billing_option_model = {}  # BillingOption
        billing_option_model['id'] = 'CFL_JJKLVZ2I0JE-_MGU'
        billing_option_model['billing_unit_id'] = 'e19fa97c9bb34963a31a2008044d8b59'
        billing_option_model['customer_id'] = '<ford_account_id>'
        billing_option_model['customer_type'] = 'ACCOUNT'
        billing_option_model['customer_name'] = 'Ford'
        billing_option_model['reseller_id'] = '<techdata_enterprise_id>'
        billing_option_model['reseller_name'] = 'TechData'
        billing_option_model['month'] = '2022-04'
        billing_option_model['errors'] = [{'anyKey': 'anyValue'}]
        billing_option_model['type'] = 'SUBSCRIPTION'
        billing_option_model['start_date'] = '2019-05-01T00:00:00Z'
        billing_option_model['end_date'] = '2020-05-01T00:00:00Z'
        billing_option_model['state'] = 'ACTIVE'
        billing_option_model['category'] = 'PLATFORM'
        billing_option_model['payment_instrument'] = {'anyKey': 'anyValue'}
        billing_option_model['part_number'] = '<PART_NUMBER_1>'
        billing_option_model['catalog_id'] = 'ibmcloud-platform-payg-commit'
        billing_option_model['order_id'] = '23wzpnpmh8'
        billing_option_model['po_number'] = '<PO_NUMBER_1>'
        billing_option_model['subscription_model'] = '4.0'
        billing_option_model['duration_in_months'] = 11
        billing_option_model['monthly_amount'] = 8333.333333333334
        billing_option_model['billing_system'] = {'anyKey': 'anyValue'}
        billing_option_model['country_code'] = 'USA'
        billing_option_model['currency_code'] = 'USD'

        # Construct a json representation of a BillingOptionsSummary model
        billing_options_summary_model_json = {}
        billing_options_summary_model_json['limit'] = 38
        billing_options_summary_model_json['first'] = billing_options_summary_first_model
        billing_options_summary_model_json['next'] = billing_options_summary_next_model
        billing_options_summary_model_json['resources'] = [billing_option_model]

        # Construct a model instance of BillingOptionsSummary by calling from_dict on the json representation
        billing_options_summary_model = BillingOptionsSummary.from_dict(billing_options_summary_model_json)
        assert billing_options_summary_model != False

        # Construct a model instance of BillingOptionsSummary by calling from_dict on the json representation
        billing_options_summary_model_dict = BillingOptionsSummary.from_dict(
            billing_options_summary_model_json
        ).__dict__
        billing_options_summary_model2 = BillingOptionsSummary(**billing_options_summary_model_dict)

        # Verify the model instances are equivalent
        assert billing_options_summary_model == billing_options_summary_model2

        # Convert model instance back to dict and verify no loss of data
        billing_options_summary_model_json2 = billing_options_summary_model.to_dict()
        assert billing_options_summary_model_json2 == billing_options_summary_model_json


class TestModel_CreditPoolsReportSummaryFirst:
    """
    Test Class for CreditPoolsReportSummaryFirst
    """

    def test_credit_pools_report_summary_first_serialization(self):
        """
        Test serialization/deserialization for CreditPoolsReportSummaryFirst
        """

        # Construct a json representation of a CreditPoolsReportSummaryFirst model
        credit_pools_report_summary_first_model_json = {}
        credit_pools_report_summary_first_model_json['href'] = 'testString'

        # Construct a model instance of CreditPoolsReportSummaryFirst by calling from_dict on the json representation
        credit_pools_report_summary_first_model = CreditPoolsReportSummaryFirst.from_dict(
            credit_pools_report_summary_first_model_json
        )
        assert credit_pools_report_summary_first_model != False

        # Construct a model instance of CreditPoolsReportSummaryFirst by calling from_dict on the json representation
        credit_pools_report_summary_first_model_dict = CreditPoolsReportSummaryFirst.from_dict(
            credit_pools_report_summary_first_model_json
        ).__dict__
        credit_pools_report_summary_first_model2 = CreditPoolsReportSummaryFirst(
            **credit_pools_report_summary_first_model_dict
        )

        # Verify the model instances are equivalent
        assert credit_pools_report_summary_first_model == credit_pools_report_summary_first_model2

        # Convert model instance back to dict and verify no loss of data
        credit_pools_report_summary_first_model_json2 = credit_pools_report_summary_first_model.to_dict()
        assert credit_pools_report_summary_first_model_json2 == credit_pools_report_summary_first_model_json


class TestModel_CreditPoolsReportSummaryNext:
    """
    Test Class for CreditPoolsReportSummaryNext
    """

    def test_credit_pools_report_summary_next_serialization(self):
        """
        Test serialization/deserialization for CreditPoolsReportSummaryNext
        """

        # Construct a json representation of a CreditPoolsReportSummaryNext model
        credit_pools_report_summary_next_model_json = {}
        credit_pools_report_summary_next_model_json['href'] = 'testString'
        credit_pools_report_summary_next_model_json['offset'] = 'testString'

        # Construct a model instance of CreditPoolsReportSummaryNext by calling from_dict on the json representation
        credit_pools_report_summary_next_model = CreditPoolsReportSummaryNext.from_dict(
            credit_pools_report_summary_next_model_json
        )
        assert credit_pools_report_summary_next_model != False

        # Construct a model instance of CreditPoolsReportSummaryNext by calling from_dict on the json representation
        credit_pools_report_summary_next_model_dict = CreditPoolsReportSummaryNext.from_dict(
            credit_pools_report_summary_next_model_json
        ).__dict__
        credit_pools_report_summary_next_model2 = CreditPoolsReportSummaryNext(
            **credit_pools_report_summary_next_model_dict
        )

        # Verify the model instances are equivalent
        assert credit_pools_report_summary_next_model == credit_pools_report_summary_next_model2

        # Convert model instance back to dict and verify no loss of data
        credit_pools_report_summary_next_model_json2 = credit_pools_report_summary_next_model.to_dict()
        assert credit_pools_report_summary_next_model_json2 == credit_pools_report_summary_next_model_json


class TestModel_CreditPoolsReport:
    """
    Test Class for CreditPoolsReport
    """

    def test_credit_pools_report_serialization(self):
        """
        Test serialization/deserialization for CreditPoolsReport
        """

        # Construct dict forms of any model objects needed in order to build this model.

        term_credits_model = {}  # TermCredits
        term_credits_model['billing_option_id'] = 'JWX986YRGFSHACQUEFOI'
        term_credits_model['billing_option_model'] = '4.0'
        term_credits_model['category'] = 'PLATFORM'
        term_credits_model['start_date'] = '2019-07-01T00:00:00Z'
        term_credits_model['end_date'] = '2019-08-31T23:59:59.999000Z'
        term_credits_model['total_credits'] = 100000
        term_credits_model['starting_balance'] = 100000
        term_credits_model['used_credits'] = 0
        term_credits_model['current_balance'] = 100000
        term_credits_model['resources'] = [{'anyKey': 'anyValue'}]

        overage_model = {}  # Overage
        overage_model['cost'] = 500
        overage_model['resources'] = [{'anyKey': 'anyValue'}]

        # Construct a json representation of a CreditPoolsReport model
        credit_pools_report_model_json = {}
        credit_pools_report_model_json['type'] = 'PLATFORM'
        credit_pools_report_model_json['billing_unit_id'] = 'e19fa97c9bb34963a31a2008044d8b59'
        credit_pools_report_model_json['customer_id'] = '<ford_account_id>'
        credit_pools_report_model_json['customer_type'] = 'ACCOUNT'
        credit_pools_report_model_json['customer_name'] = 'Ford'
        credit_pools_report_model_json['reseller_id'] = '<techdata_enterprise_id>'
        credit_pools_report_model_json['reseller_name'] = 'TechData'
        credit_pools_report_model_json['month'] = '2022-04'
        credit_pools_report_model_json['currency_code'] = 'USD'
        credit_pools_report_model_json['term_credits'] = [term_credits_model]
        credit_pools_report_model_json['overage'] = overage_model

        # Construct a model instance of CreditPoolsReport by calling from_dict on the json representation
        credit_pools_report_model = CreditPoolsReport.from_dict(credit_pools_report_model_json)
        assert credit_pools_report_model != False

        # Construct a model instance of CreditPoolsReport by calling from_dict on the json representation
        credit_pools_report_model_dict = CreditPoolsReport.from_dict(credit_pools_report_model_json).__dict__
        credit_pools_report_model2 = CreditPoolsReport(**credit_pools_report_model_dict)

        # Verify the model instances are equivalent
        assert credit_pools_report_model == credit_pools_report_model2

        # Convert model instance back to dict and verify no loss of data
        credit_pools_report_model_json2 = credit_pools_report_model.to_dict()
        assert credit_pools_report_model_json2 == credit_pools_report_model_json


class TestModel_CreditPoolsReportSummary:
    """
    Test Class for CreditPoolsReportSummary
    """

    def test_credit_pools_report_summary_serialization(self):
        """
        Test serialization/deserialization for CreditPoolsReportSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        credit_pools_report_summary_first_model = {}  # CreditPoolsReportSummaryFirst
        credit_pools_report_summary_first_model['href'] = 'testString'

        credit_pools_report_summary_next_model = {}  # CreditPoolsReportSummaryNext
        credit_pools_report_summary_next_model['href'] = 'testString'
        credit_pools_report_summary_next_model['offset'] = 'testString'

        term_credits_model = {}  # TermCredits
        term_credits_model['billing_option_id'] = 'JWX986YRGFSHACQUEFOI'
        term_credits_model['billing_option_model'] = '4.0'
        term_credits_model['category'] = 'PLATFORM'
        term_credits_model['start_date'] = '2019-07-01T00:00:00Z'
        term_credits_model['end_date'] = '2019-08-31T23:59:59.999000Z'
        term_credits_model['total_credits'] = 100000
        term_credits_model['starting_balance'] = 100000
        term_credits_model['used_credits'] = 0
        term_credits_model['current_balance'] = 100000
        term_credits_model['resources'] = [{'anyKey': 'anyValue'}]

        overage_model = {}  # Overage
        overage_model['cost'] = 500
        overage_model['resources'] = [{'anyKey': 'anyValue'}]

        credit_pools_report_model = {}  # CreditPoolsReport
        credit_pools_report_model['type'] = 'PLATFORM'
        credit_pools_report_model['billing_unit_id'] = 'e19fa97c9bb34963a31a2008044d8b59'
        credit_pools_report_model['customer_id'] = '<ford_account_id>'
        credit_pools_report_model['customer_type'] = 'ACCOUNT'
        credit_pools_report_model['customer_name'] = 'Ford'
        credit_pools_report_model['reseller_id'] = '<techdata_enterprise_id>'
        credit_pools_report_model['reseller_name'] = 'TechData'
        credit_pools_report_model['month'] = '2022-04'
        credit_pools_report_model['currency_code'] = 'USD'
        credit_pools_report_model['term_credits'] = [term_credits_model]
        credit_pools_report_model['overage'] = overage_model

        # Construct a json representation of a CreditPoolsReportSummary model
        credit_pools_report_summary_model_json = {}
        credit_pools_report_summary_model_json['limit'] = 38
        credit_pools_report_summary_model_json['first'] = credit_pools_report_summary_first_model
        credit_pools_report_summary_model_json['next'] = credit_pools_report_summary_next_model
        credit_pools_report_summary_model_json['resources'] = [credit_pools_report_model]

        # Construct a model instance of CreditPoolsReportSummary by calling from_dict on the json representation
        credit_pools_report_summary_model = CreditPoolsReportSummary.from_dict(credit_pools_report_summary_model_json)
        assert credit_pools_report_summary_model != False

        # Construct a model instance of CreditPoolsReportSummary by calling from_dict on the json representation
        credit_pools_report_summary_model_dict = CreditPoolsReportSummary.from_dict(
            credit_pools_report_summary_model_json
        ).__dict__
        credit_pools_report_summary_model2 = CreditPoolsReportSummary(**credit_pools_report_summary_model_dict)

        # Verify the model instances are equivalent
        assert credit_pools_report_summary_model == credit_pools_report_summary_model2

        # Convert model instance back to dict and verify no loss of data
        credit_pools_report_summary_model_json2 = credit_pools_report_summary_model.to_dict()
        assert credit_pools_report_summary_model_json2 == credit_pools_report_summary_model_json


class TestModel_Overage:
    """
    Test Class for Overage
    """

    def test_overage_serialization(self):
        """
        Test serialization/deserialization for Overage
        """

        # Construct a json representation of a Overage model
        overage_model_json = {}
        overage_model_json['cost'] = 500
        overage_model_json['resources'] = [{'anyKey': 'anyValue'}]

        # Construct a model instance of Overage by calling from_dict on the json representation
        overage_model = Overage.from_dict(overage_model_json)
        assert overage_model != False

        # Construct a model instance of Overage by calling from_dict on the json representation
        overage_model_dict = Overage.from_dict(overage_model_json).__dict__
        overage_model2 = Overage(**overage_model_dict)

        # Verify the model instances are equivalent
        assert overage_model == overage_model2

        # Convert model instance back to dict and verify no loss of data
        overage_model_json2 = overage_model.to_dict()
        assert overage_model_json2 == overage_model_json


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
        term_credits_model_json['billing_option_model'] = '4.0'
        term_credits_model_json['category'] = 'PLATFORM'
        term_credits_model_json['start_date'] = '2019-07-01T00:00:00Z'
        term_credits_model_json['end_date'] = '2019-08-31T23:59:59.999000Z'
        term_credits_model_json['total_credits'] = 100000
        term_credits_model_json['starting_balance'] = 100000
        term_credits_model_json['used_credits'] = 0
        term_credits_model_json['current_balance'] = 100000
        term_credits_model_json['resources'] = [{'anyKey': 'anyValue'}]

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
