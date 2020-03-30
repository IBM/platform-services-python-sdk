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
import io
import json
import pytest
import requests
import responses
import tempfile
from platform_services.case_management_v1 import *


service = CaseManagementV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://support-center.cloud.ibm.com/'
service.set_service_url(base_url)

##############################################################################
# Start of Service: CaseManagement
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_cases
#-----------------------------------------------------------------------------
class TestGetCases():

    #--------------------------------------------------------
    # get_cases()
    #--------------------------------------------------------
    @responses.activate
    def test_get_cases_all_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases'
        mock_response = '{"total_count": 11, "first": {"href": "href"}, "next": {"href": "href"}, "previous": {"href": "href"}, "last": {"href": "href"}, "cases": [{"number": "number", "short_escription": "short_escription", "description": "description", "created_at": "created_at", "created_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "updated_at": "updated_at", "updated_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "contact_type": "Cloud Support Center", "contact": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "status": "status", "severity": 8, "support_tier": "Free", "resolution": "resolution", "close_notes": "close_notes", "eu": {"support": false, "data_center": "data_center"}, "watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}], "offering": {"id": "id", "value": "value"}, "resources": [{"crn": "crn", "name": "name", "type": "type", "id": 2, "note": "note"}], "comments": [{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}]}]}'
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
            fields=fields
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'search={}'.format(search) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'status={}'.format(','.join(status)) in query_string
        assert 'fields={}'.format(','.join(fields)) in query_string


    #--------------------------------------------------------
    # test_get_cases_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_cases_required_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases'
        mock_response = '{"total_count": 11, "first": {"href": "href"}, "next": {"href": "href"}, "previous": {"href": "href"}, "last": {"href": "href"}, "cases": [{"number": "number", "short_escription": "short_escription", "description": "description", "created_at": "created_at", "created_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "updated_at": "updated_at", "updated_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "contact_type": "Cloud Support Center", "contact": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "status": "status", "severity": 8, "support_tier": "Free", "resolution": "resolution", "close_notes": "close_notes", "eu": {"support": false, "data_center": "data_center"}, "watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}], "offering": {"id": "id", "value": "value"}, "resources": [{"crn": "crn", "name": "name", "type": "type", "id": 2, "note": "note"}], "comments": [{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}]}]}'
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


