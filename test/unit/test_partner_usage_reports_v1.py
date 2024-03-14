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
Unit Tests for PartnerUsageReportsV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_platform_services.partner_usage_reports_v1 import *


_service = PartnerUsageReportsV1(authenticator=NoAuthAuthenticator())

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
    if not request_url.endswith('/'):
        return request_url
    return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: PartnerUsageReports
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

        service = PartnerUsageReportsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, PartnerUsageReportsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = PartnerUsageReportsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetResourceUsageReport:
    """
    Test Class for get_resource_usage_report
    """

    @responses.activate
    def test_get_resource_usage_report_all_params(self):
        """
        get_resource_usage_report()
        """
        # Set up mock
        url = preprocess_url('/v1/resource-usage-reports')
        mock_response = '{"limit": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "reports": [{"entity_id": "<distributor_enterprise_id>", "entity_type": "enterprise", "entity_crn": "crn:v1:bluemix:public:enterprise::a/fa359b76ff2c41eda727aad47b7e4063::enterprise:33a7eb04e7d547cd9489e90c99d476a5", "entity_name": "Arrow", "entity_partner_type": "DISTRIBUTOR", "viewpoint": "DISTRIBUTOR", "month": "2024-01", "currency_code": "EUR", "country_code": "FRA", "billable_cost": 2331828.33275813, "billable_rated_cost": 3817593.35186263, "non_billable_cost": 0, "non_billable_rated_cost": 0, "resources": [{"resource_id": "cloudant", "resource_name": "Cloudant", "billable_cost": 75, "billable_rated_cost": 75, "non_billable_cost": 0, "non_billable_rated_cost": 0, "plans": [{"plan_id": "cloudant-standard", "pricing_region": "Standard", "pricing_plan_id": "billable:v4:cloudant-standard::1552694400000:", "billable": true, "cost": 75, "rated_cost": 75, "usage": [{"metric": "GB_STORAGE_ACCRUED_PER_MONTH", "unit": "GIGABYTE_MONTHS", "quantity": 10, "rateable_quantity": 10, "cost": 10, "rated_cost": 10, "price": [{"anyKey": "anyValue"}]}]}]}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        partner_id = 'testString'
        reseller_id = 'testString'
        customer_id = 'testString'
        children = False
        month = '2024-01'
        viewpoint = 'DISTRIBUTOR'
        recurse = False
        limit = 30
        offset = 'testString'

        # Invoke method
        response = _service.get_resource_usage_report(
            partner_id,
            reseller_id=reseller_id,
            customer_id=customer_id,
            children=children,
            month=month,
            viewpoint=viewpoint,
            recurse=recurse,
            limit=limit,
            offset=offset,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'partner_id={}'.format(partner_id) in query_string
        assert 'reseller_id={}'.format(reseller_id) in query_string
        assert 'customer_id={}'.format(customer_id) in query_string
        assert 'children={}'.format('true' if children else 'false') in query_string
        assert 'month={}'.format(month) in query_string
        assert 'viewpoint={}'.format(viewpoint) in query_string
        assert 'recurse={}'.format('true' if recurse else 'false') in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string

    def test_get_resource_usage_report_all_params_with_retries(self):
        # Enable retries and run test_get_resource_usage_report_all_params.
        _service.enable_retries()
        self.test_get_resource_usage_report_all_params()

        # Disable retries and run test_get_resource_usage_report_all_params.
        _service.disable_retries()
        self.test_get_resource_usage_report_all_params()

    @responses.activate
    def test_get_resource_usage_report_required_params(self):
        """
        test_get_resource_usage_report_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/resource-usage-reports')
        mock_response = '{"limit": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "reports": [{"entity_id": "<distributor_enterprise_id>", "entity_type": "enterprise", "entity_crn": "crn:v1:bluemix:public:enterprise::a/fa359b76ff2c41eda727aad47b7e4063::enterprise:33a7eb04e7d547cd9489e90c99d476a5", "entity_name": "Arrow", "entity_partner_type": "DISTRIBUTOR", "viewpoint": "DISTRIBUTOR", "month": "2024-01", "currency_code": "EUR", "country_code": "FRA", "billable_cost": 2331828.33275813, "billable_rated_cost": 3817593.35186263, "non_billable_cost": 0, "non_billable_rated_cost": 0, "resources": [{"resource_id": "cloudant", "resource_name": "Cloudant", "billable_cost": 75, "billable_rated_cost": 75, "non_billable_cost": 0, "non_billable_rated_cost": 0, "plans": [{"plan_id": "cloudant-standard", "pricing_region": "Standard", "pricing_plan_id": "billable:v4:cloudant-standard::1552694400000:", "billable": true, "cost": 75, "rated_cost": 75, "usage": [{"metric": "GB_STORAGE_ACCRUED_PER_MONTH", "unit": "GIGABYTE_MONTHS", "quantity": 10, "rateable_quantity": 10, "cost": 10, "rated_cost": 10, "price": [{"anyKey": "anyValue"}]}]}]}]}]}'
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
        response = _service.get_resource_usage_report(
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

    def test_get_resource_usage_report_required_params_with_retries(self):
        # Enable retries and run test_get_resource_usage_report_required_params.
        _service.enable_retries()
        self.test_get_resource_usage_report_required_params()

        # Disable retries and run test_get_resource_usage_report_required_params.
        _service.disable_retries()
        self.test_get_resource_usage_report_required_params()

    @responses.activate
    def test_get_resource_usage_report_value_error(self):
        """
        test_get_resource_usage_report_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/resource-usage-reports')
        mock_response = '{"limit": 5, "first": {"href": "href"}, "next": {"href": "href", "offset": "offset"}, "reports": [{"entity_id": "<distributor_enterprise_id>", "entity_type": "enterprise", "entity_crn": "crn:v1:bluemix:public:enterprise::a/fa359b76ff2c41eda727aad47b7e4063::enterprise:33a7eb04e7d547cd9489e90c99d476a5", "entity_name": "Arrow", "entity_partner_type": "DISTRIBUTOR", "viewpoint": "DISTRIBUTOR", "month": "2024-01", "currency_code": "EUR", "country_code": "FRA", "billable_cost": 2331828.33275813, "billable_rated_cost": 3817593.35186263, "non_billable_cost": 0, "non_billable_rated_cost": 0, "resources": [{"resource_id": "cloudant", "resource_name": "Cloudant", "billable_cost": 75, "billable_rated_cost": 75, "non_billable_cost": 0, "non_billable_rated_cost": 0, "plans": [{"plan_id": "cloudant-standard", "pricing_region": "Standard", "pricing_plan_id": "billable:v4:cloudant-standard::1552694400000:", "billable": true, "cost": 75, "rated_cost": 75, "usage": [{"metric": "GB_STORAGE_ACCRUED_PER_MONTH", "unit": "GIGABYTE_MONTHS", "quantity": 10, "rateable_quantity": 10, "cost": 10, "rated_cost": 10, "price": [{"anyKey": "anyValue"}]}]}]}]}]}'
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
                _service.get_resource_usage_report(**req_copy)

    def test_get_resource_usage_report_value_error_with_retries(self):
        # Enable retries and run test_get_resource_usage_report_value_error.
        _service.enable_retries()
        self.test_get_resource_usage_report_value_error()

        # Disable retries and run test_get_resource_usage_report_value_error.
        _service.disable_retries()
        self.test_get_resource_usage_report_value_error()

    @responses.activate
    def test_get_resource_usage_report_with_pager_get_next(self):
        """
        test_get_resource_usage_report_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/resource-usage-reports')
        mock_response1 = '{"next":{"offset":"1"},"reports":[{"entity_id":"<distributor_enterprise_id>","entity_type":"enterprise","entity_crn":"crn:v1:bluemix:public:enterprise::a/fa359b76ff2c41eda727aad47b7e4063::enterprise:33a7eb04e7d547cd9489e90c99d476a5","entity_name":"Arrow","entity_partner_type":"DISTRIBUTOR","viewpoint":"DISTRIBUTOR","month":"2024-01","currency_code":"EUR","country_code":"FRA","billable_cost":2331828.33275813,"billable_rated_cost":3817593.35186263,"non_billable_cost":0,"non_billable_rated_cost":0,"resources":[{"resource_id":"cloudant","resource_name":"Cloudant","billable_cost":75,"billable_rated_cost":75,"non_billable_cost":0,"non_billable_rated_cost":0,"plans":[{"plan_id":"cloudant-standard","pricing_region":"Standard","pricing_plan_id":"billable:v4:cloudant-standard::1552694400000:","billable":true,"cost":75,"rated_cost":75,"usage":[{"metric":"GB_STORAGE_ACCRUED_PER_MONTH","unit":"GIGABYTE_MONTHS","quantity":10,"rateable_quantity":10,"cost":10,"rated_cost":10,"price":[{"anyKey":"anyValue"}]}]}]}]}],"total_count":2,"limit":1}'
        mock_response2 = '{"reports":[{"entity_id":"<distributor_enterprise_id>","entity_type":"enterprise","entity_crn":"crn:v1:bluemix:public:enterprise::a/fa359b76ff2c41eda727aad47b7e4063::enterprise:33a7eb04e7d547cd9489e90c99d476a5","entity_name":"Arrow","entity_partner_type":"DISTRIBUTOR","viewpoint":"DISTRIBUTOR","month":"2024-01","currency_code":"EUR","country_code":"FRA","billable_cost":2331828.33275813,"billable_rated_cost":3817593.35186263,"non_billable_cost":0,"non_billable_rated_cost":0,"resources":[{"resource_id":"cloudant","resource_name":"Cloudant","billable_cost":75,"billable_rated_cost":75,"non_billable_cost":0,"non_billable_rated_cost":0,"plans":[{"plan_id":"cloudant-standard","pricing_region":"Standard","pricing_plan_id":"billable:v4:cloudant-standard::1552694400000:","billable":true,"cost":75,"rated_cost":75,"usage":[{"metric":"GB_STORAGE_ACCRUED_PER_MONTH","unit":"GIGABYTE_MONTHS","quantity":10,"rateable_quantity":10,"cost":10,"rated_cost":10,"price":[{"anyKey":"anyValue"}]}]}]}]}],"total_count":2,"limit":1}'
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
        pager = GetResourceUsageReportPager(
            client=_service,
            partner_id='testString',
            reseller_id='testString',
            customer_id='testString',
            children=False,
            month='2024-01',
            viewpoint='DISTRIBUTOR',
            recurse=False,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_get_resource_usage_report_with_pager_get_all(self):
        """
        test_get_resource_usage_report_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/resource-usage-reports')
        mock_response1 = '{"next":{"offset":"1"},"reports":[{"entity_id":"<distributor_enterprise_id>","entity_type":"enterprise","entity_crn":"crn:v1:bluemix:public:enterprise::a/fa359b76ff2c41eda727aad47b7e4063::enterprise:33a7eb04e7d547cd9489e90c99d476a5","entity_name":"Arrow","entity_partner_type":"DISTRIBUTOR","viewpoint":"DISTRIBUTOR","month":"2024-01","currency_code":"EUR","country_code":"FRA","billable_cost":2331828.33275813,"billable_rated_cost":3817593.35186263,"non_billable_cost":0,"non_billable_rated_cost":0,"resources":[{"resource_id":"cloudant","resource_name":"Cloudant","billable_cost":75,"billable_rated_cost":75,"non_billable_cost":0,"non_billable_rated_cost":0,"plans":[{"plan_id":"cloudant-standard","pricing_region":"Standard","pricing_plan_id":"billable:v4:cloudant-standard::1552694400000:","billable":true,"cost":75,"rated_cost":75,"usage":[{"metric":"GB_STORAGE_ACCRUED_PER_MONTH","unit":"GIGABYTE_MONTHS","quantity":10,"rateable_quantity":10,"cost":10,"rated_cost":10,"price":[{"anyKey":"anyValue"}]}]}]}]}],"total_count":2,"limit":1}'
        mock_response2 = '{"reports":[{"entity_id":"<distributor_enterprise_id>","entity_type":"enterprise","entity_crn":"crn:v1:bluemix:public:enterprise::a/fa359b76ff2c41eda727aad47b7e4063::enterprise:33a7eb04e7d547cd9489e90c99d476a5","entity_name":"Arrow","entity_partner_type":"DISTRIBUTOR","viewpoint":"DISTRIBUTOR","month":"2024-01","currency_code":"EUR","country_code":"FRA","billable_cost":2331828.33275813,"billable_rated_cost":3817593.35186263,"non_billable_cost":0,"non_billable_rated_cost":0,"resources":[{"resource_id":"cloudant","resource_name":"Cloudant","billable_cost":75,"billable_rated_cost":75,"non_billable_cost":0,"non_billable_rated_cost":0,"plans":[{"plan_id":"cloudant-standard","pricing_region":"Standard","pricing_plan_id":"billable:v4:cloudant-standard::1552694400000:","billable":true,"cost":75,"rated_cost":75,"usage":[{"metric":"GB_STORAGE_ACCRUED_PER_MONTH","unit":"GIGABYTE_MONTHS","quantity":10,"rateable_quantity":10,"cost":10,"rated_cost":10,"price":[{"anyKey":"anyValue"}]}]}]}]}],"total_count":2,"limit":1}'
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
        pager = GetResourceUsageReportPager(
            client=_service,
            partner_id='testString',
            reseller_id='testString',
            customer_id='testString',
            children=False,
            month='2024-01',
            viewpoint='DISTRIBUTOR',
            recurse=False,
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


# endregion
##############################################################################
# End of Service: PartnerUsageReports
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_MetricUsage:
    """
    Test Class for MetricUsage
    """

    def test_metric_usage_serialization(self):
        """
        Test serialization/deserialization for MetricUsage
        """

        # Construct a json representation of a MetricUsage model
        metric_usage_model_json = {}
        metric_usage_model_json['metric'] = 'GB_STORAGE_ACCRUED_PER_MONTH'
        metric_usage_model_json['unit'] = 'GIGABYTE_MONTHS'
        metric_usage_model_json['quantity'] = 10
        metric_usage_model_json['rateable_quantity'] = 10
        metric_usage_model_json['cost'] = 10
        metric_usage_model_json['rated_cost'] = 10
        metric_usage_model_json['price'] = [{'anyKey': 'anyValue'}]

        # Construct a model instance of MetricUsage by calling from_dict on the json representation
        metric_usage_model = MetricUsage.from_dict(metric_usage_model_json)
        assert metric_usage_model != False

        # Construct a model instance of MetricUsage by calling from_dict on the json representation
        metric_usage_model_dict = MetricUsage.from_dict(metric_usage_model_json).__dict__
        metric_usage_model2 = MetricUsage(**metric_usage_model_dict)

        # Verify the model instances are equivalent
        assert metric_usage_model == metric_usage_model2

        # Convert model instance back to dict and verify no loss of data
        metric_usage_model_json2 = metric_usage_model.to_dict()
        assert metric_usage_model_json2 == metric_usage_model_json


class TestModel_PartnerUsageReportSummaryFirst:
    """
    Test Class for PartnerUsageReportSummaryFirst
    """

    def test_partner_usage_report_summary_first_serialization(self):
        """
        Test serialization/deserialization for PartnerUsageReportSummaryFirst
        """

        # Construct a json representation of a PartnerUsageReportSummaryFirst model
        partner_usage_report_summary_first_model_json = {}
        partner_usage_report_summary_first_model_json['href'] = 'testString'

        # Construct a model instance of PartnerUsageReportSummaryFirst by calling from_dict on the json representation
        partner_usage_report_summary_first_model = PartnerUsageReportSummaryFirst.from_dict(
            partner_usage_report_summary_first_model_json
        )
        assert partner_usage_report_summary_first_model != False

        # Construct a model instance of PartnerUsageReportSummaryFirst by calling from_dict on the json representation
        partner_usage_report_summary_first_model_dict = PartnerUsageReportSummaryFirst.from_dict(
            partner_usage_report_summary_first_model_json
        ).__dict__
        partner_usage_report_summary_first_model2 = PartnerUsageReportSummaryFirst(
            **partner_usage_report_summary_first_model_dict
        )

        # Verify the model instances are equivalent
        assert partner_usage_report_summary_first_model == partner_usage_report_summary_first_model2

        # Convert model instance back to dict and verify no loss of data
        partner_usage_report_summary_first_model_json2 = partner_usage_report_summary_first_model.to_dict()
        assert partner_usage_report_summary_first_model_json2 == partner_usage_report_summary_first_model_json


class TestModel_PartnerUsageReportSummaryNext:
    """
    Test Class for PartnerUsageReportSummaryNext
    """

    def test_partner_usage_report_summary_next_serialization(self):
        """
        Test serialization/deserialization for PartnerUsageReportSummaryNext
        """

        # Construct a json representation of a PartnerUsageReportSummaryNext model
        partner_usage_report_summary_next_model_json = {}
        partner_usage_report_summary_next_model_json['href'] = 'testString'
        partner_usage_report_summary_next_model_json['offset'] = 'testString'

        # Construct a model instance of PartnerUsageReportSummaryNext by calling from_dict on the json representation
        partner_usage_report_summary_next_model = PartnerUsageReportSummaryNext.from_dict(
            partner_usage_report_summary_next_model_json
        )
        assert partner_usage_report_summary_next_model != False

        # Construct a model instance of PartnerUsageReportSummaryNext by calling from_dict on the json representation
        partner_usage_report_summary_next_model_dict = PartnerUsageReportSummaryNext.from_dict(
            partner_usage_report_summary_next_model_json
        ).__dict__
        partner_usage_report_summary_next_model2 = PartnerUsageReportSummaryNext(
            **partner_usage_report_summary_next_model_dict
        )

        # Verify the model instances are equivalent
        assert partner_usage_report_summary_next_model == partner_usage_report_summary_next_model2

        # Convert model instance back to dict and verify no loss of data
        partner_usage_report_summary_next_model_json2 = partner_usage_report_summary_next_model.to_dict()
        assert partner_usage_report_summary_next_model_json2 == partner_usage_report_summary_next_model_json


class TestModel_PartnerUsageReport:
    """
    Test Class for PartnerUsageReport
    """

    def test_partner_usage_report_serialization(self):
        """
        Test serialization/deserialization for PartnerUsageReport
        """

        # Construct dict forms of any model objects needed in order to build this model.

        metric_usage_model = {}  # MetricUsage
        metric_usage_model['metric'] = 'GB_STORAGE_ACCRUED_PER_MONTH'
        metric_usage_model['unit'] = 'GIGABYTE_MONTHS'
        metric_usage_model['quantity'] = 10
        metric_usage_model['rateable_quantity'] = 10
        metric_usage_model['cost'] = 10
        metric_usage_model['rated_cost'] = 10
        metric_usage_model['price'] = [{'anyKey': 'anyValue'}]

        plan_usage_model = {}  # PlanUsage
        plan_usage_model['plan_id'] = 'cloudant-standard'
        plan_usage_model['pricing_region'] = 'Standard'
        plan_usage_model['pricing_plan_id'] = 'billable:v4:cloudant-standard::1552694400000:'
        plan_usage_model['billable'] = True
        plan_usage_model['cost'] = 75
        plan_usage_model['rated_cost'] = 75
        plan_usage_model['usage'] = [metric_usage_model]

        resource_usage_model = {}  # ResourceUsage
        resource_usage_model['resource_id'] = 'cloudant'
        resource_usage_model['resource_name'] = 'Cloudant'
        resource_usage_model['billable_cost'] = 75
        resource_usage_model['billable_rated_cost'] = 75
        resource_usage_model['non_billable_cost'] = 0
        resource_usage_model['non_billable_rated_cost'] = 0
        resource_usage_model['plans'] = [plan_usage_model]

        # Construct a json representation of a PartnerUsageReport model
        partner_usage_report_model_json = {}
        partner_usage_report_model_json['entity_id'] = '<distributor_enterprise_id>'
        partner_usage_report_model_json['entity_type'] = 'enterprise'
        partner_usage_report_model_json['entity_crn'] = (
            'crn:v1:bluemix:public:enterprise::a/fa359b76ff2c41eda727aad47b7e4063::enterprise:33a7eb04e7d547cd9489e90c99d476a5'
        )
        partner_usage_report_model_json['entity_name'] = 'Arrow'
        partner_usage_report_model_json['entity_partner_type'] = 'DISTRIBUTOR'
        partner_usage_report_model_json['viewpoint'] = 'DISTRIBUTOR'
        partner_usage_report_model_json['month'] = '2024-01'
        partner_usage_report_model_json['currency_code'] = 'EUR'
        partner_usage_report_model_json['country_code'] = 'FRA'
        partner_usage_report_model_json['billable_cost'] = 2331828.33275813
        partner_usage_report_model_json['billable_rated_cost'] = 3817593.35186263
        partner_usage_report_model_json['non_billable_cost'] = 0
        partner_usage_report_model_json['non_billable_rated_cost'] = 0
        partner_usage_report_model_json['resources'] = [resource_usage_model]

        # Construct a model instance of PartnerUsageReport by calling from_dict on the json representation
        partner_usage_report_model = PartnerUsageReport.from_dict(partner_usage_report_model_json)
        assert partner_usage_report_model != False

        # Construct a model instance of PartnerUsageReport by calling from_dict on the json representation
        partner_usage_report_model_dict = PartnerUsageReport.from_dict(partner_usage_report_model_json).__dict__
        partner_usage_report_model2 = PartnerUsageReport(**partner_usage_report_model_dict)

        # Verify the model instances are equivalent
        assert partner_usage_report_model == partner_usage_report_model2

        # Convert model instance back to dict and verify no loss of data
        partner_usage_report_model_json2 = partner_usage_report_model.to_dict()
        assert partner_usage_report_model_json2 == partner_usage_report_model_json


class TestModel_PartnerUsageReportSummary:
    """
    Test Class for PartnerUsageReportSummary
    """

    def test_partner_usage_report_summary_serialization(self):
        """
        Test serialization/deserialization for PartnerUsageReportSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        partner_usage_report_summary_first_model = {}  # PartnerUsageReportSummaryFirst
        partner_usage_report_summary_first_model['href'] = 'testString'

        partner_usage_report_summary_next_model = {}  # PartnerUsageReportSummaryNext
        partner_usage_report_summary_next_model['href'] = 'testString'
        partner_usage_report_summary_next_model['offset'] = 'testString'

        metric_usage_model = {}  # MetricUsage
        metric_usage_model['metric'] = 'GB_STORAGE_ACCRUED_PER_MONTH'
        metric_usage_model['unit'] = 'GIGABYTE_MONTHS'
        metric_usage_model['quantity'] = 10
        metric_usage_model['rateable_quantity'] = 10
        metric_usage_model['cost'] = 10
        metric_usage_model['rated_cost'] = 10
        metric_usage_model['price'] = [{'anyKey': 'anyValue'}]

        plan_usage_model = {}  # PlanUsage
        plan_usage_model['plan_id'] = 'cloudant-standard'
        plan_usage_model['pricing_region'] = 'Standard'
        plan_usage_model['pricing_plan_id'] = 'billable:v4:cloudant-standard::1552694400000:'
        plan_usage_model['billable'] = True
        plan_usage_model['cost'] = 75
        plan_usage_model['rated_cost'] = 75
        plan_usage_model['usage'] = [metric_usage_model]

        resource_usage_model = {}  # ResourceUsage
        resource_usage_model['resource_id'] = 'cloudant'
        resource_usage_model['resource_name'] = 'Cloudant'
        resource_usage_model['billable_cost'] = 75
        resource_usage_model['billable_rated_cost'] = 75
        resource_usage_model['non_billable_cost'] = 0
        resource_usage_model['non_billable_rated_cost'] = 0
        resource_usage_model['plans'] = [plan_usage_model]

        partner_usage_report_model = {}  # PartnerUsageReport
        partner_usage_report_model['entity_id'] = '<distributor_enterprise_id>'
        partner_usage_report_model['entity_type'] = 'enterprise'
        partner_usage_report_model['entity_crn'] = (
            'crn:v1:bluemix:public:enterprise::a/fa359b76ff2c41eda727aad47b7e4063::enterprise:33a7eb04e7d547cd9489e90c99d476a5'
        )
        partner_usage_report_model['entity_name'] = 'Arrow'
        partner_usage_report_model['entity_partner_type'] = 'DISTRIBUTOR'
        partner_usage_report_model['viewpoint'] = 'DISTRIBUTOR'
        partner_usage_report_model['month'] = '2024-01'
        partner_usage_report_model['currency_code'] = 'EUR'
        partner_usage_report_model['country_code'] = 'FRA'
        partner_usage_report_model['billable_cost'] = 2331828.33275813
        partner_usage_report_model['billable_rated_cost'] = 3817593.35186263
        partner_usage_report_model['non_billable_cost'] = 0
        partner_usage_report_model['non_billable_rated_cost'] = 0
        partner_usage_report_model['resources'] = [resource_usage_model]

        # Construct a json representation of a PartnerUsageReportSummary model
        partner_usage_report_summary_model_json = {}
        partner_usage_report_summary_model_json['limit'] = 38
        partner_usage_report_summary_model_json['first'] = partner_usage_report_summary_first_model
        partner_usage_report_summary_model_json['next'] = partner_usage_report_summary_next_model
        partner_usage_report_summary_model_json['reports'] = [partner_usage_report_model]

        # Construct a model instance of PartnerUsageReportSummary by calling from_dict on the json representation
        partner_usage_report_summary_model = PartnerUsageReportSummary.from_dict(
            partner_usage_report_summary_model_json
        )
        assert partner_usage_report_summary_model != False

        # Construct a model instance of PartnerUsageReportSummary by calling from_dict on the json representation
        partner_usage_report_summary_model_dict = PartnerUsageReportSummary.from_dict(
            partner_usage_report_summary_model_json
        ).__dict__
        partner_usage_report_summary_model2 = PartnerUsageReportSummary(**partner_usage_report_summary_model_dict)

        # Verify the model instances are equivalent
        assert partner_usage_report_summary_model == partner_usage_report_summary_model2

        # Convert model instance back to dict and verify no loss of data
        partner_usage_report_summary_model_json2 = partner_usage_report_summary_model.to_dict()
        assert partner_usage_report_summary_model_json2 == partner_usage_report_summary_model_json


class TestModel_PlanUsage:
    """
    Test Class for PlanUsage
    """

    def test_plan_usage_serialization(self):
        """
        Test serialization/deserialization for PlanUsage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        metric_usage_model = {}  # MetricUsage
        metric_usage_model['metric'] = 'GB_STORAGE_ACCRUED_PER_MONTH'
        metric_usage_model['unit'] = 'GIGABYTE_MONTHS'
        metric_usage_model['quantity'] = 10
        metric_usage_model['rateable_quantity'] = 10
        metric_usage_model['cost'] = 10
        metric_usage_model['rated_cost'] = 10
        metric_usage_model['price'] = [{'anyKey': 'anyValue'}]

        # Construct a json representation of a PlanUsage model
        plan_usage_model_json = {}
        plan_usage_model_json['plan_id'] = 'cloudant-standard'
        plan_usage_model_json['pricing_region'] = 'Standard'
        plan_usage_model_json['pricing_plan_id'] = 'billable:v4:cloudant-standard::1552694400000:'
        plan_usage_model_json['billable'] = True
        plan_usage_model_json['cost'] = 75
        plan_usage_model_json['rated_cost'] = 75
        plan_usage_model_json['usage'] = [metric_usage_model]

        # Construct a model instance of PlanUsage by calling from_dict on the json representation
        plan_usage_model = PlanUsage.from_dict(plan_usage_model_json)
        assert plan_usage_model != False

        # Construct a model instance of PlanUsage by calling from_dict on the json representation
        plan_usage_model_dict = PlanUsage.from_dict(plan_usage_model_json).__dict__
        plan_usage_model2 = PlanUsage(**plan_usage_model_dict)

        # Verify the model instances are equivalent
        assert plan_usage_model == plan_usage_model2

        # Convert model instance back to dict and verify no loss of data
        plan_usage_model_json2 = plan_usage_model.to_dict()
        assert plan_usage_model_json2 == plan_usage_model_json


class TestModel_ResourceUsage:
    """
    Test Class for ResourceUsage
    """

    def test_resource_usage_serialization(self):
        """
        Test serialization/deserialization for ResourceUsage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        metric_usage_model = {}  # MetricUsage
        metric_usage_model['metric'] = 'GB_STORAGE_ACCRUED_PER_MONTH'
        metric_usage_model['unit'] = 'GIGABYTE_MONTHS'
        metric_usage_model['quantity'] = 10
        metric_usage_model['rateable_quantity'] = 10
        metric_usage_model['cost'] = 10
        metric_usage_model['rated_cost'] = 10
        metric_usage_model['price'] = [{'anyKey': 'anyValue'}]

        plan_usage_model = {}  # PlanUsage
        plan_usage_model['plan_id'] = 'cloudant-standard'
        plan_usage_model['pricing_region'] = 'Standard'
        plan_usage_model['pricing_plan_id'] = 'billable:v4:cloudant-standard::1552694400000:'
        plan_usage_model['billable'] = True
        plan_usage_model['cost'] = 75
        plan_usage_model['rated_cost'] = 75
        plan_usage_model['usage'] = [metric_usage_model]

        # Construct a json representation of a ResourceUsage model
        resource_usage_model_json = {}
        resource_usage_model_json['resource_id'] = 'cloudant'
        resource_usage_model_json['resource_name'] = 'Cloudant'
        resource_usage_model_json['billable_cost'] = 75
        resource_usage_model_json['billable_rated_cost'] = 75
        resource_usage_model_json['non_billable_cost'] = 0
        resource_usage_model_json['non_billable_rated_cost'] = 0
        resource_usage_model_json['plans'] = [plan_usage_model]

        # Construct a model instance of ResourceUsage by calling from_dict on the json representation
        resource_usage_model = ResourceUsage.from_dict(resource_usage_model_json)
        assert resource_usage_model != False

        # Construct a model instance of ResourceUsage by calling from_dict on the json representation
        resource_usage_model_dict = ResourceUsage.from_dict(resource_usage_model_json).__dict__
        resource_usage_model2 = ResourceUsage(**resource_usage_model_dict)

        # Verify the model instances are equivalent
        assert resource_usage_model == resource_usage_model2

        # Convert model instance back to dict and verify no loss of data
        resource_usage_model_json2 = resource_usage_model.to_dict()
        assert resource_usage_model_json2 == resource_usage_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
