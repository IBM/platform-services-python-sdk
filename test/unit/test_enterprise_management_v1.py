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
Unit Tests for EnterpriseManagementV1
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
from ibm_platform_services.enterprise_management_v1 import *


_service = EnterpriseManagementV1(authenticator=NoAuthAuthenticator())

_base_url = 'https://enterprise.cloud.ibm.com/v1'
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
# Start of Service: EnterpriseOperations
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

        service = EnterpriseManagementV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, EnterpriseManagementV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = EnterpriseManagementV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateEnterprise:
    """
    Test Class for create_enterprise
    """

    @responses.activate
    def test_create_enterprise_all_params(self):
        """
        create_enterprise()
        """
        # Set up mock
        url = preprocess_url('/enterprises')
        mock_response = '{"enterprise_id": "enterprise_id", "enterprise_account_id": "enterprise_account_id"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=202)

        # Set up parameter values
        source_account_id = 'testString'
        name = 'testString'
        primary_contact_iam_id = 'testString'
        domain = 'testString'

        # Invoke method
        response = _service.create_enterprise(
            source_account_id, name, primary_contact_iam_id, domain=domain, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['source_account_id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['primary_contact_iam_id'] == 'testString'
        assert req_body['domain'] == 'testString'

    def test_create_enterprise_all_params_with_retries(self):
        # Enable retries and run test_create_enterprise_all_params.
        _service.enable_retries()
        self.test_create_enterprise_all_params()

        # Disable retries and run test_create_enterprise_all_params.
        _service.disable_retries()
        self.test_create_enterprise_all_params()

    @responses.activate
    def test_create_enterprise_value_error(self):
        """
        test_create_enterprise_value_error()
        """
        # Set up mock
        url = preprocess_url('/enterprises')
        mock_response = '{"enterprise_id": "enterprise_id", "enterprise_account_id": "enterprise_account_id"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=202)

        # Set up parameter values
        source_account_id = 'testString'
        name = 'testString'
        primary_contact_iam_id = 'testString'
        domain = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "source_account_id": source_account_id,
            "name": name,
            "primary_contact_iam_id": primary_contact_iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_enterprise(**req_copy)

    def test_create_enterprise_value_error_with_retries(self):
        # Enable retries and run test_create_enterprise_value_error.
        _service.enable_retries()
        self.test_create_enterprise_value_error()

        # Disable retries and run test_create_enterprise_value_error.
        _service.disable_retries()
        self.test_create_enterprise_value_error()


class TestListEnterprises:
    """
    Test Class for list_enterprises
    """

    @responses.activate
    def test_list_enterprises_all_params(self):
        """
        list_enterprises()
        """
        # Set up mock
        url = preprocess_url('/enterprises')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "enterprise_account_id": "enterprise_account_id", "crn": "crn", "name": "name", "domain": "domain", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "source_account_id": "source_account_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        enterprise_account_id = 'testString'
        account_group_id = 'testString'
        account_id = 'testString'
        next_docid = 'testString'
        limit = 100

        # Invoke method
        response = _service.list_enterprises(
            enterprise_account_id=enterprise_account_id,
            account_group_id=account_group_id,
            account_id=account_id,
            next_docid=next_docid,
            limit=limit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'enterprise_account_id={}'.format(enterprise_account_id) in query_string
        assert 'account_group_id={}'.format(account_group_id) in query_string
        assert 'account_id={}'.format(account_id) in query_string
        assert 'next_docid={}'.format(next_docid) in query_string
        assert 'limit={}'.format(limit) in query_string

    def test_list_enterprises_all_params_with_retries(self):
        # Enable retries and run test_list_enterprises_all_params.
        _service.enable_retries()
        self.test_list_enterprises_all_params()

        # Disable retries and run test_list_enterprises_all_params.
        _service.disable_retries()
        self.test_list_enterprises_all_params()

    @responses.activate
    def test_list_enterprises_required_params(self):
        """
        test_list_enterprises_required_params()
        """
        # Set up mock
        url = preprocess_url('/enterprises')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "enterprise_account_id": "enterprise_account_id", "crn": "crn", "name": "name", "domain": "domain", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "source_account_id": "source_account_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Invoke method
        response = _service.list_enterprises()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_enterprises_required_params_with_retries(self):
        # Enable retries and run test_list_enterprises_required_params.
        _service.enable_retries()
        self.test_list_enterprises_required_params()

        # Disable retries and run test_list_enterprises_required_params.
        _service.disable_retries()
        self.test_list_enterprises_required_params()

    @responses.activate
    def test_list_enterprises_with_pager_get_next(self):
        """
        test_list_enterprises_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/enterprises')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?next_docid=1","resources":[{"url":"url","id":"id","enterprise_account_id":"enterprise_account_id","crn":"crn","name":"name","domain":"domain","state":"state","primary_contact_iam_id":"primary_contact_iam_id","primary_contact_email":"primary_contact_email","source_account_id":"source_account_id","created_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_at":"2019-01-01T12:00:00.000Z","updated_by":"updated_by"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"url":"url","id":"id","enterprise_account_id":"enterprise_account_id","crn":"crn","name":"name","domain":"domain","state":"state","primary_contact_iam_id":"primary_contact_iam_id","primary_contact_email":"primary_contact_email","source_account_id":"source_account_id","created_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_at":"2019-01-01T12:00:00.000Z","updated_by":"updated_by"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = EnterprisesPager(
            client=_service,
            enterprise_account_id='testString',
            account_group_id='testString',
            account_id='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_enterprises_with_pager_get_all(self):
        """
        test_list_enterprises_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/enterprises')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?next_docid=1","resources":[{"url":"url","id":"id","enterprise_account_id":"enterprise_account_id","crn":"crn","name":"name","domain":"domain","state":"state","primary_contact_iam_id":"primary_contact_iam_id","primary_contact_email":"primary_contact_email","source_account_id":"source_account_id","created_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_at":"2019-01-01T12:00:00.000Z","updated_by":"updated_by"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"url":"url","id":"id","enterprise_account_id":"enterprise_account_id","crn":"crn","name":"name","domain":"domain","state":"state","primary_contact_iam_id":"primary_contact_iam_id","primary_contact_email":"primary_contact_email","source_account_id":"source_account_id","created_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_at":"2019-01-01T12:00:00.000Z","updated_by":"updated_by"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = EnterprisesPager(
            client=_service,
            enterprise_account_id='testString',
            account_group_id='testString',
            account_id='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetEnterprise:
    """
    Test Class for get_enterprise
    """

    @responses.activate
    def test_get_enterprise_all_params(self):
        """
        get_enterprise()
        """
        # Set up mock
        url = preprocess_url('/enterprises/testString')
        mock_response = '{"url": "url", "id": "id", "enterprise_account_id": "enterprise_account_id", "crn": "crn", "name": "name", "domain": "domain", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "source_account_id": "source_account_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        enterprise_id = 'testString'

        # Invoke method
        response = _service.get_enterprise(enterprise_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_enterprise_all_params_with_retries(self):
        # Enable retries and run test_get_enterprise_all_params.
        _service.enable_retries()
        self.test_get_enterprise_all_params()

        # Disable retries and run test_get_enterprise_all_params.
        _service.disable_retries()
        self.test_get_enterprise_all_params()

    @responses.activate
    def test_get_enterprise_value_error(self):
        """
        test_get_enterprise_value_error()
        """
        # Set up mock
        url = preprocess_url('/enterprises/testString')
        mock_response = '{"url": "url", "id": "id", "enterprise_account_id": "enterprise_account_id", "crn": "crn", "name": "name", "domain": "domain", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "source_account_id": "source_account_id", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        enterprise_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "enterprise_id": enterprise_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_enterprise(**req_copy)

    def test_get_enterprise_value_error_with_retries(self):
        # Enable retries and run test_get_enterprise_value_error.
        _service.enable_retries()
        self.test_get_enterprise_value_error()

        # Disable retries and run test_get_enterprise_value_error.
        _service.disable_retries()
        self.test_get_enterprise_value_error()


class TestUpdateEnterprise:
    """
    Test Class for update_enterprise
    """

    @responses.activate
    def test_update_enterprise_all_params(self):
        """
        update_enterprise()
        """
        # Set up mock
        url = preprocess_url('/enterprises/testString')
        responses.add(responses.PATCH, url, status=204)

        # Set up parameter values
        enterprise_id = 'testString'
        name = 'testString'
        domain = 'testString'
        primary_contact_iam_id = 'testString'

        # Invoke method
        response = _service.update_enterprise(
            enterprise_id, name=name, domain=domain, primary_contact_iam_id=primary_contact_iam_id, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['domain'] == 'testString'
        assert req_body['primary_contact_iam_id'] == 'testString'

    def test_update_enterprise_all_params_with_retries(self):
        # Enable retries and run test_update_enterprise_all_params.
        _service.enable_retries()
        self.test_update_enterprise_all_params()

        # Disable retries and run test_update_enterprise_all_params.
        _service.disable_retries()
        self.test_update_enterprise_all_params()

    @responses.activate
    def test_update_enterprise_value_error(self):
        """
        test_update_enterprise_value_error()
        """
        # Set up mock
        url = preprocess_url('/enterprises/testString')
        responses.add(responses.PATCH, url, status=204)

        # Set up parameter values
        enterprise_id = 'testString'
        name = 'testString'
        domain = 'testString'
        primary_contact_iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "enterprise_id": enterprise_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_enterprise(**req_copy)

    def test_update_enterprise_value_error_with_retries(self):
        # Enable retries and run test_update_enterprise_value_error.
        _service.enable_retries()
        self.test_update_enterprise_value_error()

        # Disable retries and run test_update_enterprise_value_error.
        _service.disable_retries()
        self.test_update_enterprise_value_error()


# endregion
##############################################################################
# End of Service: EnterpriseOperations
##############################################################################

##############################################################################
# Start of Service: AccountOperations
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

        service = EnterpriseManagementV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, EnterpriseManagementV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = EnterpriseManagementV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestImportAccountToEnterprise:
    """
    Test Class for import_account_to_enterprise
    """

    @responses.activate
    def test_import_account_to_enterprise_all_params(self):
        """
        import_account_to_enterprise()
        """
        # Set up mock
        url = preprocess_url('/enterprises/testString/import/accounts/testString')
        responses.add(responses.PUT, url, status=202)

        # Set up parameter values
        enterprise_id = 'testString'
        account_id = 'testString'
        parent = 'testString'
        billing_unit_id = 'testString'

        # Invoke method
        response = _service.import_account_to_enterprise(
            enterprise_id, account_id, parent=parent, billing_unit_id=billing_unit_id, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parent'] == 'testString'
        assert req_body['billing_unit_id'] == 'testString'

    def test_import_account_to_enterprise_all_params_with_retries(self):
        # Enable retries and run test_import_account_to_enterprise_all_params.
        _service.enable_retries()
        self.test_import_account_to_enterprise_all_params()

        # Disable retries and run test_import_account_to_enterprise_all_params.
        _service.disable_retries()
        self.test_import_account_to_enterprise_all_params()

    @responses.activate
    def test_import_account_to_enterprise_required_params(self):
        """
        test_import_account_to_enterprise_required_params()
        """
        # Set up mock
        url = preprocess_url('/enterprises/testString/import/accounts/testString')
        responses.add(responses.PUT, url, status=202)

        # Set up parameter values
        enterprise_id = 'testString'
        account_id = 'testString'

        # Invoke method
        response = _service.import_account_to_enterprise(enterprise_id, account_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_import_account_to_enterprise_required_params_with_retries(self):
        # Enable retries and run test_import_account_to_enterprise_required_params.
        _service.enable_retries()
        self.test_import_account_to_enterprise_required_params()

        # Disable retries and run test_import_account_to_enterprise_required_params.
        _service.disable_retries()
        self.test_import_account_to_enterprise_required_params()

    @responses.activate
    def test_import_account_to_enterprise_value_error(self):
        """
        test_import_account_to_enterprise_value_error()
        """
        # Set up mock
        url = preprocess_url('/enterprises/testString/import/accounts/testString')
        responses.add(responses.PUT, url, status=202)

        # Set up parameter values
        enterprise_id = 'testString'
        account_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "enterprise_id": enterprise_id,
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.import_account_to_enterprise(**req_copy)

    def test_import_account_to_enterprise_value_error_with_retries(self):
        # Enable retries and run test_import_account_to_enterprise_value_error.
        _service.enable_retries()
        self.test_import_account_to_enterprise_value_error()

        # Disable retries and run test_import_account_to_enterprise_value_error.
        _service.disable_retries()
        self.test_import_account_to_enterprise_value_error()


class TestCreateAccount:
    """
    Test Class for create_account
    """

    @responses.activate
    def test_create_account_all_params(self):
        """
        create_account()
        """
        # Set up mock
        url = preprocess_url('/accounts')
        mock_response = '{"account_id": "account_id"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=202)

        # Construct a dict representation of a CreateAccountRequestTraits model
        create_account_request_traits_model = {}
        create_account_request_traits_model['mfa'] = 'testString'
        create_account_request_traits_model['enterprise_iam_managed'] = True

        # Construct a dict representation of a CreateAccountRequestOptions model
        create_account_request_options_model = {}
        create_account_request_options_model['create_iam_service_id_with_apikey_and_owner_policies'] = True

        # Set up parameter values
        parent = 'testString'
        name = 'testString'
        owner_iam_id = 'testString'
        traits = create_account_request_traits_model
        options = create_account_request_options_model

        # Invoke method
        response = _service.create_account(parent, name, owner_iam_id, traits=traits, options=options, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parent'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['owner_iam_id'] == 'testString'
        assert req_body['traits'] == create_account_request_traits_model
        assert req_body['options'] == create_account_request_options_model

    def test_create_account_all_params_with_retries(self):
        # Enable retries and run test_create_account_all_params.
        _service.enable_retries()
        self.test_create_account_all_params()

        # Disable retries and run test_create_account_all_params.
        _service.disable_retries()
        self.test_create_account_all_params()

    @responses.activate
    def test_create_account_value_error(self):
        """
        test_create_account_value_error()
        """
        # Set up mock
        url = preprocess_url('/accounts')
        mock_response = '{"account_id": "account_id"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=202)

        # Construct a dict representation of a CreateAccountRequestTraits model
        create_account_request_traits_model = {}
        create_account_request_traits_model['mfa'] = 'testString'
        create_account_request_traits_model['enterprise_iam_managed'] = True

        # Construct a dict representation of a CreateAccountRequestOptions model
        create_account_request_options_model = {}
        create_account_request_options_model['create_iam_service_id_with_apikey_and_owner_policies'] = True

        # Set up parameter values
        parent = 'testString'
        name = 'testString'
        owner_iam_id = 'testString'
        traits = create_account_request_traits_model
        options = create_account_request_options_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "parent": parent,
            "name": name,
            "owner_iam_id": owner_iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_account(**req_copy)

    def test_create_account_value_error_with_retries(self):
        # Enable retries and run test_create_account_value_error.
        _service.enable_retries()
        self.test_create_account_value_error()

        # Disable retries and run test_create_account_value_error.
        _service.disable_retries()
        self.test_create_account_value_error()


class TestListAccounts:
    """
    Test Class for list_accounts
    """

    @responses.activate
    def test_list_accounts_all_params(self):
        """
        list_accounts()
        """
        # Set up mock
        url = preprocess_url('/accounts')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "owner_iam_id": "owner_iam_id", "paid": true, "owner_email": "owner_email", "is_enterprise_account": false, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        enterprise_id = 'testString'
        account_group_id = 'testString'
        next_docid = 'testString'
        parent = 'testString'
        limit = 100
        include_deleted = True

        # Invoke method
        response = _service.list_accounts(
            enterprise_id=enterprise_id,
            account_group_id=account_group_id,
            next_docid=next_docid,
            parent=parent,
            limit=limit,
            include_deleted=include_deleted,
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
        assert 'next_docid={}'.format(next_docid) in query_string
        assert 'parent={}'.format(parent) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'include_deleted={}'.format('true' if include_deleted else 'false') in query_string

    def test_list_accounts_all_params_with_retries(self):
        # Enable retries and run test_list_accounts_all_params.
        _service.enable_retries()
        self.test_list_accounts_all_params()

        # Disable retries and run test_list_accounts_all_params.
        _service.disable_retries()
        self.test_list_accounts_all_params()

    @responses.activate
    def test_list_accounts_required_params(self):
        """
        test_list_accounts_required_params()
        """
        # Set up mock
        url = preprocess_url('/accounts')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "owner_iam_id": "owner_iam_id", "paid": true, "owner_email": "owner_email", "is_enterprise_account": false, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Invoke method
        response = _service.list_accounts()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_accounts_required_params_with_retries(self):
        # Enable retries and run test_list_accounts_required_params.
        _service.enable_retries()
        self.test_list_accounts_required_params()

        # Disable retries and run test_list_accounts_required_params.
        _service.disable_retries()
        self.test_list_accounts_required_params()

    @responses.activate
    def test_list_accounts_with_pager_get_next(self):
        """
        test_list_accounts_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/accounts')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?next_docid=1","resources":[{"url":"url","id":"id","crn":"crn","parent":"parent","enterprise_account_id":"enterprise_account_id","enterprise_id":"enterprise_id","enterprise_path":"enterprise_path","name":"name","state":"state","owner_iam_id":"owner_iam_id","paid":true,"owner_email":"owner_email","is_enterprise_account":false,"created_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_at":"2019-01-01T12:00:00.000Z","updated_by":"updated_by"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"url":"url","id":"id","crn":"crn","parent":"parent","enterprise_account_id":"enterprise_account_id","enterprise_id":"enterprise_id","enterprise_path":"enterprise_path","name":"name","state":"state","owner_iam_id":"owner_iam_id","paid":true,"owner_email":"owner_email","is_enterprise_account":false,"created_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_at":"2019-01-01T12:00:00.000Z","updated_by":"updated_by"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = AccountsPager(
            client=_service,
            enterprise_id='testString',
            account_group_id='testString',
            parent='testString',
            limit=10,
            include_deleted=True,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_accounts_with_pager_get_all(self):
        """
        test_list_accounts_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/accounts')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?next_docid=1","resources":[{"url":"url","id":"id","crn":"crn","parent":"parent","enterprise_account_id":"enterprise_account_id","enterprise_id":"enterprise_id","enterprise_path":"enterprise_path","name":"name","state":"state","owner_iam_id":"owner_iam_id","paid":true,"owner_email":"owner_email","is_enterprise_account":false,"created_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_at":"2019-01-01T12:00:00.000Z","updated_by":"updated_by"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"url":"url","id":"id","crn":"crn","parent":"parent","enterprise_account_id":"enterprise_account_id","enterprise_id":"enterprise_id","enterprise_path":"enterprise_path","name":"name","state":"state","owner_iam_id":"owner_iam_id","paid":true,"owner_email":"owner_email","is_enterprise_account":false,"created_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_at":"2019-01-01T12:00:00.000Z","updated_by":"updated_by"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = AccountsPager(
            client=_service,
            enterprise_id='testString',
            account_group_id='testString',
            parent='testString',
            limit=10,
            include_deleted=True,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetAccount:
    """
    Test Class for get_account
    """

    @responses.activate
    def test_get_account_all_params(self):
        """
        get_account()
        """
        # Set up mock
        url = preprocess_url('/accounts/testString')
        mock_response = '{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "owner_iam_id": "owner_iam_id", "paid": true, "owner_email": "owner_email", "is_enterprise_account": false, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.get_account(account_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_account_all_params_with_retries(self):
        # Enable retries and run test_get_account_all_params.
        _service.enable_retries()
        self.test_get_account_all_params()

        # Disable retries and run test_get_account_all_params.
        _service.disable_retries()
        self.test_get_account_all_params()

    @responses.activate
    def test_get_account_value_error(self):
        """
        test_get_account_value_error()
        """
        # Set up mock
        url = preprocess_url('/accounts/testString')
        mock_response = '{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "owner_iam_id": "owner_iam_id", "paid": true, "owner_email": "owner_email", "is_enterprise_account": false, "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_account(**req_copy)

    def test_get_account_value_error_with_retries(self):
        # Enable retries and run test_get_account_value_error.
        _service.enable_retries()
        self.test_get_account_value_error()

        # Disable retries and run test_get_account_value_error.
        _service.disable_retries()
        self.test_get_account_value_error()


class TestUpdateAccount:
    """
    Test Class for update_account
    """

    @responses.activate
    def test_update_account_all_params(self):
        """
        update_account()
        """
        # Set up mock
        url = preprocess_url('/accounts/testString')
        responses.add(responses.PATCH, url, status=202)

        # Set up parameter values
        account_id = 'testString'
        parent = 'testString'

        # Invoke method
        response = _service.update_account(account_id, parent, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parent'] == 'testString'

    def test_update_account_all_params_with_retries(self):
        # Enable retries and run test_update_account_all_params.
        _service.enable_retries()
        self.test_update_account_all_params()

        # Disable retries and run test_update_account_all_params.
        _service.disable_retries()
        self.test_update_account_all_params()

    @responses.activate
    def test_update_account_value_error(self):
        """
        test_update_account_value_error()
        """
        # Set up mock
        url = preprocess_url('/accounts/testString')
        responses.add(responses.PATCH, url, status=202)

        # Set up parameter values
        account_id = 'testString'
        parent = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "parent": parent,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_account(**req_copy)

    def test_update_account_value_error_with_retries(self):
        # Enable retries and run test_update_account_value_error.
        _service.enable_retries()
        self.test_update_account_value_error()

        # Disable retries and run test_update_account_value_error.
        _service.disable_retries()
        self.test_update_account_value_error()


class TestDeleteAccount:
    """
    Test Class for delete_account
    """

    @responses.activate
    def test_delete_account_all_params(self):
        """
        delete_account()
        """
        # Set up mock
        url = preprocess_url('/accounts/testString')
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.delete_account(account_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_account_all_params_with_retries(self):
        # Enable retries and run test_delete_account_all_params.
        _service.enable_retries()
        self.test_delete_account_all_params()

        # Disable retries and run test_delete_account_all_params.
        _service.disable_retries()
        self.test_delete_account_all_params()

    @responses.activate
    def test_delete_account_value_error(self):
        """
        test_delete_account_value_error()
        """
        # Set up mock
        url = preprocess_url('/accounts/testString')
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        account_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_account(**req_copy)

    def test_delete_account_value_error_with_retries(self):
        # Enable retries and run test_delete_account_value_error.
        _service.enable_retries()
        self.test_delete_account_value_error()

        # Disable retries and run test_delete_account_value_error.
        _service.disable_retries()
        self.test_delete_account_value_error()


# endregion
##############################################################################
# End of Service: AccountOperations
##############################################################################

##############################################################################
# Start of Service: AccountGroupOperations
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

        service = EnterpriseManagementV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, EnterpriseManagementV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = EnterpriseManagementV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateAccountGroup:
    """
    Test Class for create_account_group
    """

    @responses.activate
    def test_create_account_group_all_params(self):
        """
        create_account_group()
        """
        # Set up mock
        url = preprocess_url('/account-groups')
        mock_response = '{"account_group_id": "account_group_id"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Set up parameter values
        parent = 'testString'
        name = 'testString'
        primary_contact_iam_id = 'testString'

        # Invoke method
        response = _service.create_account_group(parent, name, primary_contact_iam_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parent'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['primary_contact_iam_id'] == 'testString'

    def test_create_account_group_all_params_with_retries(self):
        # Enable retries and run test_create_account_group_all_params.
        _service.enable_retries()
        self.test_create_account_group_all_params()

        # Disable retries and run test_create_account_group_all_params.
        _service.disable_retries()
        self.test_create_account_group_all_params()

    @responses.activate
    def test_create_account_group_value_error(self):
        """
        test_create_account_group_value_error()
        """
        # Set up mock
        url = preprocess_url('/account-groups')
        mock_response = '{"account_group_id": "account_group_id"}'
        responses.add(responses.POST, url, body=mock_response, content_type='application/json', status=201)

        # Set up parameter values
        parent = 'testString'
        name = 'testString'
        primary_contact_iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "parent": parent,
            "name": name,
            "primary_contact_iam_id": primary_contact_iam_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_account_group(**req_copy)

    def test_create_account_group_value_error_with_retries(self):
        # Enable retries and run test_create_account_group_value_error.
        _service.enable_retries()
        self.test_create_account_group_value_error()

        # Disable retries and run test_create_account_group_value_error.
        _service.disable_retries()
        self.test_create_account_group_value_error()


class TestListAccountGroups:
    """
    Test Class for list_account_groups
    """

    @responses.activate
    def test_list_account_groups_all_params(self):
        """
        list_account_groups()
        """
        # Set up mock
        url = preprocess_url('/account-groups')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        enterprise_id = 'testString'
        parent_account_group_id = 'testString'
        next_docid = 'testString'
        parent = 'testString'
        limit = 100
        include_deleted = True

        # Invoke method
        response = _service.list_account_groups(
            enterprise_id=enterprise_id,
            parent_account_group_id=parent_account_group_id,
            next_docid=next_docid,
            parent=parent,
            limit=limit,
            include_deleted=include_deleted,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'enterprise_id={}'.format(enterprise_id) in query_string
        assert 'parent_account_group_id={}'.format(parent_account_group_id) in query_string
        assert 'next_docid={}'.format(next_docid) in query_string
        assert 'parent={}'.format(parent) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'include_deleted={}'.format('true' if include_deleted else 'false') in query_string

    def test_list_account_groups_all_params_with_retries(self):
        # Enable retries and run test_list_account_groups_all_params.
        _service.enable_retries()
        self.test_list_account_groups_all_params()

        # Disable retries and run test_list_account_groups_all_params.
        _service.disable_retries()
        self.test_list_account_groups_all_params()

    @responses.activate
    def test_list_account_groups_required_params(self):
        """
        test_list_account_groups_required_params()
        """
        # Set up mock
        url = preprocess_url('/account-groups')
        mock_response = '{"rows_count": 10, "next_url": "next_url", "resources": [{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}]}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Invoke method
        response = _service.list_account_groups()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_account_groups_required_params_with_retries(self):
        # Enable retries and run test_list_account_groups_required_params.
        _service.enable_retries()
        self.test_list_account_groups_required_params()

        # Disable retries and run test_list_account_groups_required_params.
        _service.disable_retries()
        self.test_list_account_groups_required_params()

    @responses.activate
    def test_list_account_groups_with_pager_get_next(self):
        """
        test_list_account_groups_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/account-groups')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?next_docid=1","resources":[{"url":"url","id":"id","crn":"crn","parent":"parent","enterprise_account_id":"enterprise_account_id","enterprise_id":"enterprise_id","enterprise_path":"enterprise_path","name":"name","state":"state","primary_contact_iam_id":"primary_contact_iam_id","primary_contact_email":"primary_contact_email","created_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_at":"2019-01-01T12:00:00.000Z","updated_by":"updated_by"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"url":"url","id":"id","crn":"crn","parent":"parent","enterprise_account_id":"enterprise_account_id","enterprise_id":"enterprise_id","enterprise_path":"enterprise_path","name":"name","state":"state","primary_contact_iam_id":"primary_contact_iam_id","primary_contact_email":"primary_contact_email","created_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_at":"2019-01-01T12:00:00.000Z","updated_by":"updated_by"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = AccountGroupsPager(
            client=_service,
            enterprise_id='testString',
            parent_account_group_id='testString',
            parent='testString',
            limit=10,
            include_deleted=True,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_account_groups_with_pager_get_all(self):
        """
        test_list_account_groups_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/account-groups')
        mock_response1 = '{"total_count":2,"limit":1,"next_url":"https://myhost.com/somePath?next_docid=1","resources":[{"url":"url","id":"id","crn":"crn","parent":"parent","enterprise_account_id":"enterprise_account_id","enterprise_id":"enterprise_id","enterprise_path":"enterprise_path","name":"name","state":"state","primary_contact_iam_id":"primary_contact_iam_id","primary_contact_email":"primary_contact_email","created_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_at":"2019-01-01T12:00:00.000Z","updated_by":"updated_by"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"url":"url","id":"id","crn":"crn","parent":"parent","enterprise_account_id":"enterprise_account_id","enterprise_id":"enterprise_id","enterprise_path":"enterprise_path","name":"name","state":"state","primary_contact_iam_id":"primary_contact_iam_id","primary_contact_email":"primary_contact_email","created_at":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_at":"2019-01-01T12:00:00.000Z","updated_by":"updated_by"}]}'
        responses.add(responses.GET, url, body=mock_response1, content_type='application/json', status=200)
        responses.add(responses.GET, url, body=mock_response2, content_type='application/json', status=200)

        # Exercise the pager class for this operation
        pager = AccountGroupsPager(
            client=_service,
            enterprise_id='testString',
            parent_account_group_id='testString',
            parent='testString',
            limit=10,
            include_deleted=True,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetAccountGroup:
    """
    Test Class for get_account_group
    """

    @responses.activate
    def test_get_account_group_all_params(self):
        """
        get_account_group()
        """
        # Set up mock
        url = preprocess_url('/account-groups/testString')
        mock_response = '{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_group_id = 'testString'

        # Invoke method
        response = _service.get_account_group(account_group_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_account_group_all_params_with_retries(self):
        # Enable retries and run test_get_account_group_all_params.
        _service.enable_retries()
        self.test_get_account_group_all_params()

        # Disable retries and run test_get_account_group_all_params.
        _service.disable_retries()
        self.test_get_account_group_all_params()

    @responses.activate
    def test_get_account_group_value_error(self):
        """
        test_get_account_group_value_error()
        """
        # Set up mock
        url = preprocess_url('/account-groups/testString')
        mock_response = '{"url": "url", "id": "id", "crn": "crn", "parent": "parent", "enterprise_account_id": "enterprise_account_id", "enterprise_id": "enterprise_id", "enterprise_path": "enterprise_path", "name": "name", "state": "state", "primary_contact_iam_id": "primary_contact_iam_id", "primary_contact_email": "primary_contact_email", "created_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by"}'
        responses.add(responses.GET, url, body=mock_response, content_type='application/json', status=200)

        # Set up parameter values
        account_group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_group_id": account_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_account_group(**req_copy)

    def test_get_account_group_value_error_with_retries(self):
        # Enable retries and run test_get_account_group_value_error.
        _service.enable_retries()
        self.test_get_account_group_value_error()

        # Disable retries and run test_get_account_group_value_error.
        _service.disable_retries()
        self.test_get_account_group_value_error()


class TestUpdateAccountGroup:
    """
    Test Class for update_account_group
    """

    @responses.activate
    def test_update_account_group_all_params(self):
        """
        update_account_group()
        """
        # Set up mock
        url = preprocess_url('/account-groups/testString')
        responses.add(responses.PATCH, url, status=204)

        # Set up parameter values
        account_group_id = 'testString'
        name = 'testString'
        primary_contact_iam_id = 'testString'

        # Invoke method
        response = _service.update_account_group(
            account_group_id, name=name, primary_contact_iam_id=primary_contact_iam_id, headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['primary_contact_iam_id'] == 'testString'

    def test_update_account_group_all_params_with_retries(self):
        # Enable retries and run test_update_account_group_all_params.
        _service.enable_retries()
        self.test_update_account_group_all_params()

        # Disable retries and run test_update_account_group_all_params.
        _service.disable_retries()
        self.test_update_account_group_all_params()

    @responses.activate
    def test_update_account_group_value_error(self):
        """
        test_update_account_group_value_error()
        """
        # Set up mock
        url = preprocess_url('/account-groups/testString')
        responses.add(responses.PATCH, url, status=204)

        # Set up parameter values
        account_group_id = 'testString'
        name = 'testString'
        primary_contact_iam_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_group_id": account_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_account_group(**req_copy)

    def test_update_account_group_value_error_with_retries(self):
        # Enable retries and run test_update_account_group_value_error.
        _service.enable_retries()
        self.test_update_account_group_value_error()

        # Disable retries and run test_update_account_group_value_error.
        _service.disable_retries()
        self.test_update_account_group_value_error()


class TestDeleteAccountGroup:
    """
    Test Class for delete_account_group
    """

    @responses.activate
    def test_delete_account_group_all_params(self):
        """
        delete_account_group()
        """
        # Set up mock
        url = preprocess_url('/account-groups/testString')
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        account_group_id = 'testString'

        # Invoke method
        response = _service.delete_account_group(account_group_id, headers={})

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_account_group_all_params_with_retries(self):
        # Enable retries and run test_delete_account_group_all_params.
        _service.enable_retries()
        self.test_delete_account_group_all_params()

        # Disable retries and run test_delete_account_group_all_params.
        _service.disable_retries()
        self.test_delete_account_group_all_params()

    @responses.activate
    def test_delete_account_group_value_error(self):
        """
        test_delete_account_group_value_error()
        """
        # Set up mock
        url = preprocess_url('/account-groups/testString')
        responses.add(responses.DELETE, url, status=204)

        # Set up parameter values
        account_group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_group_id": account_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_account_group(**req_copy)

    def test_delete_account_group_value_error_with_retries(self):
        # Enable retries and run test_delete_account_group_value_error.
        _service.enable_retries()
        self.test_delete_account_group_value_error()

        # Disable retries and run test_delete_account_group_value_error.
        _service.disable_retries()
        self.test_delete_account_group_value_error()


# endregion
##############################################################################
# End of Service: AccountGroupOperations
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_Account:
    """
    Test Class for Account
    """

    def test_account_serialization(self):
        """
        Test serialization/deserialization for Account
        """

        # Construct a json representation of a Account model
        account_model_json = {}
        account_model_json['url'] = 'testString'
        account_model_json['id'] = 'testString'
        account_model_json['crn'] = 'testString'
        account_model_json['parent'] = 'testString'
        account_model_json['enterprise_account_id'] = 'testString'
        account_model_json['enterprise_id'] = 'testString'
        account_model_json['enterprise_path'] = 'testString'
        account_model_json['name'] = 'testString'
        account_model_json['state'] = 'testString'
        account_model_json['owner_iam_id'] = 'testString'
        account_model_json['paid'] = True
        account_model_json['owner_email'] = 'testString'
        account_model_json['is_enterprise_account'] = True
        account_model_json['created_at'] = '2019-01-01T12:00:00Z'
        account_model_json['created_by'] = 'testString'
        account_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        account_model_json['updated_by'] = 'testString'

        # Construct a model instance of Account by calling from_dict on the json representation
        account_model = Account.from_dict(account_model_json)
        assert account_model != False

        # Construct a model instance of Account by calling from_dict on the json representation
        account_model_dict = Account.from_dict(account_model_json).__dict__
        account_model2 = Account(**account_model_dict)

        # Verify the model instances are equivalent
        assert account_model == account_model2

        # Convert model instance back to dict and verify no loss of data
        account_model_json2 = account_model.to_dict()
        assert account_model_json2 == account_model_json


class TestModel_AccountGroup:
    """
    Test Class for AccountGroup
    """

    def test_account_group_serialization(self):
        """
        Test serialization/deserialization for AccountGroup
        """

        # Construct a json representation of a AccountGroup model
        account_group_model_json = {}
        account_group_model_json['url'] = 'testString'
        account_group_model_json['id'] = 'testString'
        account_group_model_json['crn'] = 'testString'
        account_group_model_json['parent'] = 'testString'
        account_group_model_json['enterprise_account_id'] = 'testString'
        account_group_model_json['enterprise_id'] = 'testString'
        account_group_model_json['enterprise_path'] = 'testString'
        account_group_model_json['name'] = 'testString'
        account_group_model_json['state'] = 'testString'
        account_group_model_json['primary_contact_iam_id'] = 'testString'
        account_group_model_json['primary_contact_email'] = 'testString'
        account_group_model_json['created_at'] = '2019-01-01T12:00:00Z'
        account_group_model_json['created_by'] = 'testString'
        account_group_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        account_group_model_json['updated_by'] = 'testString'

        # Construct a model instance of AccountGroup by calling from_dict on the json representation
        account_group_model = AccountGroup.from_dict(account_group_model_json)
        assert account_group_model != False

        # Construct a model instance of AccountGroup by calling from_dict on the json representation
        account_group_model_dict = AccountGroup.from_dict(account_group_model_json).__dict__
        account_group_model2 = AccountGroup(**account_group_model_dict)

        # Verify the model instances are equivalent
        assert account_group_model == account_group_model2

        # Convert model instance back to dict and verify no loss of data
        account_group_model_json2 = account_group_model.to_dict()
        assert account_group_model_json2 == account_group_model_json


class TestModel_CreateAccountGroupResponse:
    """
    Test Class for CreateAccountGroupResponse
    """

    def test_create_account_group_response_serialization(self):
        """
        Test serialization/deserialization for CreateAccountGroupResponse
        """

        # Construct a json representation of a CreateAccountGroupResponse model
        create_account_group_response_model_json = {}
        create_account_group_response_model_json['account_group_id'] = 'testString'

        # Construct a model instance of CreateAccountGroupResponse by calling from_dict on the json representation
        create_account_group_response_model = CreateAccountGroupResponse.from_dict(
            create_account_group_response_model_json
        )
        assert create_account_group_response_model != False

        # Construct a model instance of CreateAccountGroupResponse by calling from_dict on the json representation
        create_account_group_response_model_dict = CreateAccountGroupResponse.from_dict(
            create_account_group_response_model_json
        ).__dict__
        create_account_group_response_model2 = CreateAccountGroupResponse(**create_account_group_response_model_dict)

        # Verify the model instances are equivalent
        assert create_account_group_response_model == create_account_group_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_account_group_response_model_json2 = create_account_group_response_model.to_dict()
        assert create_account_group_response_model_json2 == create_account_group_response_model_json


class TestModel_CreateAccountRequestOptions:
    """
    Test Class for CreateAccountRequestOptions
    """

    def test_create_account_request_options_serialization(self):
        """
        Test serialization/deserialization for CreateAccountRequestOptions
        """

        # Construct a json representation of a CreateAccountRequestOptions model
        create_account_request_options_model_json = {}
        create_account_request_options_model_json['create_iam_service_id_with_apikey_and_owner_policies'] = True

        # Construct a model instance of CreateAccountRequestOptions by calling from_dict on the json representation
        create_account_request_options_model = CreateAccountRequestOptions.from_dict(
            create_account_request_options_model_json
        )
        assert create_account_request_options_model != False

        # Construct a model instance of CreateAccountRequestOptions by calling from_dict on the json representation
        create_account_request_options_model_dict = CreateAccountRequestOptions.from_dict(
            create_account_request_options_model_json
        ).__dict__
        create_account_request_options_model2 = CreateAccountRequestOptions(**create_account_request_options_model_dict)

        # Verify the model instances are equivalent
        assert create_account_request_options_model == create_account_request_options_model2

        # Convert model instance back to dict and verify no loss of data
        create_account_request_options_model_json2 = create_account_request_options_model.to_dict()
        assert create_account_request_options_model_json2 == create_account_request_options_model_json


class TestModel_CreateAccountRequestTraits:
    """
    Test Class for CreateAccountRequestTraits
    """

    def test_create_account_request_traits_serialization(self):
        """
        Test serialization/deserialization for CreateAccountRequestTraits
        """

        # Construct a json representation of a CreateAccountRequestTraits model
        create_account_request_traits_model_json = {}
        create_account_request_traits_model_json['mfa'] = 'testString'
        create_account_request_traits_model_json['enterprise_iam_managed'] = True

        # Construct a model instance of CreateAccountRequestTraits by calling from_dict on the json representation
        create_account_request_traits_model = CreateAccountRequestTraits.from_dict(
            create_account_request_traits_model_json
        )
        assert create_account_request_traits_model != False

        # Construct a model instance of CreateAccountRequestTraits by calling from_dict on the json representation
        create_account_request_traits_model_dict = CreateAccountRequestTraits.from_dict(
            create_account_request_traits_model_json
        ).__dict__
        create_account_request_traits_model2 = CreateAccountRequestTraits(**create_account_request_traits_model_dict)

        # Verify the model instances are equivalent
        assert create_account_request_traits_model == create_account_request_traits_model2

        # Convert model instance back to dict and verify no loss of data
        create_account_request_traits_model_json2 = create_account_request_traits_model.to_dict()
        assert create_account_request_traits_model_json2 == create_account_request_traits_model_json


class TestModel_CreateAccountResponse:
    """
    Test Class for CreateAccountResponse
    """

    def test_create_account_response_serialization(self):
        """
        Test serialization/deserialization for CreateAccountResponse
        """

        # Construct a json representation of a CreateAccountResponse model
        create_account_response_model_json = {}
        create_account_response_model_json['account_id'] = 'testString'

        # Construct a model instance of CreateAccountResponse by calling from_dict on the json representation
        create_account_response_model = CreateAccountResponse.from_dict(create_account_response_model_json)
        assert create_account_response_model != False

        # Construct a model instance of CreateAccountResponse by calling from_dict on the json representation
        create_account_response_model_dict = CreateAccountResponse.from_dict(
            create_account_response_model_json
        ).__dict__
        create_account_response_model2 = CreateAccountResponse(**create_account_response_model_dict)

        # Verify the model instances are equivalent
        assert create_account_response_model == create_account_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_account_response_model_json2 = create_account_response_model.to_dict()
        assert create_account_response_model_json2 == create_account_response_model_json


class TestModel_CreateEnterpriseResponse:
    """
    Test Class for CreateEnterpriseResponse
    """

    def test_create_enterprise_response_serialization(self):
        """
        Test serialization/deserialization for CreateEnterpriseResponse
        """

        # Construct a json representation of a CreateEnterpriseResponse model
        create_enterprise_response_model_json = {}
        create_enterprise_response_model_json['enterprise_id'] = 'testString'
        create_enterprise_response_model_json['enterprise_account_id'] = 'testString'

        # Construct a model instance of CreateEnterpriseResponse by calling from_dict on the json representation
        create_enterprise_response_model = CreateEnterpriseResponse.from_dict(create_enterprise_response_model_json)
        assert create_enterprise_response_model != False

        # Construct a model instance of CreateEnterpriseResponse by calling from_dict on the json representation
        create_enterprise_response_model_dict = CreateEnterpriseResponse.from_dict(
            create_enterprise_response_model_json
        ).__dict__
        create_enterprise_response_model2 = CreateEnterpriseResponse(**create_enterprise_response_model_dict)

        # Verify the model instances are equivalent
        assert create_enterprise_response_model == create_enterprise_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_enterprise_response_model_json2 = create_enterprise_response_model.to_dict()
        assert create_enterprise_response_model_json2 == create_enterprise_response_model_json


class TestModel_Enterprise:
    """
    Test Class for Enterprise
    """

    def test_enterprise_serialization(self):
        """
        Test serialization/deserialization for Enterprise
        """

        # Construct a json representation of a Enterprise model
        enterprise_model_json = {}
        enterprise_model_json['url'] = 'testString'
        enterprise_model_json['id'] = 'testString'
        enterprise_model_json['enterprise_account_id'] = 'testString'
        enterprise_model_json['crn'] = 'testString'
        enterprise_model_json['name'] = 'testString'
        enterprise_model_json['domain'] = 'testString'
        enterprise_model_json['state'] = 'testString'
        enterprise_model_json['primary_contact_iam_id'] = 'testString'
        enterprise_model_json['primary_contact_email'] = 'testString'
        enterprise_model_json['source_account_id'] = 'testString'
        enterprise_model_json['created_at'] = '2019-01-01T12:00:00Z'
        enterprise_model_json['created_by'] = 'testString'
        enterprise_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        enterprise_model_json['updated_by'] = 'testString'

        # Construct a model instance of Enterprise by calling from_dict on the json representation
        enterprise_model = Enterprise.from_dict(enterprise_model_json)
        assert enterprise_model != False

        # Construct a model instance of Enterprise by calling from_dict on the json representation
        enterprise_model_dict = Enterprise.from_dict(enterprise_model_json).__dict__
        enterprise_model2 = Enterprise(**enterprise_model_dict)

        # Verify the model instances are equivalent
        assert enterprise_model == enterprise_model2

        # Convert model instance back to dict and verify no loss of data
        enterprise_model_json2 = enterprise_model.to_dict()
        assert enterprise_model_json2 == enterprise_model_json


class TestModel_ListAccountGroupsResponse:
    """
    Test Class for ListAccountGroupsResponse
    """

    def test_list_account_groups_response_serialization(self):
        """
        Test serialization/deserialization for ListAccountGroupsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        account_group_model = {}  # AccountGroup
        account_group_model['url'] = 'testString'
        account_group_model['id'] = 'testString'
        account_group_model['crn'] = 'testString'
        account_group_model['parent'] = 'testString'
        account_group_model['enterprise_account_id'] = 'testString'
        account_group_model['enterprise_id'] = 'testString'
        account_group_model['enterprise_path'] = 'testString'
        account_group_model['name'] = 'testString'
        account_group_model['state'] = 'testString'
        account_group_model['primary_contact_iam_id'] = 'testString'
        account_group_model['primary_contact_email'] = 'testString'
        account_group_model['created_at'] = '2019-01-01T12:00:00Z'
        account_group_model['created_by'] = 'testString'
        account_group_model['updated_at'] = '2019-01-01T12:00:00Z'
        account_group_model['updated_by'] = 'testString'

        # Construct a json representation of a ListAccountGroupsResponse model
        list_account_groups_response_model_json = {}
        list_account_groups_response_model_json['rows_count'] = 38
        list_account_groups_response_model_json['next_url'] = 'testString'
        list_account_groups_response_model_json['resources'] = [account_group_model]

        # Construct a model instance of ListAccountGroupsResponse by calling from_dict on the json representation
        list_account_groups_response_model = ListAccountGroupsResponse.from_dict(
            list_account_groups_response_model_json
        )
        assert list_account_groups_response_model != False

        # Construct a model instance of ListAccountGroupsResponse by calling from_dict on the json representation
        list_account_groups_response_model_dict = ListAccountGroupsResponse.from_dict(
            list_account_groups_response_model_json
        ).__dict__
        list_account_groups_response_model2 = ListAccountGroupsResponse(**list_account_groups_response_model_dict)

        # Verify the model instances are equivalent
        assert list_account_groups_response_model == list_account_groups_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_account_groups_response_model_json2 = list_account_groups_response_model.to_dict()
        assert list_account_groups_response_model_json2 == list_account_groups_response_model_json


class TestModel_ListAccountsResponse:
    """
    Test Class for ListAccountsResponse
    """

    def test_list_accounts_response_serialization(self):
        """
        Test serialization/deserialization for ListAccountsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        account_model = {}  # Account
        account_model['url'] = 'testString'
        account_model['id'] = 'testString'
        account_model['crn'] = 'testString'
        account_model['parent'] = 'testString'
        account_model['enterprise_account_id'] = 'testString'
        account_model['enterprise_id'] = 'testString'
        account_model['enterprise_path'] = 'testString'
        account_model['name'] = 'testString'
        account_model['state'] = 'testString'
        account_model['owner_iam_id'] = 'testString'
        account_model['paid'] = True
        account_model['owner_email'] = 'testString'
        account_model['is_enterprise_account'] = True
        account_model['created_at'] = '2019-01-01T12:00:00Z'
        account_model['created_by'] = 'testString'
        account_model['updated_at'] = '2019-01-01T12:00:00Z'
        account_model['updated_by'] = 'testString'

        # Construct a json representation of a ListAccountsResponse model
        list_accounts_response_model_json = {}
        list_accounts_response_model_json['rows_count'] = 38
        list_accounts_response_model_json['next_url'] = 'testString'
        list_accounts_response_model_json['resources'] = [account_model]

        # Construct a model instance of ListAccountsResponse by calling from_dict on the json representation
        list_accounts_response_model = ListAccountsResponse.from_dict(list_accounts_response_model_json)
        assert list_accounts_response_model != False

        # Construct a model instance of ListAccountsResponse by calling from_dict on the json representation
        list_accounts_response_model_dict = ListAccountsResponse.from_dict(list_accounts_response_model_json).__dict__
        list_accounts_response_model2 = ListAccountsResponse(**list_accounts_response_model_dict)

        # Verify the model instances are equivalent
        assert list_accounts_response_model == list_accounts_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_accounts_response_model_json2 = list_accounts_response_model.to_dict()
        assert list_accounts_response_model_json2 == list_accounts_response_model_json


class TestModel_ListEnterprisesResponse:
    """
    Test Class for ListEnterprisesResponse
    """

    def test_list_enterprises_response_serialization(self):
        """
        Test serialization/deserialization for ListEnterprisesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        enterprise_model = {}  # Enterprise
        enterprise_model['url'] = 'testString'
        enterprise_model['id'] = 'testString'
        enterprise_model['enterprise_account_id'] = 'testString'
        enterprise_model['crn'] = 'testString'
        enterprise_model['name'] = 'testString'
        enterprise_model['domain'] = 'testString'
        enterprise_model['state'] = 'testString'
        enterprise_model['primary_contact_iam_id'] = 'testString'
        enterprise_model['primary_contact_email'] = 'testString'
        enterprise_model['source_account_id'] = 'testString'
        enterprise_model['created_at'] = '2019-01-01T12:00:00Z'
        enterprise_model['created_by'] = 'testString'
        enterprise_model['updated_at'] = '2019-01-01T12:00:00Z'
        enterprise_model['updated_by'] = 'testString'

        # Construct a json representation of a ListEnterprisesResponse model
        list_enterprises_response_model_json = {}
        list_enterprises_response_model_json['rows_count'] = 38
        list_enterprises_response_model_json['next_url'] = 'testString'
        list_enterprises_response_model_json['resources'] = [enterprise_model]

        # Construct a model instance of ListEnterprisesResponse by calling from_dict on the json representation
        list_enterprises_response_model = ListEnterprisesResponse.from_dict(list_enterprises_response_model_json)
        assert list_enterprises_response_model != False

        # Construct a model instance of ListEnterprisesResponse by calling from_dict on the json representation
        list_enterprises_response_model_dict = ListEnterprisesResponse.from_dict(
            list_enterprises_response_model_json
        ).__dict__
        list_enterprises_response_model2 = ListEnterprisesResponse(**list_enterprises_response_model_dict)

        # Verify the model instances are equivalent
        assert list_enterprises_response_model == list_enterprises_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_enterprises_response_model_json2 = list_enterprises_response_model.to_dict()
        assert list_enterprises_response_model_json2 == list_enterprises_response_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
