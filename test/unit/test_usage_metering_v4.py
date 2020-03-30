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
import responses
from platform_services.usage_metering_v4 import *


service = UsageMeteringV4(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://billing.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Default
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for report_resource_usage
#-----------------------------------------------------------------------------
class TestReportResourceUsage():

    #--------------------------------------------------------
    # report_resource_usage()
    #--------------------------------------------------------
    @responses.activate
    def test_report_resource_usage_all_params(self):
        # Set up mock
        url = base_url + '/v4/metering/resources/testString/usage'
        mock_response = '{"resources": [{"status": 6, "location": "location", "code": "code", "message": "message"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a MeasureAndQuantity model
        measure_and_quantity_model = {}
        measure_and_quantity_model['measure'] = 'STORAGE' 
        measure_and_quantity_model['quantity'] = { 'foo': 'bar' } 

        # Construct a dict representation of a ResourceInstanceUsage model
        resource_instance_usage_model = {}
        resource_instance_usage_model['resource_instance_id'] = 'crn:v1:bluemix:public:database-service:us-south:a/1c8ae972c35e470d994b6faff9494ce1:793ff3d3-9fe3-4329-9ea0-404703a3c371::' 
        resource_instance_usage_model['plan_id'] = 'database-lite' 
        resource_instance_usage_model['region'] = 'us-south' 
        resource_instance_usage_model['start'] = 1485907200000 
        resource_instance_usage_model['end'] = 1485907200000 
        resource_instance_usage_model['measured_usage'] = [measure_and_quantity_model] 
        resource_instance_usage_model['consumer_id'] = 'cf-application:ed20abbe-8870-44e6-90f7-56d764c21127' 

        # Set up parameter values
        resource_id = 'testString'
        resource_instance_usage = [resource_instance_usage_model]

        # Invoke method
        response = service.report_resource_usage(
            resource_id,
            resource_instance_usage
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == resource_instance_usage


    #--------------------------------------------------------
    # test_report_resource_usage_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_report_resource_usage_required_params(self):
        # Set up mock
        url = base_url + '/v4/metering/resources/testString/usage'
        mock_response = '{"resources": [{"status": 6, "location": "location", "code": "code", "message": "message"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a MeasureAndQuantity model
        measure_and_quantity_model = {}
        measure_and_quantity_model['measure'] = 'STORAGE' 
        measure_and_quantity_model['quantity'] = { 'foo': 'bar' } 

        # Construct a dict representation of a ResourceInstanceUsage model
        resource_instance_usage_model = {}
        resource_instance_usage_model['resource_instance_id'] = 'crn:v1:bluemix:public:database-service:us-south:a/1c8ae972c35e470d994b6faff9494ce1:793ff3d3-9fe3-4329-9ea0-404703a3c371::' 
        resource_instance_usage_model['plan_id'] = 'database-lite' 
        resource_instance_usage_model['region'] = 'us-south' 
        resource_instance_usage_model['start'] = 1485907200000 
        resource_instance_usage_model['end'] = 1485907200000 
        resource_instance_usage_model['measured_usage'] = [measure_and_quantity_model] 
        resource_instance_usage_model['consumer_id'] = 'cf-application:ed20abbe-8870-44e6-90f7-56d764c21127' 

        # Set up parameter values
        resource_id = 'testString'
        resource_instance_usage = [resource_instance_usage_model]

        # Invoke method
        response = service.report_resource_usage(
            resource_id,
            resource_instance_usage
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == resource_instance_usage


#-----------------------------------------------------------------------------
# Test Class for report_cfresource_usage
#-----------------------------------------------------------------------------
class TestReportCfresourceUsage():

    #--------------------------------------------------------
    # report_cfresource_usage()
    #--------------------------------------------------------
    @responses.activate
    def test_report_cfresource_usage_all_params(self):
        # Set up mock
        url = base_url + '/v1/metering/resources/testString/usage'
        mock_response = '{"resources": [{"status": 6, "location": "location", "code": "code", "message": "message"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a MeasureAndQuantity model
        measure_and_quantity_model = {}
        measure_and_quantity_model['measure'] = 'STORAGE' 
        measure_and_quantity_model['quantity'] = { 'foo': 'bar' } 

        # Construct a dict representation of a CfResourceInstanceUsage model
        cf_resource_instance_usage_model = {}
        cf_resource_instance_usage_model['organization_id'] = 'Public: us-south:102d9527-315a-4a71-afc2-068b1db6d68e Syndicated: ibm:dys0:us-south:e2566380-89cf-4c38-9290-7eb48cfca8f9' 
        cf_resource_instance_usage_model['space_id'] = '89f0839a-812c-4180-8494-a453514c55e6' 
        cf_resource_instance_usage_model['resource_instance_id'] = '5ca426de-5091-4f2f-8d87-28d37e7ff711' 
        cf_resource_instance_usage_model['plan_id'] = 'database-lite' 
        cf_resource_instance_usage_model['region'] = 'us-south' 
        cf_resource_instance_usage_model['start'] = 1485907200000 
        cf_resource_instance_usage_model['end'] = 1485907200000 
        cf_resource_instance_usage_model['measured_usage'] = [measure_and_quantity_model] 
        cf_resource_instance_usage_model['consumer_id'] = 'cf-application:ed20abbe-8870-44e6-90f7-56d764c21127' 

        # Set up parameter values
        resource_id = 'testString'
        cf_resource_instance_usage = [cf_resource_instance_usage_model]

        # Invoke method
        response = service.report_cfresource_usage(
            resource_id,
            cf_resource_instance_usage
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == cf_resource_instance_usage


    #--------------------------------------------------------
    # test_report_cfresource_usage_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_report_cfresource_usage_required_params(self):
        # Set up mock
        url = base_url + '/v1/metering/resources/testString/usage'
        mock_response = '{"resources": [{"status": 6, "location": "location", "code": "code", "message": "message"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a MeasureAndQuantity model
        measure_and_quantity_model = {}
        measure_and_quantity_model['measure'] = 'STORAGE' 
        measure_and_quantity_model['quantity'] = { 'foo': 'bar' } 

        # Construct a dict representation of a CfResourceInstanceUsage model
        cf_resource_instance_usage_model = {}
        cf_resource_instance_usage_model['organization_id'] = 'Public: us-south:102d9527-315a-4a71-afc2-068b1db6d68e Syndicated: ibm:dys0:us-south:e2566380-89cf-4c38-9290-7eb48cfca8f9' 
        cf_resource_instance_usage_model['space_id'] = '89f0839a-812c-4180-8494-a453514c55e6' 
        cf_resource_instance_usage_model['resource_instance_id'] = '5ca426de-5091-4f2f-8d87-28d37e7ff711' 
        cf_resource_instance_usage_model['plan_id'] = 'database-lite' 
        cf_resource_instance_usage_model['region'] = 'us-south' 
        cf_resource_instance_usage_model['start'] = 1485907200000 
        cf_resource_instance_usage_model['end'] = 1485907200000 
        cf_resource_instance_usage_model['measured_usage'] = [measure_and_quantity_model] 
        cf_resource_instance_usage_model['consumer_id'] = 'cf-application:ed20abbe-8870-44e6-90f7-56d764c21127' 

        # Set up parameter values
        resource_id = 'testString'
        cf_resource_instance_usage = [cf_resource_instance_usage_model]

        # Invoke method
        response = service.report_cfresource_usage(
            resource_id,
            cf_resource_instance_usage
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == cf_resource_instance_usage


# endregion
##############################################################################
# End of Service: Default
##############################################################################