#-----------------------------------------------------------------------------
# Test Class for create_case
#-----------------------------------------------------------------------------
class TestCreateCase():

    #--------------------------------------------------------
    # create_case()
    #--------------------------------------------------------
    @responses.activate
    def test_create_case_all_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases'
        mock_response = '{"number": "number", "short_escription": "short_escription", "description": "description", "created_at": "created_at", "created_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "updated_at": "updated_at", "updated_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "contact_type": "Cloud Support Center", "contact": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "status": "status", "severity": 8, "support_tier": "Free", "resolution": "resolution", "close_notes": "close_notes", "eu": {"support": false, "data_center": "data_center"}, "watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}], "offering": {"id": "id", "value": "value"}, "resources": [{"crn": "crn", "name": "name", "type": "type", "id": 2, "note": "note"}], "comments": [{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a EuPayload model
        eu_payload_model = {}
        eu_payload_model['supported'] = True 
        eu_payload_model['data_center'] = 38 

        # Construct a dict representation of a OfferingPayloadType model
        offering_payload_type_model = {}
        offering_payload_type_model['group'] = 'crn_service_name' 
        offering_payload_type_model['key'] = 'testString' 
        offering_payload_type_model['id'] = 'testString' 
        offering_payload_type_model['kind'] = 'testString' 

        # Construct a dict representation of a OfferingPayload model
        offering_payload_model = {}
        offering_payload_model['name'] = 'testString' 
        offering_payload_model['type'] = offering_payload_type_model 

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['crn'] = 'testString' 
        resource_model['name'] = 'testString' 
        resource_model['type'] = 'testString' 
        resource_model['id'] = 38 
        resource_model['note'] = 'testString' 

        # Construct a dict representation of a User model
        user_model = {}
        user_model['name'] = 'testString' 
        user_model['realm'] = 'IBMid' 
        user_model['user_id'] = 'abc@ibm.com' 

        # Set up parameter values
        type = 'technical'
        subject = 'testString'
        description = 'testString'
        severity = 1
        eu = eu_payload_model
        offering = offering_payload_model
        resources = [resource_model]
        watchlist = [user_model]
        invoice_number = 'testString'
        sla_credit_request = True

        # Invoke method
        response = service.create_case(
            type=type,
            subject=subject,
            description=description,
            severity=severity,
            eu=eu,
            offering=offering,
            resources=resources,
            watchlist=watchlist,
            invoice_number=invoice_number,
            sla_credit_request=sla_credit_request,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == type
        assert req_body['subject'] == subject
        assert req_body['description'] == description
        assert req_body['severity'] == severity
        assert req_body['eu'] == eu
        assert req_body['offering'] == offering
        assert req_body['resources'] == resources
        assert req_body['watchlist'] == watchlist
        assert req_body['invoice_number'] == invoice_number
        assert req_body['sla_credit_request'] == sla_credit_request


    #--------------------------------------------------------
    # test_create_case_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_case_required_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases'
        mock_response = '{"number": "number", "short_escription": "short_escription", "description": "description", "created_at": "created_at", "created_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "updated_at": "updated_at", "updated_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "contact_type": "Cloud Support Center", "contact": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "status": "status", "severity": 8, "support_tier": "Free", "resolution": "resolution", "close_notes": "close_notes", "eu": {"support": false, "data_center": "data_center"}, "watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}], "offering": {"id": "id", "value": "value"}, "resources": [{"crn": "crn", "name": "name", "type": "type", "id": 2, "note": "note"}], "comments": [{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.create_case()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_case
#-----------------------------------------------------------------------------
class TestGetCase():

    #--------------------------------------------------------
    # get_case()
    #--------------------------------------------------------
    @responses.activate
    def test_get_case_all_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString'
        mock_response = '{"number": "number", "short_escription": "short_escription", "description": "description", "created_at": "created_at", "created_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "updated_at": "updated_at", "updated_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "contact_type": "Cloud Support Center", "contact": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "status": "status", "severity": 8, "support_tier": "Free", "resolution": "resolution", "close_notes": "close_notes", "eu": {"support": false, "data_center": "data_center"}, "watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}], "offering": {"id": "id", "value": "value"}, "resources": [{"crn": "crn", "name": "name", "type": "type", "id": 2, "note": "note"}], "comments": [{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'
        fields = ['testString']

        # Invoke method
        response = service.get_case(
            case_number,
            fields=fields
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'fields={}'.format(','.join(fields)) in query_string


    #--------------------------------------------------------
    # test_get_case_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_case_required_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString'
        mock_response = '{"number": "number", "short_escription": "short_escription", "description": "description", "created_at": "created_at", "created_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "updated_at": "updated_at", "updated_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "contact_type": "Cloud Support Center", "contact": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "status": "status", "severity": 8, "support_tier": "Free", "resolution": "resolution", "close_notes": "close_notes", "eu": {"support": false, "data_center": "data_center"}, "watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}], "offering": {"id": "id", "value": "value"}, "resources": [{"crn": "crn", "name": "name", "type": "type", "id": 2, "note": "note"}], "comments": [{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'

        # Invoke method
        response = service.get_case(
            case_number
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_case_status
#-----------------------------------------------------------------------------
class TestUpdateCaseStatus():

    #--------------------------------------------------------
    # update_case_status()
    #--------------------------------------------------------
    @responses.activate
    def test_update_case_status_all_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString/status'
        mock_response = '{"number": "number", "short_escription": "short_escription", "description": "description", "created_at": "created_at", "created_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "updated_at": "updated_at", "updated_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "contact_type": "Cloud Support Center", "contact": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "status": "status", "severity": 8, "support_tier": "Free", "resolution": "resolution", "close_notes": "close_notes", "eu": {"support": false, "data_center": "data_center"}, "watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}], "offering": {"id": "id", "value": "value"}, "resources": [{"crn": "crn", "name": "name", "type": "type", "id": 2, "note": "note"}], "comments": [{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'
        action = 'resolve'
        comment = 'testString'
        resolution_code = 1

        # Invoke method
        response = service.update_case_status(
            case_number,
            action,
            comment=comment,
            resolution_code=resolution_code,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action'] == action
        assert req_body['comment'] == comment
        assert req_body['resolution_code'] == resolution_code


    #--------------------------------------------------------
    # test_update_case_status_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_case_status_required_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString/status'
        mock_response = '{"number": "number", "short_escription": "short_escription", "description": "description", "created_at": "created_at", "created_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "updated_at": "updated_at", "updated_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "contact_type": "Cloud Support Center", "contact": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}, "status": "status", "severity": 8, "support_tier": "Free", "resolution": "resolution", "close_notes": "close_notes", "eu": {"support": false, "data_center": "data_center"}, "watchlist": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "attachments": [{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}], "offering": {"id": "id", "value": "value"}, "resources": [{"crn": "crn", "name": "name", "type": "type", "id": 2, "note": "note"}], "comments": [{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'
        action = 'resolve'
        comment = 'testString'
        resolution_code = 1

        # Invoke method
        response = service.update_case_status(
            case_number,
            action,
            comment=comment,
            resolution_code=resolution_code,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action'] == action
        assert req_body['comment'] == comment
        assert req_body['resolution_code'] == resolution_code


#-----------------------------------------------------------------------------
# Test Class for add_comment
#-----------------------------------------------------------------------------
class TestAddComment():

    #--------------------------------------------------------
    # add_comment()
    #--------------------------------------------------------
    @responses.activate
    def test_add_comment_all_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString/comments'
        mock_response = '{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'
        comment = 'testString'

        # Invoke method
        response = service.add_comment(
            case_number,
            comment,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['comment'] == comment


    #--------------------------------------------------------
    # test_add_comment_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_add_comment_required_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString/comments'
        mock_response = '{"value": "value", "added_at": "added_at", "added_by": {"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'
        comment = 'testString'

        # Invoke method
        response = service.add_comment(
            case_number,
            comment,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['comment'] == comment


#-----------------------------------------------------------------------------
# Test Class for add_watchlist
#-----------------------------------------------------------------------------
class TestAddWatchlist():

    #--------------------------------------------------------
    # add_watchlist()
    #--------------------------------------------------------
    @responses.activate
    def test_add_watchlist_all_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString/watchlist'
        mock_response = '{"added": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "failed": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a UserIdAndRealm model
        user_id_and_realm_model = {}
        user_id_and_realm_model['realm'] = 'IBMid' 
        user_id_and_realm_model['user_id'] = 'testString' 

        # Set up parameter values
        case_number = 'testString'
        watchlist = [user_id_and_realm_model]

        # Invoke method
        response = service.add_watchlist(
            case_number,
            watchlist=watchlist,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['watchlist'] == watchlist


    #--------------------------------------------------------
    # test_add_watchlist_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_add_watchlist_required_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString/watchlist'
        mock_response = '{"added": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}], "failed": [{"name": "name", "realm": "IBMid", "user_id": "abc@ibm.com"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a UserIdAndRealm model
        user_id_and_realm_model = {}
        user_id_and_realm_model['realm'] = 'IBMid' 
        user_id_and_realm_model['user_id'] = 'testString' 

        # Set up parameter values
        case_number = 'testString'
        watchlist = [user_id_and_realm_model]

        # Invoke method
        response = service.add_watchlist(
            case_number,
            watchlist=watchlist,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['watchlist'] == watchlist


#-----------------------------------------------------------------------------
# Test Class for remove_watchlist
#-----------------------------------------------------------------------------
class TestRemoveWatchlist():

    #--------------------------------------------------------
    # remove_watchlist()
    #--------------------------------------------------------
    @responses.activate
    def test_remove_watchlist_all_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString/watchlist'
        mock_response = '[{}]'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a UserIdAndRealm model
        user_id_and_realm_model = {}
        user_id_and_realm_model['realm'] = 'IBMid' 
        user_id_and_realm_model['user_id'] = 'testString' 

        # Set up parameter values
        case_number = 'testString'
        watchlist = [user_id_and_realm_model]

        # Invoke method
        response = service.remove_watchlist(
            case_number,
            watchlist=watchlist,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['watchlist'] == watchlist


    #--------------------------------------------------------
    # test_remove_watchlist_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_remove_watchlist_required_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString/watchlist'
        mock_response = '[{}]'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a UserIdAndRealm model
        user_id_and_realm_model = {}
        user_id_and_realm_model['realm'] = 'IBMid' 
        user_id_and_realm_model['user_id'] = 'testString' 

        # Set up parameter values
        case_number = 'testString'
        watchlist = [user_id_and_realm_model]

        # Invoke method
        response = service.remove_watchlist(
            case_number,
            watchlist=watchlist,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['watchlist'] == watchlist


#-----------------------------------------------------------------------------
# Test Class for add_resource
#-----------------------------------------------------------------------------
class TestAddResource():

    #--------------------------------------------------------
    # add_resource()
    #--------------------------------------------------------
    @responses.activate
    def test_add_resource_all_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString/resources'
        mock_response = '{"crn": "crn", "name": "name", "type": "type", "id": 2, "note": "note"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'
        crn = 'testString'
        name = 'testString'
        type = 'testString'
        id = 38
        note = 'testString'

        # Invoke method
        response = service.add_resource(
            case_number,
            crn=crn,
            name=name,
            type=type,
            id=id,
            note=note,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['crn'] == crn
        assert req_body['name'] == name
        assert req_body['type'] == type
        assert req_body['id'] == id
        assert req_body['note'] == note


    #--------------------------------------------------------
    # test_add_resource_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_add_resource_required_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString/resources'
        mock_response = '{"crn": "crn", "name": "name", "type": "type", "id": 2, "note": "note"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'

        # Invoke method
        response = service.add_resource(
            case_number
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for upload_file
#-----------------------------------------------------------------------------
class TestUploadFile():

    #--------------------------------------------------------
    # upload_file()
    #--------------------------------------------------------
    @responses.activate
    def test_upload_file_all_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString/attachments'
        mock_response = '{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'
        file = io.BytesIO(b'This is a mock file.').getvalue()
        file_content_type = 'testString'

        # Invoke method
        response = service.upload_file(
            case_number,
            file,
            file_content_type=file_content_type
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_upload_file_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_upload_file_required_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString/attachments'
        mock_response = '{"id": "id", "filename": "filename", "size_in_bytes": 13, "created_at": "created_at", "url": "url"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        case_number = 'testString'
        file = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = service.upload_file(
            case_number,
            file
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for download_file
#-----------------------------------------------------------------------------
class TestDownloadFile():

    #--------------------------------------------------------
    # download_file()
    #--------------------------------------------------------
    @responses.activate
    def test_download_file_all_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString/attachments/testString'
        mock_response = 'Contents of response byte-stream...'
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
            file_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_download_file_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_download_file_required_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString/attachments/testString'
        mock_response = 'Contents of response byte-stream...'
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
            file_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_file
#-----------------------------------------------------------------------------
class TestDeleteFile():

    #--------------------------------------------------------
    # delete_file()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_file_all_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString/attachments/testString'
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
            file_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_file_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_file_required_params(self):
        # Set up mock
        url = base_url + '/case-management/v1/cases/testString/attachments/testString'
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
            file_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: CaseManagement
##############################################################################

##############################################################################
# Start of Service: Utilities
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_eu_support
#-----------------------------------------------------------------------------
class TestGetEuSupport():

    #--------------------------------------------------------
    # get_eu_support()
    #--------------------------------------------------------
    @responses.activate
    def test_get_eu_support_all_params(self):
        # Set up mock
        url = base_url + '/case-management/utilities/v1/eu-support'
        mock_response = '{"property": "supported", "values": [{"anyKey": "anyValue"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_eu_support()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_eu_support_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_eu_support_required_params(self):
        # Set up mock
        url = base_url + '/case-management/utilities/v1/eu-support'
        mock_response = '{"property": "supported", "values": [{"anyKey": "anyValue"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_eu_support()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_technical_offerings
#-----------------------------------------------------------------------------
class TestGetTechnicalOfferings():

    #--------------------------------------------------------
    # get_technical_offerings()
    #--------------------------------------------------------
    @responses.activate
    def test_get_technical_offerings_all_params(self):
        # Set up mock
        url = base_url + '/case-management/utilities/v1/offerings/technical'
        mock_response = '{"offerings": [{"name": "name", "type": {"group": "crn_service_name", "key": "key"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_technical_offerings()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_technical_offerings_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_technical_offerings_required_params(self):
        # Set up mock
        url = base_url + '/case-management/utilities/v1/offerings/technical'
        mock_response = '{"offerings": [{"name": "name", "type": {"group": "crn_service_name", "key": "key"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_technical_offerings()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_resolution_codes
#-----------------------------------------------------------------------------
class TestGetResolutionCodes():

    #--------------------------------------------------------
    # get_resolution_codes()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resolution_codes_all_params(self):
        # Set up mock
        url = base_url + '/case-management/utilities/v1/constants/resolution-codes'
        mock_response = '{"resolution_codes": [{"id": 2, "value": "value"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_resolution_codes()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_resolution_codes_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resolution_codes_required_params(self):
        # Set up mock
        url = base_url + '/case-management/utilities/v1/constants/resolution-codes'
        mock_response = '{"resolution_codes": [{"id": 2, "value": "value"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_resolution_codes()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_statuses
#-----------------------------------------------------------------------------
class TestGetStatuses():

    #--------------------------------------------------------
    # get_statuses()
    #--------------------------------------------------------
    @responses.activate
    def test_get_statuses_all_params(self):
        # Set up mock
        url = base_url + '/case-management/utilities/v1/constants/statuses'
        mock_response = '{"statuses": [{"id": "id", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_statuses()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_statuses_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_statuses_required_params(self):
        # Set up mock
        url = base_url + '/case-management/utilities/v1/constants/statuses'
        mock_response = '{"statuses": [{"id": "id", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_statuses()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Utilities
##############################################################################

