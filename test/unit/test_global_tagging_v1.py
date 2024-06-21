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
Unit Tests for GlobalTaggingV1
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
from ibm_platform_services.global_tagging_v1 import *


_service = GlobalTaggingV1(authenticator=NoAuthAuthenticator())

_base_url = 'https://tags.global-search-tagging.cloud.ibm.com'
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
# Start of Service: Tags
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

        service = GlobalTaggingV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, GlobalTaggingV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = GlobalTaggingV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListTags:
    """
    Test Class for list_tags
    """

    @responses.activate
    def test_list_tags_all_params(self):
        """
        list_tags()
        """
        # Set up mock
        url = preprocess_url('/v3/tags')
        mock_response = '{"total_count": 0, "offset": 0, "limit": 1, "items": [{"name": "name"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        x_request_id = 'testString'
        x_correlation_id = 'testString'
        account_id = 'testString'
        tag_type = 'user'
        full_data = False
        providers = ['ghost']
        attached_to = 'testString'
        offset = 0
        limit = 100
        timeout = 0
        order_by_name = 'asc'
        attached_only = False

        # Invoke method
        response = _service.list_tags(
            x_request_id=x_request_id,
            x_correlation_id=x_correlation_id,
            account_id=account_id,
            tag_type=tag_type,
            full_data=full_data,
            providers=providers,
            attached_to=attached_to,
            offset=offset,
            limit=limit,
            timeout=timeout,
            order_by_name=order_by_name,
            attached_only=attached_only,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'tag_type={}'.format(tag_type) in query_string
        assert 'full_data={}'.format('true' if full_data else 'false') in query_string
        assert 'providers={}'.format(','.join(providers)) in query_string
        assert 'attached_to={}'.format(attached_to) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'timeout={}'.format(timeout) in query_string
        assert 'order_by_name={}'.format(order_by_name) in query_string
        assert 'attached_only={}'.format('true' if attached_only else 'false') in query_string

    def test_list_tags_all_params_with_retries(self):
        # Enable retries and run test_list_tags_all_params.
        _service.enable_retries()
        self.test_list_tags_all_params()

        # Disable retries and run test_list_tags_all_params.
        _service.disable_retries()
        self.test_list_tags_all_params()

    @responses.activate
    def test_list_tags_required_params(self):
        """
        test_list_tags_required_params()
        """
        # Set up mock
        url = preprocess_url('/v3/tags')
        mock_response = '{"total_count": 0, "offset": 0, "limit": 1, "items": [{"name": "name"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_tags()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_tags_required_params_with_retries(self):
        # Enable retries and run test_list_tags_required_params.
        _service.enable_retries()
        self.test_list_tags_required_params()

        # Disable retries and run test_list_tags_required_params.
        _service.disable_retries()
        self.test_list_tags_required_params()


class TestCreateTag:
    """
    Test Class for create_tag
    """

    @responses.activate
    def test_create_tag_all_params(self):
        """
        create_tag()
        """
        # Set up mock
        url = preprocess_url('/v3/tags')
        mock_response = '{"results": [{"tag_name": "tag_name", "is_error": true}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        tag_names = ['testString']
        x_request_id = 'testString'
        x_correlation_id = 'testString'
        account_id = 'testString'
        tag_type = 'access'

        # Invoke method
        response = _service.create_tag(
            tag_names,
            x_request_id=x_request_id,
            x_correlation_id=x_correlation_id,
            account_id=account_id,
            tag_type=tag_type,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'tag_type={}'.format(tag_type) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['tag_names'] == ['testString']

    def test_create_tag_all_params_with_retries(self):
        # Enable retries and run test_create_tag_all_params.
        _service.enable_retries()
        self.test_create_tag_all_params()

        # Disable retries and run test_create_tag_all_params.
        _service.disable_retries()
        self.test_create_tag_all_params()

    @responses.activate
    def test_create_tag_required_params(self):
        """
        test_create_tag_required_params()
        """
        # Set up mock
        url = preprocess_url('/v3/tags')
        mock_response = '{"results": [{"tag_name": "tag_name", "is_error": true}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        tag_names = ['testString']

        # Invoke method
        response = _service.create_tag(
            tag_names,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['tag_names'] == ['testString']

    def test_create_tag_required_params_with_retries(self):
        # Enable retries and run test_create_tag_required_params.
        _service.enable_retries()
        self.test_create_tag_required_params()

        # Disable retries and run test_create_tag_required_params.
        _service.disable_retries()
        self.test_create_tag_required_params()

    @responses.activate
    def test_create_tag_value_error(self):
        """
        test_create_tag_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/tags')
        mock_response = '{"results": [{"tag_name": "tag_name", "is_error": true}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        tag_names = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "tag_names": tag_names,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_tag(**req_copy)

    def test_create_tag_value_error_with_retries(self):
        # Enable retries and run test_create_tag_value_error.
        _service.enable_retries()
        self.test_create_tag_value_error()

        # Disable retries and run test_create_tag_value_error.
        _service.disable_retries()
        self.test_create_tag_value_error()


class TestDeleteTagAll:
    """
    Test Class for delete_tag_all
    """

    @responses.activate
    def test_delete_tag_all_all_params(self):
        """
        delete_tag_all()
        """
        # Set up mock
        url = preprocess_url('/v3/tags')
        mock_response = '{"total_count": 11, "errors": true, "items": [{"tag_name": "tag_name", "is_error": true}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        x_request_id = 'testString'
        x_correlation_id = 'testString'
        providers = 'ghost'
        account_id = 'testString'
        tag_type = 'user'

        # Invoke method
        response = _service.delete_tag_all(
            x_request_id=x_request_id,
            x_correlation_id=x_correlation_id,
            providers=providers,
            account_id=account_id,
            tag_type=tag_type,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'providers={}'.format(providers) in query_string
        assert 'account_id={}'.format(account_id) in query_string
        assert 'tag_type={}'.format(tag_type) in query_string

    def test_delete_tag_all_all_params_with_retries(self):
        # Enable retries and run test_delete_tag_all_all_params.
        _service.enable_retries()
        self.test_delete_tag_all_all_params()

        # Disable retries and run test_delete_tag_all_all_params.
        _service.disable_retries()
        self.test_delete_tag_all_all_params()

    @responses.activate
    def test_delete_tag_all_required_params(self):
        """
        test_delete_tag_all_required_params()
        """
        # Set up mock
        url = preprocess_url('/v3/tags')
        mock_response = '{"total_count": 11, "errors": true, "items": [{"tag_name": "tag_name", "is_error": true}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.delete_tag_all()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_tag_all_required_params_with_retries(self):
        # Enable retries and run test_delete_tag_all_required_params.
        _service.enable_retries()
        self.test_delete_tag_all_required_params()

        # Disable retries and run test_delete_tag_all_required_params.
        _service.disable_retries()
        self.test_delete_tag_all_required_params()


class TestDeleteTag:
    """
    Test Class for delete_tag
    """

    @responses.activate
    def test_delete_tag_all_params(self):
        """
        delete_tag()
        """
        # Set up mock
        url = preprocess_url('/v3/tags/testString')
        mock_response = '{"results": [{"provider": "ghost", "is_error": true}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        tag_name = 'testString'
        x_request_id = 'testString'
        x_correlation_id = 'testString'
        providers = ['ghost']
        account_id = 'testString'
        tag_type = 'user'

        # Invoke method
        response = _service.delete_tag(
            tag_name,
            x_request_id=x_request_id,
            x_correlation_id=x_correlation_id,
            providers=providers,
            account_id=account_id,
            tag_type=tag_type,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'providers={}'.format(','.join(providers)) in query_string
        assert 'account_id={}'.format(account_id) in query_string
        assert 'tag_type={}'.format(tag_type) in query_string

    def test_delete_tag_all_params_with_retries(self):
        # Enable retries and run test_delete_tag_all_params.
        _service.enable_retries()
        self.test_delete_tag_all_params()

        # Disable retries and run test_delete_tag_all_params.
        _service.disable_retries()
        self.test_delete_tag_all_params()

    @responses.activate
    def test_delete_tag_required_params(self):
        """
        test_delete_tag_required_params()
        """
        # Set up mock
        url = preprocess_url('/v3/tags/testString')
        mock_response = '{"results": [{"provider": "ghost", "is_error": true}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        tag_name = 'testString'

        # Invoke method
        response = _service.delete_tag(
            tag_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_tag_required_params_with_retries(self):
        # Enable retries and run test_delete_tag_required_params.
        _service.enable_retries()
        self.test_delete_tag_required_params()

        # Disable retries and run test_delete_tag_required_params.
        _service.disable_retries()
        self.test_delete_tag_required_params()

    @responses.activate
    def test_delete_tag_value_error(self):
        """
        test_delete_tag_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/tags/testString')
        mock_response = '{"results": [{"provider": "ghost", "is_error": true}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        tag_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "tag_name": tag_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_tag(**req_copy)

    def test_delete_tag_value_error_with_retries(self):
        # Enable retries and run test_delete_tag_value_error.
        _service.enable_retries()
        self.test_delete_tag_value_error()

        # Disable retries and run test_delete_tag_value_error.
        _service.disable_retries()
        self.test_delete_tag_value_error()


class TestAttachTag:
    """
    Test Class for attach_tag
    """

    @responses.activate
    def test_attach_tag_all_params(self):
        """
        attach_tag()
        """
        # Set up mock
        url = preprocess_url('/v3/tags/attach')
        mock_response = '{"results": [{"resource_id": "resource_id", "is_error": true}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['resource_id'] = 'testString'
        resource_model['resource_type'] = 'testString'

        # Set up parameter values
        resources = [resource_model]
        tag_name = 'testString'
        tag_names = ['testString']
        x_request_id = 'testString'
        x_correlation_id = 'testString'
        account_id = 'testString'
        tag_type = 'user'
        replace = False
        update = False

        # Invoke method
        response = _service.attach_tag(
            resources,
            tag_name=tag_name,
            tag_names=tag_names,
            x_request_id=x_request_id,
            x_correlation_id=x_correlation_id,
            account_id=account_id,
            tag_type=tag_type,
            replace=replace,
            update=update,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'tag_type={}'.format(tag_type) in query_string
        assert 'replace={}'.format('true' if replace else 'false') in query_string
        assert 'update={}'.format('true' if update else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['resources'] == [resource_model]
        assert req_body['tag_name'] == 'testString'
        assert req_body['tag_names'] == ['testString']

    def test_attach_tag_all_params_with_retries(self):
        # Enable retries and run test_attach_tag_all_params.
        _service.enable_retries()
        self.test_attach_tag_all_params()

        # Disable retries and run test_attach_tag_all_params.
        _service.disable_retries()
        self.test_attach_tag_all_params()

    @responses.activate
    def test_attach_tag_required_params(self):
        """
        test_attach_tag_required_params()
        """
        # Set up mock
        url = preprocess_url('/v3/tags/attach')
        mock_response = '{"results": [{"resource_id": "resource_id", "is_error": true}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['resource_id'] = 'testString'
        resource_model['resource_type'] = 'testString'

        # Set up parameter values
        resources = [resource_model]
        tag_name = 'testString'
        tag_names = ['testString']

        # Invoke method
        response = _service.attach_tag(
            resources,
            tag_name=tag_name,
            tag_names=tag_names,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['resources'] == [resource_model]
        assert req_body['tag_name'] == 'testString'
        assert req_body['tag_names'] == ['testString']

    def test_attach_tag_required_params_with_retries(self):
        # Enable retries and run test_attach_tag_required_params.
        _service.enable_retries()
        self.test_attach_tag_required_params()

        # Disable retries and run test_attach_tag_required_params.
        _service.disable_retries()
        self.test_attach_tag_required_params()

    @responses.activate
    def test_attach_tag_value_error(self):
        """
        test_attach_tag_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/tags/attach')
        mock_response = '{"results": [{"resource_id": "resource_id", "is_error": true}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.attach_tag(**req_copy)

    def test_attach_tag_value_error_with_retries(self):
        # Enable retries and run test_attach_tag_value_error.
        _service.enable_retries()
        self.test_attach_tag_value_error()

        # Disable retries and run test_attach_tag_value_error.
        _service.disable_retries()
        self.test_attach_tag_value_error()


class TestDetachTag:
    """
    Test Class for detach_tag
    """

    @responses.activate
    def test_detach_tag_all_params(self):
        """
        detach_tag()
        """
        # Set up mock
        url = preprocess_url('/v3/tags/detach')
        mock_response = '{"results": [{"resource_id": "resource_id", "is_error": true}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['resource_id'] = 'testString'
        resource_model['resource_type'] = 'testString'

        # Set up parameter values
        resources = [resource_model]
        tag_name = 'testString'
        tag_names = ['testString']
        x_request_id = 'testString'
        x_correlation_id = 'testString'
        account_id = 'testString'
        tag_type = 'user'

        # Invoke method
        response = _service.detach_tag(
            resources,
            tag_name=tag_name,
            tag_names=tag_names,
            x_request_id=x_request_id,
            x_correlation_id=x_correlation_id,
            account_id=account_id,
            tag_type=tag_type,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'tag_type={}'.format(tag_type) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['resources'] == [resource_model]
        assert req_body['tag_name'] == 'testString'
        assert req_body['tag_names'] == ['testString']

    def test_detach_tag_all_params_with_retries(self):
        # Enable retries and run test_detach_tag_all_params.
        _service.enable_retries()
        self.test_detach_tag_all_params()

        # Disable retries and run test_detach_tag_all_params.
        _service.disable_retries()
        self.test_detach_tag_all_params()

    @responses.activate
    def test_detach_tag_required_params(self):
        """
        test_detach_tag_required_params()
        """
        # Set up mock
        url = preprocess_url('/v3/tags/detach')
        mock_response = '{"results": [{"resource_id": "resource_id", "is_error": true}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['resource_id'] = 'testString'
        resource_model['resource_type'] = 'testString'

        # Set up parameter values
        resources = [resource_model]
        tag_name = 'testString'
        tag_names = ['testString']

        # Invoke method
        response = _service.detach_tag(
            resources,
            tag_name=tag_name,
            tag_names=tag_names,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['resources'] == [resource_model]
        assert req_body['tag_name'] == 'testString'
        assert req_body['tag_names'] == ['testString']

    def test_detach_tag_required_params_with_retries(self):
        # Enable retries and run test_detach_tag_required_params.
        _service.enable_retries()
        self.test_detach_tag_required_params()

        # Disable retries and run test_detach_tag_required_params.
        _service.disable_retries()
        self.test_detach_tag_required_params()

    @responses.activate
    def test_detach_tag_value_error(self):
        """
        test_detach_tag_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/tags/detach')
        mock_response = '{"results": [{"resource_id": "resource_id", "is_error": true}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.detach_tag(**req_copy)

    def test_detach_tag_value_error_with_retries(self):
        # Enable retries and run test_detach_tag_value_error.
        _service.enable_retries()
        self.test_detach_tag_value_error()

        # Disable retries and run test_detach_tag_value_error.
        _service.disable_retries()
        self.test_detach_tag_value_error()


# endregion
##############################################################################
# End of Service: Tags
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_CreateTagResults:
    """
    Test Class for CreateTagResults
    """

    def test_create_tag_results_serialization(self):
        """
        Test serialization/deserialization for CreateTagResults
        """

        # Construct dict forms of any model objects needed in order to build this model.

        create_tag_results_results_item_model = {}  # CreateTagResultsResultsItem
        create_tag_results_results_item_model['tag_name'] = 'testString'
        create_tag_results_results_item_model['is_error'] = True

        # Construct a json representation of a CreateTagResults model
        create_tag_results_model_json = {}
        create_tag_results_model_json['results'] = [create_tag_results_results_item_model]

        # Construct a model instance of CreateTagResults by calling from_dict on the json representation
        create_tag_results_model = CreateTagResults.from_dict(create_tag_results_model_json)
        assert create_tag_results_model != False

        # Construct a model instance of CreateTagResults by calling from_dict on the json representation
        create_tag_results_model_dict = CreateTagResults.from_dict(create_tag_results_model_json).__dict__
        create_tag_results_model2 = CreateTagResults(**create_tag_results_model_dict)

        # Verify the model instances are equivalent
        assert create_tag_results_model == create_tag_results_model2

        # Convert model instance back to dict and verify no loss of data
        create_tag_results_model_json2 = create_tag_results_model.to_dict()
        assert create_tag_results_model_json2 == create_tag_results_model_json


class TestModel_CreateTagResultsResultsItem:
    """
    Test Class for CreateTagResultsResultsItem
    """

    def test_create_tag_results_results_item_serialization(self):
        """
        Test serialization/deserialization for CreateTagResultsResultsItem
        """

        # Construct a json representation of a CreateTagResultsResultsItem model
        create_tag_results_results_item_model_json = {}
        create_tag_results_results_item_model_json['tag_name'] = 'testString'
        create_tag_results_results_item_model_json['is_error'] = True

        # Construct a model instance of CreateTagResultsResultsItem by calling from_dict on the json representation
        create_tag_results_results_item_model = CreateTagResultsResultsItem.from_dict(
            create_tag_results_results_item_model_json
        )
        assert create_tag_results_results_item_model != False

        # Construct a model instance of CreateTagResultsResultsItem by calling from_dict on the json representation
        create_tag_results_results_item_model_dict = CreateTagResultsResultsItem.from_dict(
            create_tag_results_results_item_model_json
        ).__dict__
        create_tag_results_results_item_model2 = CreateTagResultsResultsItem(
            **create_tag_results_results_item_model_dict
        )

        # Verify the model instances are equivalent
        assert create_tag_results_results_item_model == create_tag_results_results_item_model2

        # Convert model instance back to dict and verify no loss of data
        create_tag_results_results_item_model_json2 = create_tag_results_results_item_model.to_dict()
        assert create_tag_results_results_item_model_json2 == create_tag_results_results_item_model_json


class TestModel_DeleteTagResults:
    """
    Test Class for DeleteTagResults
    """

    def test_delete_tag_results_serialization(self):
        """
        Test serialization/deserialization for DeleteTagResults
        """

        # Construct dict forms of any model objects needed in order to build this model.

        delete_tag_results_item_model = {}  # DeleteTagResultsItem
        delete_tag_results_item_model['provider'] = 'ghost'
        delete_tag_results_item_model['is_error'] = True
        delete_tag_results_item_model['foo'] = 'testString'

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


class TestModel_DeleteTagResultsItem:
    """
    Test Class for DeleteTagResultsItem
    """

    def test_delete_tag_results_item_serialization(self):
        """
        Test serialization/deserialization for DeleteTagResultsItem
        """

        # Construct a json representation of a DeleteTagResultsItem model
        delete_tag_results_item_model_json = {}
        delete_tag_results_item_model_json['provider'] = 'ghost'
        delete_tag_results_item_model_json['is_error'] = True
        delete_tag_results_item_model_json['foo'] = 'testString'

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

        # Test get_properties and set_properties methods.
        delete_tag_results_item_model.set_properties({})
        actual_dict = delete_tag_results_item_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        delete_tag_results_item_model.set_properties(expected_dict)
        actual_dict = delete_tag_results_item_model.get_properties()
        assert actual_dict == expected_dict


class TestModel_DeleteTagsResult:
    """
    Test Class for DeleteTagsResult
    """

    def test_delete_tags_result_serialization(self):
        """
        Test serialization/deserialization for DeleteTagsResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        delete_tags_result_item_model = {}  # DeleteTagsResultItem
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


class TestModel_DeleteTagsResultItem:
    """
    Test Class for DeleteTagsResultItem
    """

    def test_delete_tags_result_item_serialization(self):
        """
        Test serialization/deserialization for DeleteTagsResultItem
        """

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


class TestModel_Resource:
    """
    Test Class for Resource
    """

    def test_resource_serialization(self):
        """
        Test serialization/deserialization for Resource
        """

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


class TestModel_Tag:
    """
    Test Class for Tag
    """

    def test_tag_serialization(self):
        """
        Test serialization/deserialization for Tag
        """

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


class TestModel_TagList:
    """
    Test Class for TagList
    """

    def test_tag_list_serialization(self):
        """
        Test serialization/deserialization for TagList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tag_model = {}  # Tag
        tag_model['name'] = 'testString'

        # Construct a json representation of a TagList model
        tag_list_model_json = {}
        tag_list_model_json['total_count'] = 0
        tag_list_model_json['offset'] = 0
        tag_list_model_json['limit'] = 1
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


class TestModel_TagResults:
    """
    Test Class for TagResults
    """

    def test_tag_results_serialization(self):
        """
        Test serialization/deserialization for TagResults
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tag_results_item_model = {}  # TagResultsItem
        tag_results_item_model['resource_id'] = (
            'crn:v1:staging:public:resource-controller::a/5c2ac0d93c69e82c6c9c7c78dc4beda3::resource-group:1c061f4485b34360a8f8ee049880dc13'
        )
        tag_results_item_model['is_error'] = False

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


class TestModel_TagResultsItem:
    """
    Test Class for TagResultsItem
    """

    def test_tag_results_item_serialization(self):
        """
        Test serialization/deserialization for TagResultsItem
        """

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
