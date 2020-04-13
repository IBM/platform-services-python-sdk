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
            attached_only=attached_only,
            headers={}
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
            providers=providers,
            headers={}
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
            providers=providers,
            headers={}
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
            tag_name,
            headers={}
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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['resources'] == [resource_model]
        assert req_body['tag_name'] == 'testString'
        assert req_body['tag_names'] == ['testString']


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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['resources'] == [resource_model]
        assert req_body['tag_name'] == 'testString'
        assert req_body['tag_names'] == ['testString']


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


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for DeleteTagResults
#-----------------------------------------------------------------------------
class TestDeleteTagResults():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteTagResults
    #--------------------------------------------------------
    def test_delete_tag_results_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        delete_tag_results_item_model = {} # DeleteTagResultsItem
        delete_tag_results_item_model['provider'] = 'ghost'
        delete_tag_results_item_model['is_error'] = True
        delete_tag_results_item_model['foo'] = { 'foo': 'bar' }

        # Construct a json representation of a DeleteTagResults model
        delete_tag_results_model_json = {}
        delete_tag_results_model_json['results'] = [delete_tag_results_item_model]

        # Construct a model instance of DeleteTagResults by calling from_dict on the json representation
        delete_tag_results_model = DeleteTagResults.from_dict(delete_tag_results_model_json)
        assert delete_tag_results_model != False

        # Construct a model instance of DeleteTagResults by calling from_dict on the json representation
        delete_tag_results_model_dict = DeleteTagResults.from_dict(delete_tag_results_model_json).__dict__
        delete_tag_results_model2 = DeleteTagResults(**delete_tag_results_model_dict)

        # Verify the model instances are equivalent
        assert delete_tag_results_model == delete_tag_results_model2

        # Convert model instance back to dict and verify no loss of data
        delete_tag_results_model_json2 = delete_tag_results_model.to_dict()
        assert delete_tag_results_model_json2 == delete_tag_results_model_json

#-----------------------------------------------------------------------------
# Test Class for DeleteTagResultsItem
#-----------------------------------------------------------------------------
class TestDeleteTagResultsItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteTagResultsItem
    #--------------------------------------------------------
    def test_delete_tag_results_item_serialization(self):

        # Construct a json representation of a DeleteTagResultsItem model
        delete_tag_results_item_model_json = {}
        delete_tag_results_item_model_json['provider'] = 'ghost'
        delete_tag_results_item_model_json['is_error'] = True
        delete_tag_results_item_model_json['foo'] = { 'foo': 'bar' }

        # Construct a model instance of DeleteTagResultsItem by calling from_dict on the json representation
        delete_tag_results_item_model = DeleteTagResultsItem.from_dict(delete_tag_results_item_model_json)
        assert delete_tag_results_item_model != False

        # Construct a model instance of DeleteTagResultsItem by calling from_dict on the json representation
        delete_tag_results_item_model_dict = DeleteTagResultsItem.from_dict(delete_tag_results_item_model_json).__dict__
        delete_tag_results_item_model2 = DeleteTagResultsItem(**delete_tag_results_item_model_dict)

        # Verify the model instances are equivalent
        assert delete_tag_results_item_model == delete_tag_results_item_model2

        # Convert model instance back to dict and verify no loss of data
        delete_tag_results_item_model_json2 = delete_tag_results_item_model.to_dict()
        assert delete_tag_results_item_model_json2 == delete_tag_results_item_model_json

