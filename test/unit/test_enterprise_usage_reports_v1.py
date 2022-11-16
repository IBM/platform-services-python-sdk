# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2022.
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
Unit Tests for EnterpriseUsageReportsV1
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
from ibm_platform_services.enterprise_usage_reports_v1 import *


_service = EnterpriseUsageReportsV1(authenticator=NoAuthAuthenticator())

_base_url = 'https://enterprise.cloud.ibm.com'
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
# Start of Service: EnterpriseUsageReports
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

        service = EnterpriseUsageReportsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, EnterpriseUsageReportsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = EnterpriseUsageReportsV1.new_instance(
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
        mock_response = '{"limit": 5, "first": {"href": "href"}, "next": {"href": "href"}, "reports": [{"entity_id": "de129b787b86403db7d3a14be2ae5f76", "entity_type": "enterprise", "entity_crn": "crn:v1:bluemix:public:enterprise::a/e9a57260546c4b4aa9ebfa316a82e56e::enterprise:de129b787b86403db7d3a14be2ae5f76", "entity_name": "Platform-Services", "billing_unit_id": "65719a07280a4022a9efa2f6ff4c3369", "billing_unit_crn": "crn:v1:bluemix:public:billing::a/3f99f8accbc848ea96f3c61a0ae22c44::billing-unit:65719a07280a4022a9efa2f6ff4c3369", "billing_unit_name": "Operations", "country_code": "USA", "currency_code": "USD", "month": "2017-08", "billable_cost": 13, "non_billable_cost": 17, "billable_rated_cost": 19, "non_billable_rated_cost": 23, "resources": [{"resource_id": "resource_id", "billable_cost": 13, "billable_rated_cost": 19, "non_billable_cost": 17, "non_billable_rated_cost": 23, "plans": [{"plan_id": "plan_id", "pricing_region": "pricing_region", "pricing_plan_id": "pricing_plan_id", "billable": true, "cost": 4, "rated_cost": 10, "usage": [{"metric": "UP-TIME", "unit": "HOURS", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130, "price": [{"anyKey": "anyValue"}]}]}]}]}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        enterprise_id = 'abc12340d4bf4e36b0423d209b286f24'
        account_group_id = 'def456a237b94b9a9238ef024e204c9f'
        account_id = '987abcba31834216b8c726a7dd9eb8d6'
        children = True
        month = '2019-06'
        billing_unit_id = 'testString'
        limit = 10
        offset = 'testString'

        # Invoke method
        response = _service.get_resource_usage_report(
            enterprise_id=enterprise_id,
            account_group_id=account_group_id,
            account_id=account_id,
            children=children,
            month=month,
            billing_unit_id=billing_unit_id,
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
        assert 'enterprise_id={}'.format(enterprise_id) in query_string
        assert 'account_group_id={}'.format(account_group_id) in query_string
        assert 'account_id={}'.format(account_id) in query_string
        assert 'children={}'.format('true' if children else 'false') in query_string
        assert 'month={}'.format(month) in query_string
        assert 'billing_unit_id={}'.format(billing_unit_id) in query_string
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
        mock_response = '{"limit": 5, "first": {"href": "href"}, "next": {"href": "href"}, "reports": [{"entity_id": "de129b787b86403db7d3a14be2ae5f76", "entity_type": "enterprise", "entity_crn": "crn:v1:bluemix:public:enterprise::a/e9a57260546c4b4aa9ebfa316a82e56e::enterprise:de129b787b86403db7d3a14be2ae5f76", "entity_name": "Platform-Services", "billing_unit_id": "65719a07280a4022a9efa2f6ff4c3369", "billing_unit_crn": "crn:v1:bluemix:public:billing::a/3f99f8accbc848ea96f3c61a0ae22c44::billing-unit:65719a07280a4022a9efa2f6ff4c3369", "billing_unit_name": "Operations", "country_code": "USA", "currency_code": "USD", "month": "2017-08", "billable_cost": 13, "non_billable_cost": 17, "billable_rated_cost": 19, "non_billable_rated_cost": 23, "resources": [{"resource_id": "resource_id", "billable_cost": 13, "billable_rated_cost": 19, "non_billable_cost": 17, "non_billable_rated_cost": 23, "plans": [{"plan_id": "plan_id", "pricing_region": "pricing_region", "pricing_plan_id": "pricing_plan_id", "billable": true, "cost": 4, "rated_cost": 10, "usage": [{"metric": "UP-TIME", "unit": "HOURS", "quantity": 711.11, "rateable_quantity": 700, "cost": 123.45, "rated_cost": 130, "price": [{"anyKey": "anyValue"}]}]}]}]}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Invoke method
        response = _service.get_resource_usage_report()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_resource_usage_report_required_params_with_retries(self):
        # Enable retries and run test_get_resource_usage_report_required_params.
        _service.enable_retries()
        self.test_get_resource_usage_report_required_params()

        # Disable retries and run test_get_resource_usage_report_required_params.
        _service.disable_retries()
        self.test_get_resource_usage_report_required_params()

    @responses.activate
    def test_get_resource_usage_report_with_pager_get_next(self):
        """
        test_get_resource_usage_report_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/resource-usage-reports')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"reports":[{"entity_id":"de129b787b86403db7d3a14be2ae5f76","entity_type":"enterprise","entity_crn":"crn:v1:bluemix:public:enterprise::a/e9a57260546c4b4aa9ebfa316a82e56e::enterprise:de129b787b86403db7d3a14be2ae5f76","entity_name":"Platform-Services","billing_unit_id":"65719a07280a4022a9efa2f6ff4c3369","billing_unit_crn":"crn:v1:bluemix:public:billing::a/3f99f8accbc848ea96f3c61a0ae22c44::billing-unit:65719a07280a4022a9efa2f6ff4c3369","billing_unit_name":"Operations","country_code":"USA","currency_code":"USD","month":"2017-08","billable_cost":13,"non_billable_cost":17,"billable_rated_cost":19,"non_billable_rated_cost":23,"resources":[{"resource_id":"resource_id","billable_cost":13,"billable_rated_cost":19,"non_billable_cost":17,"non_billable_rated_cost":23,"plans":[{"plan_id":"plan_id","pricing_region":"pricing_region","pricing_plan_id":"pricing_plan_id","billable":true,"cost":4,"rated_cost":10,"usage":[{"metric":"UP-TIME","unit":"HOURS","quantity":711.11,"rateable_quantity":700,"cost":123.45,"rated_cost":130,"price":[{"anyKey":"anyValue"}]}]}]}]}],"total_count":2,"limit":1}'
        mock_response2 = '{"reports":[{"entity_id":"de129b787b86403db7d3a14be2ae5f76","entity_type":"enterprise","entity_crn":"crn:v1:bluemix:public:enterprise::a/e9a57260546c4b4aa9ebfa316a82e56e::enterprise:de129b787b86403db7d3a14be2ae5f76","entity_name":"Platform-Services","billing_unit_id":"65719a07280a4022a9efa2f6ff4c3369","billing_unit_crn":"crn:v1:bluemix:public:billing::a/3f99f8accbc848ea96f3c61a0ae22c44::billing-unit:65719a07280a4022a9efa2f6ff4c3369","billing_unit_name":"Operations","country_code":"USA","currency_code":"USD","month":"2017-08","billable_cost":13,"non_billable_cost":17,"billable_rated_cost":19,"non_billable_rated_cost":23,"resources":[{"resource_id":"resource_id","billable_cost":13,"billable_rated_cost":19,"non_billable_cost":17,"non_billable_rated_cost":23,"plans":[{"plan_id":"plan_id","pricing_region":"pricing_region","pricing_plan_id":"pricing_plan_id","billable":true,"cost":4,"rated_cost":10,"usage":[{"metric":"UP-TIME","unit":"HOURS","quantity":711.11,"rateable_quantity":700,"cost":123.45,"rated_cost":130,"price":[{"anyKey":"anyValue"}]}]}]}]}],"total_count":2,"limit":1}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = GetResourceUsageReportPager(
            client=_service,
            enterprise_id='abc12340d4bf4e36b0423d209b286f24',
            account_group_id='def456a237b94b9a9238ef024e204c9f',
            account_id='987abcba31834216b8c726a7dd9eb8d6',
            children=True,
            month='2019-06',
            billing_unit_id='testString',
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
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"reports":[{"entity_id":"de129b787b86403db7d3a14be2ae5f76","entity_type":"enterprise","entity_crn":"crn:v1:bluemix:public:enterprise::a/e9a57260546c4b4aa9ebfa316a82e56e::enterprise:de129b787b86403db7d3a14be2ae5f76","entity_name":"Platform-Services","billing_unit_id":"65719a07280a4022a9efa2f6ff4c3369","billing_unit_crn":"crn:v1:bluemix:public:billing::a/3f99f8accbc848ea96f3c61a0ae22c44::billing-unit:65719a07280a4022a9efa2f6ff4c3369","billing_unit_name":"Operations","country_code":"USA","currency_code":"USD","month":"2017-08","billable_cost":13,"non_billable_cost":17,"billable_rated_cost":19,"non_billable_rated_cost":23,"resources":[{"resource_id":"resource_id","billable_cost":13,"billable_rated_cost":19,"non_billable_cost":17,"non_billable_rated_cost":23,"plans":[{"plan_id":"plan_id","pricing_region":"pricing_region","pricing_plan_id":"pricing_plan_id","billable":true,"cost":4,"rated_cost":10,"usage":[{"metric":"UP-TIME","unit":"HOURS","quantity":711.11,"rateable_quantity":700,"cost":123.45,"rated_cost":130,"price":[{"anyKey":"anyValue"}]}]}]}]}],"total_count":2,"limit":1}'
        mock_response2 = '{"reports":[{"entity_id":"de129b787b86403db7d3a14be2ae5f76","entity_type":"enterprise","entity_crn":"crn:v1:bluemix:public:enterprise::a/e9a57260546c4b4aa9ebfa316a82e56e::enterprise:de129b787b86403db7d3a14be2ae5f76","entity_name":"Platform-Services","billing_unit_id":"65719a07280a4022a9efa2f6ff4c3369","billing_unit_crn":"crn:v1:bluemix:public:billing::a/3f99f8accbc848ea96f3c61a0ae22c44::billing-unit:65719a07280a4022a9efa2f6ff4c3369","billing_unit_name":"Operations","country_code":"USA","currency_code":"USD","month":"2017-08","billable_cost":13,"non_billable_cost":17,"billable_rated_cost":19,"non_billable_rated_cost":23,"resources":[{"resource_id":"resource_id","billable_cost":13,"billable_rated_cost":19,"non_billable_cost":17,"non_billable_rated_cost":23,"plans":[{"plan_id":"plan_id","pricing_region":"pricing_region","pricing_plan_id":"pricing_plan_id","billable":true,"cost":4,"rated_cost":10,"usage":[{"metric":"UP-TIME","unit":"HOURS","quantity":711.11,"rateable_quantity":700,"cost":123.45,"rated_cost":130,"price":[{"anyKey":"anyValue"}]}]}]}]}],"total_count":2,"limit":1}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = GetResourceUsageReportPager(
            client=_service,
            enterprise_id='abc12340d4bf4e36b0423d209b286f24',
            account_group_id='def456a237b94b9a9238ef024e204c9f',
            account_id='987abcba31834216b8c726a7dd9eb8d6',
            children=True,
            month='2019-06',
            billing_unit_id='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


# endregion
##############################################################################
# End of Service: EnterpriseUsageReports
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_Link:
    """
    Test Class for Link
    """

    def test_link_serialization(self):
        """
        Test serialization/deserialization for Link
        """

        # Construct a json representation of a Link model
        link_model_json = {}
        link_model_json['href'] = 'testString'

        # Construct a model instance of Link by calling from_dict on the json representation
        link_model = Link.from_dict(link_model_json)
        assert link_model != False

        # Construct a model instance of Link by calling from_dict on the json representation
        link_model_dict = Link.from_dict(link_model_json).__dict__
        link_model2 = Link(**link_model_dict)

        # Verify the model instances are equivalent
        assert link_model == link_model2

        # Convert model instance back to dict and verify no loss of data
        link_model_json2 = link_model.to_dict()
        assert link_model_json2 == link_model_json


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
        metric_usage_model_json['metric'] = 'UP-TIME'
        metric_usage_model_json['unit'] = 'HOURS'
        metric_usage_model_json['quantity'] = 711.11
        metric_usage_model_json['rateable_quantity'] = 700
        metric_usage_model_json['cost'] = 123.45
        metric_usage_model_json['rated_cost'] = 130
        metric_usage_model_json['price'] = [{'foo': 'bar'}]

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
        metric_usage_model['metric'] = 'UP-TIME'
        metric_usage_model['unit'] = 'HOURS'
        metric_usage_model['quantity'] = 711.11
        metric_usage_model['rateable_quantity'] = 700
        metric_usage_model['cost'] = 123.45
        metric_usage_model['rated_cost'] = 130
        metric_usage_model['price'] = [{'foo': 'bar'}]

        # Construct a json representation of a PlanUsage model
        plan_usage_model_json = {}
        plan_usage_model_json['plan_id'] = 'testString'
        plan_usage_model_json['pricing_region'] = 'testString'
        plan_usage_model_json['pricing_plan_id'] = 'testString'
        plan_usage_model_json['billable'] = True
        plan_usage_model_json['cost'] = 72.5
        plan_usage_model_json['rated_cost'] = 72.5
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


class TestModel_Reports:
    """
    Test Class for Reports
    """

    def test_reports_serialization(self):
        """
        Test serialization/deserialization for Reports
        """

        # Construct dict forms of any model objects needed in order to build this model.

        link_model = {}  # Link
        link_model[
            'href'
        ] = '/v1/resource-usage-reports?enterprise_id=5ac9eb23c91b429b893e038aa5a2dec8&children=true&month=2019-06&limit=2'

        metric_usage_model = {}  # MetricUsage
        metric_usage_model['metric'] = 'GB_STORAGE_ACCRUED_PER_MONTH'
        metric_usage_model['unit'] = 'GIGABYTE_MONTHS'
        metric_usage_model['quantity'] = 10
        metric_usage_model['rateable_quantity'] = 10
        metric_usage_model['cost'] = 10
        metric_usage_model['rated_cost'] = 10
        metric_usage_model['price'] = [{'foo': 'bar'}]

        plan_usage_model = {}  # PlanUsage
        plan_usage_model['plan_id'] = 'cloudant-standard'
        plan_usage_model['pricing_region'] = 'testString'
        plan_usage_model['pricing_plan_id'] = 'billable:v4:cloudant-standard::1552694400000:'
        plan_usage_model['billable'] = True
        plan_usage_model['cost'] = 75
        plan_usage_model['rated_cost'] = 75
        plan_usage_model['usage'] = [metric_usage_model]

        resource_usage_model = {}  # ResourceUsage
        resource_usage_model['resource_id'] = 'cloudant'
        resource_usage_model['billable_cost'] = 75
        resource_usage_model['billable_rated_cost'] = 75
        resource_usage_model['non_billable_cost'] = 0
        resource_usage_model['non_billable_rated_cost'] = 0
        resource_usage_model['plans'] = [plan_usage_model]

        resource_usage_report_model = {}  # ResourceUsageReport
        resource_usage_report_model['entity_id'] = '41848d0e2711434bbc134242452f7fc7'
        resource_usage_report_model['entity_type'] = 'account'
        resource_usage_report_model[
            'entity_crn'
        ] = 'crn:v1:bluemix:public:enterprise::a/3f99f8accbc848ea96f3c61a0ae22c44::account:41848d0e2711434bbc134242452f7fc7'
        resource_usage_report_model['entity_name'] = 'Example Account'
        resource_usage_report_model['billing_unit_id'] = '65719a07280a4022a9efa2f6ff4c3369'
        resource_usage_report_model[
            'billing_unit_crn'
        ] = 'crn:v1:bluemix:public:billing::a/3f99f8accbc848ea96f3c61a0ae22c44::billing-unit:65719a07280a4022a9efa2f6ff4c3369'
        resource_usage_report_model['billing_unit_name'] = 'Example Billing Unit'
        resource_usage_report_model['country_code'] = 'USA'
        resource_usage_report_model['currency_code'] = 'USD'
        resource_usage_report_model['month'] = '2019-06'
        resource_usage_report_model['billable_cost'] = 75
        resource_usage_report_model['non_billable_cost'] = 0
        resource_usage_report_model['billable_rated_cost'] = 75
        resource_usage_report_model['non_billable_rated_cost'] = 0
        resource_usage_report_model['resources'] = [resource_usage_model]

        # Construct a json representation of a Reports model
        reports_model_json = {}
        reports_model_json['limit'] = 38
        reports_model_json['first'] = link_model
        reports_model_json['next'] = link_model
        reports_model_json['reports'] = [resource_usage_report_model]

        # Construct a model instance of Reports by calling from_dict on the json representation
        reports_model = Reports.from_dict(reports_model_json)
        assert reports_model != False

        # Construct a model instance of Reports by calling from_dict on the json representation
        reports_model_dict = Reports.from_dict(reports_model_json).__dict__
        reports_model2 = Reports(**reports_model_dict)

        # Verify the model instances are equivalent
        assert reports_model == reports_model2

        # Convert model instance back to dict and verify no loss of data
        reports_model_json2 = reports_model.to_dict()
        assert reports_model_json2 == reports_model_json


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
        metric_usage_model['metric'] = 'UP-TIME'
        metric_usage_model['unit'] = 'HOURS'
        metric_usage_model['quantity'] = 711.11
        metric_usage_model['rateable_quantity'] = 700
        metric_usage_model['cost'] = 123.45
        metric_usage_model['rated_cost'] = 130
        metric_usage_model['price'] = [{'foo': 'bar'}]

        plan_usage_model = {}  # PlanUsage
        plan_usage_model['plan_id'] = 'testString'
        plan_usage_model['pricing_region'] = 'testString'
        plan_usage_model['pricing_plan_id'] = 'testString'
        plan_usage_model['billable'] = True
        plan_usage_model['cost'] = 72.5
        plan_usage_model['rated_cost'] = 72.5
        plan_usage_model['usage'] = [metric_usage_model]

        # Construct a json representation of a ResourceUsage model
        resource_usage_model_json = {}
        resource_usage_model_json['resource_id'] = 'testString'
        resource_usage_model_json['billable_cost'] = 72.5
        resource_usage_model_json['billable_rated_cost'] = 72.5
        resource_usage_model_json['non_billable_cost'] = 72.5
        resource_usage_model_json['non_billable_rated_cost'] = 72.5
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


class TestModel_ResourceUsageReport:
    """
    Test Class for ResourceUsageReport
    """

    def test_resource_usage_report_serialization(self):
        """
        Test serialization/deserialization for ResourceUsageReport
        """

        # Construct dict forms of any model objects needed in order to build this model.

        metric_usage_model = {}  # MetricUsage
        metric_usage_model['metric'] = 'UP-TIME'
        metric_usage_model['unit'] = 'HOURS'
        metric_usage_model['quantity'] = 711.11
        metric_usage_model['rateable_quantity'] = 700
        metric_usage_model['cost'] = 123.45
        metric_usage_model['rated_cost'] = 130
        metric_usage_model['price'] = [{'foo': 'bar'}]

        plan_usage_model = {}  # PlanUsage
        plan_usage_model['plan_id'] = 'testString'
        plan_usage_model['pricing_region'] = 'testString'
        plan_usage_model['pricing_plan_id'] = 'testString'
        plan_usage_model['billable'] = True
        plan_usage_model['cost'] = 72.5
        plan_usage_model['rated_cost'] = 72.5
        plan_usage_model['usage'] = [metric_usage_model]

        resource_usage_model = {}  # ResourceUsage
        resource_usage_model['resource_id'] = 'testString'
        resource_usage_model['billable_cost'] = 72.5
        resource_usage_model['billable_rated_cost'] = 72.5
        resource_usage_model['non_billable_cost'] = 72.5
        resource_usage_model['non_billable_rated_cost'] = 72.5
        resource_usage_model['plans'] = [plan_usage_model]

        # Construct a json representation of a ResourceUsageReport model
        resource_usage_report_model_json = {}
        resource_usage_report_model_json['entity_id'] = 'de129b787b86403db7d3a14be2ae5f76'
        resource_usage_report_model_json['entity_type'] = 'enterprise'
        resource_usage_report_model_json[
            'entity_crn'
        ] = 'crn:v1:bluemix:public:enterprise::a/e9a57260546c4b4aa9ebfa316a82e56e::enterprise:de129b787b86403db7d3a14be2ae5f76'
        resource_usage_report_model_json['entity_name'] = 'Platform-Services'
        resource_usage_report_model_json['billing_unit_id'] = '65719a07280a4022a9efa2f6ff4c3369'
        resource_usage_report_model_json[
            'billing_unit_crn'
        ] = 'crn:v1:bluemix:public:billing::a/3f99f8accbc848ea96f3c61a0ae22c44::billing-unit:65719a07280a4022a9efa2f6ff4c3369'
        resource_usage_report_model_json['billing_unit_name'] = 'Operations'
        resource_usage_report_model_json['country_code'] = 'USA'
        resource_usage_report_model_json['currency_code'] = 'USD'
        resource_usage_report_model_json['month'] = '2017-08'
        resource_usage_report_model_json['billable_cost'] = 72.5
        resource_usage_report_model_json['non_billable_cost'] = 72.5
        resource_usage_report_model_json['billable_rated_cost'] = 72.5
        resource_usage_report_model_json['non_billable_rated_cost'] = 72.5
        resource_usage_report_model_json['resources'] = [resource_usage_model]

        # Construct a model instance of ResourceUsageReport by calling from_dict on the json representation
        resource_usage_report_model = ResourceUsageReport.from_dict(resource_usage_report_model_json)
        assert resource_usage_report_model != False

        # Construct a model instance of ResourceUsageReport by calling from_dict on the json representation
        resource_usage_report_model_dict = ResourceUsageReport.from_dict(resource_usage_report_model_json).__dict__
        resource_usage_report_model2 = ResourceUsageReport(**resource_usage_report_model_dict)

        # Verify the model instances are equivalent
        assert resource_usage_report_model == resource_usage_report_model2

        # Convert model instance back to dict and verify no loss of data
        resource_usage_report_model_json2 = resource_usage_report_model.to_dict()
        assert resource_usage_report_model_json2 == resource_usage_report_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
