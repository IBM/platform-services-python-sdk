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
Unit Tests for UsageMeteringV4
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import responses
import urllib
from ibm_platform_services.usage_metering_v4 import *


service = UsageMeteringV4(authenticator=NoAuthAuthenticator())

base_url = 'https://billing.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: ResourceUsage
##############################################################################
# region


class TestReportResourceUsage:
    """
    Test Class for report_resource_usage
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_report_resource_usage_all_params(self):
        """
        report_resource_usage()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v4/metering/resources/testString/usage')
        mock_response = '{"resources": [{"status": 6, "location": "location", "code": "code", "message": "message"}]}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=202)

        # Construct a dict representation of a MeasureAndQuantity model
        measure_and_quantity_model = {}
        measure_and_quantity_model['measure'] = 'STORAGE'
        measure_and_quantity_model['quantity'] = {'foo': 'bar'}

        # Construct a dict representation of a ResourceInstanceUsage model
        resource_instance_usage_model = {}
        resource_instance_usage_model['resource_instance_id'] = (
            'crn:v1:bluemix:staging:database-service:us-south:a/1c8ae972c35e470d994b6faff9494ce1:793ff3d3-9fe3-4329-9ea0-404703a3c371::'
        )
        resource_instance_usage_model['plan_id'] = 'database-lite'
        resource_instance_usage_model['region'] = 'us-south'
        resource_instance_usage_model['start'] = 1485907200000
        resource_instance_usage_model['end'] = 1485907200000
        resource_instance_usage_model['measured_usage'] = [measure_and_quantity_model]
        resource_instance_usage_model['consumer_id'] = 'cf-application:ed20abbe-8870-44e6-90f7-56d764c21127'

        # Set up parameter values
        resource_id = 'testString'
        resource_usage = [resource_instance_usage_model]

        # Invoke method
        response = service.report_resource_usage(resource_id, resource_usage, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == resource_usage

    @responses.activate
    def test_report_resource_usage_value_error(self):
        """
        test_report_resource_usage_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v4/metering/resources/testString/usage')
        mock_response = '{"resources": [{"status": 6, "location": "location", "code": "code", "message": "message"}]}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=202)

        # Construct a dict representation of a MeasureAndQuantity model
        measure_and_quantity_model = {}
        measure_and_quantity_model['measure'] = 'STORAGE'
        measure_and_quantity_model['quantity'] = {'foo': 'bar'}

        # Construct a dict representation of a ResourceInstanceUsage model
        resource_instance_usage_model = {}
        resource_instance_usage_model['resource_instance_id'] = (
            'crn:v1:bluemix:staging:database-service:us-south:a/1c8ae972c35e470d994b6faff9494ce1:793ff3d3-9fe3-4329-9ea0-404703a3c371::'
        )
        resource_instance_usage_model['plan_id'] = 'database-lite'
        resource_instance_usage_model['region'] = 'us-south'
        resource_instance_usage_model['start'] = 1485907200000
        resource_instance_usage_model['end'] = 1485907200000
        resource_instance_usage_model['measured_usage'] = [measure_and_quantity_model]
        resource_instance_usage_model['consumer_id'] = 'cf-application:ed20abbe-8870-44e6-90f7-56d764c21127'

        # Set up parameter values
        resource_id = 'testString'
        resource_usage = [resource_instance_usage_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "resource_id": resource_id,
            "resource_usage": resource_usage,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.report_resource_usage(**req_copy)


# endregion
##############################################################################
# End of Service: ResourceUsage
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestMeasureAndQuantity:
    """
    Test Class for MeasureAndQuantity
    """

    def test_measure_and_quantity_serialization(self):
        """
        Test serialization/deserialization for MeasureAndQuantity
        """

        # Construct a json representation of a MeasureAndQuantity model
        measure_and_quantity_model_json = {}
        measure_and_quantity_model_json['measure'] = 'STORAGE'
        measure_and_quantity_model_json['quantity'] = {'foo': 'bar'}

        # Construct a model instance of MeasureAndQuantity by calling from_dict on the json representation
        measure_and_quantity_model = MeasureAndQuantity.from_dict(measure_and_quantity_model_json)
        assert measure_and_quantity_model != False

        # Construct a model instance of MeasureAndQuantity by calling from_dict on the json representation
        measure_and_quantity_model_dict = MeasureAndQuantity.from_dict(measure_and_quantity_model_json).__dict__
        measure_and_quantity_model2 = MeasureAndQuantity(**measure_and_quantity_model_dict)

        # Verify the model instances are equivalent
        assert measure_and_quantity_model == measure_and_quantity_model2

        # Convert model instance back to dict and verify no loss of data
        measure_and_quantity_model_json2 = measure_and_quantity_model.to_dict()
        assert measure_and_quantity_model_json2 == measure_and_quantity_model_json


class TestResourceInstanceUsage:
    """
    Test Class for ResourceInstanceUsage
    """

    def test_resource_instance_usage_serialization(self):
        """
        Test serialization/deserialization for ResourceInstanceUsage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        measure_and_quantity_model = {}  # MeasureAndQuantity
        measure_and_quantity_model['measure'] = 'STORAGE'
        measure_and_quantity_model['quantity'] = {'foo': 'bar'}

        # Construct a json representation of a ResourceInstanceUsage model
        resource_instance_usage_model_json = {}
        resource_instance_usage_model_json['resource_instance_id'] = (
            'crn:v1:bluemix:staging:database-service:us-south:a/1c8ae972c35e470d994b6faff9494ce1:793ff3d3-9fe3-4329-9ea0-404703a3c371::'
        )
        resource_instance_usage_model_json['plan_id'] = 'database-lite'
        resource_instance_usage_model_json['region'] = 'us-south'
        resource_instance_usage_model_json['start'] = 1485907200000
        resource_instance_usage_model_json['end'] = 1485907200000
        resource_instance_usage_model_json['measured_usage'] = [measure_and_quantity_model]
        resource_instance_usage_model_json['consumer_id'] = 'cf-application:ed20abbe-8870-44e6-90f7-56d764c21127'

        # Construct a model instance of ResourceInstanceUsage by calling from_dict on the json representation
        resource_instance_usage_model = ResourceInstanceUsage.from_dict(resource_instance_usage_model_json)
        assert resource_instance_usage_model != False

        # Construct a model instance of ResourceInstanceUsage by calling from_dict on the json representation
        resource_instance_usage_model_dict = ResourceInstanceUsage.from_dict(
            resource_instance_usage_model_json
        ).__dict__
        resource_instance_usage_model2 = ResourceInstanceUsage(**resource_instance_usage_model_dict)

        # Verify the model instances are equivalent
        assert resource_instance_usage_model == resource_instance_usage_model2

        # Convert model instance back to dict and verify no loss of data
        resource_instance_usage_model_json2 = resource_instance_usage_model.to_dict()
        assert resource_instance_usage_model_json2 == resource_instance_usage_model_json


class TestResourceUsageDetails:
    """
    Test Class for ResourceUsageDetails
    """

    def test_resource_usage_details_serialization(self):
        """
        Test serialization/deserialization for ResourceUsageDetails
        """

        # Construct a json representation of a ResourceUsageDetails model
        resource_usage_details_model_json = {}
        resource_usage_details_model_json['status'] = 38
        resource_usage_details_model_json['location'] = 'testString'
        resource_usage_details_model_json['code'] = 'testString'
        resource_usage_details_model_json['message'] = 'testString'

        # Construct a model instance of ResourceUsageDetails by calling from_dict on the json representation
        resource_usage_details_model = ResourceUsageDetails.from_dict(resource_usage_details_model_json)
        assert resource_usage_details_model != False

        # Construct a model instance of ResourceUsageDetails by calling from_dict on the json representation
        resource_usage_details_model_dict = ResourceUsageDetails.from_dict(resource_usage_details_model_json).__dict__
        resource_usage_details_model2 = ResourceUsageDetails(**resource_usage_details_model_dict)

        # Verify the model instances are equivalent
        assert resource_usage_details_model == resource_usage_details_model2

        # Convert model instance back to dict and verify no loss of data
        resource_usage_details_model_json2 = resource_usage_details_model.to_dict()
        assert resource_usage_details_model_json2 == resource_usage_details_model_json


class TestResponseAccepted:
    """
    Test Class for ResponseAccepted
    """

    def test_response_accepted_serialization(self):
        """
        Test serialization/deserialization for ResponseAccepted
        """

        # Construct dict forms of any model objects needed in order to build this model.

        resource_usage_details_model = {}  # ResourceUsageDetails
        resource_usage_details_model['status'] = 38
        resource_usage_details_model['location'] = 'testString'
        resource_usage_details_model['code'] = 'testString'
        resource_usage_details_model['message'] = 'testString'

        # Construct a json representation of a ResponseAccepted model
        response_accepted_model_json = {}
        response_accepted_model_json['resources'] = [resource_usage_details_model]

        # Construct a model instance of ResponseAccepted by calling from_dict on the json representation
        response_accepted_model = ResponseAccepted.from_dict(response_accepted_model_json)
        assert response_accepted_model != False

        # Construct a model instance of ResponseAccepted by calling from_dict on the json representation
        response_accepted_model_dict = ResponseAccepted.from_dict(response_accepted_model_json).__dict__
        response_accepted_model2 = ResponseAccepted(**response_accepted_model_dict)

        # Verify the model instances are equivalent
        assert response_accepted_model == response_accepted_model2

        # Convert model instance back to dict and verify no loss of data
        response_accepted_model_json2 = response_accepted_model.to_dict()
        assert response_accepted_model_json2 == response_accepted_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