#-----------------------------------------------------------------------------
# Test Class for DeleteTagsResult
#-----------------------------------------------------------------------------
class TestDeleteTagsResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteTagsResult
    #--------------------------------------------------------
    def test_delete_tags_result_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        delete_tags_result_item_model = {} # DeleteTagsResultItem
        delete_tags_result_item_model['tag_name'] = 'testString'
        delete_tags_result_item_model['is_error'] = True

        # Construct a json representation of a DeleteTagsResult model
        delete_tags_result_model_json = {}
        delete_tags_result_model_json['total_count'] = 38
        delete_tags_result_model_json['errors'] = True
        delete_tags_result_model_json['items'] = [delete_tags_result_item_model]

        # Construct a model instance of DeleteTagsResult by calling from_dict on the json representation
        delete_tags_result_model = DeleteTagsResult.from_dict(delete_tags_result_model_json)
        assert delete_tags_result_model != False

        # Construct a model instance of DeleteTagsResult by calling from_dict on the json representation
        delete_tags_result_model_dict = DeleteTagsResult.from_dict(delete_tags_result_model_json).__dict__
        delete_tags_result_model2 = DeleteTagsResult(**delete_tags_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_tags_result_model == delete_tags_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_tags_result_model_json2 = delete_tags_result_model.to_dict()
        assert delete_tags_result_model_json2 == delete_tags_result_model_json

#-----------------------------------------------------------------------------
# Test Class for DeleteTagsResultItem
#-----------------------------------------------------------------------------
class TestDeleteTagsResultItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteTagsResultItem
    #--------------------------------------------------------
    def test_delete_tags_result_item_serialization(self):

        # Construct a json representation of a DeleteTagsResultItem model
        delete_tags_result_item_model_json = {}
        delete_tags_result_item_model_json['tag_name'] = 'testString'
        delete_tags_result_item_model_json['is_error'] = True

        # Construct a model instance of DeleteTagsResultItem by calling from_dict on the json representation
        delete_tags_result_item_model = DeleteTagsResultItem.from_dict(delete_tags_result_item_model_json)
        assert delete_tags_result_item_model != False

        # Construct a model instance of DeleteTagsResultItem by calling from_dict on the json representation
        delete_tags_result_item_model_dict = DeleteTagsResultItem.from_dict(delete_tags_result_item_model_json).__dict__
        delete_tags_result_item_model2 = DeleteTagsResultItem(**delete_tags_result_item_model_dict)

        # Verify the model instances are equivalent
        assert delete_tags_result_item_model == delete_tags_result_item_model2

        # Convert model instance back to dict and verify no loss of data
        delete_tags_result_item_model_json2 = delete_tags_result_item_model.to_dict()
        assert delete_tags_result_item_model_json2 == delete_tags_result_item_model_json

#-----------------------------------------------------------------------------
# Test Class for Resource
#-----------------------------------------------------------------------------
class TestResource():

    #--------------------------------------------------------
    # Test serialization/deserialization for Resource
    #--------------------------------------------------------
    def test_resource_serialization(self):

        # Construct a json representation of a Resource model
        resource_model_json = {}
        resource_model_json['resource_id'] = 'testString'
        resource_model_json['resource_type'] = 'testString'

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

#-----------------------------------------------------------------------------
# Test Class for Tag
#-----------------------------------------------------------------------------
class TestTag():

    #--------------------------------------------------------
    # Test serialization/deserialization for Tag
    #--------------------------------------------------------
    def test_tag_serialization(self):

        # Construct a json representation of a Tag model
        tag_model_json = {}
        tag_model_json['name'] = 'testString'

        # Construct a model instance of Tag by calling from_dict on the json representation
        tag_model = Tag.from_dict(tag_model_json)
        assert tag_model != False

        # Construct a model instance of Tag by calling from_dict on the json representation
        tag_model_dict = Tag.from_dict(tag_model_json).__dict__
        tag_model2 = Tag(**tag_model_dict)

        # Verify the model instances are equivalent
        assert tag_model == tag_model2

        # Convert model instance back to dict and verify no loss of data
        tag_model_json2 = tag_model.to_dict()
        assert tag_model_json2 == tag_model_json

#-----------------------------------------------------------------------------
# Test Class for TagList
#-----------------------------------------------------------------------------
class TestTagList():

    #--------------------------------------------------------
    # Test serialization/deserialization for TagList
    #--------------------------------------------------------
    def test_tag_list_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        tag_model = {} # Tag
        tag_model['name'] = 'testString'

        # Construct a json representation of a TagList model
        tag_list_model_json = {}
        tag_list_model_json['total_count'] = 38
        tag_list_model_json['offset'] = 38
        tag_list_model_json['limit'] = 38
        tag_list_model_json['items'] = [tag_model]

        # Construct a model instance of TagList by calling from_dict on the json representation
        tag_list_model = TagList.from_dict(tag_list_model_json)
        assert tag_list_model != False

        # Construct a model instance of TagList by calling from_dict on the json representation
        tag_list_model_dict = TagList.from_dict(tag_list_model_json).__dict__
        tag_list_model2 = TagList(**tag_list_model_dict)

        # Verify the model instances are equivalent
        assert tag_list_model == tag_list_model2

        # Convert model instance back to dict and verify no loss of data
        tag_list_model_json2 = tag_list_model.to_dict()
        assert tag_list_model_json2 == tag_list_model_json

#-----------------------------------------------------------------------------
# Test Class for TagResults
#-----------------------------------------------------------------------------
class TestTagResults():

    #--------------------------------------------------------
    # Test serialization/deserialization for TagResults
    #--------------------------------------------------------
    def test_tag_results_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        tag_results_item_model = {} # TagResultsItem
        tag_results_item_model['resource_id'] = 'testString'
        tag_results_item_model['is_error'] = True

        # Construct a json representation of a TagResults model
        tag_results_model_json = {}
        tag_results_model_json['results'] = [tag_results_item_model]

        # Construct a model instance of TagResults by calling from_dict on the json representation
        tag_results_model = TagResults.from_dict(tag_results_model_json)
        assert tag_results_model != False

        # Construct a model instance of TagResults by calling from_dict on the json representation
        tag_results_model_dict = TagResults.from_dict(tag_results_model_json).__dict__
        tag_results_model2 = TagResults(**tag_results_model_dict)

        # Verify the model instances are equivalent
        assert tag_results_model == tag_results_model2

        # Convert model instance back to dict and verify no loss of data
        tag_results_model_json2 = tag_results_model.to_dict()
        assert tag_results_model_json2 == tag_results_model_json

#-----------------------------------------------------------------------------
# Test Class for TagResultsItem
#-----------------------------------------------------------------------------
class TestTagResultsItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for TagResultsItem
    #--------------------------------------------------------
    def test_tag_results_item_serialization(self):

        # Construct a json representation of a TagResultsItem model
        tag_results_item_model_json = {}
        tag_results_item_model_json['resource_id'] = 'testString'
        tag_results_item_model_json['is_error'] = True

        # Construct a model instance of TagResultsItem by calling from_dict on the json representation
        tag_results_item_model = TagResultsItem.from_dict(tag_results_item_model_json)
        assert tag_results_item_model != False

        # Construct a model instance of TagResultsItem by calling from_dict on the json representation
        tag_results_item_model_dict = TagResultsItem.from_dict(tag_results_item_model_json).__dict__
        tag_results_item_model2 = TagResultsItem(**tag_results_item_model_dict)

        # Verify the model instances are equivalent
        assert tag_results_item_model == tag_results_item_model2

        # Convert model instance back to dict and verify no loss of data
        tag_results_item_model_json2 = tag_results_item_model.to_dict()
        assert tag_results_item_model_json2 == tag_results_item_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
