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
from ibm_platform_services.global_tagging_v1 import *


service = GlobalTaggingV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://tags.global-search-tagging.cloud.ibm.com/'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Tags
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_tags
#-----------------------------------------------------------------------------
class TestListTags():

    #--------------------------------------------------------
    # list_tags()
    #--------------------------------------------------------
    @responses.activate
    def test_list_tags_all_params(self):
        # Set up mock
        url = base_url + '/v3/tags'
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "items": [{"name": "name"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        providers = ['ghost']
        attached_to = 'testString'
        full_data = True
        offset = 38
        limit = 38
        order_by_name = 'asc'
        timeout = 38
        attached_only = True

        # Invoke method
        response = service.list_tags(
            providers=providers,
            attached_to=attached_to,
            full_data=full_data,
            offset=offset,
            limit=limit,
            order_by_name=order_by_name,
            timeout=timeout,
            attached_only=attached_only
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'providers={}'.format(','.join(providers)) in query_string
        assert 'attached_to={}'.format(attached_to) in query_string
        assert 'full_data={}'.format('true' if full_data else 'false') in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'order_by_name={}'.format(order_by_name) in query_string
        assert 'timeout={}'.format(timeout) in query_string
        assert 'attached_only={}'.format('true' if attached_only else 'false') in query_string


    #--------------------------------------------------------
    # test_list_tags_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_tags_required_params(self):
        # Set up mock
        url = base_url + '/v3/tags'
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "items": [{"name": "name"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_tags()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_tag_all
#-----------------------------------------------------------------------------
class TestDeleteTagAll():

    #--------------------------------------------------------
    # delete_tag_all()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_tag_all_all_params(self):
        # Set up mock
        url = base_url + '/v3/tags'
        mock_response = '{"total_count": 11, "errors": true, "items": [{"tag_name": "tag_name", "is_error": true}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        providers = 'ghost'

        # Invoke method
        response = service.delete_tag_all(
            providers=providers
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'providers={}'.format(providers) in query_string


    #--------------------------------------------------------
    # test_delete_tag_all_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_tag_all_required_params(self):
        # Set up mock
        url = base_url + '/v3/tags'
        mock_response = '{"total_count": 11, "errors": true, "items": [{"tag_name": "tag_name", "is_error": true}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.delete_tag_all()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_tag
#-----------------------------------------------------------------------------
class TestDeleteTag():

    #--------------------------------------------------------
    # delete_tag()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_tag_all_params(self):
        # Set up mock
        url = base_url + '/v3/tags/testString'
        mock_response = '{"results": [{"provider": "ghost", "is_error": true}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        tag_name = 'testString'
        providers = ['ghost']

        # Invoke method
        response = service.delete_tag(
            tag_name,
            providers=providers
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'providers={}'.format(','.join(providers)) in query_string


    #--------------------------------------------------------
    # test_delete_tag_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_tag_required_params(self):
        # Set up mock
        url = base_url + '/v3/tags/testString'
        mock_response = '{"results": [{"provider": "ghost", "is_error": true}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        tag_name = 'testString'

        # Invoke method
        response = service.delete_tag(
            tag_name
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_tag_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_tag_value_error(self):
        # Set up mock
        url = base_url + '/v3/tags/testString'
        mock_response = '{"results": [{"provider": "ghost", "is_error": true}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        tag_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "tag_name": tag_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_tag(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for attach_tag
#-----------------------------------------------------------------------------
class TestAttachTag():

    #--------------------------------------------------------
    # attach_tag()
    #--------------------------------------------------------
    @responses.activate
    def test_attach_tag_all_params(self):
        # Set up mock
        url = base_url + '/v3/tags/attach'
        mock_response = '{"results": [{"resource_id": "resource_id", "is_error": true}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['resource_id'] = 'testString'
        resource_model['resource_type'] = 'testString'

        # Set up parameter values
        resources = [resource_model]
        tag_name = 'testString'
        tag_names = ['testString']

        # Invoke method
        response = service.attach_tag(
            resources,
            tag_name=tag_name,
            tag_names=tag_names,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['resources'] == resources
        assert req_body['tag_name'] == tag_name
        assert req_body['tag_names'] == tag_names


    #--------------------------------------------------------
    # test_attach_tag_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_attach_tag_value_error(self):
        # Set up mock
        url = base_url + '/v3/tags/attach'
        mock_response = '{"results": [{"resource_id": "resource_id", "is_error": true}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['resource_id'] = 'testString'
        resource_model['resource_type'] = 'testString'

        # Set up parameter values
        resources = [resource_model]
        tag_name = 'testString'
        tag_names = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "resources": resources,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.attach_tag(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for detach_tag
#-----------------------------------------------------------------------------
class TestDetachTag():

    #--------------------------------------------------------
    # detach_tag()
    #--------------------------------------------------------
    @responses.activate
    def test_detach_tag_all_params(self):
        # Set up mock
        url = base_url + '/v3/tags/detach'
        mock_response = '{"results": [{"resource_id": "resource_id", "is_error": true}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['resource_id'] = 'testString'
        resource_model['resource_type'] = 'testString'

        # Set up parameter values
        resources = [resource_model]
        tag_name = 'testString'
        tag_names = ['testString']

        # Invoke method
        response = service.detach_tag(
            resources,
            tag_name=tag_name,
            tag_names=tag_names,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['resources'] == resources
        assert req_body['tag_name'] == tag_name
        assert req_body['tag_names'] == tag_names


    #--------------------------------------------------------
    # test_detach_tag_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_detach_tag_value_error(self):
        # Set up mock
        url = base_url + '/v3/tags/detach'
        mock_response = '{"results": [{"resource_id": "resource_id", "is_error": true}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['resource_id'] = 'testString'
        resource_model['resource_type'] = 'testString'

        # Set up parameter values
        resources = [resource_model]
        tag_name = 'testString'
        tag_names = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "resources": resources,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.detach_tag(**req_copy)



# endregion
##############################################################################
# End of Service: Tags
##############################################################################

