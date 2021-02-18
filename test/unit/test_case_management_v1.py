# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
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
Unit Tests for CaseManagementV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import io
import json
import pytest
import re
import requests
import responses
import tempfile
import urllib
from ibm_platform_services.case_management_v1 import *


service = CaseManagementV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://support-center.cloud.ibm.com/case-management/v1'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Default
##############################################################################
# region

class TestGetCases():
    """
    Test Class for get_cases
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_cases_all_params(self):
        """
        get_cases()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases')
        mock_response = '{"total_count": 11, "first": {"href": "href"}, "next": {"href": "href"}, "previous": {"href": "href"}, "last": {"href": "href"}, "cases": [{"number": "number", "short_description": "short_description", "description": "description", "created_at": "created_at", "created_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "updated_at": "updated_at", "updated_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "contact_type": "Cloud Support Center", "contact": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "status": "status", "severity": 8, "support_tier": "Free", "resolution": "resolution", "close_notes": "close_notes", "eu": {"support": false, "data_center": "data_center"}, "watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}], "offering": {"name": "name", "type": {"group": "crn_service_name", "key": "key", "kind": "kind", "id": "id"}}, "resources": [{"crn": "crn", "name": "name", "type": "type", "url": "url", "note": "note"}], "comments": [{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        offset = 38
        limit = 38
        search = 'testString'
        sort = 'number'
        status = ['new']
        fields = ['number']

        # Invoke method
        response = service.get_cases(
            offset=offset,
            limit=limit,
            search=search,
            sort=sort,
            status=status,
            fields=fields,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'search={}'.format(search) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'status={}'.format(','.join(status)) in query_string
        assert 'fields={}'.format(','.join(fields)) in query_string


    @responses.activate
    def test_get_cases_required_params(self):
        """
        test_get_cases_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases')
        mock_response = '{"total_count": 11, "first": {"href": "href"}, "next": {"href": "href"}, "previous": {"href": "href"}, "last": {"href": "href"}, "cases": [{"number": "number", "short_description": "short_description", "description": "description", "created_at": "created_at", "created_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "updated_at": "updated_at", "updated_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "contact_type": "Cloud Support Center", "contact": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "status": "status", "severity": 8, "support_tier": "Free", "resolution": "resolution", "close_notes": "close_notes", "eu": {"support": false, "data_center": "data_center"}, "watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}], "offering": {"name": "name", "type": {"group": "crn_service_name", "key": "key", "kind": "kind", "id": "id"}}, "resources": [{"crn": "crn", "name": "name", "type": "type", "url": "url", "note": "note"}], "comments": [{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_cases()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestCreateCase():
    """
    Test Class for create_case
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_case_all_params(self):
        """
        create_case()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases')
        mock_response = '{"number": "number", "short_description": "short_description", "description": "description", "created_at": "created_at", "created_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "updated_at": "updated_at", "updated_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "contact_type": "Cloud Support Center", "contact": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "status": "status", "severity": 8, "support_tier": "Free", "resolution": "resolution", "close_notes": "close_notes", "eu": {"support": false, "data_center": "data_center"}, "watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}], "offering": {"name": "name", "type": {"group": "crn_service_name", "key": "key", "kind": "kind", "id": "id"}}, "resources": [{"crn": "crn", "name": "name", "type": "type", "url": "url", "note": "note"}], "comments": [{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CasePayloadEu model
        case_payload_eu_model = {}
        case_payload_eu_model['supported'] = True
        case_payload_eu_model['data_center'] = 38

        # Construct a dict representation of a OfferingType model
        offering_type_model = {}
        offering_type_model['group'] = 'crn_service_name'
        offering_type_model['key'] = 'testString'
        offering_type_model['kind'] = 'testString'
        offering_type_model['id'] = 'testString'

        # Construct a dict representation of a Offering model
        offering_model = {}
        offering_model['name'] = 'testString'
        offering_model['type'] = offering_type_model

        # Construct a dict representation of a ResourcePayload model
        resource_payload_model = {}
        resource_payload_model['crn'] = 'testString'
        resource_payload_model['type'] = 'testString'
        resource_payload_model['id'] = 72.5
        resource_payload_model['note'] = 'testString'

        # Construct a dict representation of a User model
        user_model = {}
        user_model['realm'] = 'IBMid'
        user_model['user_id'] = 'abc@ibm.com'

        # Set up parameter values
        type = 'technical'
        subject = 'testString'
        description = 'testString'
        severity = 1
        eu = case_payload_eu_model
        offering = offering_model
        resources = [resource_payload_model]
        watchlist = [user_model]
        invoice_number = 'testString'
        sla_credit_request = True

        # Invoke method
        response = service.create_case(
            type,
            subject,
            description,
            severity=severity,
            eu=eu,
            offering=offering,
            resources=resources,
            watchlist=watchlist,
            invoice_number=invoice_number,
            sla_credit_request=sla_credit_request,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'technical'
        assert req_body['subject'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['severity'] == 1
        assert req_body['eu'] == case_payload_eu_model
        assert req_body['offering'] == offering_model
        assert req_body['resources'] == [resource_payload_model]
        assert req_body['watchlist'] == [user_model]
        assert req_body['invoice_number'] == 'testString'
        assert req_body['sla_credit_request'] == True


    @responses.activate
    def test_create_case_value_error(self):
        """
        test_create_case_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases')
        mock_response = '{"number": "number", "short_description": "short_description", "description": "description", "created_at": "created_at", "created_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "updated_at": "updated_at", "updated_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "contact_type": "Cloud Support Center", "contact": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "status": "status", "severity": 8, "support_tier": "Free", "resolution": "resolution", "close_notes": "close_notes", "eu": {"support": false, "data_center": "data_center"}, "watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}], "offering": {"name": "name", "type": {"group": "crn_service_name", "key": "key", "kind": "kind", "id": "id"}}, "resources": [{"crn": "crn", "name": "name", "type": "type", "url": "url", "note": "note"}], "comments": [{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CasePayloadEu model
        case_payload_eu_model = {}
        case_payload_eu_model['supported'] = True
        case_payload_eu_model['data_center'] = 38

        # Construct a dict representation of a OfferingType model
        offering_type_model = {}
        offering_type_model['group'] = 'crn_service_name'
        offering_type_model['key'] = 'testString'
        offering_type_model['kind'] = 'testString'
        offering_type_model['id'] = 'testString'

        # Construct a dict representation of a Offering model
        offering_model = {}
        offering_model['name'] = 'testString'
        offering_model['type'] = offering_type_model

        # Construct a dict representation of a ResourcePayload model
        resource_payload_model = {}
        resource_payload_model['crn'] = 'testString'
        resource_payload_model['type'] = 'testString'
        resource_payload_model['id'] = 72.5
        resource_payload_model['note'] = 'testString'

        # Construct a dict representation of a User model
        user_model = {}
        user_model['realm'] = 'IBMid'
        user_model['user_id'] = 'abc@ibm.com'

        # Set up parameter values
        type = 'technical'
        subject = 'testString'
        description = 'testString'
        severity = 1
        eu = case_payload_eu_model
        offering = offering_model
        resources = [resource_payload_model]
        watchlist = [user_model]
        invoice_number = 'testString'
        sla_credit_request = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "type": type,
            "subject": subject,
            "description": description,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_case(**req_copy)



class TestGetCase():
    """
    Test Class for get_case
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_case_all_params(self):
        """
        get_case()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString')
        mock_response = '{"number": "number", "short_description": "short_description", "description": "description", "created_at": "created_at", "created_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "updated_at": "updated_at", "updated_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "contact_type": "Cloud Support Center", "contact": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "status": "status", "severity": 8, "support_tier": "Free", "resolution": "resolution", "close_notes": "close_notes", "eu": {"support": false, "data_center": "data_center"}, "watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}], "offering": {"name": "name", "type": {"group": "crn_service_name", "key": "key", "kind": "kind", "id": "id"}}, "resources": [{"crn": "crn", "name": "name", "type": "type", "url": "url", "note": "note"}], "comments": [{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'
        fields = ['number']

        # Invoke method
        response = service.get_case(
            case_number,
            fields=fields,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'fields={}'.format(','.join(fields)) in query_string


    @responses.activate
    def test_get_case_required_params(self):
        """
        test_get_case_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString')
        mock_response = '{"number": "number", "short_description": "short_description", "description": "description", "created_at": "created_at", "created_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "updated_at": "updated_at", "updated_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "contact_type": "Cloud Support Center", "contact": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "status": "status", "severity": 8, "support_tier": "Free", "resolution": "resolution", "close_notes": "close_notes", "eu": {"support": false, "data_center": "data_center"}, "watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}], "offering": {"name": "name", "type": {"group": "crn_service_name", "key": "key", "kind": "kind", "id": "id"}}, "resources": [{"crn": "crn", "name": "name", "type": "type", "url": "url", "note": "note"}], "comments": [{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'

        # Invoke method
        response = service.get_case(
            case_number,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_case_value_error(self):
        """
        test_get_case_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString')
        mock_response = '{"number": "number", "short_description": "short_description", "description": "description", "created_at": "created_at", "created_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "updated_at": "updated_at", "updated_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "contact_type": "Cloud Support Center", "contact": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "status": "status", "severity": 8, "support_tier": "Free", "resolution": "resolution", "close_notes": "close_notes", "eu": {"support": false, "data_center": "data_center"}, "watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}], "offering": {"name": "name", "type": {"group": "crn_service_name", "key": "key", "kind": "kind", "id": "id"}}, "resources": [{"crn": "crn", "name": "name", "type": "type", "url": "url", "note": "note"}], "comments": [{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "case_number": case_number,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_case(**req_copy)



class TestUpdateCaseStatus():
    """
    Test Class for update_case_status
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_case_status_all_params(self):
        """
        update_case_status()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString/status')
        mock_response = '{"number": "number", "short_description": "short_description", "description": "description", "created_at": "created_at", "created_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "updated_at": "updated_at", "updated_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "contact_type": "Cloud Support Center", "contact": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "status": "status", "severity": 8, "support_tier": "Free", "resolution": "resolution", "close_notes": "close_notes", "eu": {"support": false, "data_center": "data_center"}, "watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}], "offering": {"name": "name", "type": {"group": "crn_service_name", "key": "key", "kind": "kind", "id": "id"}}, "resources": [{"crn": "crn", "name": "name", "type": "type", "url": "url", "note": "note"}], "comments": [{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ResolvePayload model
        status_payload_model = {}
        status_payload_model['action'] = 'resolve'
        status_payload_model['comment'] = 'It was actually a mistake'
        status_payload_model['resolution_code'] = 1

        # Set up parameter values
        case_number = 'testString'
        status_payload = status_payload_model

        # Invoke method
        response = service.update_case_status(
            case_number,
            status_payload,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == status_payload


    @responses.activate
    def test_update_case_status_value_error(self):
        """
        test_update_case_status_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString/status')
        mock_response = '{"number": "number", "short_description": "short_description", "description": "description", "created_at": "created_at", "created_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "updated_at": "updated_at", "updated_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "contact_type": "Cloud Support Center", "contact": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "status": "status", "severity": 8, "support_tier": "Free", "resolution": "resolution", "close_notes": "close_notes", "eu": {"support": false, "data_center": "data_center"}, "watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}], "offering": {"name": "name", "type": {"group": "crn_service_name", "key": "key", "kind": "kind", "id": "id"}}, "resources": [{"crn": "crn", "name": "name", "type": "type", "url": "url", "note": "note"}], "comments": [{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ResolvePayload model
        status_payload_model = {}
        status_payload_model['action'] = 'resolve'
        status_payload_model['comment'] = 'It was actually a mistake'
        status_payload_model['resolution_code'] = 1

        # Set up parameter values
        case_number = 'testString'
        status_payload = status_payload_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "case_number": case_number,
            "status_payload": status_payload,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_case_status(**req_copy)



class TestAddComment():
    """
    Test Class for add_comment
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_add_comment_all_params(self):
        """
        add_comment()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString/comments')
        mock_response = '{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'
        comment = 'This is a test comment'

        # Invoke method
        response = service.add_comment(
            case_number,
            comment,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['comment'] == 'This is a test comment'


    @responses.activate
    def test_add_comment_value_error(self):
        """
        test_add_comment_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString/comments')
        mock_response = '{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'
        comment = 'This is a test comment'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "case_number": case_number,
            "comment": comment,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.add_comment(**req_copy)



class TestAddWatchlist():
    """
    Test Class for add_watchlist
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_add_watchlist_all_params(self):
        """
        add_watchlist()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString/watchlist')
        mock_response = '{"added": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "failed": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a User model
        user_model = {}
        user_model['realm'] = 'IBMid'
        user_model['user_id'] = 'abc@ibm.com'

        # Set up parameter values
        case_number = 'testString'
        watchlist = [user_model]

        # Invoke method
        response = service.add_watchlist(
            case_number,
            watchlist=watchlist,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['watchlist'] == [user_model]


    @responses.activate
    def test_add_watchlist_value_error(self):
        """
        test_add_watchlist_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString/watchlist')
        mock_response = '{"added": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "failed": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a User model
        user_model = {}
        user_model['realm'] = 'IBMid'
        user_model['user_id'] = 'abc@ibm.com'

        # Set up parameter values
        case_number = 'testString'
        watchlist = [user_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "case_number": case_number,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.add_watchlist(**req_copy)



class TestRemoveWatchlist():
    """
    Test Class for remove_watchlist
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_remove_watchlist_all_params(self):
        """
        remove_watchlist()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString/watchlist')
        mock_response = '{"watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a User model
        user_model = {}
        user_model['realm'] = 'IBMid'
        user_model['user_id'] = 'abc@ibm.com'

        # Set up parameter values
        case_number = 'testString'
        watchlist = [user_model]

        # Invoke method
        response = service.remove_watchlist(
            case_number,
            watchlist=watchlist,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['watchlist'] == [user_model]


    @responses.activate
    def test_remove_watchlist_value_error(self):
        """
        test_remove_watchlist_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString/watchlist')
        mock_response = '{"watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a User model
        user_model = {}
        user_model['realm'] = 'IBMid'
        user_model['user_id'] = 'abc@ibm.com'

        # Set up parameter values
        case_number = 'testString'
        watchlist = [user_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "case_number": case_number,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.remove_watchlist(**req_copy)



class TestAddResource():
    """
    Test Class for add_resource
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_add_resource_all_params(self):
        """
        add_resource()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString/resources')
        mock_response = '{"crn": "crn", "name": "name", "type": "type", "url": "url", "note": "note"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'
        crn = 'testString'
        type = 'testString'
        id = 72.5
        note = 'testString'

        # Invoke method
        response = service.add_resource(
            case_number,
            crn=crn,
            type=type,
            id=id,
            note=note,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['crn'] == 'testString'
        assert req_body['type'] == 'testString'
        assert req_body['id'] == 72.5
        assert req_body['note'] == 'testString'


    @responses.activate
    def test_add_resource_value_error(self):
        """
        test_add_resource_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString/resources')
        mock_response = '{"crn": "crn", "name": "name", "type": "type", "url": "url", "note": "note"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'
        crn = 'testString'
        type = 'testString'
        id = 72.5
        note = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "case_number": case_number,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.add_resource(**req_copy)



class TestUploadFile():
    """
    Test Class for upload_file
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_upload_file_all_params(self):
        """
        upload_file()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString/attachments')
        mock_response = '{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a FileWithMetadata model
        file_with_metadata_model = {}
        file_with_metadata_model['data'] = io.BytesIO(b'This is a mock file.').getvalue()
        file_with_metadata_model['filename'] = 'testString'
        file_with_metadata_model['content_type'] = 'testString'

        # Set up parameter values
        case_number = 'testString'
        file = [file_with_metadata_model]

        # Invoke method
        response = service.upload_file(
            case_number,
            file,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_upload_file_value_error(self):
        """
        test_upload_file_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString/attachments')
        mock_response = '{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a FileWithMetadata model
        file_with_metadata_model = {}
        file_with_metadata_model['data'] = io.BytesIO(b'This is a mock file.').getvalue()
        file_with_metadata_model['filename'] = 'testString'
        file_with_metadata_model['content_type'] = 'testString'

        # Set up parameter values
        case_number = 'testString'
        file = [file_with_metadata_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "case_number": case_number,
            "file": file,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.upload_file(**req_copy)



class TestDownloadFile():
    """
    Test Class for download_file
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_download_file_all_params(self):
        """
        download_file()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString/attachments/testString')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/octet-stream',
                      status=200)

        # Set up parameter values
        case_number = 'testString'
        file_id = 'testString'

        # Invoke method
        response = service.download_file(
            case_number,
            file_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_download_file_value_error(self):
        """
        test_download_file_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString/attachments/testString')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/octet-stream',
                      status=200)

        # Set up parameter values
        case_number = 'testString'
        file_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "case_number": case_number,
            "file_id": file_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.download_file(**req_copy)



class TestDeleteFile():
    """
    Test Class for delete_file
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_file_all_params(self):
        """
        delete_file()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString/attachments/testString')
        mock_response = '{"attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'
        file_id = 'testString'

        # Invoke method
        response = service.delete_file(
            case_number,
            file_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_file_value_error(self):
        """
        test_delete_file_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/cases/testString/attachments/testString')
        mock_response = '{"attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'
        file_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "case_number": case_number,
            "file_id": file_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_file(**req_copy)



# endregion
##############################################################################
# End of Service: Default
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestAttachment():
    """
    Test Class for Attachment
    """

    def test_attachment_serialization(self):
        """
        Test serialization/deserialization for Attachment
        """

        # Construct a json representation of a Attachment model
        attachment_model_json = {}
        attachment_model_json['id'] = 'testString'
        attachment_model_json['filename'] = 'testString'
        attachment_model_json['size_in_bytes'] = 38
        attachment_model_json['created_at'] = 'testString'
        attachment_model_json['url'] = 'testString'

        # Construct a model instance of Attachment by calling from_dict on the json representation
        attachment_model = Attachment.from_dict(attachment_model_json)
        assert attachment_model != False

        # Construct a model instance of Attachment by calling from_dict on the json representation
        attachment_model_dict = Attachment.from_dict(attachment_model_json).__dict__
        attachment_model2 = Attachment(**attachment_model_dict)

        # Verify the model instances are equivalent
        assert attachment_model == attachment_model2

        # Convert model instance back to dict and verify no loss of data
        attachment_model_json2 = attachment_model.to_dict()
        assert attachment_model_json2 == attachment_model_json

class TestAttachmentList():
    """
    Test Class for AttachmentList
    """

    def test_attachment_list_serialization(self):
        """
        Test serialization/deserialization for AttachmentList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attachment_model = {} # Attachment
        attachment_model['id'] = 'string'
        attachment_model['filename'] = 'string'
        attachment_model['size_in_bytes'] = 0
        attachment_model['created_at'] = '2019-07-31 07:26:36'
        attachment_model['url'] = 'string'

        # Construct a json representation of a AttachmentList model
        attachment_list_model_json = {}
        attachment_list_model_json['attachments'] = [attachment_model]

        # Construct a model instance of AttachmentList by calling from_dict on the json representation
        attachment_list_model = AttachmentList.from_dict(attachment_list_model_json)
        assert attachment_list_model != False

        # Construct a model instance of AttachmentList by calling from_dict on the json representation
        attachment_list_model_dict = AttachmentList.from_dict(attachment_list_model_json).__dict__
        attachment_list_model2 = AttachmentList(**attachment_list_model_dict)

        # Verify the model instances are equivalent
        assert attachment_list_model == attachment_list_model2

        # Convert model instance back to dict and verify no loss of data
        attachment_list_model_json2 = attachment_list_model.to_dict()
        assert attachment_list_model_json2 == attachment_list_model_json

class TestCase():
    """
    Test Class for Case
    """

    def test_case_serialization(self):
        """
        Test serialization/deserialization for Case
        """

        # Construct dict forms of any model objects needed in order to build this model.

        user_model = {} # User
        user_model['name'] = 'testString'
        user_model['realm'] = 'IBMid'
        user_model['user_id'] = 'abc@ibm.com'

        case_eu_model = {} # CaseEu
        case_eu_model['support'] = True
        case_eu_model['data_center'] = 'testString'

        attachment_model = {} # Attachment
        attachment_model['id'] = 'testString'
        attachment_model['filename'] = 'testString'
        attachment_model['size_in_bytes'] = 38
        attachment_model['created_at'] = 'testString'
        attachment_model['url'] = 'testString'

        offering_type_model = {} # OfferingType
        offering_type_model['group'] = 'crn_service_name'
        offering_type_model['key'] = 'testString'
        offering_type_model['kind'] = 'testString'
        offering_type_model['id'] = 'testString'

        offering_model = {} # Offering
        offering_model['name'] = 'testString'
        offering_model['type'] = offering_type_model

        resource_model = {} # Resource
        resource_model['crn'] = 'testString'
        resource_model['name'] = 'testString'
        resource_model['type'] = 'testString'
        resource_model['url'] = 'testString'
        resource_model['note'] = 'testString'

        comment_model = {} # Comment
        comment_model['value'] = 'testString'
        comment_model['added_at'] = 'testString'
        comment_model['added_by'] = user_model

        # Construct a json representation of a Case model
        case_model_json = {}
        case_model_json['number'] = 'testString'
        case_model_json['short_description'] = 'testString'
        case_model_json['description'] = 'testString'
        case_model_json['created_at'] = 'testString'
        case_model_json['created_by'] = user_model
        case_model_json['updated_at'] = 'testString'
        case_model_json['updated_by'] = user_model
        case_model_json['contact_type'] = 'Cloud Support Center'
        case_model_json['contact'] = user_model
        case_model_json['status'] = 'testString'
        case_model_json['severity'] = 72.5
        case_model_json['support_tier'] = 'Free'
        case_model_json['resolution'] = 'testString'
        case_model_json['close_notes'] = 'testString'
        case_model_json['eu'] = case_eu_model
        case_model_json['watchlist'] = [user_model]
        case_model_json['attachments'] = [attachment_model]
        case_model_json['offering'] = offering_model
        case_model_json['resources'] = [resource_model]
        case_model_json['comments'] = [comment_model]

        # Construct a model instance of Case by calling from_dict on the json representation
        case_model = Case.from_dict(case_model_json)
        assert case_model != False

        # Construct a model instance of Case by calling from_dict on the json representation
        case_model_dict = Case.from_dict(case_model_json).__dict__
        case_model2 = Case(**case_model_dict)

        # Verify the model instances are equivalent
        assert case_model == case_model2

        # Convert model instance back to dict and verify no loss of data
        case_model_json2 = case_model.to_dict()
        assert case_model_json2 == case_model_json

class TestCaseEu():
    """
    Test Class for CaseEu
    """

    def test_case_eu_serialization(self):
        """
        Test serialization/deserialization for CaseEu
        """

        # Construct a json representation of a CaseEu model
        case_eu_model_json = {}
        case_eu_model_json['support'] = True
        case_eu_model_json['data_center'] = 'testString'

        # Construct a model instance of CaseEu by calling from_dict on the json representation
        case_eu_model = CaseEu.from_dict(case_eu_model_json)
        assert case_eu_model != False

        # Construct a model instance of CaseEu by calling from_dict on the json representation
        case_eu_model_dict = CaseEu.from_dict(case_eu_model_json).__dict__
        case_eu_model2 = CaseEu(**case_eu_model_dict)

        # Verify the model instances are equivalent
        assert case_eu_model == case_eu_model2

        # Convert model instance back to dict and verify no loss of data
        case_eu_model_json2 = case_eu_model.to_dict()
        assert case_eu_model_json2 == case_eu_model_json

class TestCaseList():
    """
    Test Class for CaseList
    """

    def test_case_list_serialization(self):
        """
        Test serialization/deserialization for CaseList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        pagination_link_model = {} # PaginationLink
        pagination_link_model['href'] = 'testString'

        user_model = {} # User
        user_model['name'] = 'testString'
        user_model['realm'] = 'IBMid'
        user_model['user_id'] = 'abc@ibm.com'

        case_eu_model = {} # CaseEu
        case_eu_model['support'] = True
        case_eu_model['data_center'] = 'testString'

        attachment_model = {} # Attachment
        attachment_model['id'] = 'testString'
        attachment_model['filename'] = 'testString'
        attachment_model['size_in_bytes'] = 38
        attachment_model['created_at'] = 'testString'
        attachment_model['url'] = 'testString'

        offering_type_model = {} # OfferingType
        offering_type_model['group'] = 'crn_service_name'
        offering_type_model['key'] = 'testString'
        offering_type_model['kind'] = 'testString'
        offering_type_model['id'] = 'testString'

        offering_model = {} # Offering
        offering_model['name'] = 'testString'
        offering_model['type'] = offering_type_model

        resource_model = {} # Resource
        resource_model['crn'] = 'testString'
        resource_model['name'] = 'testString'
        resource_model['type'] = 'testString'
        resource_model['url'] = 'testString'
        resource_model['note'] = 'testString'

        comment_model = {} # Comment
        comment_model['value'] = 'testString'
        comment_model['added_at'] = 'testString'
        comment_model['added_by'] = user_model

        case_model = {} # Case
        case_model['number'] = 'testString'
        case_model['short_description'] = 'testString'
        case_model['description'] = 'testString'
        case_model['created_at'] = 'testString'
        case_model['created_by'] = user_model
        case_model['updated_at'] = 'testString'
        case_model['updated_by'] = user_model
        case_model['contact_type'] = 'Cloud Support Center'
        case_model['contact'] = user_model
        case_model['status'] = 'testString'
        case_model['severity'] = 72.5
        case_model['support_tier'] = 'Free'
        case_model['resolution'] = 'testString'
        case_model['close_notes'] = 'testString'
        case_model['eu'] = case_eu_model
        case_model['watchlist'] = [user_model]
        case_model['attachments'] = [attachment_model]
        case_model['offering'] = offering_model
        case_model['resources'] = [resource_model]
        case_model['comments'] = [comment_model]

        # Construct a json representation of a CaseList model
        case_list_model_json = {}
        case_list_model_json['total_count'] = 38
        case_list_model_json['first'] = pagination_link_model
        case_list_model_json['next'] = pagination_link_model
        case_list_model_json['previous'] = pagination_link_model
        case_list_model_json['last'] = pagination_link_model
        case_list_model_json['cases'] = [case_model]

        # Construct a model instance of CaseList by calling from_dict on the json representation
        case_list_model = CaseList.from_dict(case_list_model_json)
        assert case_list_model != False

        # Construct a model instance of CaseList by calling from_dict on the json representation
        case_list_model_dict = CaseList.from_dict(case_list_model_json).__dict__
        case_list_model2 = CaseList(**case_list_model_dict)

        # Verify the model instances are equivalent
        assert case_list_model == case_list_model2

        # Convert model instance back to dict and verify no loss of data
        case_list_model_json2 = case_list_model.to_dict()
        assert case_list_model_json2 == case_list_model_json

class TestCasePayloadEu():
    """
    Test Class for CasePayloadEu
    """

    def test_case_payload_eu_serialization(self):
        """
        Test serialization/deserialization for CasePayloadEu
        """

        # Construct a json representation of a CasePayloadEu model
        case_payload_eu_model_json = {}
        case_payload_eu_model_json['supported'] = True
        case_payload_eu_model_json['data_center'] = 38

        # Construct a model instance of CasePayloadEu by calling from_dict on the json representation
        case_payload_eu_model = CasePayloadEu.from_dict(case_payload_eu_model_json)
        assert case_payload_eu_model != False

        # Construct a model instance of CasePayloadEu by calling from_dict on the json representation
        case_payload_eu_model_dict = CasePayloadEu.from_dict(case_payload_eu_model_json).__dict__
        case_payload_eu_model2 = CasePayloadEu(**case_payload_eu_model_dict)

        # Verify the model instances are equivalent
        assert case_payload_eu_model == case_payload_eu_model2

        # Convert model instance back to dict and verify no loss of data
        case_payload_eu_model_json2 = case_payload_eu_model.to_dict()
        assert case_payload_eu_model_json2 == case_payload_eu_model_json

class TestComment():
    """
    Test Class for Comment
    """

    def test_comment_serialization(self):
        """
        Test serialization/deserialization for Comment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        user_model = {} # User
        user_model['name'] = 'testString'
        user_model['realm'] = 'IBMid'
        user_model['user_id'] = 'abc@ibm.com'

        # Construct a json representation of a Comment model
        comment_model_json = {}
        comment_model_json['value'] = 'testString'
        comment_model_json['added_at'] = 'testString'
        comment_model_json['added_by'] = user_model

        # Construct a model instance of Comment by calling from_dict on the json representation
        comment_model = Comment.from_dict(comment_model_json)
        assert comment_model != False

        # Construct a model instance of Comment by calling from_dict on the json representation
        comment_model_dict = Comment.from_dict(comment_model_json).__dict__
        comment_model2 = Comment(**comment_model_dict)

        # Verify the model instances are equivalent
        assert comment_model == comment_model2

        # Convert model instance back to dict and verify no loss of data
        comment_model_json2 = comment_model.to_dict()
        assert comment_model_json2 == comment_model_json

class TestOffering():
    """
    Test Class for Offering
    """

    def test_offering_serialization(self):
        """
        Test serialization/deserialization for Offering
        """

        # Construct dict forms of any model objects needed in order to build this model.

        offering_type_model = {} # OfferingType
        offering_type_model['group'] = 'crn_service_name'
        offering_type_model['key'] = 'testString'
        offering_type_model['kind'] = 'testString'
        offering_type_model['id'] = 'testString'

        # Construct a json representation of a Offering model
        offering_model_json = {}
        offering_model_json['name'] = 'testString'
        offering_model_json['type'] = offering_type_model

        # Construct a model instance of Offering by calling from_dict on the json representation
        offering_model = Offering.from_dict(offering_model_json)
        assert offering_model != False

        # Construct a model instance of Offering by calling from_dict on the json representation
        offering_model_dict = Offering.from_dict(offering_model_json).__dict__
        offering_model2 = Offering(**offering_model_dict)

        # Verify the model instances are equivalent
        assert offering_model == offering_model2

        # Convert model instance back to dict and verify no loss of data
        offering_model_json2 = offering_model.to_dict()
        assert offering_model_json2 == offering_model_json

class TestOfferingType():
    """
    Test Class for OfferingType
    """

    def test_offering_type_serialization(self):
        """
        Test serialization/deserialization for OfferingType
        """

        # Construct a json representation of a OfferingType model
        offering_type_model_json = {}
        offering_type_model_json['group'] = 'crn_service_name'
        offering_type_model_json['key'] = 'testString'
        offering_type_model_json['kind'] = 'testString'
        offering_type_model_json['id'] = 'testString'

        # Construct a model instance of OfferingType by calling from_dict on the json representation
        offering_type_model = OfferingType.from_dict(offering_type_model_json)
        assert offering_type_model != False

        # Construct a model instance of OfferingType by calling from_dict on the json representation
        offering_type_model_dict = OfferingType.from_dict(offering_type_model_json).__dict__
        offering_type_model2 = OfferingType(**offering_type_model_dict)

        # Verify the model instances are equivalent
        assert offering_type_model == offering_type_model2

        # Convert model instance back to dict and verify no loss of data
        offering_type_model_json2 = offering_type_model.to_dict()
        assert offering_type_model_json2 == offering_type_model_json

class TestPaginationLink():
    """
    Test Class for PaginationLink
    """

    def test_pagination_link_serialization(self):
        """
        Test serialization/deserialization for PaginationLink
        """

        # Construct a json representation of a PaginationLink model
        pagination_link_model_json = {}
        pagination_link_model_json['href'] = 'testString'

        # Construct a model instance of PaginationLink by calling from_dict on the json representation
        pagination_link_model = PaginationLink.from_dict(pagination_link_model_json)
        assert pagination_link_model != False

        # Construct a model instance of PaginationLink by calling from_dict on the json representation
        pagination_link_model_dict = PaginationLink.from_dict(pagination_link_model_json).__dict__
        pagination_link_model2 = PaginationLink(**pagination_link_model_dict)

        # Verify the model instances are equivalent
        assert pagination_link_model == pagination_link_model2

        # Convert model instance back to dict and verify no loss of data
        pagination_link_model_json2 = pagination_link_model.to_dict()
        assert pagination_link_model_json2 == pagination_link_model_json

class TestResource():
    """
    Test Class for Resource
    """

    def test_resource_serialization(self):
        """
        Test serialization/deserialization for Resource
        """

        # Construct a json representation of a Resource model
        resource_model_json = {}
        resource_model_json['crn'] = 'testString'
        resource_model_json['name'] = 'testString'
        resource_model_json['type'] = 'testString'
        resource_model_json['url'] = 'testString'
        resource_model_json['note'] = 'testString'

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

class TestResourcePayload():
    """
    Test Class for ResourcePayload
    """

    def test_resource_payload_serialization(self):
        """
        Test serialization/deserialization for ResourcePayload
        """

        # Construct a json representation of a ResourcePayload model
        resource_payload_model_json = {}
        resource_payload_model_json['crn'] = 'testString'
        resource_payload_model_json['type'] = 'testString'
        resource_payload_model_json['id'] = 72.5
        resource_payload_model_json['note'] = 'testString'

        # Construct a model instance of ResourcePayload by calling from_dict on the json representation
        resource_payload_model = ResourcePayload.from_dict(resource_payload_model_json)
        assert resource_payload_model != False

        # Construct a model instance of ResourcePayload by calling from_dict on the json representation
        resource_payload_model_dict = ResourcePayload.from_dict(resource_payload_model_json).__dict__
        resource_payload_model2 = ResourcePayload(**resource_payload_model_dict)

        # Verify the model instances are equivalent
        assert resource_payload_model == resource_payload_model2

        # Convert model instance back to dict and verify no loss of data
        resource_payload_model_json2 = resource_payload_model.to_dict()
        assert resource_payload_model_json2 == resource_payload_model_json

class TestUser():
    """
    Test Class for User
    """

    def test_user_serialization(self):
        """
        Test serialization/deserialization for User
        """

        # Construct a json representation of a User model
        user_model_json = {}
        user_model_json['name'] = 'testString'
        user_model_json['realm'] = 'IBMid'
        user_model_json['user_id'] = 'abc@ibm.com'

        # Construct a model instance of User by calling from_dict on the json representation
        user_model = User.from_dict(user_model_json)
        assert user_model != False

        # Construct a model instance of User by calling from_dict on the json representation
        user_model_dict = User.from_dict(user_model_json).__dict__
        user_model2 = User(**user_model_dict)

        # Verify the model instances are equivalent
        assert user_model == user_model2

        # Convert model instance back to dict and verify no loss of data
        user_model_json2 = user_model.to_dict()
        assert user_model_json2 == user_model_json

class TestWatchlist():
    """
    Test Class for Watchlist
    """

    def test_watchlist_serialization(self):
        """
        Test serialization/deserialization for Watchlist
        """

        # Construct dict forms of any model objects needed in order to build this model.

        user_model = {} # User
        user_model['name'] = 'testString'
        user_model['realm'] = 'IBMid'
        user_model['user_id'] = 'abc@ibm.com'

        # Construct a json representation of a Watchlist model
        watchlist_model_json = {}
        watchlist_model_json['watchlist'] = [user_model]

        # Construct a model instance of Watchlist by calling from_dict on the json representation
        watchlist_model = Watchlist.from_dict(watchlist_model_json)
        assert watchlist_model != False

        # Construct a model instance of Watchlist by calling from_dict on the json representation
        watchlist_model_dict = Watchlist.from_dict(watchlist_model_json).__dict__
        watchlist_model2 = Watchlist(**watchlist_model_dict)

        # Verify the model instances are equivalent
        assert watchlist_model == watchlist_model2

        # Convert model instance back to dict and verify no loss of data
        watchlist_model_json2 = watchlist_model.to_dict()
        assert watchlist_model_json2 == watchlist_model_json

class TestWatchlistAddResponse():
    """
    Test Class for WatchlistAddResponse
    """

    def test_watchlist_add_response_serialization(self):
        """
        Test serialization/deserialization for WatchlistAddResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        user_model = {} # User
        user_model['name'] = 'John Doe'
        user_model['realm'] = 'IBMid'
        user_model['user_id'] = 'johndoe@ibm.com'

        # Construct a json representation of a WatchlistAddResponse model
        watchlist_add_response_model_json = {}
        watchlist_add_response_model_json['added'] = [user_model]
        watchlist_add_response_model_json['failed'] = [user_model]

        # Construct a model instance of WatchlistAddResponse by calling from_dict on the json representation
        watchlist_add_response_model = WatchlistAddResponse.from_dict(watchlist_add_response_model_json)
        assert watchlist_add_response_model != False

        # Construct a model instance of WatchlistAddResponse by calling from_dict on the json representation
        watchlist_add_response_model_dict = WatchlistAddResponse.from_dict(watchlist_add_response_model_json).__dict__
        watchlist_add_response_model2 = WatchlistAddResponse(**watchlist_add_response_model_dict)

        # Verify the model instances are equivalent
        assert watchlist_add_response_model == watchlist_add_response_model2

        # Convert model instance back to dict and verify no loss of data
        watchlist_add_response_model_json2 = watchlist_add_response_model.to_dict()
        assert watchlist_add_response_model_json2 == watchlist_add_response_model_json

class TestAcceptPayload():
    """
    Test Class for AcceptPayload
    """

    def test_accept_payload_serialization(self):
        """
        Test serialization/deserialization for AcceptPayload
        """

        # Construct a json representation of a AcceptPayload model
        accept_payload_model_json = {}
        accept_payload_model_json['action'] = 'accept'
        accept_payload_model_json['comment'] = 'testString'

        # Construct a model instance of AcceptPayload by calling from_dict on the json representation
        accept_payload_model = AcceptPayload.from_dict(accept_payload_model_json)
        assert accept_payload_model != False

        # Construct a model instance of AcceptPayload by calling from_dict on the json representation
        accept_payload_model_dict = AcceptPayload.from_dict(accept_payload_model_json).__dict__
        accept_payload_model2 = AcceptPayload(**accept_payload_model_dict)

        # Verify the model instances are equivalent
        assert accept_payload_model == accept_payload_model2

        # Convert model instance back to dict and verify no loss of data
        accept_payload_model_json2 = accept_payload_model.to_dict()
        assert accept_payload_model_json2 == accept_payload_model_json

class TestResolvePayload():
    """
    Test Class for ResolvePayload
    """

    def test_resolve_payload_serialization(self):
        """
        Test serialization/deserialization for ResolvePayload
        """

        # Construct a json representation of a ResolvePayload model
        resolve_payload_model_json = {}
        resolve_payload_model_json['action'] = 'resolve'
        resolve_payload_model_json['comment'] = 'testString'
        resolve_payload_model_json['resolution_code'] = 1

        # Construct a model instance of ResolvePayload by calling from_dict on the json representation
        resolve_payload_model = ResolvePayload.from_dict(resolve_payload_model_json)
        assert resolve_payload_model != False

        # Construct a model instance of ResolvePayload by calling from_dict on the json representation
        resolve_payload_model_dict = ResolvePayload.from_dict(resolve_payload_model_json).__dict__
        resolve_payload_model2 = ResolvePayload(**resolve_payload_model_dict)

        # Verify the model instances are equivalent
        assert resolve_payload_model == resolve_payload_model2

        # Convert model instance back to dict and verify no loss of data
        resolve_payload_model_json2 = resolve_payload_model.to_dict()
        assert resolve_payload_model_json2 == resolve_payload_model_json

class TestUnresolvePayload():
    """
    Test Class for UnresolvePayload
    """

    def test_unresolve_payload_serialization(self):
        """
        Test serialization/deserialization for UnresolvePayload
        """

        # Construct a json representation of a UnresolvePayload model
        unresolve_payload_model_json = {}
        unresolve_payload_model_json['action'] = 'unresolve'
        unresolve_payload_model_json['comment'] = 'testString'

        # Construct a model instance of UnresolvePayload by calling from_dict on the json representation
        unresolve_payload_model = UnresolvePayload.from_dict(unresolve_payload_model_json)
        assert unresolve_payload_model != False

        # Construct a model instance of UnresolvePayload by calling from_dict on the json representation
        unresolve_payload_model_dict = UnresolvePayload.from_dict(unresolve_payload_model_json).__dict__
        unresolve_payload_model2 = UnresolvePayload(**unresolve_payload_model_dict)

        # Verify the model instances are equivalent
        assert unresolve_payload_model == unresolve_payload_model2

        # Convert model instance back to dict and verify no loss of data
        unresolve_payload_model_json2 = unresolve_payload_model.to_dict()
        assert unresolve_payload_model_json2 == unresolve_payload_model_json

class TestFileWithMetadata():
    """
    Test Class for FileWithMetadata
    """

    def test_file_with_metadata_serialization(self):
        """
        Test serialization/deserialization for FileWithMetadata
        """

        # Construct a json representation of a FileWithMetadata model
        file_with_metadata_model_json = {}
        file_with_metadata_model_json['data'] = io.BytesIO(b'This is a mock file.').getvalue()
        file_with_metadata_model_json['filename'] = 'testString'
        file_with_metadata_model_json['content_type'] = 'testString'

        # Construct a model instance of FileWithMetadata by calling from_dict on the json representation
        file_with_metadata_model = FileWithMetadata.from_dict(file_with_metadata_model_json)
        assert file_with_metadata_model != False

        # Construct a model instance of FileWithMetadata by calling from_dict on the json representation
        file_with_metadata_model_dict = FileWithMetadata.from_dict(file_with_metadata_model_json).__dict__
        file_with_metadata_model2 = FileWithMetadata(**file_with_metadata_model_dict)

        # Verify the model instances are equivalent
        assert file_with_metadata_model == file_with_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        file_with_metadata_model_json2 = file_with_metadata_model.to_dict()
        assert file_with_metadata_model_json2 == file_with_metadata_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
