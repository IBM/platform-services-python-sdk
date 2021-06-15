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
Unit Tests for CatalogManagementV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_platform_services.catalog_management_v1 import *


_service = CatalogManagementV1(
    authenticator=NoAuthAuthenticator()
    )

_base_url = 'https://cm.globalcatalog.cloud.ibm.com/api/v1-beta'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: Account
##############################################################################
# region

class TestGetCatalogAccount():
    """
    Test Class for get_catalog_account
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
    def test_get_catalog_account_all_params(self):
        """
        get_catalog_account()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogaccount')
        mock_response = '{"id": "id", "hide_IBM_cloud_catalog": true, "account_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.get_catalog_account()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestUpdateCatalogAccount():
    """
    Test Class for update_catalog_account
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
    def test_update_catalog_account_all_params(self):
        """
        update_catalog_account()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogaccount')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a FilterTerms model
        filter_terms_model = {}
        filter_terms_model['filter_terms'] = ['testString']

        # Construct a dict representation of a CategoryFilter model
        category_filter_model = {}
        category_filter_model['include'] = True
        category_filter_model['filter'] = filter_terms_model

        # Construct a dict representation of a IDFilter model
        id_filter_model = {}
        id_filter_model['include'] = filter_terms_model
        id_filter_model['exclude'] = filter_terms_model

        # Construct a dict representation of a Filters model
        filters_model = {}
        filters_model['include_all'] = True
        filters_model['category_filters'] = {}
        filters_model['id_filters'] = id_filter_model

        # Set up parameter values
        id = 'testString'
        hide_ibm_cloud_catalog = True
        account_filters = filters_model

        # Invoke method
        response = _service.update_catalog_account(
            id=id,
            hide_ibm_cloud_catalog=hide_ibm_cloud_catalog,
            account_filters=account_filters,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['hide_IBM_cloud_catalog'] == True
        assert req_body['account_filters'] == filters_model


    @responses.activate
    def test_update_catalog_account_required_params(self):
        """
        test_update_catalog_account_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogaccount')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Invoke method
        response = _service.update_catalog_account()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetCatalogAccountAudit():
    """
    Test Class for get_catalog_account_audit
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
    def test_get_catalog_account_audit_all_params(self):
        """
        get_catalog_account_audit()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogaccount/audit')
        mock_response = '{"list": [{"id": "id", "created": "2019-01-01T12:00:00.000Z", "change_type": "change_type", "target_type": "target_type", "target_id": "target_id", "who_delegate_email": "who_delegate_email", "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.get_catalog_account_audit()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetCatalogAccountFilters():
    """
    Test Class for get_catalog_account_filters
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
    def test_get_catalog_account_filters_all_params(self):
        """
        get_catalog_account_filters()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogaccount/filters')
        mock_response = '{"account_filters": [{"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}], "catalog_filters": [{"catalog": {"id": "id", "name": "name"}, "filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog = 'testString'

        # Invoke method
        response = _service.get_catalog_account_filters(
            catalog=catalog,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'catalog={}'.format(catalog) in query_string


    @responses.activate
    def test_get_catalog_account_filters_required_params(self):
        """
        test_get_catalog_account_filters_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogaccount/filters')
        mock_response = '{"account_filters": [{"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}], "catalog_filters": [{"catalog": {"id": "id", "name": "name"}, "filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.get_catalog_account_filters()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Account
##############################################################################

##############################################################################
# Start of Service: Catalogs
##############################################################################
# region

class TestListCatalogs():
    """
    Test Class for list_catalogs
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
    def test_list_catalogs_all_params(self):
        """
        list_catalogs()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs')
        mock_response = '{"total_count": 11, "resources": [{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00.000Z"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00.000Z"}}, "kind": "kind"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_catalogs()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestCreateCatalog():
    """
    Test Class for create_catalog
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
    def test_create_catalog_all_params(self):
        """
        create_catalog()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs')
        mock_response = '{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00.000Z"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00.000Z"}}, "kind": "kind"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Feature model
        feature_model = {}
        feature_model['title'] = 'testString'
        feature_model['description'] = 'testString'

        # Construct a dict representation of a FilterTerms model
        filter_terms_model = {}
        filter_terms_model['filter_terms'] = ['testString']

        # Construct a dict representation of a CategoryFilter model
        category_filter_model = {}
        category_filter_model['include'] = True
        category_filter_model['filter'] = filter_terms_model

        # Construct a dict representation of a IDFilter model
        id_filter_model = {}
        id_filter_model['include'] = filter_terms_model
        id_filter_model['exclude'] = filter_terms_model

        # Construct a dict representation of a Filters model
        filters_model = {}
        filters_model['include_all'] = True
        filters_model['category_filters'] = {}
        filters_model['id_filters'] = id_filter_model

        # Construct a dict representation of a SyndicationCluster model
        syndication_cluster_model = {}
        syndication_cluster_model['region'] = 'testString'
        syndication_cluster_model['id'] = 'testString'
        syndication_cluster_model['name'] = 'testString'
        syndication_cluster_model['resource_group_name'] = 'testString'
        syndication_cluster_model['type'] = 'testString'
        syndication_cluster_model['namespaces'] = ['testString']
        syndication_cluster_model['all_namespaces'] = True

        # Construct a dict representation of a SyndicationHistory model
        syndication_history_model = {}
        syndication_history_model['namespaces'] = ['testString']
        syndication_history_model['clusters'] = [syndication_cluster_model]
        syndication_history_model['last_run'] = "2019-01-01T12:00:00Z"

        # Construct a dict representation of a SyndicationAuthorization model
        syndication_authorization_model = {}
        syndication_authorization_model['token'] = 'testString'
        syndication_authorization_model['last_run'] = "2019-01-01T12:00:00Z"

        # Construct a dict representation of a SyndicationResource model
        syndication_resource_model = {}
        syndication_resource_model['remove_related_components'] = True
        syndication_resource_model['clusters'] = [syndication_cluster_model]
        syndication_resource_model['history'] = syndication_history_model
        syndication_resource_model['authorization'] = syndication_authorization_model

        # Set up parameter values
        id = 'testString'
        rev = 'testString'
        label = 'testString'
        short_description = 'testString'
        catalog_icon_url = 'testString'
        tags = ['testString']
        features = [feature_model]
        disabled = True
        resource_group_id = 'testString'
        owning_account = 'testString'
        catalog_filters = filters_model
        syndication_settings = syndication_resource_model
        kind = 'testString'

        # Invoke method
        response = _service.create_catalog(
            id=id,
            rev=rev,
            label=label,
            short_description=short_description,
            catalog_icon_url=catalog_icon_url,
            tags=tags,
            features=features,
            disabled=disabled,
            resource_group_id=resource_group_id,
            owning_account=owning_account,
            catalog_filters=catalog_filters,
            syndication_settings=syndication_settings,
            kind=kind,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['_rev'] == 'testString'
        assert req_body['label'] == 'testString'
        assert req_body['short_description'] == 'testString'
        assert req_body['catalog_icon_url'] == 'testString'
        assert req_body['tags'] == ['testString']
        assert req_body['features'] == [feature_model]
        assert req_body['disabled'] == True
        assert req_body['resource_group_id'] == 'testString'
        assert req_body['owning_account'] == 'testString'
        assert req_body['catalog_filters'] == filters_model
        assert req_body['syndication_settings'] == syndication_resource_model
        assert req_body['kind'] == 'testString'


    @responses.activate
    def test_create_catalog_required_params(self):
        """
        test_create_catalog_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs')
        mock_response = '{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00.000Z"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00.000Z"}}, "kind": "kind"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Invoke method
        response = _service.create_catalog()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


class TestGetCatalog():
    """
    Test Class for get_catalog
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
    def test_get_catalog_all_params(self):
        """
        get_catalog()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString')
        mock_response = '{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00.000Z"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00.000Z"}}, "kind": "kind"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Invoke method
        response = _service.get_catalog(
            catalog_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_catalog_value_error(self):
        """
        test_get_catalog_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString')
        mock_response = '{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00.000Z"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00.000Z"}}, "kind": "kind"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_catalog(**req_copy)



class TestReplaceCatalog():
    """
    Test Class for replace_catalog
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
    def test_replace_catalog_all_params(self):
        """
        replace_catalog()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString')
        mock_response = '{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00.000Z"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00.000Z"}}, "kind": "kind"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Feature model
        feature_model = {}
        feature_model['title'] = 'testString'
        feature_model['description'] = 'testString'

        # Construct a dict representation of a FilterTerms model
        filter_terms_model = {}
        filter_terms_model['filter_terms'] = ['testString']

        # Construct a dict representation of a CategoryFilter model
        category_filter_model = {}
        category_filter_model['include'] = True
        category_filter_model['filter'] = filter_terms_model

        # Construct a dict representation of a IDFilter model
        id_filter_model = {}
        id_filter_model['include'] = filter_terms_model
        id_filter_model['exclude'] = filter_terms_model

        # Construct a dict representation of a Filters model
        filters_model = {}
        filters_model['include_all'] = True
        filters_model['category_filters'] = {}
        filters_model['id_filters'] = id_filter_model

        # Construct a dict representation of a SyndicationCluster model
        syndication_cluster_model = {}
        syndication_cluster_model['region'] = 'testString'
        syndication_cluster_model['id'] = 'testString'
        syndication_cluster_model['name'] = 'testString'
        syndication_cluster_model['resource_group_name'] = 'testString'
        syndication_cluster_model['type'] = 'testString'
        syndication_cluster_model['namespaces'] = ['testString']
        syndication_cluster_model['all_namespaces'] = True

        # Construct a dict representation of a SyndicationHistory model
        syndication_history_model = {}
        syndication_history_model['namespaces'] = ['testString']
        syndication_history_model['clusters'] = [syndication_cluster_model]
        syndication_history_model['last_run'] = "2019-01-01T12:00:00Z"

        # Construct a dict representation of a SyndicationAuthorization model
        syndication_authorization_model = {}
        syndication_authorization_model['token'] = 'testString'
        syndication_authorization_model['last_run'] = "2019-01-01T12:00:00Z"

        # Construct a dict representation of a SyndicationResource model
        syndication_resource_model = {}
        syndication_resource_model['remove_related_components'] = True
        syndication_resource_model['clusters'] = [syndication_cluster_model]
        syndication_resource_model['history'] = syndication_history_model
        syndication_resource_model['authorization'] = syndication_authorization_model

        # Set up parameter values
        catalog_identifier = 'testString'
        id = 'testString'
        rev = 'testString'
        label = 'testString'
        short_description = 'testString'
        catalog_icon_url = 'testString'
        tags = ['testString']
        features = [feature_model]
        disabled = True
        resource_group_id = 'testString'
        owning_account = 'testString'
        catalog_filters = filters_model
        syndication_settings = syndication_resource_model
        kind = 'testString'

        # Invoke method
        response = _service.replace_catalog(
            catalog_identifier,
            id=id,
            rev=rev,
            label=label,
            short_description=short_description,
            catalog_icon_url=catalog_icon_url,
            tags=tags,
            features=features,
            disabled=disabled,
            resource_group_id=resource_group_id,
            owning_account=owning_account,
            catalog_filters=catalog_filters,
            syndication_settings=syndication_settings,
            kind=kind,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['_rev'] == 'testString'
        assert req_body['label'] == 'testString'
        assert req_body['short_description'] == 'testString'
        assert req_body['catalog_icon_url'] == 'testString'
        assert req_body['tags'] == ['testString']
        assert req_body['features'] == [feature_model]
        assert req_body['disabled'] == True
        assert req_body['resource_group_id'] == 'testString'
        assert req_body['owning_account'] == 'testString'
        assert req_body['catalog_filters'] == filters_model
        assert req_body['syndication_settings'] == syndication_resource_model
        assert req_body['kind'] == 'testString'


    @responses.activate
    def test_replace_catalog_required_params(self):
        """
        test_replace_catalog_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString')
        mock_response = '{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00.000Z"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00.000Z"}}, "kind": "kind"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Invoke method
        response = _service.replace_catalog(
            catalog_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_replace_catalog_value_error(self):
        """
        test_replace_catalog_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString')
        mock_response = '{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00.000Z"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00.000Z"}}, "kind": "kind"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_catalog(**req_copy)



class TestDeleteCatalog():
    """
    Test Class for delete_catalog
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
    def test_delete_catalog_all_params(self):
        """
        delete_catalog()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Invoke method
        response = _service.delete_catalog(
            catalog_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_catalog_value_error(self):
        """
        test_delete_catalog_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_catalog(**req_copy)



class TestGetCatalogAudit():
    """
    Test Class for get_catalog_audit
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
    def test_get_catalog_audit_all_params(self):
        """
        get_catalog_audit()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/audit')
        mock_response = '{"list": [{"id": "id", "created": "2019-01-01T12:00:00.000Z", "change_type": "change_type", "target_type": "target_type", "target_id": "target_id", "who_delegate_email": "who_delegate_email", "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Invoke method
        response = _service.get_catalog_audit(
            catalog_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_catalog_audit_value_error(self):
        """
        test_get_catalog_audit_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/audit')
        mock_response = '{"list": [{"id": "id", "created": "2019-01-01T12:00:00.000Z", "change_type": "change_type", "target_type": "target_type", "target_id": "target_id", "who_delegate_email": "who_delegate_email", "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_catalog_audit(**req_copy)



# endregion
##############################################################################
# End of Service: Catalogs
##############################################################################

##############################################################################
# Start of Service: Offerings
##############################################################################
# region

class TestGetConsumptionOfferings():
    """
    Test Class for get_consumption_offerings
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
    def test_get_consumption_offerings_all_params(self):
        """
        get_consumption_offerings()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/offerings')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        digest = True
        catalog = 'testString'
        select = 'all'
        include_hidden = True
        limit = 1000
        offset = 38

        # Invoke method
        response = _service.get_consumption_offerings(
            digest=digest,
            catalog=catalog,
            select=select,
            include_hidden=include_hidden,
            limit=limit,
            offset=offset,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'digest={}'.format('true' if digest else 'false') in query_string
        assert 'catalog={}'.format(catalog) in query_string
        assert 'select={}'.format(select) in query_string
        assert 'includeHidden={}'.format('true' if include_hidden else 'false') in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string


    @responses.activate
    def test_get_consumption_offerings_required_params(self):
        """
        test_get_consumption_offerings_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/offerings')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.get_consumption_offerings()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestListOfferings():
    """
    Test Class for list_offerings
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
    def test_list_offerings_all_params(self):
        """
        list_offerings()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        digest = True
        limit = 1000
        offset = 38
        name = 'testString'
        sort = 'testString'

        # Invoke method
        response = _service.list_offerings(
            catalog_identifier,
            digest=digest,
            limit=limit,
            offset=offset,
            name=name,
            sort=sort,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'digest={}'.format('true' if digest else 'false') in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'sort={}'.format(sort) in query_string


    @responses.activate
    def test_list_offerings_required_params(self):
        """
        test_list_offerings_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Invoke method
        response = _service.list_offerings(
            catalog_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_offerings_value_error(self):
        """
        test_list_offerings_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_offerings(**req_copy)



class TestCreateOffering():
    """
    Test Class for create_offering
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
    def test_create_offering_all_params(self):
        """
        create_offering()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Rating model
        rating_model = {}
        rating_model['one_star_count'] = 38
        rating_model['two_star_count'] = 38
        rating_model['three_star_count'] = 38
        rating_model['four_star_count'] = 38

        # Construct a dict representation of a Feature model
        feature_model = {}
        feature_model['title'] = 'testString'
        feature_model['description'] = 'testString'

        # Construct a dict representation of a Configuration model
        configuration_model = {}
        configuration_model['key'] = 'testString'
        configuration_model['type'] = 'testString'
        configuration_model['default_value'] = { 'foo': 'bar' }
        configuration_model['value_constraint'] = 'testString'
        configuration_model['description'] = 'testString'
        configuration_model['required'] = True
        configuration_model['options'] = [{ 'foo': 'bar' }]
        configuration_model['hidden'] = True

        # Construct a dict representation of a Validation model
        validation_model = {}
        validation_model['validated'] = "2019-01-01T12:00:00Z"
        validation_model['requested'] = "2019-01-01T12:00:00Z"
        validation_model['state'] = 'testString'
        validation_model['last_operation'] = 'testString'
        validation_model['target'] = {}

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['type'] = 'mem'
        resource_model['value'] = { 'foo': 'bar' }

        # Construct a dict representation of a Script model
        script_model = {}
        script_model['instructions'] = 'testString'
        script_model['script'] = 'testString'
        script_model['script_permission'] = 'testString'
        script_model['delete_script'] = 'testString'
        script_model['scope'] = 'testString'

        # Construct a dict representation of a VersionEntitlement model
        version_entitlement_model = {}
        version_entitlement_model['provider_name'] = 'testString'
        version_entitlement_model['provider_id'] = 'testString'
        version_entitlement_model['product_id'] = 'testString'
        version_entitlement_model['part_numbers'] = ['testString']
        version_entitlement_model['image_repo_name'] = 'testString'

        # Construct a dict representation of a License model
        license_model = {}
        license_model['id'] = 'testString'
        license_model['name'] = 'testString'
        license_model['type'] = 'testString'
        license_model['url'] = 'testString'
        license_model['description'] = 'testString'

        # Construct a dict representation of a State model
        state_model = {}
        state_model['current'] = 'testString'
        state_model['current_entered'] = "2019-01-01T12:00:00Z"
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = "2019-01-01T12:00:00Z"
        state_model['previous'] = 'testString'

        # Construct a dict representation of a Version model
        version_model = {}
        version_model['id'] = 'testString'
        version_model['_rev'] = 'testString'
        version_model['crn'] = 'testString'
        version_model['version'] = 'testString'
        version_model['sha'] = 'testString'
        version_model['created'] = "2019-01-01T12:00:00Z"
        version_model['updated'] = "2019-01-01T12:00:00Z"
        version_model['offering_id'] = 'testString'
        version_model['catalog_id'] = 'testString'
        version_model['kind_id'] = 'testString'
        version_model['tags'] = ['testString']
        version_model['repo_url'] = 'testString'
        version_model['source_url'] = 'testString'
        version_model['tgz_url'] = 'testString'
        version_model['configuration'] = [configuration_model]
        version_model['metadata'] = {}
        version_model['validation'] = validation_model
        version_model['required_resources'] = [resource_model]
        version_model['single_instance'] = True
        version_model['install'] = script_model
        version_model['pre_install'] = [script_model]
        version_model['entitlement'] = version_entitlement_model
        version_model['licenses'] = [license_model]
        version_model['image_manifest_url'] = 'testString'
        version_model['deprecated'] = True
        version_model['package_version'] = 'testString'
        version_model['state'] = state_model
        version_model['version_locator'] = 'testString'
        version_model['console_url'] = 'testString'
        version_model['long_description'] = 'testString'
        version_model['whitelisted_accounts'] = ['testString']

        # Construct a dict representation of a Deployment model
        deployment_model = {}
        deployment_model['id'] = 'testString'
        deployment_model['label'] = 'testString'
        deployment_model['name'] = 'testString'
        deployment_model['short_description'] = 'testString'
        deployment_model['long_description'] = 'testString'
        deployment_model['metadata'] = {}
        deployment_model['tags'] = ['testString']
        deployment_model['created'] = "2019-01-01T12:00:00Z"
        deployment_model['updated'] = "2019-01-01T12:00:00Z"

        # Construct a dict representation of a Plan model
        plan_model = {}
        plan_model['id'] = 'testString'
        plan_model['label'] = 'testString'
        plan_model['name'] = 'testString'
        plan_model['short_description'] = 'testString'
        plan_model['long_description'] = 'testString'
        plan_model['metadata'] = {}
        plan_model['tags'] = ['testString']
        plan_model['additional_features'] = [feature_model]
        plan_model['created'] = "2019-01-01T12:00:00Z"
        plan_model['updated'] = "2019-01-01T12:00:00Z"
        plan_model['deployments'] = [deployment_model]

        # Construct a dict representation of a Kind model
        kind_model = {}
        kind_model['id'] = 'testString'
        kind_model['format_kind'] = 'testString'
        kind_model['target_kind'] = 'testString'
        kind_model['metadata'] = {}
        kind_model['install_description'] = 'testString'
        kind_model['tags'] = ['testString']
        kind_model['additional_features'] = [feature_model]
        kind_model['created'] = "2019-01-01T12:00:00Z"
        kind_model['updated'] = "2019-01-01T12:00:00Z"
        kind_model['versions'] = [version_model]
        kind_model['plans'] = [plan_model]

        # Construct a dict representation of a RepoInfo model
        repo_info_model = {}
        repo_info_model['token'] = 'testString'
        repo_info_model['type'] = 'testString'

        # Set up parameter values
        catalog_identifier = 'testString'
        id = 'testString'
        rev = 'testString'
        url = 'testString'
        crn = 'testString'
        label = 'testString'
        name = 'testString'
        offering_icon_url = 'testString'
        offering_docs_url = 'testString'
        offering_support_url = 'testString'
        tags = ['testString']
        keywords = ['testString']
        rating = rating_model
        created = string_to_datetime('2019-01-01T12:00:00.000Z')
        updated = string_to_datetime('2019-01-01T12:00:00.000Z')
        short_description = 'testString'
        long_description = 'testString'
        features = [feature_model]
        kinds = [kind_model]
        permit_request_ibm_public_publish = True
        ibm_publish_approved = True
        public_publish_approved = True
        public_original_crn = 'testString'
        publish_public_crn = 'testString'
        portal_approval_record = 'testString'
        portal_ui_url = 'testString'
        catalog_id = 'testString'
        catalog_name = 'testString'
        metadata = {}
        disclaimer = 'testString'
        hidden = True
        provider = 'testString'
        repo_info = repo_info_model

        # Invoke method
        response = _service.create_offering(
            catalog_identifier,
            id=id,
            rev=rev,
            url=url,
            crn=crn,
            label=label,
            name=name,
            offering_icon_url=offering_icon_url,
            offering_docs_url=offering_docs_url,
            offering_support_url=offering_support_url,
            tags=tags,
            keywords=keywords,
            rating=rating,
            created=created,
            updated=updated,
            short_description=short_description,
            long_description=long_description,
            features=features,
            kinds=kinds,
            permit_request_ibm_public_publish=permit_request_ibm_public_publish,
            ibm_publish_approved=ibm_publish_approved,
            public_publish_approved=public_publish_approved,
            public_original_crn=public_original_crn,
            publish_public_crn=publish_public_crn,
            portal_approval_record=portal_approval_record,
            portal_ui_url=portal_ui_url,
            catalog_id=catalog_id,
            catalog_name=catalog_name,
            metadata=metadata,
            disclaimer=disclaimer,
            hidden=hidden,
            provider=provider,
            repo_info=repo_info,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['_rev'] == 'testString'
        assert req_body['url'] == 'testString'
        assert req_body['crn'] == 'testString'
        assert req_body['label'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['offering_icon_url'] == 'testString'
        assert req_body['offering_docs_url'] == 'testString'
        assert req_body['offering_support_url'] == 'testString'
        assert req_body['tags'] == ['testString']
        assert req_body['keywords'] == ['testString']
        assert req_body['rating'] == rating_model
        assert req_body['created'] == "2019-01-01T12:00:00Z"
        assert req_body['updated'] == "2019-01-01T12:00:00Z"
        assert req_body['short_description'] == 'testString'
        assert req_body['long_description'] == 'testString'
        assert req_body['features'] == [feature_model]
        assert req_body['kinds'] == [kind_model]
        assert req_body['permit_request_ibm_public_publish'] == True
        assert req_body['ibm_publish_approved'] == True
        assert req_body['public_publish_approved'] == True
        assert req_body['public_original_crn'] == 'testString'
        assert req_body['publish_public_crn'] == 'testString'
        assert req_body['portal_approval_record'] == 'testString'
        assert req_body['portal_ui_url'] == 'testString'
        assert req_body['catalog_id'] == 'testString'
        assert req_body['catalog_name'] == 'testString'
        assert req_body['metadata'] == {}
        assert req_body['disclaimer'] == 'testString'
        assert req_body['hidden'] == True
        assert req_body['provider'] == 'testString'
        assert req_body['repo_info'] == repo_info_model


    @responses.activate
    def test_create_offering_required_params(self):
        """
        test_create_offering_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Invoke method
        response = _service.create_offering(
            catalog_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_create_offering_value_error(self):
        """
        test_create_offering_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_offering(**req_copy)



class TestImportOfferingVersion():
    """
    Test Class for import_offering_version
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
    def test_import_offering_version_all_params(self):
        """
        import_offering_version()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString/version')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        tags = ['testString']
        target_kinds = ['testString']
        content = b'This is a mock byte array value.'
        zipurl = 'testString'
        target_version = 'testString'
        include_config = True
        is_vsi = True
        repo_type = 'testString'

        # Invoke method
        response = _service.import_offering_version(
            catalog_identifier,
            offering_id,
            tags=tags,
            target_kinds=target_kinds,
            content=content,
            zipurl=zipurl,
            target_version=target_version,
            include_config=include_config,
            is_vsi=is_vsi,
            repo_type=repo_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'zipurl={}'.format(zipurl) in query_string
        assert 'targetVersion={}'.format(target_version) in query_string
        assert 'includeConfig={}'.format('true' if include_config else 'false') in query_string
        assert 'isVSI={}'.format('true' if is_vsi else 'false') in query_string
        assert 'repoType={}'.format(repo_type) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['tags'] == ['testString']
        assert req_body['target_kinds'] == ['testString']
        assert req_body['content'] == 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='


    @responses.activate
    def test_import_offering_version_required_params(self):
        """
        test_import_offering_version_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString/version')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'

        # Invoke method
        response = _service.import_offering_version(
            catalog_identifier,
            offering_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_import_offering_version_value_error(self):
        """
        test_import_offering_version_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString/version')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "offering_id": offering_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.import_offering_version(**req_copy)



class TestImportOffering():
    """
    Test Class for import_offering
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
    def test_import_offering_all_params(self):
        """
        import_offering()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/import/offerings')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        tags = ['testString']
        target_kinds = ['testString']
        content = b'This is a mock byte array value.'
        zipurl = 'testString'
        offering_id = 'testString'
        target_version = 'testString'
        include_config = True
        is_vsi = True
        repo_type = 'testString'
        x_auth_token = 'testString'

        # Invoke method
        response = _service.import_offering(
            catalog_identifier,
            tags=tags,
            target_kinds=target_kinds,
            content=content,
            zipurl=zipurl,
            offering_id=offering_id,
            target_version=target_version,
            include_config=include_config,
            is_vsi=is_vsi,
            repo_type=repo_type,
            x_auth_token=x_auth_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'zipurl={}'.format(zipurl) in query_string
        assert 'offeringID={}'.format(offering_id) in query_string
        assert 'targetVersion={}'.format(target_version) in query_string
        assert 'includeConfig={}'.format('true' if include_config else 'false') in query_string
        assert 'isVSI={}'.format('true' if is_vsi else 'false') in query_string
        assert 'repoType={}'.format(repo_type) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['tags'] == ['testString']
        assert req_body['target_kinds'] == ['testString']
        assert req_body['content'] == 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='


    @responses.activate
    def test_import_offering_required_params(self):
        """
        test_import_offering_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/import/offerings')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Invoke method
        response = _service.import_offering(
            catalog_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_import_offering_value_error(self):
        """
        test_import_offering_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/import/offerings')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.import_offering(**req_copy)



class TestReloadOffering():
    """
    Test Class for reload_offering
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
    def test_reload_offering_all_params(self):
        """
        reload_offering()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString/reload')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        target_version = 'testString'
        tags = ['testString']
        target_kinds = ['testString']
        content = b'This is a mock byte array value.'
        zipurl = 'testString'
        repo_type = 'testString'

        # Invoke method
        response = _service.reload_offering(
            catalog_identifier,
            offering_id,
            target_version,
            tags=tags,
            target_kinds=target_kinds,
            content=content,
            zipurl=zipurl,
            repo_type=repo_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'targetVersion={}'.format(target_version) in query_string
        assert 'zipurl={}'.format(zipurl) in query_string
        assert 'repoType={}'.format(repo_type) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['tags'] == ['testString']
        assert req_body['target_kinds'] == ['testString']
        assert req_body['content'] == 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='


    @responses.activate
    def test_reload_offering_required_params(self):
        """
        test_reload_offering_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString/reload')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        target_version = 'testString'

        # Invoke method
        response = _service.reload_offering(
            catalog_identifier,
            offering_id,
            target_version,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'targetVersion={}'.format(target_version) in query_string


    @responses.activate
    def test_reload_offering_value_error(self):
        """
        test_reload_offering_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString/reload')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        target_version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "offering_id": offering_id,
            "target_version": target_version,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.reload_offering(**req_copy)



class TestGetOffering():
    """
    Test Class for get_offering
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
    def test_get_offering_all_params(self):
        """
        get_offering()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'

        # Invoke method
        response = _service.get_offering(
            catalog_identifier,
            offering_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_offering_value_error(self):
        """
        test_get_offering_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "offering_id": offering_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_offering(**req_copy)



class TestReplaceOffering():
    """
    Test Class for replace_offering
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
    def test_replace_offering_all_params(self):
        """
        replace_offering()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Rating model
        rating_model = {}
        rating_model['one_star_count'] = 38
        rating_model['two_star_count'] = 38
        rating_model['three_star_count'] = 38
        rating_model['four_star_count'] = 38

        # Construct a dict representation of a Feature model
        feature_model = {}
        feature_model['title'] = 'testString'
        feature_model['description'] = 'testString'

        # Construct a dict representation of a Configuration model
        configuration_model = {}
        configuration_model['key'] = 'testString'
        configuration_model['type'] = 'testString'
        configuration_model['default_value'] = { 'foo': 'bar' }
        configuration_model['value_constraint'] = 'testString'
        configuration_model['description'] = 'testString'
        configuration_model['required'] = True
        configuration_model['options'] = [{ 'foo': 'bar' }]
        configuration_model['hidden'] = True

        # Construct a dict representation of a Validation model
        validation_model = {}
        validation_model['validated'] = "2019-01-01T12:00:00Z"
        validation_model['requested'] = "2019-01-01T12:00:00Z"
        validation_model['state'] = 'testString'
        validation_model['last_operation'] = 'testString'
        validation_model['target'] = {}

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['type'] = 'mem'
        resource_model['value'] = { 'foo': 'bar' }

        # Construct a dict representation of a Script model
        script_model = {}
        script_model['instructions'] = 'testString'
        script_model['script'] = 'testString'
        script_model['script_permission'] = 'testString'
        script_model['delete_script'] = 'testString'
        script_model['scope'] = 'testString'

        # Construct a dict representation of a VersionEntitlement model
        version_entitlement_model = {}
        version_entitlement_model['provider_name'] = 'testString'
        version_entitlement_model['provider_id'] = 'testString'
        version_entitlement_model['product_id'] = 'testString'
        version_entitlement_model['part_numbers'] = ['testString']
        version_entitlement_model['image_repo_name'] = 'testString'

        # Construct a dict representation of a License model
        license_model = {}
        license_model['id'] = 'testString'
        license_model['name'] = 'testString'
        license_model['type'] = 'testString'
        license_model['url'] = 'testString'
        license_model['description'] = 'testString'

        # Construct a dict representation of a State model
        state_model = {}
        state_model['current'] = 'testString'
        state_model['current_entered'] = "2019-01-01T12:00:00Z"
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = "2019-01-01T12:00:00Z"
        state_model['previous'] = 'testString'

        # Construct a dict representation of a Version model
        version_model = {}
        version_model['id'] = 'testString'
        version_model['_rev'] = 'testString'
        version_model['crn'] = 'testString'
        version_model['version'] = 'testString'
        version_model['sha'] = 'testString'
        version_model['created'] = "2019-01-01T12:00:00Z"
        version_model['updated'] = "2019-01-01T12:00:00Z"
        version_model['offering_id'] = 'testString'
        version_model['catalog_id'] = 'testString'
        version_model['kind_id'] = 'testString'
        version_model['tags'] = ['testString']
        version_model['repo_url'] = 'testString'
        version_model['source_url'] = 'testString'
        version_model['tgz_url'] = 'testString'
        version_model['configuration'] = [configuration_model]
        version_model['metadata'] = {}
        version_model['validation'] = validation_model
        version_model['required_resources'] = [resource_model]
        version_model['single_instance'] = True
        version_model['install'] = script_model
        version_model['pre_install'] = [script_model]
        version_model['entitlement'] = version_entitlement_model
        version_model['licenses'] = [license_model]
        version_model['image_manifest_url'] = 'testString'
        version_model['deprecated'] = True
        version_model['package_version'] = 'testString'
        version_model['state'] = state_model
        version_model['version_locator'] = 'testString'
        version_model['console_url'] = 'testString'
        version_model['long_description'] = 'testString'
        version_model['whitelisted_accounts'] = ['testString']

        # Construct a dict representation of a Deployment model
        deployment_model = {}
        deployment_model['id'] = 'testString'
        deployment_model['label'] = 'testString'
        deployment_model['name'] = 'testString'
        deployment_model['short_description'] = 'testString'
        deployment_model['long_description'] = 'testString'
        deployment_model['metadata'] = {}
        deployment_model['tags'] = ['testString']
        deployment_model['created'] = "2019-01-01T12:00:00Z"
        deployment_model['updated'] = "2019-01-01T12:00:00Z"

        # Construct a dict representation of a Plan model
        plan_model = {}
        plan_model['id'] = 'testString'
        plan_model['label'] = 'testString'
        plan_model['name'] = 'testString'
        plan_model['short_description'] = 'testString'
        plan_model['long_description'] = 'testString'
        plan_model['metadata'] = {}
        plan_model['tags'] = ['testString']
        plan_model['additional_features'] = [feature_model]
        plan_model['created'] = "2019-01-01T12:00:00Z"
        plan_model['updated'] = "2019-01-01T12:00:00Z"
        plan_model['deployments'] = [deployment_model]

        # Construct a dict representation of a Kind model
        kind_model = {}
        kind_model['id'] = 'testString'
        kind_model['format_kind'] = 'testString'
        kind_model['target_kind'] = 'testString'
        kind_model['metadata'] = {}
        kind_model['install_description'] = 'testString'
        kind_model['tags'] = ['testString']
        kind_model['additional_features'] = [feature_model]
        kind_model['created'] = "2019-01-01T12:00:00Z"
        kind_model['updated'] = "2019-01-01T12:00:00Z"
        kind_model['versions'] = [version_model]
        kind_model['plans'] = [plan_model]

        # Construct a dict representation of a RepoInfo model
        repo_info_model = {}
        repo_info_model['token'] = 'testString'
        repo_info_model['type'] = 'testString'

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        id = 'testString'
        rev = 'testString'
        url = 'testString'
        crn = 'testString'
        label = 'testString'
        name = 'testString'
        offering_icon_url = 'testString'
        offering_docs_url = 'testString'
        offering_support_url = 'testString'
        tags = ['testString']
        keywords = ['testString']
        rating = rating_model
        created = string_to_datetime('2019-01-01T12:00:00.000Z')
        updated = string_to_datetime('2019-01-01T12:00:00.000Z')
        short_description = 'testString'
        long_description = 'testString'
        features = [feature_model]
        kinds = [kind_model]
        permit_request_ibm_public_publish = True
        ibm_publish_approved = True
        public_publish_approved = True
        public_original_crn = 'testString'
        publish_public_crn = 'testString'
        portal_approval_record = 'testString'
        portal_ui_url = 'testString'
        catalog_id = 'testString'
        catalog_name = 'testString'
        metadata = {}
        disclaimer = 'testString'
        hidden = True
        provider = 'testString'
        repo_info = repo_info_model

        # Invoke method
        response = _service.replace_offering(
            catalog_identifier,
            offering_id,
            id=id,
            rev=rev,
            url=url,
            crn=crn,
            label=label,
            name=name,
            offering_icon_url=offering_icon_url,
            offering_docs_url=offering_docs_url,
            offering_support_url=offering_support_url,
            tags=tags,
            keywords=keywords,
            rating=rating,
            created=created,
            updated=updated,
            short_description=short_description,
            long_description=long_description,
            features=features,
            kinds=kinds,
            permit_request_ibm_public_publish=permit_request_ibm_public_publish,
            ibm_publish_approved=ibm_publish_approved,
            public_publish_approved=public_publish_approved,
            public_original_crn=public_original_crn,
            publish_public_crn=publish_public_crn,
            portal_approval_record=portal_approval_record,
            portal_ui_url=portal_ui_url,
            catalog_id=catalog_id,
            catalog_name=catalog_name,
            metadata=metadata,
            disclaimer=disclaimer,
            hidden=hidden,
            provider=provider,
            repo_info=repo_info,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['_rev'] == 'testString'
        assert req_body['url'] == 'testString'
        assert req_body['crn'] == 'testString'
        assert req_body['label'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['offering_icon_url'] == 'testString'
        assert req_body['offering_docs_url'] == 'testString'
        assert req_body['offering_support_url'] == 'testString'
        assert req_body['tags'] == ['testString']
        assert req_body['keywords'] == ['testString']
        assert req_body['rating'] == rating_model
        assert req_body['created'] == "2019-01-01T12:00:00Z"
        assert req_body['updated'] == "2019-01-01T12:00:00Z"
        assert req_body['short_description'] == 'testString'
        assert req_body['long_description'] == 'testString'
        assert req_body['features'] == [feature_model]
        assert req_body['kinds'] == [kind_model]
        assert req_body['permit_request_ibm_public_publish'] == True
        assert req_body['ibm_publish_approved'] == True
        assert req_body['public_publish_approved'] == True
        assert req_body['public_original_crn'] == 'testString'
        assert req_body['publish_public_crn'] == 'testString'
        assert req_body['portal_approval_record'] == 'testString'
        assert req_body['portal_ui_url'] == 'testString'
        assert req_body['catalog_id'] == 'testString'
        assert req_body['catalog_name'] == 'testString'
        assert req_body['metadata'] == {}
        assert req_body['disclaimer'] == 'testString'
        assert req_body['hidden'] == True
        assert req_body['provider'] == 'testString'
        assert req_body['repo_info'] == repo_info_model


    @responses.activate
    def test_replace_offering_required_params(self):
        """
        test_replace_offering_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'

        # Invoke method
        response = _service.replace_offering(
            catalog_identifier,
            offering_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_replace_offering_value_error(self):
        """
        test_replace_offering_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "offering_id": offering_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_offering(**req_copy)



class TestDeleteOffering():
    """
    Test Class for delete_offering
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
    def test_delete_offering_all_params(self):
        """
        delete_offering()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'

        # Invoke method
        response = _service.delete_offering(
            catalog_identifier,
            offering_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_offering_value_error(self):
        """
        test_delete_offering_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "offering_id": offering_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_offering(**req_copy)



class TestGetOfferingAudit():
    """
    Test Class for get_offering_audit
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
    def test_get_offering_audit_all_params(self):
        """
        get_offering_audit()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString/audit')
        mock_response = '{"list": [{"id": "id", "created": "2019-01-01T12:00:00.000Z", "change_type": "change_type", "target_type": "target_type", "target_id": "target_id", "who_delegate_email": "who_delegate_email", "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'

        # Invoke method
        response = _service.get_offering_audit(
            catalog_identifier,
            offering_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_offering_audit_value_error(self):
        """
        test_get_offering_audit_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString/audit')
        mock_response = '{"list": [{"id": "id", "created": "2019-01-01T12:00:00.000Z", "change_type": "change_type", "target_type": "target_type", "target_id": "target_id", "who_delegate_email": "who_delegate_email", "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "offering_id": offering_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_offering_audit(**req_copy)



class TestReplaceOfferingIcon():
    """
    Test Class for replace_offering_icon
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
    def test_replace_offering_icon_all_params(self):
        """
        replace_offering_icon()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString/icon/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        file_name = 'testString'

        # Invoke method
        response = _service.replace_offering_icon(
            catalog_identifier,
            offering_id,
            file_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_replace_offering_icon_value_error(self):
        """
        test_replace_offering_icon_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString/icon/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        file_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "offering_id": offering_id,
            "file_name": file_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_offering_icon(**req_copy)



class TestUpdateOfferingIbm():
    """
    Test Class for update_offering_ibm
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
    def test_update_offering_ibm_all_params(self):
        """
        update_offering_ibm()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString/publish/allow_request/true')
        mock_response = '{"allow_request": false, "ibm": false, "public": true, "changed": false}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        approval_type = 'allow_request'
        approved = 'true'

        # Invoke method
        response = _service.update_offering_ibm(
            catalog_identifier,
            offering_id,
            approval_type,
            approved,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_update_offering_ibm_value_error(self):
        """
        test_update_offering_ibm_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString/publish/allow_request/true')
        mock_response = '{"allow_request": false, "ibm": false, "public": true, "changed": false}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        approval_type = 'allow_request'
        approved = 'true'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "offering_id": offering_id,
            "approval_type": approval_type,
            "approved": approved,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_offering_ibm(**req_copy)



class TestGetOfferingUpdates():
    """
    Test Class for get_offering_updates
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
    def test_get_offering_updates_all_params(self):
        """
        get_offering_updates()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString/updates')
        mock_response = '[{"version_locator": "version_locator", "version": "version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "package_version": "package_version", "can_update": true, "messages": {"mapKey": "inner"}}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        kind = 'testString'
        version = 'testString'
        cluster_id = 'testString'
        region = 'testString'
        resource_group_id = 'testString'
        namespace = 'testString'

        # Invoke method
        response = _service.get_offering_updates(
            catalog_identifier,
            offering_id,
            kind,
            version=version,
            cluster_id=cluster_id,
            region=region,
            resource_group_id=resource_group_id,
            namespace=namespace,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'kind={}'.format(kind) in query_string
        assert 'version={}'.format(version) in query_string
        assert 'cluster_id={}'.format(cluster_id) in query_string
        assert 'region={}'.format(region) in query_string
        assert 'resource_group_id={}'.format(resource_group_id) in query_string
        assert 'namespace={}'.format(namespace) in query_string


    @responses.activate
    def test_get_offering_updates_required_params(self):
        """
        test_get_offering_updates_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString/updates')
        mock_response = '[{"version_locator": "version_locator", "version": "version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "package_version": "package_version", "can_update": true, "messages": {"mapKey": "inner"}}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        kind = 'testString'

        # Invoke method
        response = _service.get_offering_updates(
            catalog_identifier,
            offering_id,
            kind,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'kind={}'.format(kind) in query_string


    @responses.activate
    def test_get_offering_updates_value_error(self):
        """
        test_get_offering_updates_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/offerings/testString/updates')
        mock_response = '[{"version_locator": "version_locator", "version": "version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "package_version": "package_version", "can_update": true, "messages": {"mapKey": "inner"}}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        kind = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "offering_id": offering_id,
            "kind": kind,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_offering_updates(**req_copy)



# endregion
##############################################################################
# End of Service: Offerings
##############################################################################

##############################################################################
# Start of Service: Versions
##############################################################################
# region

class TestGetOfferingAbout():
    """
    Test Class for get_offering_about
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
    def test_get_offering_about_all_params(self):
        """
        get_offering_about()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/about')
        mock_response = '"operation_response"'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='text/markdown',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = _service.get_offering_about(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_offering_about_value_error(self):
        """
        test_get_offering_about_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/about')
        mock_response = '"operation_response"'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='text/markdown',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_offering_about(**req_copy)



class TestGetOfferingLicense():
    """
    Test Class for get_offering_license
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
    def test_get_offering_license_all_params(self):
        """
        get_offering_license()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/licenses/testString')
        mock_response = '"operation_response"'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='text/plain',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'
        license_id = 'testString'

        # Invoke method
        response = _service.get_offering_license(
            version_loc_id,
            license_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_offering_license_value_error(self):
        """
        test_get_offering_license_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/licenses/testString')
        mock_response = '"operation_response"'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='text/plain',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'
        license_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
            "license_id": license_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_offering_license(**req_copy)



class TestGetOfferingContainerImages():
    """
    Test Class for get_offering_container_images
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
    def test_get_offering_container_images_all_params(self):
        """
        get_offering_container_images()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/containerImages')
        mock_response = '{"description": "description", "images": [{"image": "image"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = _service.get_offering_container_images(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_offering_container_images_value_error(self):
        """
        test_get_offering_container_images_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/containerImages')
        mock_response = '{"description": "description", "images": [{"image": "image"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_offering_container_images(**req_copy)



class TestDeprecateVersion():
    """
    Test Class for deprecate_version
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
    def test_deprecate_version_all_params(self):
        """
        deprecate_version()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/deprecate')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = _service.deprecate_version(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_deprecate_version_value_error(self):
        """
        test_deprecate_version_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/deprecate')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.deprecate_version(**req_copy)



class TestAccountPublishVersion():
    """
    Test Class for account_publish_version
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
    def test_account_publish_version_all_params(self):
        """
        account_publish_version()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/account-publish')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = _service.account_publish_version(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_account_publish_version_value_error(self):
        """
        test_account_publish_version_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/account-publish')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.account_publish_version(**req_copy)



class TestIbmPublishVersion():
    """
    Test Class for ibm_publish_version
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
    def test_ibm_publish_version_all_params(self):
        """
        ibm_publish_version()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/ibm-publish')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = _service.ibm_publish_version(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_ibm_publish_version_value_error(self):
        """
        test_ibm_publish_version_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/ibm-publish')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.ibm_publish_version(**req_copy)



class TestPublicPublishVersion():
    """
    Test Class for public_publish_version
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
    def test_public_publish_version_all_params(self):
        """
        public_publish_version()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/public-publish')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = _service.public_publish_version(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_public_publish_version_value_error(self):
        """
        test_public_publish_version_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/public-publish')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.public_publish_version(**req_copy)



class TestCommitVersion():
    """
    Test Class for commit_version
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
    def test_commit_version_all_params(self):
        """
        commit_version()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/commit')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = _service.commit_version(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_commit_version_value_error(self):
        """
        test_commit_version_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/commit')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.commit_version(**req_copy)



class TestCopyVersion():
    """
    Test Class for copy_version
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
    def test_copy_version_all_params(self):
        """
        copy_version()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/copy')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'
        tags = ['testString']
        target_kinds = ['testString']
        content = b'This is a mock byte array value.'

        # Invoke method
        response = _service.copy_version(
            version_loc_id,
            tags=tags,
            target_kinds=target_kinds,
            content=content,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['tags'] == ['testString']
        assert req_body['target_kinds'] == ['testString']
        assert req_body['content'] == 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='


    @responses.activate
    def test_copy_version_required_params(self):
        """
        test_copy_version_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/copy')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = _service.copy_version(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_copy_version_value_error(self):
        """
        test_copy_version_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/copy')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.copy_version(**req_copy)



class TestGetOfferingWorkingCopy():
    """
    Test Class for get_offering_working_copy
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
    def test_get_offering_working_copy_all_params(self):
        """
        get_offering_working_copy()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/workingcopy')
        mock_response = '{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = _service.get_offering_working_copy(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_offering_working_copy_value_error(self):
        """
        test_get_offering_working_copy_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/workingcopy')
        mock_response = '{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_offering_working_copy(**req_copy)



class TestGetVersion():
    """
    Test Class for get_version
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
    def test_get_version_all_params(self):
        """
        get_version()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = _service.get_version(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_version_value_error(self):
        """
        test_get_version_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "keywords": ["keywords"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"mapKey": {"anyKey": "anyValue"}}, "validation": {"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_version(**req_copy)



class TestDeleteVersion():
    """
    Test Class for delete_version
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
    def test_delete_version_all_params(self):
        """
        delete_version()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = _service.delete_version(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_version_value_error(self):
        """
        test_delete_version_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_version(**req_copy)



# endregion
##############################################################################
# End of Service: Versions
##############################################################################

##############################################################################
# Start of Service: Deploy
##############################################################################
# region

class TestGetCluster():
    """
    Test Class for get_cluster
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
    def test_get_cluster_all_params(self):
        """
        get_cluster()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/deploy/kubernetes/clusters/testString')
        mock_response = '{"resource_group_id": "resource_group_id", "resource_group_name": "resource_group_name", "id": "id", "name": "name", "region": "region"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cluster_id = 'testString'
        region = 'testString'
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = _service.get_cluster(
            cluster_id,
            region,
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'region={}'.format(region) in query_string


    @responses.activate
    def test_get_cluster_value_error(self):
        """
        test_get_cluster_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/deploy/kubernetes/clusters/testString')
        mock_response = '{"resource_group_id": "resource_group_id", "resource_group_name": "resource_group_name", "id": "id", "name": "name", "region": "region"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cluster_id = 'testString'
        region = 'testString'
        x_auth_refresh_token = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cluster_id": cluster_id,
            "region": region,
            "x_auth_refresh_token": x_auth_refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_cluster(**req_copy)



class TestGetNamespaces():
    """
    Test Class for get_namespaces
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
    def test_get_namespaces_all_params(self):
        """
        get_namespaces()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/deploy/kubernetes/clusters/testString/namespaces')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": ["resources"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cluster_id = 'testString'
        region = 'testString'
        x_auth_refresh_token = 'testString'
        limit = 1000
        offset = 38

        # Invoke method
        response = _service.get_namespaces(
            cluster_id,
            region,
            x_auth_refresh_token,
            limit=limit,
            offset=offset,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'region={}'.format(region) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string


    @responses.activate
    def test_get_namespaces_required_params(self):
        """
        test_get_namespaces_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/deploy/kubernetes/clusters/testString/namespaces')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": ["resources"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cluster_id = 'testString'
        region = 'testString'
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = _service.get_namespaces(
            cluster_id,
            region,
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'region={}'.format(region) in query_string


    @responses.activate
    def test_get_namespaces_value_error(self):
        """
        test_get_namespaces_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/deploy/kubernetes/clusters/testString/namespaces')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": ["resources"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cluster_id = 'testString'
        region = 'testString'
        x_auth_refresh_token = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cluster_id": cluster_id,
            "region": region,
            "x_auth_refresh_token": x_auth_refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_namespaces(**req_copy)



class TestDeployOperators():
    """
    Test Class for deploy_operators
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
    def test_deploy_operators_all_params(self):
        """
        deploy_operators()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/deploy/kubernetes/olm/operator')
        mock_response = '[{"phase": "phase", "message": "message", "link": "link", "name": "name", "version": "version", "namespace": "namespace", "package_name": "package_name", "catalog_id": "catalog_id"}]'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_refresh_token = 'testString'
        cluster_id = 'testString'
        region = 'testString'
        namespaces = ['testString']
        all_namespaces = True
        version_locator_id = 'testString'

        # Invoke method
        response = _service.deploy_operators(
            x_auth_refresh_token,
            cluster_id=cluster_id,
            region=region,
            namespaces=namespaces,
            all_namespaces=all_namespaces,
            version_locator_id=version_locator_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['cluster_id'] == 'testString'
        assert req_body['region'] == 'testString'
        assert req_body['namespaces'] == ['testString']
        assert req_body['all_namespaces'] == True
        assert req_body['version_locator_id'] == 'testString'


    @responses.activate
    def test_deploy_operators_required_params(self):
        """
        test_deploy_operators_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/deploy/kubernetes/olm/operator')
        mock_response = '[{"phase": "phase", "message": "message", "link": "link", "name": "name", "version": "version", "namespace": "namespace", "package_name": "package_name", "catalog_id": "catalog_id"}]'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = _service.deploy_operators(
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_deploy_operators_value_error(self):
        """
        test_deploy_operators_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/deploy/kubernetes/olm/operator')
        mock_response = '[{"phase": "phase", "message": "message", "link": "link", "name": "name", "version": "version", "namespace": "namespace", "package_name": "package_name", "catalog_id": "catalog_id"}]'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_refresh_token = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "x_auth_refresh_token": x_auth_refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.deploy_operators(**req_copy)



class TestListOperators():
    """
    Test Class for list_operators
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
    def test_list_operators_all_params(self):
        """
        list_operators()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/deploy/kubernetes/olm/operator')
        mock_response = '[{"phase": "phase", "message": "message", "link": "link", "name": "name", "version": "version", "namespace": "namespace", "package_name": "package_name", "catalog_id": "catalog_id"}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_refresh_token = 'testString'
        cluster_id = 'testString'
        region = 'testString'
        version_locator_id = 'testString'

        # Invoke method
        response = _service.list_operators(
            x_auth_refresh_token,
            cluster_id,
            region,
            version_locator_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'cluster_id={}'.format(cluster_id) in query_string
        assert 'region={}'.format(region) in query_string
        assert 'version_locator_id={}'.format(version_locator_id) in query_string


    @responses.activate
    def test_list_operators_value_error(self):
        """
        test_list_operators_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/deploy/kubernetes/olm/operator')
        mock_response = '[{"phase": "phase", "message": "message", "link": "link", "name": "name", "version": "version", "namespace": "namespace", "package_name": "package_name", "catalog_id": "catalog_id"}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_refresh_token = 'testString'
        cluster_id = 'testString'
        region = 'testString'
        version_locator_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "x_auth_refresh_token": x_auth_refresh_token,
            "cluster_id": cluster_id,
            "region": region,
            "version_locator_id": version_locator_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_operators(**req_copy)



class TestReplaceOperators():
    """
    Test Class for replace_operators
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
    def test_replace_operators_all_params(self):
        """
        replace_operators()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/deploy/kubernetes/olm/operator')
        mock_response = '[{"phase": "phase", "message": "message", "link": "link", "name": "name", "version": "version", "namespace": "namespace", "package_name": "package_name", "catalog_id": "catalog_id"}]'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_refresh_token = 'testString'
        cluster_id = 'testString'
        region = 'testString'
        namespaces = ['testString']
        all_namespaces = True
        version_locator_id = 'testString'

        # Invoke method
        response = _service.replace_operators(
            x_auth_refresh_token,
            cluster_id=cluster_id,
            region=region,
            namespaces=namespaces,
            all_namespaces=all_namespaces,
            version_locator_id=version_locator_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['cluster_id'] == 'testString'
        assert req_body['region'] == 'testString'
        assert req_body['namespaces'] == ['testString']
        assert req_body['all_namespaces'] == True
        assert req_body['version_locator_id'] == 'testString'


    @responses.activate
    def test_replace_operators_required_params(self):
        """
        test_replace_operators_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/deploy/kubernetes/olm/operator')
        mock_response = '[{"phase": "phase", "message": "message", "link": "link", "name": "name", "version": "version", "namespace": "namespace", "package_name": "package_name", "catalog_id": "catalog_id"}]'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = _service.replace_operators(
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_replace_operators_value_error(self):
        """
        test_replace_operators_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/deploy/kubernetes/olm/operator')
        mock_response = '[{"phase": "phase", "message": "message", "link": "link", "name": "name", "version": "version", "namespace": "namespace", "package_name": "package_name", "catalog_id": "catalog_id"}]'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_refresh_token = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "x_auth_refresh_token": x_auth_refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_operators(**req_copy)



class TestDeleteOperators():
    """
    Test Class for delete_operators
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
    def test_delete_operators_all_params(self):
        """
        delete_operators()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/deploy/kubernetes/olm/operator')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        x_auth_refresh_token = 'testString'
        cluster_id = 'testString'
        region = 'testString'
        version_locator_id = 'testString'

        # Invoke method
        response = _service.delete_operators(
            x_auth_refresh_token,
            cluster_id,
            region,
            version_locator_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'cluster_id={}'.format(cluster_id) in query_string
        assert 'region={}'.format(region) in query_string
        assert 'version_locator_id={}'.format(version_locator_id) in query_string


    @responses.activate
    def test_delete_operators_value_error(self):
        """
        test_delete_operators_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/deploy/kubernetes/olm/operator')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        x_auth_refresh_token = 'testString'
        cluster_id = 'testString'
        region = 'testString'
        version_locator_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "x_auth_refresh_token": x_auth_refresh_token,
            "cluster_id": cluster_id,
            "region": region,
            "version_locator_id": version_locator_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_operators(**req_copy)



class TestInstallVersion():
    """
    Test Class for install_version
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
    def test_install_version_all_params(self):
        """
        install_version()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/install')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Construct a dict representation of a DeployRequestBodySchematics model
        deploy_request_body_schematics_model = {}
        deploy_request_body_schematics_model['name'] = 'testString'
        deploy_request_body_schematics_model['description'] = 'testString'
        deploy_request_body_schematics_model['tags'] = ['testString']
        deploy_request_body_schematics_model['resource_group_id'] = 'testString'

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'
        cluster_id = 'testString'
        region = 'testString'
        namespace = 'testString'
        override_values = {}
        entitlement_apikey = 'testString'
        schematics = deploy_request_body_schematics_model
        script = 'testString'
        script_id = 'testString'
        version_locator_id = 'testString'
        vcenter_id = 'testString'
        vcenter_user = 'testString'
        vcenter_password = 'testString'
        vcenter_location = 'testString'
        vcenter_datastore = 'testString'

        # Invoke method
        response = _service.install_version(
            version_loc_id,
            x_auth_refresh_token,
            cluster_id=cluster_id,
            region=region,
            namespace=namespace,
            override_values=override_values,
            entitlement_apikey=entitlement_apikey,
            schematics=schematics,
            script=script,
            script_id=script_id,
            version_locator_id=version_locator_id,
            vcenter_id=vcenter_id,
            vcenter_user=vcenter_user,
            vcenter_password=vcenter_password,
            vcenter_location=vcenter_location,
            vcenter_datastore=vcenter_datastore,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['cluster_id'] == 'testString'
        assert req_body['region'] == 'testString'
        assert req_body['namespace'] == 'testString'
        assert req_body['override_values'] == {}
        assert req_body['entitlement_apikey'] == 'testString'
        assert req_body['schematics'] == deploy_request_body_schematics_model
        assert req_body['script'] == 'testString'
        assert req_body['script_id'] == 'testString'
        assert req_body['version_locator_id'] == 'testString'
        assert req_body['vcenter_id'] == 'testString'
        assert req_body['vcenter_user'] == 'testString'
        assert req_body['vcenter_password'] == 'testString'
        assert req_body['vcenter_location'] == 'testString'
        assert req_body['vcenter_datastore'] == 'testString'


    @responses.activate
    def test_install_version_required_params(self):
        """
        test_install_version_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/install')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = _service.install_version(
            version_loc_id,
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_install_version_value_error(self):
        """
        test_install_version_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/install')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
            "x_auth_refresh_token": x_auth_refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.install_version(**req_copy)



class TestPreinstallVersion():
    """
    Test Class for preinstall_version
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
    def test_preinstall_version_all_params(self):
        """
        preinstall_version()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/preinstall')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Construct a dict representation of a DeployRequestBodySchematics model
        deploy_request_body_schematics_model = {}
        deploy_request_body_schematics_model['name'] = 'testString'
        deploy_request_body_schematics_model['description'] = 'testString'
        deploy_request_body_schematics_model['tags'] = ['testString']
        deploy_request_body_schematics_model['resource_group_id'] = 'testString'

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'
        cluster_id = 'testString'
        region = 'testString'
        namespace = 'testString'
        override_values = {}
        entitlement_apikey = 'testString'
        schematics = deploy_request_body_schematics_model
        script = 'testString'
        script_id = 'testString'
        version_locator_id = 'testString'
        vcenter_id = 'testString'
        vcenter_user = 'testString'
        vcenter_password = 'testString'
        vcenter_location = 'testString'
        vcenter_datastore = 'testString'

        # Invoke method
        response = _service.preinstall_version(
            version_loc_id,
            x_auth_refresh_token,
            cluster_id=cluster_id,
            region=region,
            namespace=namespace,
            override_values=override_values,
            entitlement_apikey=entitlement_apikey,
            schematics=schematics,
            script=script,
            script_id=script_id,
            version_locator_id=version_locator_id,
            vcenter_id=vcenter_id,
            vcenter_user=vcenter_user,
            vcenter_password=vcenter_password,
            vcenter_location=vcenter_location,
            vcenter_datastore=vcenter_datastore,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['cluster_id'] == 'testString'
        assert req_body['region'] == 'testString'
        assert req_body['namespace'] == 'testString'
        assert req_body['override_values'] == {}
        assert req_body['entitlement_apikey'] == 'testString'
        assert req_body['schematics'] == deploy_request_body_schematics_model
        assert req_body['script'] == 'testString'
        assert req_body['script_id'] == 'testString'
        assert req_body['version_locator_id'] == 'testString'
        assert req_body['vcenter_id'] == 'testString'
        assert req_body['vcenter_user'] == 'testString'
        assert req_body['vcenter_password'] == 'testString'
        assert req_body['vcenter_location'] == 'testString'
        assert req_body['vcenter_datastore'] == 'testString'


    @responses.activate
    def test_preinstall_version_required_params(self):
        """
        test_preinstall_version_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/preinstall')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = _service.preinstall_version(
            version_loc_id,
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_preinstall_version_value_error(self):
        """
        test_preinstall_version_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/preinstall')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
            "x_auth_refresh_token": x_auth_refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.preinstall_version(**req_copy)



class TestGetPreinstall():
    """
    Test Class for get_preinstall
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
    def test_get_preinstall_all_params(self):
        """
        get_preinstall()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/preinstall')
        mock_response = '{"metadata": {"cluster_id": "cluster_id", "region": "region", "namespace": "namespace", "workspace_id": "workspace_id", "workspace_name": "workspace_name"}, "release": {"deployments": [{"mapKey": {"anyKey": "anyValue"}}], "replicasets": [{"mapKey": {"anyKey": "anyValue"}}], "statefulsets": [{"mapKey": {"anyKey": "anyValue"}}], "pods": [{"mapKey": {"anyKey": "anyValue"}}], "errors": [{"mapKey": "inner"}]}, "content_mgmt": {"pods": [{"mapKey": "inner"}], "errors": [{"mapKey": "inner"}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'
        cluster_id = 'testString'
        region = 'testString'
        namespace = 'testString'

        # Invoke method
        response = _service.get_preinstall(
            version_loc_id,
            x_auth_refresh_token,
            cluster_id=cluster_id,
            region=region,
            namespace=namespace,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'cluster_id={}'.format(cluster_id) in query_string
        assert 'region={}'.format(region) in query_string
        assert 'namespace={}'.format(namespace) in query_string


    @responses.activate
    def test_get_preinstall_required_params(self):
        """
        test_get_preinstall_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/preinstall')
        mock_response = '{"metadata": {"cluster_id": "cluster_id", "region": "region", "namespace": "namespace", "workspace_id": "workspace_id", "workspace_name": "workspace_name"}, "release": {"deployments": [{"mapKey": {"anyKey": "anyValue"}}], "replicasets": [{"mapKey": {"anyKey": "anyValue"}}], "statefulsets": [{"mapKey": {"anyKey": "anyValue"}}], "pods": [{"mapKey": {"anyKey": "anyValue"}}], "errors": [{"mapKey": "inner"}]}, "content_mgmt": {"pods": [{"mapKey": "inner"}], "errors": [{"mapKey": "inner"}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = _service.get_preinstall(
            version_loc_id,
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_preinstall_value_error(self):
        """
        test_get_preinstall_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/preinstall')
        mock_response = '{"metadata": {"cluster_id": "cluster_id", "region": "region", "namespace": "namespace", "workspace_id": "workspace_id", "workspace_name": "workspace_name"}, "release": {"deployments": [{"mapKey": {"anyKey": "anyValue"}}], "replicasets": [{"mapKey": {"anyKey": "anyValue"}}], "statefulsets": [{"mapKey": {"anyKey": "anyValue"}}], "pods": [{"mapKey": {"anyKey": "anyValue"}}], "errors": [{"mapKey": "inner"}]}, "content_mgmt": {"pods": [{"mapKey": "inner"}], "errors": [{"mapKey": "inner"}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
            "x_auth_refresh_token": x_auth_refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_preinstall(**req_copy)



class TestValidateInstall():
    """
    Test Class for validate_install
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
    def test_validate_install_all_params(self):
        """
        validate_install()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/validation/install')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Construct a dict representation of a DeployRequestBodySchematics model
        deploy_request_body_schematics_model = {}
        deploy_request_body_schematics_model['name'] = 'testString'
        deploy_request_body_schematics_model['description'] = 'testString'
        deploy_request_body_schematics_model['tags'] = ['testString']
        deploy_request_body_schematics_model['resource_group_id'] = 'testString'

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'
        cluster_id = 'testString'
        region = 'testString'
        namespace = 'testString'
        override_values = {}
        entitlement_apikey = 'testString'
        schematics = deploy_request_body_schematics_model
        script = 'testString'
        script_id = 'testString'
        version_locator_id = 'testString'
        vcenter_id = 'testString'
        vcenter_user = 'testString'
        vcenter_password = 'testString'
        vcenter_location = 'testString'
        vcenter_datastore = 'testString'

        # Invoke method
        response = _service.validate_install(
            version_loc_id,
            x_auth_refresh_token,
            cluster_id=cluster_id,
            region=region,
            namespace=namespace,
            override_values=override_values,
            entitlement_apikey=entitlement_apikey,
            schematics=schematics,
            script=script,
            script_id=script_id,
            version_locator_id=version_locator_id,
            vcenter_id=vcenter_id,
            vcenter_user=vcenter_user,
            vcenter_password=vcenter_password,
            vcenter_location=vcenter_location,
            vcenter_datastore=vcenter_datastore,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['cluster_id'] == 'testString'
        assert req_body['region'] == 'testString'
        assert req_body['namespace'] == 'testString'
        assert req_body['override_values'] == {}
        assert req_body['entitlement_apikey'] == 'testString'
        assert req_body['schematics'] == deploy_request_body_schematics_model
        assert req_body['script'] == 'testString'
        assert req_body['script_id'] == 'testString'
        assert req_body['version_locator_id'] == 'testString'
        assert req_body['vcenter_id'] == 'testString'
        assert req_body['vcenter_user'] == 'testString'
        assert req_body['vcenter_password'] == 'testString'
        assert req_body['vcenter_location'] == 'testString'
        assert req_body['vcenter_datastore'] == 'testString'


    @responses.activate
    def test_validate_install_required_params(self):
        """
        test_validate_install_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/validation/install')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = _service.validate_install(
            version_loc_id,
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_validate_install_value_error(self):
        """
        test_validate_install_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/validation/install')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
            "x_auth_refresh_token": x_auth_refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.validate_install(**req_copy)



class TestGetValidationStatus():
    """
    Test Class for get_validation_status
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
    def test_get_validation_status_all_params(self):
        """
        get_validation_status()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/validation/install')
        mock_response = '{"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = _service.get_validation_status(
            version_loc_id,
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_validation_status_value_error(self):
        """
        test_get_validation_status_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/validation/install')
        mock_response = '{"validated": "2019-01-01T12:00:00.000Z", "requested": "2019-01-01T12:00:00.000Z", "state": "state", "last_operation": "last_operation", "target": {"mapKey": {"anyKey": "anyValue"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
            "x_auth_refresh_token": x_auth_refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_validation_status(**req_copy)



class TestGetOverrideValues():
    """
    Test Class for get_override_values
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
    def test_get_override_values_all_params(self):
        """
        get_override_values()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/validation/overridevalues')
        mock_response = '{"mapKey": {"anyKey": "anyValue"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = _service.get_override_values(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_override_values_value_error(self):
        """
        test_get_override_values_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/versions/testString/validation/overridevalues')
        mock_response = '{"mapKey": {"anyKey": "anyValue"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_override_values(**req_copy)



# endregion
##############################################################################
# End of Service: Deploy
##############################################################################

##############################################################################
# Start of Service: Objects
##############################################################################
# region

class TestSearchObjects():
    """
    Test Class for search_objects
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
    def test_search_objects_all_params(self):
        """
        search_objects()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/objects')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "name": "name", "_rev": "rev", "crn": "crn", "url": "url", "parent_id": "parent_id", "label_i18n": "label_i18n", "label": "label", "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "short_description_i18n": "short_description_i18n", "kind": "kind", "publish": {"permit_ibm_public_publish": false, "ibm_approved": true, "public_approved": false, "portal_approval_record": "portal_approval_record", "portal_url": "portal_url"}, "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "catalog_id": "catalog_id", "catalog_name": "catalog_name", "data": {"mapKey": {"anyKey": "anyValue"}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        query = 'testString'
        limit = 1000
        offset = 38
        collapse = True
        digest = True

        # Invoke method
        response = _service.search_objects(
            query,
            limit=limit,
            offset=offset,
            collapse=collapse,
            digest=digest,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'query={}'.format(query) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'collapse={}'.format('true' if collapse else 'false') in query_string
        assert 'digest={}'.format('true' if digest else 'false') in query_string


    @responses.activate
    def test_search_objects_required_params(self):
        """
        test_search_objects_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/objects')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "name": "name", "_rev": "rev", "crn": "crn", "url": "url", "parent_id": "parent_id", "label_i18n": "label_i18n", "label": "label", "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "short_description_i18n": "short_description_i18n", "kind": "kind", "publish": {"permit_ibm_public_publish": false, "ibm_approved": true, "public_approved": false, "portal_approval_record": "portal_approval_record", "portal_url": "portal_url"}, "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "catalog_id": "catalog_id", "catalog_name": "catalog_name", "data": {"mapKey": {"anyKey": "anyValue"}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        query = 'testString'

        # Invoke method
        response = _service.search_objects(
            query,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'query={}'.format(query) in query_string


    @responses.activate
    def test_search_objects_value_error(self):
        """
        test_search_objects_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/objects')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "name": "name", "_rev": "rev", "crn": "crn", "url": "url", "parent_id": "parent_id", "label_i18n": "label_i18n", "label": "label", "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "short_description_i18n": "short_description_i18n", "kind": "kind", "publish": {"permit_ibm_public_publish": false, "ibm_approved": true, "public_approved": false, "portal_approval_record": "portal_approval_record", "portal_url": "portal_url"}, "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "catalog_id": "catalog_id", "catalog_name": "catalog_name", "data": {"mapKey": {"anyKey": "anyValue"}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        query = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "query": query,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.search_objects(**req_copy)



class TestListObjects():
    """
    Test Class for list_objects
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
    def test_list_objects_all_params(self):
        """
        list_objects()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "name": "name", "_rev": "rev", "crn": "crn", "url": "url", "parent_id": "parent_id", "label_i18n": "label_i18n", "label": "label", "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "short_description_i18n": "short_description_i18n", "kind": "kind", "publish": {"permit_ibm_public_publish": false, "ibm_approved": true, "public_approved": false, "portal_approval_record": "portal_approval_record", "portal_url": "portal_url"}, "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "catalog_id": "catalog_id", "catalog_name": "catalog_name", "data": {"mapKey": {"anyKey": "anyValue"}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        limit = 1000
        offset = 38
        name = 'testString'
        sort = 'testString'

        # Invoke method
        response = _service.list_objects(
            catalog_identifier,
            limit=limit,
            offset=offset,
            name=name,
            sort=sort,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'sort={}'.format(sort) in query_string


    @responses.activate
    def test_list_objects_required_params(self):
        """
        test_list_objects_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "name": "name", "_rev": "rev", "crn": "crn", "url": "url", "parent_id": "parent_id", "label_i18n": "label_i18n", "label": "label", "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "short_description_i18n": "short_description_i18n", "kind": "kind", "publish": {"permit_ibm_public_publish": false, "ibm_approved": true, "public_approved": false, "portal_approval_record": "portal_approval_record", "portal_url": "portal_url"}, "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "catalog_id": "catalog_id", "catalog_name": "catalog_name", "data": {"mapKey": {"anyKey": "anyValue"}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Invoke method
        response = _service.list_objects(
            catalog_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_objects_value_error(self):
        """
        test_list_objects_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "name": "name", "_rev": "rev", "crn": "crn", "url": "url", "parent_id": "parent_id", "label_i18n": "label_i18n", "label": "label", "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "short_description_i18n": "short_description_i18n", "kind": "kind", "publish": {"permit_ibm_public_publish": false, "ibm_approved": true, "public_approved": false, "portal_approval_record": "portal_approval_record", "portal_url": "portal_url"}, "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "catalog_id": "catalog_id", "catalog_name": "catalog_name", "data": {"mapKey": {"anyKey": "anyValue"}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_objects(**req_copy)



class TestCreateObject():
    """
    Test Class for create_object
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
    def test_create_object_all_params(self):
        """
        create_object()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects')
        mock_response = '{"id": "id", "name": "name", "_rev": "rev", "crn": "crn", "url": "url", "parent_id": "parent_id", "label_i18n": "label_i18n", "label": "label", "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "short_description_i18n": "short_description_i18n", "kind": "kind", "publish": {"permit_ibm_public_publish": false, "ibm_approved": true, "public_approved": false, "portal_approval_record": "portal_approval_record", "portal_url": "portal_url"}, "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "catalog_id": "catalog_id", "catalog_name": "catalog_name", "data": {"mapKey": {"anyKey": "anyValue"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a PublishObject model
        publish_object_model = {}
        publish_object_model['permit_ibm_public_publish'] = True
        publish_object_model['ibm_approved'] = True
        publish_object_model['public_approved'] = True
        publish_object_model['portal_approval_record'] = 'testString'
        publish_object_model['portal_url'] = 'testString'

        # Construct a dict representation of a State model
        state_model = {}
        state_model['current'] = 'testString'
        state_model['current_entered'] = "2019-01-01T12:00:00Z"
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = "2019-01-01T12:00:00Z"
        state_model['previous'] = 'testString'

        # Set up parameter values
        catalog_identifier = 'testString'
        id = 'testString'
        name = 'testString'
        rev = 'testString'
        crn = 'testString'
        url = 'testString'
        parent_id = 'testString'
        label_i18n = 'testString'
        label = 'testString'
        tags = ['testString']
        created = string_to_datetime('2019-01-01T12:00:00.000Z')
        updated = string_to_datetime('2019-01-01T12:00:00.000Z')
        short_description = 'testString'
        short_description_i18n = 'testString'
        kind = 'testString'
        publish = publish_object_model
        state = state_model
        catalog_id = 'testString'
        catalog_name = 'testString'
        data = {}

        # Invoke method
        response = _service.create_object(
            catalog_identifier,
            id=id,
            name=name,
            rev=rev,
            crn=crn,
            url=url,
            parent_id=parent_id,
            label_i18n=label_i18n,
            label=label,
            tags=tags,
            created=created,
            updated=updated,
            short_description=short_description,
            short_description_i18n=short_description_i18n,
            kind=kind,
            publish=publish,
            state=state,
            catalog_id=catalog_id,
            catalog_name=catalog_name,
            data=data,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['_rev'] == 'testString'
        assert req_body['crn'] == 'testString'
        assert req_body['url'] == 'testString'
        assert req_body['parent_id'] == 'testString'
        assert req_body['label_i18n'] == 'testString'
        assert req_body['label'] == 'testString'
        assert req_body['tags'] == ['testString']
        assert req_body['created'] == "2019-01-01T12:00:00Z"
        assert req_body['updated'] == "2019-01-01T12:00:00Z"
        assert req_body['short_description'] == 'testString'
        assert req_body['short_description_i18n'] == 'testString'
        assert req_body['kind'] == 'testString'
        assert req_body['publish'] == publish_object_model
        assert req_body['state'] == state_model
        assert req_body['catalog_id'] == 'testString'
        assert req_body['catalog_name'] == 'testString'
        assert req_body['data'] == {}


    @responses.activate
    def test_create_object_required_params(self):
        """
        test_create_object_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects')
        mock_response = '{"id": "id", "name": "name", "_rev": "rev", "crn": "crn", "url": "url", "parent_id": "parent_id", "label_i18n": "label_i18n", "label": "label", "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "short_description_i18n": "short_description_i18n", "kind": "kind", "publish": {"permit_ibm_public_publish": false, "ibm_approved": true, "public_approved": false, "portal_approval_record": "portal_approval_record", "portal_url": "portal_url"}, "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "catalog_id": "catalog_id", "catalog_name": "catalog_name", "data": {"mapKey": {"anyKey": "anyValue"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Invoke method
        response = _service.create_object(
            catalog_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_create_object_value_error(self):
        """
        test_create_object_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects')
        mock_response = '{"id": "id", "name": "name", "_rev": "rev", "crn": "crn", "url": "url", "parent_id": "parent_id", "label_i18n": "label_i18n", "label": "label", "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "short_description_i18n": "short_description_i18n", "kind": "kind", "publish": {"permit_ibm_public_publish": false, "ibm_approved": true, "public_approved": false, "portal_approval_record": "portal_approval_record", "portal_url": "portal_url"}, "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "catalog_id": "catalog_id", "catalog_name": "catalog_name", "data": {"mapKey": {"anyKey": "anyValue"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_object(**req_copy)



class TestGetObject():
    """
    Test Class for get_object
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
    def test_get_object_all_params(self):
        """
        get_object()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString')
        mock_response = '{"id": "id", "name": "name", "_rev": "rev", "crn": "crn", "url": "url", "parent_id": "parent_id", "label_i18n": "label_i18n", "label": "label", "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "short_description_i18n": "short_description_i18n", "kind": "kind", "publish": {"permit_ibm_public_publish": false, "ibm_approved": true, "public_approved": false, "portal_approval_record": "portal_approval_record", "portal_url": "portal_url"}, "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "catalog_id": "catalog_id", "catalog_name": "catalog_name", "data": {"mapKey": {"anyKey": "anyValue"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Invoke method
        response = _service.get_object(
            catalog_identifier,
            object_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_object_value_error(self):
        """
        test_get_object_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString')
        mock_response = '{"id": "id", "name": "name", "_rev": "rev", "crn": "crn", "url": "url", "parent_id": "parent_id", "label_i18n": "label_i18n", "label": "label", "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "short_description_i18n": "short_description_i18n", "kind": "kind", "publish": {"permit_ibm_public_publish": false, "ibm_approved": true, "public_approved": false, "portal_approval_record": "portal_approval_record", "portal_url": "portal_url"}, "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "catalog_id": "catalog_id", "catalog_name": "catalog_name", "data": {"mapKey": {"anyKey": "anyValue"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "object_identifier": object_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_object(**req_copy)



class TestReplaceObject():
    """
    Test Class for replace_object
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
    def test_replace_object_all_params(self):
        """
        replace_object()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString')
        mock_response = '{"id": "id", "name": "name", "_rev": "rev", "crn": "crn", "url": "url", "parent_id": "parent_id", "label_i18n": "label_i18n", "label": "label", "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "short_description_i18n": "short_description_i18n", "kind": "kind", "publish": {"permit_ibm_public_publish": false, "ibm_approved": true, "public_approved": false, "portal_approval_record": "portal_approval_record", "portal_url": "portal_url"}, "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "catalog_id": "catalog_id", "catalog_name": "catalog_name", "data": {"mapKey": {"anyKey": "anyValue"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PublishObject model
        publish_object_model = {}
        publish_object_model['permit_ibm_public_publish'] = True
        publish_object_model['ibm_approved'] = True
        publish_object_model['public_approved'] = True
        publish_object_model['portal_approval_record'] = 'testString'
        publish_object_model['portal_url'] = 'testString'

        # Construct a dict representation of a State model
        state_model = {}
        state_model['current'] = 'testString'
        state_model['current_entered'] = "2019-01-01T12:00:00Z"
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = "2019-01-01T12:00:00Z"
        state_model['previous'] = 'testString'

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'
        id = 'testString'
        name = 'testString'
        rev = 'testString'
        crn = 'testString'
        url = 'testString'
        parent_id = 'testString'
        label_i18n = 'testString'
        label = 'testString'
        tags = ['testString']
        created = string_to_datetime('2019-01-01T12:00:00.000Z')
        updated = string_to_datetime('2019-01-01T12:00:00.000Z')
        short_description = 'testString'
        short_description_i18n = 'testString'
        kind = 'testString'
        publish = publish_object_model
        state = state_model
        catalog_id = 'testString'
        catalog_name = 'testString'
        data = {}

        # Invoke method
        response = _service.replace_object(
            catalog_identifier,
            object_identifier,
            id=id,
            name=name,
            rev=rev,
            crn=crn,
            url=url,
            parent_id=parent_id,
            label_i18n=label_i18n,
            label=label,
            tags=tags,
            created=created,
            updated=updated,
            short_description=short_description,
            short_description_i18n=short_description_i18n,
            kind=kind,
            publish=publish,
            state=state,
            catalog_id=catalog_id,
            catalog_name=catalog_name,
            data=data,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['_rev'] == 'testString'
        assert req_body['crn'] == 'testString'
        assert req_body['url'] == 'testString'
        assert req_body['parent_id'] == 'testString'
        assert req_body['label_i18n'] == 'testString'
        assert req_body['label'] == 'testString'
        assert req_body['tags'] == ['testString']
        assert req_body['created'] == "2019-01-01T12:00:00Z"
        assert req_body['updated'] == "2019-01-01T12:00:00Z"
        assert req_body['short_description'] == 'testString'
        assert req_body['short_description_i18n'] == 'testString'
        assert req_body['kind'] == 'testString'
        assert req_body['publish'] == publish_object_model
        assert req_body['state'] == state_model
        assert req_body['catalog_id'] == 'testString'
        assert req_body['catalog_name'] == 'testString'
        assert req_body['data'] == {}


    @responses.activate
    def test_replace_object_required_params(self):
        """
        test_replace_object_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString')
        mock_response = '{"id": "id", "name": "name", "_rev": "rev", "crn": "crn", "url": "url", "parent_id": "parent_id", "label_i18n": "label_i18n", "label": "label", "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "short_description_i18n": "short_description_i18n", "kind": "kind", "publish": {"permit_ibm_public_publish": false, "ibm_approved": true, "public_approved": false, "portal_approval_record": "portal_approval_record", "portal_url": "portal_url"}, "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "catalog_id": "catalog_id", "catalog_name": "catalog_name", "data": {"mapKey": {"anyKey": "anyValue"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Invoke method
        response = _service.replace_object(
            catalog_identifier,
            object_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_replace_object_value_error(self):
        """
        test_replace_object_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString')
        mock_response = '{"id": "id", "name": "name", "_rev": "rev", "crn": "crn", "url": "url", "parent_id": "parent_id", "label_i18n": "label_i18n", "label": "label", "tags": ["tags"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "short_description": "short_description", "short_description_i18n": "short_description_i18n", "kind": "kind", "publish": {"permit_ibm_public_publish": false, "ibm_approved": true, "public_approved": false, "portal_approval_record": "portal_approval_record", "portal_url": "portal_url"}, "state": {"current": "current", "current_entered": "2019-01-01T12:00:00.000Z", "pending": "pending", "pending_requested": "2019-01-01T12:00:00.000Z", "previous": "previous"}, "catalog_id": "catalog_id", "catalog_name": "catalog_name", "data": {"mapKey": {"anyKey": "anyValue"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "object_identifier": object_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_object(**req_copy)



class TestDeleteObject():
    """
    Test Class for delete_object
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
    def test_delete_object_all_params(self):
        """
        delete_object()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Invoke method
        response = _service.delete_object(
            catalog_identifier,
            object_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_object_value_error(self):
        """
        test_delete_object_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "object_identifier": object_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_object(**req_copy)



class TestGetObjectAudit():
    """
    Test Class for get_object_audit
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
    def test_get_object_audit_all_params(self):
        """
        get_object_audit()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/audit')
        mock_response = '{"list": [{"id": "id", "created": "2019-01-01T12:00:00.000Z", "change_type": "change_type", "target_type": "target_type", "target_id": "target_id", "who_delegate_email": "who_delegate_email", "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Invoke method
        response = _service.get_object_audit(
            catalog_identifier,
            object_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_object_audit_value_error(self):
        """
        test_get_object_audit_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/audit')
        mock_response = '{"list": [{"id": "id", "created": "2019-01-01T12:00:00.000Z", "change_type": "change_type", "target_type": "target_type", "target_id": "target_id", "who_delegate_email": "who_delegate_email", "message": "message"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "object_identifier": object_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_object_audit(**req_copy)



class TestAccountPublishObject():
    """
    Test Class for account_publish_object
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
    def test_account_publish_object_all_params(self):
        """
        account_publish_object()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/account-publish')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Invoke method
        response = _service.account_publish_object(
            catalog_identifier,
            object_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_account_publish_object_value_error(self):
        """
        test_account_publish_object_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/account-publish')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "object_identifier": object_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.account_publish_object(**req_copy)



class TestSharedPublishObject():
    """
    Test Class for shared_publish_object
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
    def test_shared_publish_object_all_params(self):
        """
        shared_publish_object()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/shared-publish')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Invoke method
        response = _service.shared_publish_object(
            catalog_identifier,
            object_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_shared_publish_object_value_error(self):
        """
        test_shared_publish_object_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/shared-publish')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "object_identifier": object_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.shared_publish_object(**req_copy)



class TestIbmPublishObject():
    """
    Test Class for ibm_publish_object
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
    def test_ibm_publish_object_all_params(self):
        """
        ibm_publish_object()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/ibm-publish')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Invoke method
        response = _service.ibm_publish_object(
            catalog_identifier,
            object_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_ibm_publish_object_value_error(self):
        """
        test_ibm_publish_object_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/ibm-publish')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "object_identifier": object_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.ibm_publish_object(**req_copy)



class TestPublicPublishObject():
    """
    Test Class for public_publish_object
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
    def test_public_publish_object_all_params(self):
        """
        public_publish_object()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/public-publish')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Invoke method
        response = _service.public_publish_object(
            catalog_identifier,
            object_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_public_publish_object_value_error(self):
        """
        test_public_publish_object_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/public-publish')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "object_identifier": object_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.public_publish_object(**req_copy)



class TestCreateObjectAccess():
    """
    Test Class for create_object_access
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
    def test_create_object_access_all_params(self):
        """
        create_object_access()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/access/testString')
        responses.add(responses.POST,
                      url,
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'
        account_identifier = 'testString'

        # Invoke method
        response = _service.create_object_access(
            catalog_identifier,
            object_identifier,
            account_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_create_object_access_value_error(self):
        """
        test_create_object_access_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/access/testString')
        responses.add(responses.POST,
                      url,
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'
        account_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "object_identifier": object_identifier,
            "account_identifier": account_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_object_access(**req_copy)



class TestGetObjectAccess():
    """
    Test Class for get_object_access
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
    def test_get_object_access_all_params(self):
        """
        get_object_access()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/access/testString')
        mock_response = '{"id": "id", "account": "account", "catalog_id": "catalog_id", "target_id": "target_id", "create": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'
        account_identifier = 'testString'

        # Invoke method
        response = _service.get_object_access(
            catalog_identifier,
            object_identifier,
            account_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_object_access_value_error(self):
        """
        test_get_object_access_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/access/testString')
        mock_response = '{"id": "id", "account": "account", "catalog_id": "catalog_id", "target_id": "target_id", "create": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'
        account_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "object_identifier": object_identifier,
            "account_identifier": account_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_object_access(**req_copy)



class TestDeleteObjectAccess():
    """
    Test Class for delete_object_access
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
    def test_delete_object_access_all_params(self):
        """
        delete_object_access()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/access/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'
        account_identifier = 'testString'

        # Invoke method
        response = _service.delete_object_access(
            catalog_identifier,
            object_identifier,
            account_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_object_access_value_error(self):
        """
        test_delete_object_access_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/access/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'
        account_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "object_identifier": object_identifier,
            "account_identifier": account_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_object_access(**req_copy)



class TestGetObjectAccessList():
    """
    Test Class for get_object_access_list
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
    def test_get_object_access_list_all_params(self):
        """
        get_object_access_list()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/access')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "account": "account", "catalog_id": "catalog_id", "target_id": "target_id", "create": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'
        limit = 1000
        offset = 38

        # Invoke method
        response = _service.get_object_access_list(
            catalog_identifier,
            object_identifier,
            limit=limit,
            offset=offset,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string


    @responses.activate
    def test_get_object_access_list_required_params(self):
        """
        test_get_object_access_list_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/access')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "account": "account", "catalog_id": "catalog_id", "target_id": "target_id", "create": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Invoke method
        response = _service.get_object_access_list(
            catalog_identifier,
            object_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_object_access_list_value_error(self):
        """
        test_get_object_access_list_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/access')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "account": "account", "catalog_id": "catalog_id", "target_id": "target_id", "create": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "object_identifier": object_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_object_access_list(**req_copy)



class TestDeleteObjectAccessList():
    """
    Test Class for delete_object_access_list
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
    def test_delete_object_access_list_all_params(self):
        """
        delete_object_access_list()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/access')
        mock_response = '{"errors": {"mapKey": "inner"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'
        accounts = ['testString']

        # Invoke method
        response = _service.delete_object_access_list(
            catalog_identifier,
            object_identifier,
            accounts,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == accounts


    @responses.activate
    def test_delete_object_access_list_value_error(self):
        """
        test_delete_object_access_list_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/access')
        mock_response = '{"errors": {"mapKey": "inner"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'
        accounts = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "object_identifier": object_identifier,
            "accounts": accounts,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_object_access_list(**req_copy)



class TestAddObjectAccessList():
    """
    Test Class for add_object_access_list
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
    def test_add_object_access_list_all_params(self):
        """
        add_object_access_list()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/access')
        mock_response = '{"errors": {"mapKey": "inner"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'
        accounts = ['testString']

        # Invoke method
        response = _service.add_object_access_list(
            catalog_identifier,
            object_identifier,
            accounts,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == accounts


    @responses.activate
    def test_add_object_access_list_value_error(self):
        """
        test_add_object_access_list_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/catalogs/testString/objects/testString/access')
        mock_response = '{"errors": {"mapKey": "inner"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        object_identifier = 'testString'
        accounts = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "object_identifier": object_identifier,
            "accounts": accounts,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_object_access_list(**req_copy)



# endregion
##############################################################################
# End of Service: Objects
##############################################################################

##############################################################################
# Start of Service: Instances
##############################################################################
# region

class TestCreateOfferingInstance():
    """
    Test Class for create_offering_instance
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
    def test_create_offering_instance_all_params(self):
        """
        create_offering_instance()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/instances/offerings')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "catalog_id": "catalog_id", "offering_id": "offering_id", "kind_format": "kind_format", "version": "version", "cluster_id": "cluster_id", "cluster_region": "cluster_region", "cluster_namespaces": ["cluster_namespaces"], "cluster_all_namespaces": true, "schematics_workspace_id": "schematics_workspace_id", "resource_group_id": "resource_group_id", "install_plan": "install_plan", "channel": "channel", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "last_operation": {"operation": "operation", "state": "state", "message": "message", "transaction_id": "transaction_id", "updated": "updated"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a OfferingInstanceLastOperation model
        offering_instance_last_operation_model = {}
        offering_instance_last_operation_model['operation'] = 'testString'
        offering_instance_last_operation_model['state'] = 'testString'
        offering_instance_last_operation_model['message'] = 'testString'
        offering_instance_last_operation_model['transaction_id'] = 'testString'
        offering_instance_last_operation_model['updated'] = 'testString'

        # Set up parameter values
        x_auth_refresh_token = 'testString'
        id = 'testString'
        rev = 'testString'
        url = 'testString'
        crn = 'testString'
        label = 'testString'
        catalog_id = 'testString'
        offering_id = 'testString'
        kind_format = 'testString'
        version = 'testString'
        cluster_id = 'testString'
        cluster_region = 'testString'
        cluster_namespaces = ['testString']
        cluster_all_namespaces = True
        schematics_workspace_id = 'testString'
        resource_group_id = 'testString'
        install_plan = 'testString'
        channel = 'testString'
        metadata = {}
        last_operation = offering_instance_last_operation_model

        # Invoke method
        response = _service.create_offering_instance(
            x_auth_refresh_token,
            id=id,
            rev=rev,
            url=url,
            crn=crn,
            label=label,
            catalog_id=catalog_id,
            offering_id=offering_id,
            kind_format=kind_format,
            version=version,
            cluster_id=cluster_id,
            cluster_region=cluster_region,
            cluster_namespaces=cluster_namespaces,
            cluster_all_namespaces=cluster_all_namespaces,
            schematics_workspace_id=schematics_workspace_id,
            resource_group_id=resource_group_id,
            install_plan=install_plan,
            channel=channel,
            metadata=metadata,
            last_operation=last_operation,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['_rev'] == 'testString'
        assert req_body['url'] == 'testString'
        assert req_body['crn'] == 'testString'
        assert req_body['label'] == 'testString'
        assert req_body['catalog_id'] == 'testString'
        assert req_body['offering_id'] == 'testString'
        assert req_body['kind_format'] == 'testString'
        assert req_body['version'] == 'testString'
        assert req_body['cluster_id'] == 'testString'
        assert req_body['cluster_region'] == 'testString'
        assert req_body['cluster_namespaces'] == ['testString']
        assert req_body['cluster_all_namespaces'] == True
        assert req_body['schematics_workspace_id'] == 'testString'
        assert req_body['resource_group_id'] == 'testString'
        assert req_body['install_plan'] == 'testString'
        assert req_body['channel'] == 'testString'
        assert req_body['metadata'] == {}
        assert req_body['last_operation'] == offering_instance_last_operation_model


    @responses.activate
    def test_create_offering_instance_required_params(self):
        """
        test_create_offering_instance_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/instances/offerings')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "catalog_id": "catalog_id", "offering_id": "offering_id", "kind_format": "kind_format", "version": "version", "cluster_id": "cluster_id", "cluster_region": "cluster_region", "cluster_namespaces": ["cluster_namespaces"], "cluster_all_namespaces": true, "schematics_workspace_id": "schematics_workspace_id", "resource_group_id": "resource_group_id", "install_plan": "install_plan", "channel": "channel", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "last_operation": {"operation": "operation", "state": "state", "message": "message", "transaction_id": "transaction_id", "updated": "updated"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = _service.create_offering_instance(
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_create_offering_instance_value_error(self):
        """
        test_create_offering_instance_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/instances/offerings')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "catalog_id": "catalog_id", "offering_id": "offering_id", "kind_format": "kind_format", "version": "version", "cluster_id": "cluster_id", "cluster_region": "cluster_region", "cluster_namespaces": ["cluster_namespaces"], "cluster_all_namespaces": true, "schematics_workspace_id": "schematics_workspace_id", "resource_group_id": "resource_group_id", "install_plan": "install_plan", "channel": "channel", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "last_operation": {"operation": "operation", "state": "state", "message": "message", "transaction_id": "transaction_id", "updated": "updated"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        x_auth_refresh_token = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "x_auth_refresh_token": x_auth_refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_offering_instance(**req_copy)



class TestGetOfferingInstance():
    """
    Test Class for get_offering_instance
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
    def test_get_offering_instance_all_params(self):
        """
        get_offering_instance()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/instances/offerings/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "catalog_id": "catalog_id", "offering_id": "offering_id", "kind_format": "kind_format", "version": "version", "cluster_id": "cluster_id", "cluster_region": "cluster_region", "cluster_namespaces": ["cluster_namespaces"], "cluster_all_namespaces": true, "schematics_workspace_id": "schematics_workspace_id", "resource_group_id": "resource_group_id", "install_plan": "install_plan", "channel": "channel", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "last_operation": {"operation": "operation", "state": "state", "message": "message", "transaction_id": "transaction_id", "updated": "updated"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_identifier = 'testString'

        # Invoke method
        response = _service.get_offering_instance(
            instance_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_offering_instance_value_error(self):
        """
        test_get_offering_instance_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/instances/offerings/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "catalog_id": "catalog_id", "offering_id": "offering_id", "kind_format": "kind_format", "version": "version", "cluster_id": "cluster_id", "cluster_region": "cluster_region", "cluster_namespaces": ["cluster_namespaces"], "cluster_all_namespaces": true, "schematics_workspace_id": "schematics_workspace_id", "resource_group_id": "resource_group_id", "install_plan": "install_plan", "channel": "channel", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "last_operation": {"operation": "operation", "state": "state", "message": "message", "transaction_id": "transaction_id", "updated": "updated"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_identifier": instance_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_offering_instance(**req_copy)



class TestPutOfferingInstance():
    """
    Test Class for put_offering_instance
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
    def test_put_offering_instance_all_params(self):
        """
        put_offering_instance()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/instances/offerings/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "catalog_id": "catalog_id", "offering_id": "offering_id", "kind_format": "kind_format", "version": "version", "cluster_id": "cluster_id", "cluster_region": "cluster_region", "cluster_namespaces": ["cluster_namespaces"], "cluster_all_namespaces": true, "schematics_workspace_id": "schematics_workspace_id", "resource_group_id": "resource_group_id", "install_plan": "install_plan", "channel": "channel", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "last_operation": {"operation": "operation", "state": "state", "message": "message", "transaction_id": "transaction_id", "updated": "updated"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a OfferingInstanceLastOperation model
        offering_instance_last_operation_model = {}
        offering_instance_last_operation_model['operation'] = 'testString'
        offering_instance_last_operation_model['state'] = 'testString'
        offering_instance_last_operation_model['message'] = 'testString'
        offering_instance_last_operation_model['transaction_id'] = 'testString'
        offering_instance_last_operation_model['updated'] = 'testString'

        # Set up parameter values
        instance_identifier = 'testString'
        x_auth_refresh_token = 'testString'
        id = 'testString'
        rev = 'testString'
        url = 'testString'
        crn = 'testString'
        label = 'testString'
        catalog_id = 'testString'
        offering_id = 'testString'
        kind_format = 'testString'
        version = 'testString'
        cluster_id = 'testString'
        cluster_region = 'testString'
        cluster_namespaces = ['testString']
        cluster_all_namespaces = True
        schematics_workspace_id = 'testString'
        resource_group_id = 'testString'
        install_plan = 'testString'
        channel = 'testString'
        metadata = {}
        last_operation = offering_instance_last_operation_model

        # Invoke method
        response = _service.put_offering_instance(
            instance_identifier,
            x_auth_refresh_token,
            id=id,
            rev=rev,
            url=url,
            crn=crn,
            label=label,
            catalog_id=catalog_id,
            offering_id=offering_id,
            kind_format=kind_format,
            version=version,
            cluster_id=cluster_id,
            cluster_region=cluster_region,
            cluster_namespaces=cluster_namespaces,
            cluster_all_namespaces=cluster_all_namespaces,
            schematics_workspace_id=schematics_workspace_id,
            resource_group_id=resource_group_id,
            install_plan=install_plan,
            channel=channel,
            metadata=metadata,
            last_operation=last_operation,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['_rev'] == 'testString'
        assert req_body['url'] == 'testString'
        assert req_body['crn'] == 'testString'
        assert req_body['label'] == 'testString'
        assert req_body['catalog_id'] == 'testString'
        assert req_body['offering_id'] == 'testString'
        assert req_body['kind_format'] == 'testString'
        assert req_body['version'] == 'testString'
        assert req_body['cluster_id'] == 'testString'
        assert req_body['cluster_region'] == 'testString'
        assert req_body['cluster_namespaces'] == ['testString']
        assert req_body['cluster_all_namespaces'] == True
        assert req_body['schematics_workspace_id'] == 'testString'
        assert req_body['resource_group_id'] == 'testString'
        assert req_body['install_plan'] == 'testString'
        assert req_body['channel'] == 'testString'
        assert req_body['metadata'] == {}
        assert req_body['last_operation'] == offering_instance_last_operation_model


    @responses.activate
    def test_put_offering_instance_required_params(self):
        """
        test_put_offering_instance_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/instances/offerings/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "catalog_id": "catalog_id", "offering_id": "offering_id", "kind_format": "kind_format", "version": "version", "cluster_id": "cluster_id", "cluster_region": "cluster_region", "cluster_namespaces": ["cluster_namespaces"], "cluster_all_namespaces": true, "schematics_workspace_id": "schematics_workspace_id", "resource_group_id": "resource_group_id", "install_plan": "install_plan", "channel": "channel", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "last_operation": {"operation": "operation", "state": "state", "message": "message", "transaction_id": "transaction_id", "updated": "updated"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_identifier = 'testString'
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = _service.put_offering_instance(
            instance_identifier,
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_put_offering_instance_value_error(self):
        """
        test_put_offering_instance_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/instances/offerings/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "catalog_id": "catalog_id", "offering_id": "offering_id", "kind_format": "kind_format", "version": "version", "cluster_id": "cluster_id", "cluster_region": "cluster_region", "cluster_namespaces": ["cluster_namespaces"], "cluster_all_namespaces": true, "schematics_workspace_id": "schematics_workspace_id", "resource_group_id": "resource_group_id", "install_plan": "install_plan", "channel": "channel", "metadata": {"mapKey": {"anyKey": "anyValue"}}, "last_operation": {"operation": "operation", "state": "state", "message": "message", "transaction_id": "transaction_id", "updated": "updated"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_identifier = 'testString'
        x_auth_refresh_token = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_identifier": instance_identifier,
            "x_auth_refresh_token": x_auth_refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.put_offering_instance(**req_copy)



class TestDeleteOfferingInstance():
    """
    Test Class for delete_offering_instance
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
    def test_delete_offering_instance_all_params(self):
        """
        delete_offering_instance()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/instances/offerings/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        instance_identifier = 'testString'
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = _service.delete_offering_instance(
            instance_identifier,
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_offering_instance_value_error(self):
        """
        test_delete_offering_instance_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/instances/offerings/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        instance_identifier = 'testString'
        x_auth_refresh_token = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_identifier": instance_identifier,
            "x_auth_refresh_token": x_auth_refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_offering_instance(**req_copy)



# endregion
##############################################################################
# End of Service: Instances
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class AccessListBulkResponseUnitTests():
    """
    Test Class for AccessListBulkResponse
    """

    def test_access_list_bulk_response_serialization(self):
        """
        Test serialization/deserialization for AccessListBulkResponse
        """

        # Construct a json representation of a AccessListBulkResponse model
        access_list_bulk_response_model_json = {}
        access_list_bulk_response_model_json['errors'] = {}

        # Construct a model instance of AccessListBulkResponse by calling from_dict on the json representation
        access_list_bulk_response_model = AccessListBulkResponse.from_dict(access_list_bulk_response_model_json)
        assert access_list_bulk_response_model != False

        # Construct a model instance of AccessListBulkResponse by calling from_dict on the json representation
        access_list_bulk_response_model_dict = AccessListBulkResponse.from_dict(access_list_bulk_response_model_json).__dict__
        access_list_bulk_response_model2 = AccessListBulkResponse(**access_list_bulk_response_model_dict)

        # Verify the model instances are equivalent
        assert access_list_bulk_response_model == access_list_bulk_response_model2

        # Convert model instance back to dict and verify no loss of data
        access_list_bulk_response_model_json2 = access_list_bulk_response_model.to_dict()
        assert access_list_bulk_response_model_json2 == access_list_bulk_response_model_json

class AccountUnitTests():
    """
    Test Class for Account
    """

    def test_account_serialization(self):
        """
        Test serialization/deserialization for Account
        """

        # Construct dict forms of any model objects needed in order to build this model.

        filter_terms_model = {} # FilterTerms
        filter_terms_model['filter_terms'] = ['testString']

        category_filter_model = {} # CategoryFilter
        category_filter_model['include'] = True
        category_filter_model['filter'] = filter_terms_model

        id_filter_model = {} # IDFilter
        id_filter_model['include'] = filter_terms_model
        id_filter_model['exclude'] = filter_terms_model

        filters_model = {} # Filters
        filters_model['include_all'] = True
        filters_model['category_filters'] = {}
        filters_model['id_filters'] = id_filter_model

        # Construct a json representation of a Account model
        account_model_json = {}
        account_model_json['id'] = 'testString'
        account_model_json['hide_IBM_cloud_catalog'] = True
        account_model_json['account_filters'] = filters_model

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

class AccumulatedFiltersUnitTests():
    """
    Test Class for AccumulatedFilters
    """

    def test_accumulated_filters_serialization(self):
        """
        Test serialization/deserialization for AccumulatedFilters
        """

        # Construct dict forms of any model objects needed in order to build this model.

        filter_terms_model = {} # FilterTerms
        filter_terms_model['filter_terms'] = ['testString']

        category_filter_model = {} # CategoryFilter
        category_filter_model['include'] = True
        category_filter_model['filter'] = filter_terms_model

        id_filter_model = {} # IDFilter
        id_filter_model['include'] = filter_terms_model
        id_filter_model['exclude'] = filter_terms_model

        filters_model = {} # Filters
        filters_model['include_all'] = True
        filters_model['category_filters'] = {}
        filters_model['id_filters'] = id_filter_model

        accumulated_filters_catalog_filters_item_catalog_model = {} # AccumulatedFiltersCatalogFiltersItemCatalog
        accumulated_filters_catalog_filters_item_catalog_model['id'] = 'testString'
        accumulated_filters_catalog_filters_item_catalog_model['name'] = 'testString'

        accumulated_filters_catalog_filters_item_model = {} # AccumulatedFiltersCatalogFiltersItem
        accumulated_filters_catalog_filters_item_model['catalog'] = accumulated_filters_catalog_filters_item_catalog_model
        accumulated_filters_catalog_filters_item_model['filters'] = filters_model

        # Construct a json representation of a AccumulatedFilters model
        accumulated_filters_model_json = {}
        accumulated_filters_model_json['account_filters'] = [filters_model]
        accumulated_filters_model_json['catalog_filters'] = [accumulated_filters_catalog_filters_item_model]

        # Construct a model instance of AccumulatedFilters by calling from_dict on the json representation
        accumulated_filters_model = AccumulatedFilters.from_dict(accumulated_filters_model_json)
        assert accumulated_filters_model != False

        # Construct a model instance of AccumulatedFilters by calling from_dict on the json representation
        accumulated_filters_model_dict = AccumulatedFilters.from_dict(accumulated_filters_model_json).__dict__
        accumulated_filters_model2 = AccumulatedFilters(**accumulated_filters_model_dict)

        # Verify the model instances are equivalent
        assert accumulated_filters_model == accumulated_filters_model2

        # Convert model instance back to dict and verify no loss of data
        accumulated_filters_model_json2 = accumulated_filters_model.to_dict()
        assert accumulated_filters_model_json2 == accumulated_filters_model_json

class AccumulatedFiltersCatalogFiltersItemUnitTests():
    """
    Test Class for AccumulatedFiltersCatalogFiltersItem
    """

    def test_accumulated_filters_catalog_filters_item_serialization(self):
        """
        Test serialization/deserialization for AccumulatedFiltersCatalogFiltersItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        accumulated_filters_catalog_filters_item_catalog_model = {} # AccumulatedFiltersCatalogFiltersItemCatalog
        accumulated_filters_catalog_filters_item_catalog_model['id'] = 'testString'
        accumulated_filters_catalog_filters_item_catalog_model['name'] = 'testString'

        filter_terms_model = {} # FilterTerms
        filter_terms_model['filter_terms'] = ['testString']

        category_filter_model = {} # CategoryFilter
        category_filter_model['include'] = True
        category_filter_model['filter'] = filter_terms_model

        id_filter_model = {} # IDFilter
        id_filter_model['include'] = filter_terms_model
        id_filter_model['exclude'] = filter_terms_model

        filters_model = {} # Filters
        filters_model['include_all'] = True
        filters_model['category_filters'] = {}
        filters_model['id_filters'] = id_filter_model

        # Construct a json representation of a AccumulatedFiltersCatalogFiltersItem model
        accumulated_filters_catalog_filters_item_model_json = {}
        accumulated_filters_catalog_filters_item_model_json['catalog'] = accumulated_filters_catalog_filters_item_catalog_model
        accumulated_filters_catalog_filters_item_model_json['filters'] = filters_model

        # Construct a model instance of AccumulatedFiltersCatalogFiltersItem by calling from_dict on the json representation
        accumulated_filters_catalog_filters_item_model = AccumulatedFiltersCatalogFiltersItem.from_dict(accumulated_filters_catalog_filters_item_model_json)
        assert accumulated_filters_catalog_filters_item_model != False

        # Construct a model instance of AccumulatedFiltersCatalogFiltersItem by calling from_dict on the json representation
        accumulated_filters_catalog_filters_item_model_dict = AccumulatedFiltersCatalogFiltersItem.from_dict(accumulated_filters_catalog_filters_item_model_json).__dict__
        accumulated_filters_catalog_filters_item_model2 = AccumulatedFiltersCatalogFiltersItem(**accumulated_filters_catalog_filters_item_model_dict)

        # Verify the model instances are equivalent
        assert accumulated_filters_catalog_filters_item_model == accumulated_filters_catalog_filters_item_model2

        # Convert model instance back to dict and verify no loss of data
        accumulated_filters_catalog_filters_item_model_json2 = accumulated_filters_catalog_filters_item_model.to_dict()
        assert accumulated_filters_catalog_filters_item_model_json2 == accumulated_filters_catalog_filters_item_model_json

class AccumulatedFiltersCatalogFiltersItemCatalogUnitTests():
    """
    Test Class for AccumulatedFiltersCatalogFiltersItemCatalog
    """

    def test_accumulated_filters_catalog_filters_item_catalog_serialization(self):
        """
        Test serialization/deserialization for AccumulatedFiltersCatalogFiltersItemCatalog
        """

        # Construct a json representation of a AccumulatedFiltersCatalogFiltersItemCatalog model
        accumulated_filters_catalog_filters_item_catalog_model_json = {}
        accumulated_filters_catalog_filters_item_catalog_model_json['id'] = 'testString'
        accumulated_filters_catalog_filters_item_catalog_model_json['name'] = 'testString'

        # Construct a model instance of AccumulatedFiltersCatalogFiltersItemCatalog by calling from_dict on the json representation
        accumulated_filters_catalog_filters_item_catalog_model = AccumulatedFiltersCatalogFiltersItemCatalog.from_dict(accumulated_filters_catalog_filters_item_catalog_model_json)
        assert accumulated_filters_catalog_filters_item_catalog_model != False

        # Construct a model instance of AccumulatedFiltersCatalogFiltersItemCatalog by calling from_dict on the json representation
        accumulated_filters_catalog_filters_item_catalog_model_dict = AccumulatedFiltersCatalogFiltersItemCatalog.from_dict(accumulated_filters_catalog_filters_item_catalog_model_json).__dict__
        accumulated_filters_catalog_filters_item_catalog_model2 = AccumulatedFiltersCatalogFiltersItemCatalog(**accumulated_filters_catalog_filters_item_catalog_model_dict)

        # Verify the model instances are equivalent
        assert accumulated_filters_catalog_filters_item_catalog_model == accumulated_filters_catalog_filters_item_catalog_model2

        # Convert model instance back to dict and verify no loss of data
        accumulated_filters_catalog_filters_item_catalog_model_json2 = accumulated_filters_catalog_filters_item_catalog_model.to_dict()
        assert accumulated_filters_catalog_filters_item_catalog_model_json2 == accumulated_filters_catalog_filters_item_catalog_model_json

class ApprovalResultUnitTests():
    """
    Test Class for ApprovalResult
    """

    def test_approval_result_serialization(self):
        """
        Test serialization/deserialization for ApprovalResult
        """

        # Construct a json representation of a ApprovalResult model
        approval_result_model_json = {}
        approval_result_model_json['allow_request'] = True
        approval_result_model_json['ibm'] = True
        approval_result_model_json['public'] = True
        approval_result_model_json['changed'] = True

        # Construct a model instance of ApprovalResult by calling from_dict on the json representation
        approval_result_model = ApprovalResult.from_dict(approval_result_model_json)
        assert approval_result_model != False

        # Construct a model instance of ApprovalResult by calling from_dict on the json representation
        approval_result_model_dict = ApprovalResult.from_dict(approval_result_model_json).__dict__
        approval_result_model2 = ApprovalResult(**approval_result_model_dict)

        # Verify the model instances are equivalent
        assert approval_result_model == approval_result_model2

        # Convert model instance back to dict and verify no loss of data
        approval_result_model_json2 = approval_result_model.to_dict()
        assert approval_result_model_json2 == approval_result_model_json

class AuditLogUnitTests():
    """
    Test Class for AuditLog
    """

    def test_audit_log_serialization(self):
        """
        Test serialization/deserialization for AuditLog
        """

        # Construct dict forms of any model objects needed in order to build this model.

        audit_record_model = {} # AuditRecord
        audit_record_model['id'] = 'testString'
        audit_record_model['created'] = "2019-01-01T12:00:00Z"
        audit_record_model['change_type'] = 'testString'
        audit_record_model['target_type'] = 'testString'
        audit_record_model['target_id'] = 'testString'
        audit_record_model['who_delegate_email'] = 'testString'
        audit_record_model['message'] = 'testString'

        # Construct a json representation of a AuditLog model
        audit_log_model_json = {}
        audit_log_model_json['list'] = [audit_record_model]

        # Construct a model instance of AuditLog by calling from_dict on the json representation
        audit_log_model = AuditLog.from_dict(audit_log_model_json)
        assert audit_log_model != False

        # Construct a model instance of AuditLog by calling from_dict on the json representation
        audit_log_model_dict = AuditLog.from_dict(audit_log_model_json).__dict__
        audit_log_model2 = AuditLog(**audit_log_model_dict)

        # Verify the model instances are equivalent
        assert audit_log_model == audit_log_model2

        # Convert model instance back to dict and verify no loss of data
        audit_log_model_json2 = audit_log_model.to_dict()
        assert audit_log_model_json2 == audit_log_model_json

class AuditRecordUnitTests():
    """
    Test Class for AuditRecord
    """

    def test_audit_record_serialization(self):
        """
        Test serialization/deserialization for AuditRecord
        """

        # Construct a json representation of a AuditRecord model
        audit_record_model_json = {}
        audit_record_model_json['id'] = 'testString'
        audit_record_model_json['created'] = "2019-01-01T12:00:00Z"
        audit_record_model_json['change_type'] = 'testString'
        audit_record_model_json['target_type'] = 'testString'
        audit_record_model_json['target_id'] = 'testString'
        audit_record_model_json['who_delegate_email'] = 'testString'
        audit_record_model_json['message'] = 'testString'

        # Construct a model instance of AuditRecord by calling from_dict on the json representation
        audit_record_model = AuditRecord.from_dict(audit_record_model_json)
        assert audit_record_model != False

        # Construct a model instance of AuditRecord by calling from_dict on the json representation
        audit_record_model_dict = AuditRecord.from_dict(audit_record_model_json).__dict__
        audit_record_model2 = AuditRecord(**audit_record_model_dict)

        # Verify the model instances are equivalent
        assert audit_record_model == audit_record_model2

        # Convert model instance back to dict and verify no loss of data
        audit_record_model_json2 = audit_record_model.to_dict()
        assert audit_record_model_json2 == audit_record_model_json

class CatalogUnitTests():
    """
    Test Class for Catalog
    """

    def test_catalog_serialization(self):
        """
        Test serialization/deserialization for Catalog
        """

        # Construct dict forms of any model objects needed in order to build this model.

        feature_model = {} # Feature
        feature_model['title'] = 'testString'
        feature_model['description'] = 'testString'

        filter_terms_model = {} # FilterTerms
        filter_terms_model['filter_terms'] = ['testString']

        category_filter_model = {} # CategoryFilter
        category_filter_model['include'] = True
        category_filter_model['filter'] = filter_terms_model

        id_filter_model = {} # IDFilter
        id_filter_model['include'] = filter_terms_model
        id_filter_model['exclude'] = filter_terms_model

        filters_model = {} # Filters
        filters_model['include_all'] = True
        filters_model['category_filters'] = {}
        filters_model['id_filters'] = id_filter_model

        syndication_cluster_model = {} # SyndicationCluster
        syndication_cluster_model['region'] = 'testString'
        syndication_cluster_model['id'] = 'testString'
        syndication_cluster_model['name'] = 'testString'
        syndication_cluster_model['resource_group_name'] = 'testString'
        syndication_cluster_model['type'] = 'testString'
        syndication_cluster_model['namespaces'] = ['testString']
        syndication_cluster_model['all_namespaces'] = True

        syndication_history_model = {} # SyndicationHistory
        syndication_history_model['namespaces'] = ['testString']
        syndication_history_model['clusters'] = [syndication_cluster_model]
        syndication_history_model['last_run'] = "2019-01-01T12:00:00Z"

        syndication_authorization_model = {} # SyndicationAuthorization
        syndication_authorization_model['token'] = 'testString'
        syndication_authorization_model['last_run'] = "2019-01-01T12:00:00Z"

        syndication_resource_model = {} # SyndicationResource
        syndication_resource_model['remove_related_components'] = True
        syndication_resource_model['clusters'] = [syndication_cluster_model]
        syndication_resource_model['history'] = syndication_history_model
        syndication_resource_model['authorization'] = syndication_authorization_model

        # Construct a json representation of a Catalog model
        catalog_model_json = {}
        catalog_model_json['id'] = 'testString'
        catalog_model_json['_rev'] = 'testString'
        catalog_model_json['label'] = 'testString'
        catalog_model_json['short_description'] = 'testString'
        catalog_model_json['catalog_icon_url'] = 'testString'
        catalog_model_json['tags'] = ['testString']
        catalog_model_json['url'] = 'testString'
        catalog_model_json['crn'] = 'testString'
        catalog_model_json['offerings_url'] = 'testString'
        catalog_model_json['features'] = [feature_model]
        catalog_model_json['disabled'] = True
        catalog_model_json['created'] = "2019-01-01T12:00:00Z"
        catalog_model_json['updated'] = "2019-01-01T12:00:00Z"
        catalog_model_json['resource_group_id'] = 'testString'
        catalog_model_json['owning_account'] = 'testString'
        catalog_model_json['catalog_filters'] = filters_model
        catalog_model_json['syndication_settings'] = syndication_resource_model
        catalog_model_json['kind'] = 'testString'

        # Construct a model instance of Catalog by calling from_dict on the json representation
        catalog_model = Catalog.from_dict(catalog_model_json)
        assert catalog_model != False

        # Construct a model instance of Catalog by calling from_dict on the json representation
        catalog_model_dict = Catalog.from_dict(catalog_model_json).__dict__
        catalog_model2 = Catalog(**catalog_model_dict)

        # Verify the model instances are equivalent
        assert catalog_model == catalog_model2

        # Convert model instance back to dict and verify no loss of data
        catalog_model_json2 = catalog_model.to_dict()
        assert catalog_model_json2 == catalog_model_json

class CatalogObjectUnitTests():
    """
    Test Class for CatalogObject
    """

    def test_catalog_object_serialization(self):
        """
        Test serialization/deserialization for CatalogObject
        """

        # Construct dict forms of any model objects needed in order to build this model.

        publish_object_model = {} # PublishObject
        publish_object_model['permit_ibm_public_publish'] = True
        publish_object_model['ibm_approved'] = True
        publish_object_model['public_approved'] = True
        publish_object_model['portal_approval_record'] = 'testString'
        publish_object_model['portal_url'] = 'testString'

        state_model = {} # State
        state_model['current'] = 'testString'
        state_model['current_entered'] = "2019-01-01T12:00:00Z"
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = "2019-01-01T12:00:00Z"
        state_model['previous'] = 'testString'

        # Construct a json representation of a CatalogObject model
        catalog_object_model_json = {}
        catalog_object_model_json['id'] = 'testString'
        catalog_object_model_json['name'] = 'testString'
        catalog_object_model_json['_rev'] = 'testString'
        catalog_object_model_json['crn'] = 'testString'
        catalog_object_model_json['url'] = 'testString'
        catalog_object_model_json['parent_id'] = 'testString'
        catalog_object_model_json['label_i18n'] = 'testString'
        catalog_object_model_json['label'] = 'testString'
        catalog_object_model_json['tags'] = ['testString']
        catalog_object_model_json['created'] = "2019-01-01T12:00:00Z"
        catalog_object_model_json['updated'] = "2019-01-01T12:00:00Z"
        catalog_object_model_json['short_description'] = 'testString'
        catalog_object_model_json['short_description_i18n'] = 'testString'
        catalog_object_model_json['kind'] = 'testString'
        catalog_object_model_json['publish'] = publish_object_model
        catalog_object_model_json['state'] = state_model
        catalog_object_model_json['catalog_id'] = 'testString'
        catalog_object_model_json['catalog_name'] = 'testString'
        catalog_object_model_json['data'] = {}

        # Construct a model instance of CatalogObject by calling from_dict on the json representation
        catalog_object_model = CatalogObject.from_dict(catalog_object_model_json)
        assert catalog_object_model != False

        # Construct a model instance of CatalogObject by calling from_dict on the json representation
        catalog_object_model_dict = CatalogObject.from_dict(catalog_object_model_json).__dict__
        catalog_object_model2 = CatalogObject(**catalog_object_model_dict)

        # Verify the model instances are equivalent
        assert catalog_object_model == catalog_object_model2

        # Convert model instance back to dict and verify no loss of data
        catalog_object_model_json2 = catalog_object_model.to_dict()
        assert catalog_object_model_json2 == catalog_object_model_json

class CatalogSearchResultUnitTests():
    """
    Test Class for CatalogSearchResult
    """

    def test_catalog_search_result_serialization(self):
        """
        Test serialization/deserialization for CatalogSearchResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        feature_model = {} # Feature
        feature_model['title'] = 'testString'
        feature_model['description'] = 'testString'

        filter_terms_model = {} # FilterTerms
        filter_terms_model['filter_terms'] = ['testString']

        category_filter_model = {} # CategoryFilter
        category_filter_model['include'] = True
        category_filter_model['filter'] = filter_terms_model

        id_filter_model = {} # IDFilter
        id_filter_model['include'] = filter_terms_model
        id_filter_model['exclude'] = filter_terms_model

        filters_model = {} # Filters
        filters_model['include_all'] = True
        filters_model['category_filters'] = {}
        filters_model['id_filters'] = id_filter_model

        syndication_cluster_model = {} # SyndicationCluster
        syndication_cluster_model['region'] = 'testString'
        syndication_cluster_model['id'] = 'testString'
        syndication_cluster_model['name'] = 'testString'
        syndication_cluster_model['resource_group_name'] = 'testString'
        syndication_cluster_model['type'] = 'testString'
        syndication_cluster_model['namespaces'] = ['testString']
        syndication_cluster_model['all_namespaces'] = True

        syndication_history_model = {} # SyndicationHistory
        syndication_history_model['namespaces'] = ['testString']
        syndication_history_model['clusters'] = [syndication_cluster_model]
        syndication_history_model['last_run'] = "2019-01-01T12:00:00Z"

        syndication_authorization_model = {} # SyndicationAuthorization
        syndication_authorization_model['token'] = 'testString'
        syndication_authorization_model['last_run'] = "2019-01-01T12:00:00Z"

        syndication_resource_model = {} # SyndicationResource
        syndication_resource_model['remove_related_components'] = True
        syndication_resource_model['clusters'] = [syndication_cluster_model]
        syndication_resource_model['history'] = syndication_history_model
        syndication_resource_model['authorization'] = syndication_authorization_model

        catalog_model = {} # Catalog
        catalog_model['id'] = 'testString'
        catalog_model['_rev'] = 'testString'
        catalog_model['label'] = 'testString'
        catalog_model['short_description'] = 'testString'
        catalog_model['catalog_icon_url'] = 'testString'
        catalog_model['tags'] = ['testString']
        catalog_model['url'] = 'testString'
        catalog_model['crn'] = 'testString'
        catalog_model['offerings_url'] = 'testString'
        catalog_model['features'] = [feature_model]
        catalog_model['disabled'] = True
        catalog_model['created'] = "2019-01-01T12:00:00Z"
        catalog_model['updated'] = "2019-01-01T12:00:00Z"
        catalog_model['resource_group_id'] = 'testString'
        catalog_model['owning_account'] = 'testString'
        catalog_model['catalog_filters'] = filters_model
        catalog_model['syndication_settings'] = syndication_resource_model
        catalog_model['kind'] = 'testString'

        # Construct a json representation of a CatalogSearchResult model
        catalog_search_result_model_json = {}
        catalog_search_result_model_json['total_count'] = 38
        catalog_search_result_model_json['resources'] = [catalog_model]

        # Construct a model instance of CatalogSearchResult by calling from_dict on the json representation
        catalog_search_result_model = CatalogSearchResult.from_dict(catalog_search_result_model_json)
        assert catalog_search_result_model != False

        # Construct a model instance of CatalogSearchResult by calling from_dict on the json representation
        catalog_search_result_model_dict = CatalogSearchResult.from_dict(catalog_search_result_model_json).__dict__
        catalog_search_result_model2 = CatalogSearchResult(**catalog_search_result_model_dict)

        # Verify the model instances are equivalent
        assert catalog_search_result_model == catalog_search_result_model2

        # Convert model instance back to dict and verify no loss of data
        catalog_search_result_model_json2 = catalog_search_result_model.to_dict()
        assert catalog_search_result_model_json2 == catalog_search_result_model_json

class CategoryFilterUnitTests():
    """
    Test Class for CategoryFilter
    """

    def test_category_filter_serialization(self):
        """
        Test serialization/deserialization for CategoryFilter
        """

        # Construct dict forms of any model objects needed in order to build this model.

        filter_terms_model = {} # FilterTerms
        filter_terms_model['filter_terms'] = ['testString']

        # Construct a json representation of a CategoryFilter model
        category_filter_model_json = {}
        category_filter_model_json['include'] = True
        category_filter_model_json['filter'] = filter_terms_model

        # Construct a model instance of CategoryFilter by calling from_dict on the json representation
        category_filter_model = CategoryFilter.from_dict(category_filter_model_json)
        assert category_filter_model != False

        # Construct a model instance of CategoryFilter by calling from_dict on the json representation
        category_filter_model_dict = CategoryFilter.from_dict(category_filter_model_json).__dict__
        category_filter_model2 = CategoryFilter(**category_filter_model_dict)

        # Verify the model instances are equivalent
        assert category_filter_model == category_filter_model2

        # Convert model instance back to dict and verify no loss of data
        category_filter_model_json2 = category_filter_model.to_dict()
        assert category_filter_model_json2 == category_filter_model_json

class ClusterInfoUnitTests():
    """
    Test Class for ClusterInfo
    """

    def test_cluster_info_serialization(self):
        """
        Test serialization/deserialization for ClusterInfo
        """

        # Construct a json representation of a ClusterInfo model
        cluster_info_model_json = {}
        cluster_info_model_json['resource_group_id'] = 'testString'
        cluster_info_model_json['resource_group_name'] = 'testString'
        cluster_info_model_json['id'] = 'testString'
        cluster_info_model_json['name'] = 'testString'
        cluster_info_model_json['region'] = 'testString'

        # Construct a model instance of ClusterInfo by calling from_dict on the json representation
        cluster_info_model = ClusterInfo.from_dict(cluster_info_model_json)
        assert cluster_info_model != False

        # Construct a model instance of ClusterInfo by calling from_dict on the json representation
        cluster_info_model_dict = ClusterInfo.from_dict(cluster_info_model_json).__dict__
        cluster_info_model2 = ClusterInfo(**cluster_info_model_dict)

        # Verify the model instances are equivalent
        assert cluster_info_model == cluster_info_model2

        # Convert model instance back to dict and verify no loss of data
        cluster_info_model_json2 = cluster_info_model.to_dict()
        assert cluster_info_model_json2 == cluster_info_model_json

class ConfigurationUnitTests():
    """
    Test Class for Configuration
    """

    def test_configuration_serialization(self):
        """
        Test serialization/deserialization for Configuration
        """

        # Construct a json representation of a Configuration model
        configuration_model_json = {}
        configuration_model_json['key'] = 'testString'
        configuration_model_json['type'] = 'testString'
        configuration_model_json['default_value'] = { 'foo': 'bar' }
        configuration_model_json['value_constraint'] = 'testString'
        configuration_model_json['description'] = 'testString'
        configuration_model_json['required'] = True
        configuration_model_json['options'] = [{ 'foo': 'bar' }]
        configuration_model_json['hidden'] = True

        # Construct a model instance of Configuration by calling from_dict on the json representation
        configuration_model = Configuration.from_dict(configuration_model_json)
        assert configuration_model != False

        # Construct a model instance of Configuration by calling from_dict on the json representation
        configuration_model_dict = Configuration.from_dict(configuration_model_json).__dict__
        configuration_model2 = Configuration(**configuration_model_dict)

        # Verify the model instances are equivalent
        assert configuration_model == configuration_model2

        # Convert model instance back to dict and verify no loss of data
        configuration_model_json2 = configuration_model.to_dict()
        assert configuration_model_json2 == configuration_model_json

class DeployRequestBodySchematicsUnitTests():
    """
    Test Class for DeployRequestBodySchematics
    """

    def test_deploy_request_body_schematics_serialization(self):
        """
        Test serialization/deserialization for DeployRequestBodySchematics
        """

        # Construct a json representation of a DeployRequestBodySchematics model
        deploy_request_body_schematics_model_json = {}
        deploy_request_body_schematics_model_json['name'] = 'testString'
        deploy_request_body_schematics_model_json['description'] = 'testString'
        deploy_request_body_schematics_model_json['tags'] = ['testString']
        deploy_request_body_schematics_model_json['resource_group_id'] = 'testString'

        # Construct a model instance of DeployRequestBodySchematics by calling from_dict on the json representation
        deploy_request_body_schematics_model = DeployRequestBodySchematics.from_dict(deploy_request_body_schematics_model_json)
        assert deploy_request_body_schematics_model != False

        # Construct a model instance of DeployRequestBodySchematics by calling from_dict on the json representation
        deploy_request_body_schematics_model_dict = DeployRequestBodySchematics.from_dict(deploy_request_body_schematics_model_json).__dict__
        deploy_request_body_schematics_model2 = DeployRequestBodySchematics(**deploy_request_body_schematics_model_dict)

        # Verify the model instances are equivalent
        assert deploy_request_body_schematics_model == deploy_request_body_schematics_model2

        # Convert model instance back to dict and verify no loss of data
        deploy_request_body_schematics_model_json2 = deploy_request_body_schematics_model.to_dict()
        assert deploy_request_body_schematics_model_json2 == deploy_request_body_schematics_model_json

class DeploymentUnitTests():
    """
    Test Class for Deployment
    """

    def test_deployment_serialization(self):
        """
        Test serialization/deserialization for Deployment
        """

        # Construct a json representation of a Deployment model
        deployment_model_json = {}
        deployment_model_json['id'] = 'testString'
        deployment_model_json['label'] = 'testString'
        deployment_model_json['name'] = 'testString'
        deployment_model_json['short_description'] = 'testString'
        deployment_model_json['long_description'] = 'testString'
        deployment_model_json['metadata'] = {}
        deployment_model_json['tags'] = ['testString']
        deployment_model_json['created'] = "2019-01-01T12:00:00Z"
        deployment_model_json['updated'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of Deployment by calling from_dict on the json representation
        deployment_model = Deployment.from_dict(deployment_model_json)
        assert deployment_model != False

        # Construct a model instance of Deployment by calling from_dict on the json representation
        deployment_model_dict = Deployment.from_dict(deployment_model_json).__dict__
        deployment_model2 = Deployment(**deployment_model_dict)

        # Verify the model instances are equivalent
        assert deployment_model == deployment_model2

        # Convert model instance back to dict and verify no loss of data
        deployment_model_json2 = deployment_model.to_dict()
        assert deployment_model_json2 == deployment_model_json

class FeatureUnitTests():
    """
    Test Class for Feature
    """

    def test_feature_serialization(self):
        """
        Test serialization/deserialization for Feature
        """

        # Construct a json representation of a Feature model
        feature_model_json = {}
        feature_model_json['title'] = 'testString'
        feature_model_json['description'] = 'testString'

        # Construct a model instance of Feature by calling from_dict on the json representation
        feature_model = Feature.from_dict(feature_model_json)
        assert feature_model != False

        # Construct a model instance of Feature by calling from_dict on the json representation
        feature_model_dict = Feature.from_dict(feature_model_json).__dict__
        feature_model2 = Feature(**feature_model_dict)

        # Verify the model instances are equivalent
        assert feature_model == feature_model2

        # Convert model instance back to dict and verify no loss of data
        feature_model_json2 = feature_model.to_dict()
        assert feature_model_json2 == feature_model_json

class FilterTermsUnitTests():
    """
    Test Class for FilterTerms
    """

    def test_filter_terms_serialization(self):
        """
        Test serialization/deserialization for FilterTerms
        """

        # Construct a json representation of a FilterTerms model
        filter_terms_model_json = {}
        filter_terms_model_json['filter_terms'] = ['testString']

        # Construct a model instance of FilterTerms by calling from_dict on the json representation
        filter_terms_model = FilterTerms.from_dict(filter_terms_model_json)
        assert filter_terms_model != False

        # Construct a model instance of FilterTerms by calling from_dict on the json representation
        filter_terms_model_dict = FilterTerms.from_dict(filter_terms_model_json).__dict__
        filter_terms_model2 = FilterTerms(**filter_terms_model_dict)

        # Verify the model instances are equivalent
        assert filter_terms_model == filter_terms_model2

        # Convert model instance back to dict and verify no loss of data
        filter_terms_model_json2 = filter_terms_model.to_dict()
        assert filter_terms_model_json2 == filter_terms_model_json

class FiltersUnitTests():
    """
    Test Class for Filters
    """

    def test_filters_serialization(self):
        """
        Test serialization/deserialization for Filters
        """

        # Construct dict forms of any model objects needed in order to build this model.

        filter_terms_model = {} # FilterTerms
        filter_terms_model['filter_terms'] = ['testString']

        category_filter_model = {} # CategoryFilter
        category_filter_model['include'] = True
        category_filter_model['filter'] = filter_terms_model

        id_filter_model = {} # IDFilter
        id_filter_model['include'] = filter_terms_model
        id_filter_model['exclude'] = filter_terms_model

        # Construct a json representation of a Filters model
        filters_model_json = {}
        filters_model_json['include_all'] = True
        filters_model_json['category_filters'] = {}
        filters_model_json['id_filters'] = id_filter_model

        # Construct a model instance of Filters by calling from_dict on the json representation
        filters_model = Filters.from_dict(filters_model_json)
        assert filters_model != False

        # Construct a model instance of Filters by calling from_dict on the json representation
        filters_model_dict = Filters.from_dict(filters_model_json).__dict__
        filters_model2 = Filters(**filters_model_dict)

        # Verify the model instances are equivalent
        assert filters_model == filters_model2

        # Convert model instance back to dict and verify no loss of data
        filters_model_json2 = filters_model.to_dict()
        assert filters_model_json2 == filters_model_json

class IDFilterUnitTests():
    """
    Test Class for IDFilter
    """

    def test_id_filter_serialization(self):
        """
        Test serialization/deserialization for IDFilter
        """

        # Construct dict forms of any model objects needed in order to build this model.

        filter_terms_model = {} # FilterTerms
        filter_terms_model['filter_terms'] = ['testString']

        # Construct a json representation of a IDFilter model
        id_filter_model_json = {}
        id_filter_model_json['include'] = filter_terms_model
        id_filter_model_json['exclude'] = filter_terms_model

        # Construct a model instance of IDFilter by calling from_dict on the json representation
        id_filter_model = IDFilter.from_dict(id_filter_model_json)
        assert id_filter_model != False

        # Construct a model instance of IDFilter by calling from_dict on the json representation
        id_filter_model_dict = IDFilter.from_dict(id_filter_model_json).__dict__
        id_filter_model2 = IDFilter(**id_filter_model_dict)

        # Verify the model instances are equivalent
        assert id_filter_model == id_filter_model2

        # Convert model instance back to dict and verify no loss of data
        id_filter_model_json2 = id_filter_model.to_dict()
        assert id_filter_model_json2 == id_filter_model_json

class ImageUnitTests():
    """
    Test Class for Image
    """

    def test_image_serialization(self):
        """
        Test serialization/deserialization for Image
        """

        # Construct a json representation of a Image model
        image_model_json = {}
        image_model_json['image'] = 'testString'

        # Construct a model instance of Image by calling from_dict on the json representation
        image_model = Image.from_dict(image_model_json)
        assert image_model != False

        # Construct a model instance of Image by calling from_dict on the json representation
        image_model_dict = Image.from_dict(image_model_json).__dict__
        image_model2 = Image(**image_model_dict)

        # Verify the model instances are equivalent
        assert image_model == image_model2

        # Convert model instance back to dict and verify no loss of data
        image_model_json2 = image_model.to_dict()
        assert image_model_json2 == image_model_json

class ImageManifestUnitTests():
    """
    Test Class for ImageManifest
    """

    def test_image_manifest_serialization(self):
        """
        Test serialization/deserialization for ImageManifest
        """

        # Construct dict forms of any model objects needed in order to build this model.

        image_model = {} # Image
        image_model['image'] = 'testString'

        # Construct a json representation of a ImageManifest model
        image_manifest_model_json = {}
        image_manifest_model_json['description'] = 'testString'
        image_manifest_model_json['images'] = [image_model]

        # Construct a model instance of ImageManifest by calling from_dict on the json representation
        image_manifest_model = ImageManifest.from_dict(image_manifest_model_json)
        assert image_manifest_model != False

        # Construct a model instance of ImageManifest by calling from_dict on the json representation
        image_manifest_model_dict = ImageManifest.from_dict(image_manifest_model_json).__dict__
        image_manifest_model2 = ImageManifest(**image_manifest_model_dict)

        # Verify the model instances are equivalent
        assert image_manifest_model == image_manifest_model2

        # Convert model instance back to dict and verify no loss of data
        image_manifest_model_json2 = image_manifest_model.to_dict()
        assert image_manifest_model_json2 == image_manifest_model_json

class InstallStatusUnitTests():
    """
    Test Class for InstallStatus
    """

    def test_install_status_serialization(self):
        """
        Test serialization/deserialization for InstallStatus
        """

        # Construct dict forms of any model objects needed in order to build this model.

        install_status_metadata_model = {} # InstallStatusMetadata
        install_status_metadata_model['cluster_id'] = 'testString'
        install_status_metadata_model['region'] = 'testString'
        install_status_metadata_model['namespace'] = 'testString'
        install_status_metadata_model['workspace_id'] = 'testString'
        install_status_metadata_model['workspace_name'] = 'testString'

        install_status_release_model = {} # InstallStatusRelease
        install_status_release_model['deployments'] = [{}]
        install_status_release_model['replicasets'] = [{}]
        install_status_release_model['statefulsets'] = [{}]
        install_status_release_model['pods'] = [{}]
        install_status_release_model['errors'] = [{}]

        install_status_content_mgmt_model = {} # InstallStatusContentMgmt
        install_status_content_mgmt_model['pods'] = [{}]
        install_status_content_mgmt_model['errors'] = [{}]

        # Construct a json representation of a InstallStatus model
        install_status_model_json = {}
        install_status_model_json['metadata'] = install_status_metadata_model
        install_status_model_json['release'] = install_status_release_model
        install_status_model_json['content_mgmt'] = install_status_content_mgmt_model

        # Construct a model instance of InstallStatus by calling from_dict on the json representation
        install_status_model = InstallStatus.from_dict(install_status_model_json)
        assert install_status_model != False

        # Construct a model instance of InstallStatus by calling from_dict on the json representation
        install_status_model_dict = InstallStatus.from_dict(install_status_model_json).__dict__
        install_status_model2 = InstallStatus(**install_status_model_dict)

        # Verify the model instances are equivalent
        assert install_status_model == install_status_model2

        # Convert model instance back to dict and verify no loss of data
        install_status_model_json2 = install_status_model.to_dict()
        assert install_status_model_json2 == install_status_model_json

class InstallStatusContentMgmtUnitTests():
    """
    Test Class for InstallStatusContentMgmt
    """

    def test_install_status_content_mgmt_serialization(self):
        """
        Test serialization/deserialization for InstallStatusContentMgmt
        """

        # Construct a json representation of a InstallStatusContentMgmt model
        install_status_content_mgmt_model_json = {}
        install_status_content_mgmt_model_json['pods'] = [{}]
        install_status_content_mgmt_model_json['errors'] = [{}]

        # Construct a model instance of InstallStatusContentMgmt by calling from_dict on the json representation
        install_status_content_mgmt_model = InstallStatusContentMgmt.from_dict(install_status_content_mgmt_model_json)
        assert install_status_content_mgmt_model != False

        # Construct a model instance of InstallStatusContentMgmt by calling from_dict on the json representation
        install_status_content_mgmt_model_dict = InstallStatusContentMgmt.from_dict(install_status_content_mgmt_model_json).__dict__
        install_status_content_mgmt_model2 = InstallStatusContentMgmt(**install_status_content_mgmt_model_dict)

        # Verify the model instances are equivalent
        assert install_status_content_mgmt_model == install_status_content_mgmt_model2

        # Convert model instance back to dict and verify no loss of data
        install_status_content_mgmt_model_json2 = install_status_content_mgmt_model.to_dict()
        assert install_status_content_mgmt_model_json2 == install_status_content_mgmt_model_json

class InstallStatusMetadataUnitTests():
    """
    Test Class for InstallStatusMetadata
    """

    def test_install_status_metadata_serialization(self):
        """
        Test serialization/deserialization for InstallStatusMetadata
        """

        # Construct a json representation of a InstallStatusMetadata model
        install_status_metadata_model_json = {}
        install_status_metadata_model_json['cluster_id'] = 'testString'
        install_status_metadata_model_json['region'] = 'testString'
        install_status_metadata_model_json['namespace'] = 'testString'
        install_status_metadata_model_json['workspace_id'] = 'testString'
        install_status_metadata_model_json['workspace_name'] = 'testString'

        # Construct a model instance of InstallStatusMetadata by calling from_dict on the json representation
        install_status_metadata_model = InstallStatusMetadata.from_dict(install_status_metadata_model_json)
        assert install_status_metadata_model != False

        # Construct a model instance of InstallStatusMetadata by calling from_dict on the json representation
        install_status_metadata_model_dict = InstallStatusMetadata.from_dict(install_status_metadata_model_json).__dict__
        install_status_metadata_model2 = InstallStatusMetadata(**install_status_metadata_model_dict)

        # Verify the model instances are equivalent
        assert install_status_metadata_model == install_status_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        install_status_metadata_model_json2 = install_status_metadata_model.to_dict()
        assert install_status_metadata_model_json2 == install_status_metadata_model_json

class InstallStatusReleaseUnitTests():
    """
    Test Class for InstallStatusRelease
    """

    def test_install_status_release_serialization(self):
        """
        Test serialization/deserialization for InstallStatusRelease
        """

        # Construct a json representation of a InstallStatusRelease model
        install_status_release_model_json = {}
        install_status_release_model_json['deployments'] = [{}]
        install_status_release_model_json['replicasets'] = [{}]
        install_status_release_model_json['statefulsets'] = [{}]
        install_status_release_model_json['pods'] = [{}]
        install_status_release_model_json['errors'] = [{}]

        # Construct a model instance of InstallStatusRelease by calling from_dict on the json representation
        install_status_release_model = InstallStatusRelease.from_dict(install_status_release_model_json)
        assert install_status_release_model != False

        # Construct a model instance of InstallStatusRelease by calling from_dict on the json representation
        install_status_release_model_dict = InstallStatusRelease.from_dict(install_status_release_model_json).__dict__
        install_status_release_model2 = InstallStatusRelease(**install_status_release_model_dict)

        # Verify the model instances are equivalent
        assert install_status_release_model == install_status_release_model2

        # Convert model instance back to dict and verify no loss of data
        install_status_release_model_json2 = install_status_release_model.to_dict()
        assert install_status_release_model_json2 == install_status_release_model_json

class KindUnitTests():
    """
    Test Class for Kind
    """

    def test_kind_serialization(self):
        """
        Test serialization/deserialization for Kind
        """

        # Construct dict forms of any model objects needed in order to build this model.

        feature_model = {} # Feature
        feature_model['title'] = 'testString'
        feature_model['description'] = 'testString'

        configuration_model = {} # Configuration
        configuration_model['key'] = 'testString'
        configuration_model['type'] = 'testString'
        configuration_model['default_value'] = { 'foo': 'bar' }
        configuration_model['value_constraint'] = 'testString'
        configuration_model['description'] = 'testString'
        configuration_model['required'] = True
        configuration_model['options'] = [{ 'foo': 'bar' }]
        configuration_model['hidden'] = True

        validation_model = {} # Validation
        validation_model['validated'] = "2019-01-01T12:00:00Z"
        validation_model['requested'] = "2019-01-01T12:00:00Z"
        validation_model['state'] = 'testString'
        validation_model['last_operation'] = 'testString'
        validation_model['target'] = {}

        resource_model = {} # Resource
        resource_model['type'] = 'mem'
        resource_model['value'] = { 'foo': 'bar' }

        script_model = {} # Script
        script_model['instructions'] = 'testString'
        script_model['script'] = 'testString'
        script_model['script_permission'] = 'testString'
        script_model['delete_script'] = 'testString'
        script_model['scope'] = 'testString'

        version_entitlement_model = {} # VersionEntitlement
        version_entitlement_model['provider_name'] = 'testString'
        version_entitlement_model['provider_id'] = 'testString'
        version_entitlement_model['product_id'] = 'testString'
        version_entitlement_model['part_numbers'] = ['testString']
        version_entitlement_model['image_repo_name'] = 'testString'

        license_model = {} # License
        license_model['id'] = 'testString'
        license_model['name'] = 'testString'
        license_model['type'] = 'testString'
        license_model['url'] = 'testString'
        license_model['description'] = 'testString'

        state_model = {} # State
        state_model['current'] = 'testString'
        state_model['current_entered'] = "2019-01-01T12:00:00Z"
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = "2019-01-01T12:00:00Z"
        state_model['previous'] = 'testString'

        version_model = {} # Version
        version_model['id'] = 'testString'
        version_model['_rev'] = 'testString'
        version_model['crn'] = 'testString'
        version_model['version'] = 'testString'
        version_model['sha'] = 'testString'
        version_model['created'] = "2019-01-01T12:00:00Z"
        version_model['updated'] = "2019-01-01T12:00:00Z"
        version_model['offering_id'] = 'testString'
        version_model['catalog_id'] = 'testString'
        version_model['kind_id'] = 'testString'
        version_model['tags'] = ['testString']
        version_model['repo_url'] = 'testString'
        version_model['source_url'] = 'testString'
        version_model['tgz_url'] = 'testString'
        version_model['configuration'] = [configuration_model]
        version_model['metadata'] = {}
        version_model['validation'] = validation_model
        version_model['required_resources'] = [resource_model]
        version_model['single_instance'] = True
        version_model['install'] = script_model
        version_model['pre_install'] = [script_model]
        version_model['entitlement'] = version_entitlement_model
        version_model['licenses'] = [license_model]
        version_model['image_manifest_url'] = 'testString'
        version_model['deprecated'] = True
        version_model['package_version'] = 'testString'
        version_model['state'] = state_model
        version_model['version_locator'] = 'testString'
        version_model['console_url'] = 'testString'
        version_model['long_description'] = 'testString'
        version_model['whitelisted_accounts'] = ['testString']

        deployment_model = {} # Deployment
        deployment_model['id'] = 'testString'
        deployment_model['label'] = 'testString'
        deployment_model['name'] = 'testString'
        deployment_model['short_description'] = 'testString'
        deployment_model['long_description'] = 'testString'
        deployment_model['metadata'] = {}
        deployment_model['tags'] = ['testString']
        deployment_model['created'] = "2019-01-01T12:00:00Z"
        deployment_model['updated'] = "2019-01-01T12:00:00Z"

        plan_model = {} # Plan
        plan_model['id'] = 'testString'
        plan_model['label'] = 'testString'
        plan_model['name'] = 'testString'
        plan_model['short_description'] = 'testString'
        plan_model['long_description'] = 'testString'
        plan_model['metadata'] = {}
        plan_model['tags'] = ['testString']
        plan_model['additional_features'] = [feature_model]
        plan_model['created'] = "2019-01-01T12:00:00Z"
        plan_model['updated'] = "2019-01-01T12:00:00Z"
        plan_model['deployments'] = [deployment_model]

        # Construct a json representation of a Kind model
        kind_model_json = {}
        kind_model_json['id'] = 'testString'
        kind_model_json['format_kind'] = 'testString'
        kind_model_json['target_kind'] = 'testString'
        kind_model_json['metadata'] = {}
        kind_model_json['install_description'] = 'testString'
        kind_model_json['tags'] = ['testString']
        kind_model_json['additional_features'] = [feature_model]
        kind_model_json['created'] = "2019-01-01T12:00:00Z"
        kind_model_json['updated'] = "2019-01-01T12:00:00Z"
        kind_model_json['versions'] = [version_model]
        kind_model_json['plans'] = [plan_model]

        # Construct a model instance of Kind by calling from_dict on the json representation
        kind_model = Kind.from_dict(kind_model_json)
        assert kind_model != False

        # Construct a model instance of Kind by calling from_dict on the json representation
        kind_model_dict = Kind.from_dict(kind_model_json).__dict__
        kind_model2 = Kind(**kind_model_dict)

        # Verify the model instances are equivalent
        assert kind_model == kind_model2

        # Convert model instance back to dict and verify no loss of data
        kind_model_json2 = kind_model.to_dict()
        assert kind_model_json2 == kind_model_json

class LicenseUnitTests():
    """
    Test Class for License
    """

    def test_license_serialization(self):
        """
        Test serialization/deserialization for License
        """

        # Construct a json representation of a License model
        license_model_json = {}
        license_model_json['id'] = 'testString'
        license_model_json['name'] = 'testString'
        license_model_json['type'] = 'testString'
        license_model_json['url'] = 'testString'
        license_model_json['description'] = 'testString'

        # Construct a model instance of License by calling from_dict on the json representation
        license_model = License.from_dict(license_model_json)
        assert license_model != False

        # Construct a model instance of License by calling from_dict on the json representation
        license_model_dict = License.from_dict(license_model_json).__dict__
        license_model2 = License(**license_model_dict)

        # Verify the model instances are equivalent
        assert license_model == license_model2

        # Convert model instance back to dict and verify no loss of data
        license_model_json2 = license_model.to_dict()
        assert license_model_json2 == license_model_json

class NamespaceSearchResultUnitTests():
    """
    Test Class for NamespaceSearchResult
    """

    def test_namespace_search_result_serialization(self):
        """
        Test serialization/deserialization for NamespaceSearchResult
        """

        # Construct a json representation of a NamespaceSearchResult model
        namespace_search_result_model_json = {}
        namespace_search_result_model_json['offset'] = 38
        namespace_search_result_model_json['limit'] = 38
        namespace_search_result_model_json['total_count'] = 38
        namespace_search_result_model_json['resource_count'] = 38
        namespace_search_result_model_json['first'] = 'testString'
        namespace_search_result_model_json['last'] = 'testString'
        namespace_search_result_model_json['prev'] = 'testString'
        namespace_search_result_model_json['next'] = 'testString'
        namespace_search_result_model_json['resources'] = ['testString']

        # Construct a model instance of NamespaceSearchResult by calling from_dict on the json representation
        namespace_search_result_model = NamespaceSearchResult.from_dict(namespace_search_result_model_json)
        assert namespace_search_result_model != False

        # Construct a model instance of NamespaceSearchResult by calling from_dict on the json representation
        namespace_search_result_model_dict = NamespaceSearchResult.from_dict(namespace_search_result_model_json).__dict__
        namespace_search_result_model2 = NamespaceSearchResult(**namespace_search_result_model_dict)

        # Verify the model instances are equivalent
        assert namespace_search_result_model == namespace_search_result_model2

        # Convert model instance back to dict and verify no loss of data
        namespace_search_result_model_json2 = namespace_search_result_model.to_dict()
        assert namespace_search_result_model_json2 == namespace_search_result_model_json

class ObjectAccessUnitTests():
    """
    Test Class for ObjectAccess
    """

    def test_object_access_serialization(self):
        """
        Test serialization/deserialization for ObjectAccess
        """

        # Construct a json representation of a ObjectAccess model
        object_access_model_json = {}
        object_access_model_json['id'] = 'testString'
        object_access_model_json['account'] = 'testString'
        object_access_model_json['catalog_id'] = 'testString'
        object_access_model_json['target_id'] = 'testString'
        object_access_model_json['create'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of ObjectAccess by calling from_dict on the json representation
        object_access_model = ObjectAccess.from_dict(object_access_model_json)
        assert object_access_model != False

        # Construct a model instance of ObjectAccess by calling from_dict on the json representation
        object_access_model_dict = ObjectAccess.from_dict(object_access_model_json).__dict__
        object_access_model2 = ObjectAccess(**object_access_model_dict)

        # Verify the model instances are equivalent
        assert object_access_model == object_access_model2

        # Convert model instance back to dict and verify no loss of data
        object_access_model_json2 = object_access_model.to_dict()
        assert object_access_model_json2 == object_access_model_json

class ObjectAccessListResultUnitTests():
    """
    Test Class for ObjectAccessListResult
    """

    def test_object_access_list_result_serialization(self):
        """
        Test serialization/deserialization for ObjectAccessListResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        object_access_model = {} # ObjectAccess
        object_access_model['id'] = 'testString'
        object_access_model['account'] = 'testString'
        object_access_model['catalog_id'] = 'testString'
        object_access_model['target_id'] = 'testString'
        object_access_model['create'] = "2019-01-01T12:00:00Z"

        # Construct a json representation of a ObjectAccessListResult model
        object_access_list_result_model_json = {}
        object_access_list_result_model_json['offset'] = 38
        object_access_list_result_model_json['limit'] = 38
        object_access_list_result_model_json['total_count'] = 38
        object_access_list_result_model_json['resource_count'] = 38
        object_access_list_result_model_json['first'] = 'testString'
        object_access_list_result_model_json['last'] = 'testString'
        object_access_list_result_model_json['prev'] = 'testString'
        object_access_list_result_model_json['next'] = 'testString'
        object_access_list_result_model_json['resources'] = [object_access_model]

        # Construct a model instance of ObjectAccessListResult by calling from_dict on the json representation
        object_access_list_result_model = ObjectAccessListResult.from_dict(object_access_list_result_model_json)
        assert object_access_list_result_model != False

        # Construct a model instance of ObjectAccessListResult by calling from_dict on the json representation
        object_access_list_result_model_dict = ObjectAccessListResult.from_dict(object_access_list_result_model_json).__dict__
        object_access_list_result_model2 = ObjectAccessListResult(**object_access_list_result_model_dict)

        # Verify the model instances are equivalent
        assert object_access_list_result_model == object_access_list_result_model2

        # Convert model instance back to dict and verify no loss of data
        object_access_list_result_model_json2 = object_access_list_result_model.to_dict()
        assert object_access_list_result_model_json2 == object_access_list_result_model_json

class ObjectListResultUnitTests():
    """
    Test Class for ObjectListResult
    """

    def test_object_list_result_serialization(self):
        """
        Test serialization/deserialization for ObjectListResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        publish_object_model = {} # PublishObject
        publish_object_model['permit_ibm_public_publish'] = True
        publish_object_model['ibm_approved'] = True
        publish_object_model['public_approved'] = True
        publish_object_model['portal_approval_record'] = 'testString'
        publish_object_model['portal_url'] = 'testString'

        state_model = {} # State
        state_model['current'] = 'testString'
        state_model['current_entered'] = "2019-01-01T12:00:00Z"
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = "2019-01-01T12:00:00Z"
        state_model['previous'] = 'testString'

        catalog_object_model = {} # CatalogObject
        catalog_object_model['id'] = 'testString'
        catalog_object_model['name'] = 'testString'
        catalog_object_model['_rev'] = 'testString'
        catalog_object_model['crn'] = 'testString'
        catalog_object_model['url'] = 'testString'
        catalog_object_model['parent_id'] = 'testString'
        catalog_object_model['label_i18n'] = 'testString'
        catalog_object_model['label'] = 'testString'
        catalog_object_model['tags'] = ['testString']
        catalog_object_model['created'] = "2019-01-01T12:00:00Z"
        catalog_object_model['updated'] = "2019-01-01T12:00:00Z"
        catalog_object_model['short_description'] = 'testString'
        catalog_object_model['short_description_i18n'] = 'testString'
        catalog_object_model['kind'] = 'testString'
        catalog_object_model['publish'] = publish_object_model
        catalog_object_model['state'] = state_model
        catalog_object_model['catalog_id'] = 'testString'
        catalog_object_model['catalog_name'] = 'testString'
        catalog_object_model['data'] = {}

        # Construct a json representation of a ObjectListResult model
        object_list_result_model_json = {}
        object_list_result_model_json['offset'] = 38
        object_list_result_model_json['limit'] = 38
        object_list_result_model_json['total_count'] = 38
        object_list_result_model_json['resource_count'] = 38
        object_list_result_model_json['first'] = 'testString'
        object_list_result_model_json['last'] = 'testString'
        object_list_result_model_json['prev'] = 'testString'
        object_list_result_model_json['next'] = 'testString'
        object_list_result_model_json['resources'] = [catalog_object_model]

        # Construct a model instance of ObjectListResult by calling from_dict on the json representation
        object_list_result_model = ObjectListResult.from_dict(object_list_result_model_json)
        assert object_list_result_model != False

        # Construct a model instance of ObjectListResult by calling from_dict on the json representation
        object_list_result_model_dict = ObjectListResult.from_dict(object_list_result_model_json).__dict__
        object_list_result_model2 = ObjectListResult(**object_list_result_model_dict)

        # Verify the model instances are equivalent
        assert object_list_result_model == object_list_result_model2

        # Convert model instance back to dict and verify no loss of data
        object_list_result_model_json2 = object_list_result_model.to_dict()
        assert object_list_result_model_json2 == object_list_result_model_json

class ObjectSearchResultUnitTests():
    """
    Test Class for ObjectSearchResult
    """

    def test_object_search_result_serialization(self):
        """
        Test serialization/deserialization for ObjectSearchResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        publish_object_model = {} # PublishObject
        publish_object_model['permit_ibm_public_publish'] = True
        publish_object_model['ibm_approved'] = True
        publish_object_model['public_approved'] = True
        publish_object_model['portal_approval_record'] = 'testString'
        publish_object_model['portal_url'] = 'testString'

        state_model = {} # State
        state_model['current'] = 'testString'
        state_model['current_entered'] = "2019-01-01T12:00:00Z"
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = "2019-01-01T12:00:00Z"
        state_model['previous'] = 'testString'

        catalog_object_model = {} # CatalogObject
        catalog_object_model['id'] = 'testString'
        catalog_object_model['name'] = 'testString'
        catalog_object_model['_rev'] = 'testString'
        catalog_object_model['crn'] = 'testString'
        catalog_object_model['url'] = 'testString'
        catalog_object_model['parent_id'] = 'testString'
        catalog_object_model['label_i18n'] = 'testString'
        catalog_object_model['label'] = 'testString'
        catalog_object_model['tags'] = ['testString']
        catalog_object_model['created'] = "2019-01-01T12:00:00Z"
        catalog_object_model['updated'] = "2019-01-01T12:00:00Z"
        catalog_object_model['short_description'] = 'testString'
        catalog_object_model['short_description_i18n'] = 'testString'
        catalog_object_model['kind'] = 'testString'
        catalog_object_model['publish'] = publish_object_model
        catalog_object_model['state'] = state_model
        catalog_object_model['catalog_id'] = 'testString'
        catalog_object_model['catalog_name'] = 'testString'
        catalog_object_model['data'] = {}

        # Construct a json representation of a ObjectSearchResult model
        object_search_result_model_json = {}
        object_search_result_model_json['offset'] = 38
        object_search_result_model_json['limit'] = 38
        object_search_result_model_json['total_count'] = 38
        object_search_result_model_json['resource_count'] = 38
        object_search_result_model_json['first'] = 'testString'
        object_search_result_model_json['last'] = 'testString'
        object_search_result_model_json['prev'] = 'testString'
        object_search_result_model_json['next'] = 'testString'
        object_search_result_model_json['resources'] = [catalog_object_model]

        # Construct a model instance of ObjectSearchResult by calling from_dict on the json representation
        object_search_result_model = ObjectSearchResult.from_dict(object_search_result_model_json)
        assert object_search_result_model != False

        # Construct a model instance of ObjectSearchResult by calling from_dict on the json representation
        object_search_result_model_dict = ObjectSearchResult.from_dict(object_search_result_model_json).__dict__
        object_search_result_model2 = ObjectSearchResult(**object_search_result_model_dict)

        # Verify the model instances are equivalent
        assert object_search_result_model == object_search_result_model2

        # Convert model instance back to dict and verify no loss of data
        object_search_result_model_json2 = object_search_result_model.to_dict()
        assert object_search_result_model_json2 == object_search_result_model_json

class OfferingUnitTests():
    """
    Test Class for Offering
    """

    def test_offering_serialization(self):
        """
        Test serialization/deserialization for Offering
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rating_model = {} # Rating
        rating_model['one_star_count'] = 38
        rating_model['two_star_count'] = 38
        rating_model['three_star_count'] = 38
        rating_model['four_star_count'] = 38

        feature_model = {} # Feature
        feature_model['title'] = 'testString'
        feature_model['description'] = 'testString'

        configuration_model = {} # Configuration
        configuration_model['key'] = 'testString'
        configuration_model['type'] = 'testString'
        configuration_model['default_value'] = { 'foo': 'bar' }
        configuration_model['value_constraint'] = 'testString'
        configuration_model['description'] = 'testString'
        configuration_model['required'] = True
        configuration_model['options'] = [{ 'foo': 'bar' }]
        configuration_model['hidden'] = True

        validation_model = {} # Validation
        validation_model['validated'] = "2019-01-01T12:00:00Z"
        validation_model['requested'] = "2019-01-01T12:00:00Z"
        validation_model['state'] = 'testString'
        validation_model['last_operation'] = 'testString'
        validation_model['target'] = {}

        resource_model = {} # Resource
        resource_model['type'] = 'mem'
        resource_model['value'] = { 'foo': 'bar' }

        script_model = {} # Script
        script_model['instructions'] = 'testString'
        script_model['script'] = 'testString'
        script_model['script_permission'] = 'testString'
        script_model['delete_script'] = 'testString'
        script_model['scope'] = 'testString'

        version_entitlement_model = {} # VersionEntitlement
        version_entitlement_model['provider_name'] = 'testString'
        version_entitlement_model['provider_id'] = 'testString'
        version_entitlement_model['product_id'] = 'testString'
        version_entitlement_model['part_numbers'] = ['testString']
        version_entitlement_model['image_repo_name'] = 'testString'

        license_model = {} # License
        license_model['id'] = 'testString'
        license_model['name'] = 'testString'
        license_model['type'] = 'testString'
        license_model['url'] = 'testString'
        license_model['description'] = 'testString'

        state_model = {} # State
        state_model['current'] = 'testString'
        state_model['current_entered'] = "2019-01-01T12:00:00Z"
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = "2019-01-01T12:00:00Z"
        state_model['previous'] = 'testString'

        version_model = {} # Version
        version_model['id'] = 'testString'
        version_model['_rev'] = 'testString'
        version_model['crn'] = 'testString'
        version_model['version'] = 'testString'
        version_model['sha'] = 'testString'
        version_model['created'] = "2019-01-01T12:00:00Z"
        version_model['updated'] = "2019-01-01T12:00:00Z"
        version_model['offering_id'] = 'testString'
        version_model['catalog_id'] = 'testString'
        version_model['kind_id'] = 'testString'
        version_model['tags'] = ['testString']
        version_model['repo_url'] = 'testString'
        version_model['source_url'] = 'testString'
        version_model['tgz_url'] = 'testString'
        version_model['configuration'] = [configuration_model]
        version_model['metadata'] = {}
        version_model['validation'] = validation_model
        version_model['required_resources'] = [resource_model]
        version_model['single_instance'] = True
        version_model['install'] = script_model
        version_model['pre_install'] = [script_model]
        version_model['entitlement'] = version_entitlement_model
        version_model['licenses'] = [license_model]
        version_model['image_manifest_url'] = 'testString'
        version_model['deprecated'] = True
        version_model['package_version'] = 'testString'
        version_model['state'] = state_model
        version_model['version_locator'] = 'testString'
        version_model['console_url'] = 'testString'
        version_model['long_description'] = 'testString'
        version_model['whitelisted_accounts'] = ['testString']

        deployment_model = {} # Deployment
        deployment_model['id'] = 'testString'
        deployment_model['label'] = 'testString'
        deployment_model['name'] = 'testString'
        deployment_model['short_description'] = 'testString'
        deployment_model['long_description'] = 'testString'
        deployment_model['metadata'] = {}
        deployment_model['tags'] = ['testString']
        deployment_model['created'] = "2019-01-01T12:00:00Z"
        deployment_model['updated'] = "2019-01-01T12:00:00Z"

        plan_model = {} # Plan
        plan_model['id'] = 'testString'
        plan_model['label'] = 'testString'
        plan_model['name'] = 'testString'
        plan_model['short_description'] = 'testString'
        plan_model['long_description'] = 'testString'
        plan_model['metadata'] = {}
        plan_model['tags'] = ['testString']
        plan_model['additional_features'] = [feature_model]
        plan_model['created'] = "2019-01-01T12:00:00Z"
        plan_model['updated'] = "2019-01-01T12:00:00Z"
        plan_model['deployments'] = [deployment_model]

        kind_model = {} # Kind
        kind_model['id'] = 'testString'
        kind_model['format_kind'] = 'testString'
        kind_model['target_kind'] = 'testString'
        kind_model['metadata'] = {}
        kind_model['install_description'] = 'testString'
        kind_model['tags'] = ['testString']
        kind_model['additional_features'] = [feature_model]
        kind_model['created'] = "2019-01-01T12:00:00Z"
        kind_model['updated'] = "2019-01-01T12:00:00Z"
        kind_model['versions'] = [version_model]
        kind_model['plans'] = [plan_model]

        repo_info_model = {} # RepoInfo
        repo_info_model['token'] = 'testString'
        repo_info_model['type'] = 'testString'

        # Construct a json representation of a Offering model
        offering_model_json = {}
        offering_model_json['id'] = 'testString'
        offering_model_json['_rev'] = 'testString'
        offering_model_json['url'] = 'testString'
        offering_model_json['crn'] = 'testString'
        offering_model_json['label'] = 'testString'
        offering_model_json['name'] = 'testString'
        offering_model_json['offering_icon_url'] = 'testString'
        offering_model_json['offering_docs_url'] = 'testString'
        offering_model_json['offering_support_url'] = 'testString'
        offering_model_json['tags'] = ['testString']
        offering_model_json['keywords'] = ['testString']
        offering_model_json['rating'] = rating_model
        offering_model_json['created'] = "2019-01-01T12:00:00Z"
        offering_model_json['updated'] = "2019-01-01T12:00:00Z"
        offering_model_json['short_description'] = 'testString'
        offering_model_json['long_description'] = 'testString'
        offering_model_json['features'] = [feature_model]
        offering_model_json['kinds'] = [kind_model]
        offering_model_json['permit_request_ibm_public_publish'] = True
        offering_model_json['ibm_publish_approved'] = True
        offering_model_json['public_publish_approved'] = True
        offering_model_json['public_original_crn'] = 'testString'
        offering_model_json['publish_public_crn'] = 'testString'
        offering_model_json['portal_approval_record'] = 'testString'
        offering_model_json['portal_ui_url'] = 'testString'
        offering_model_json['catalog_id'] = 'testString'
        offering_model_json['catalog_name'] = 'testString'
        offering_model_json['metadata'] = {}
        offering_model_json['disclaimer'] = 'testString'
        offering_model_json['hidden'] = True
        offering_model_json['provider'] = 'testString'
        offering_model_json['repo_info'] = repo_info_model

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

class OfferingInstanceUnitTests():
    """
    Test Class for OfferingInstance
    """

    def test_offering_instance_serialization(self):
        """
        Test serialization/deserialization for OfferingInstance
        """

        # Construct dict forms of any model objects needed in order to build this model.

        offering_instance_last_operation_model = {} # OfferingInstanceLastOperation
        offering_instance_last_operation_model['operation'] = 'testString'
        offering_instance_last_operation_model['state'] = 'testString'
        offering_instance_last_operation_model['message'] = 'testString'
        offering_instance_last_operation_model['transaction_id'] = 'testString'
        offering_instance_last_operation_model['updated'] = 'testString'

        # Construct a json representation of a OfferingInstance model
        offering_instance_model_json = {}
        offering_instance_model_json['id'] = 'testString'
        offering_instance_model_json['_rev'] = 'testString'
        offering_instance_model_json['url'] = 'testString'
        offering_instance_model_json['crn'] = 'testString'
        offering_instance_model_json['label'] = 'testString'
        offering_instance_model_json['catalog_id'] = 'testString'
        offering_instance_model_json['offering_id'] = 'testString'
        offering_instance_model_json['kind_format'] = 'testString'
        offering_instance_model_json['version'] = 'testString'
        offering_instance_model_json['cluster_id'] = 'testString'
        offering_instance_model_json['cluster_region'] = 'testString'
        offering_instance_model_json['cluster_namespaces'] = ['testString']
        offering_instance_model_json['cluster_all_namespaces'] = True
        offering_instance_model_json['schematics_workspace_id'] = 'testString'
        offering_instance_model_json['resource_group_id'] = 'testString'
        offering_instance_model_json['install_plan'] = 'testString'
        offering_instance_model_json['channel'] = 'testString'
        offering_instance_model_json['metadata'] = {}
        offering_instance_model_json['last_operation'] = offering_instance_last_operation_model

        # Construct a model instance of OfferingInstance by calling from_dict on the json representation
        offering_instance_model = OfferingInstance.from_dict(offering_instance_model_json)
        assert offering_instance_model != False

        # Construct a model instance of OfferingInstance by calling from_dict on the json representation
        offering_instance_model_dict = OfferingInstance.from_dict(offering_instance_model_json).__dict__
        offering_instance_model2 = OfferingInstance(**offering_instance_model_dict)

        # Verify the model instances are equivalent
        assert offering_instance_model == offering_instance_model2

        # Convert model instance back to dict and verify no loss of data
        offering_instance_model_json2 = offering_instance_model.to_dict()
        assert offering_instance_model_json2 == offering_instance_model_json

class OfferingInstanceLastOperationUnitTests():
    """
    Test Class for OfferingInstanceLastOperation
    """

    def test_offering_instance_last_operation_serialization(self):
        """
        Test serialization/deserialization for OfferingInstanceLastOperation
        """

        # Construct a json representation of a OfferingInstanceLastOperation model
        offering_instance_last_operation_model_json = {}
        offering_instance_last_operation_model_json['operation'] = 'testString'
        offering_instance_last_operation_model_json['state'] = 'testString'
        offering_instance_last_operation_model_json['message'] = 'testString'
        offering_instance_last_operation_model_json['transaction_id'] = 'testString'
        offering_instance_last_operation_model_json['updated'] = 'testString'

        # Construct a model instance of OfferingInstanceLastOperation by calling from_dict on the json representation
        offering_instance_last_operation_model = OfferingInstanceLastOperation.from_dict(offering_instance_last_operation_model_json)
        assert offering_instance_last_operation_model != False

        # Construct a model instance of OfferingInstanceLastOperation by calling from_dict on the json representation
        offering_instance_last_operation_model_dict = OfferingInstanceLastOperation.from_dict(offering_instance_last_operation_model_json).__dict__
        offering_instance_last_operation_model2 = OfferingInstanceLastOperation(**offering_instance_last_operation_model_dict)

        # Verify the model instances are equivalent
        assert offering_instance_last_operation_model == offering_instance_last_operation_model2

        # Convert model instance back to dict and verify no loss of data
        offering_instance_last_operation_model_json2 = offering_instance_last_operation_model.to_dict()
        assert offering_instance_last_operation_model_json2 == offering_instance_last_operation_model_json

class OfferingSearchResultUnitTests():
    """
    Test Class for OfferingSearchResult
    """

    def test_offering_search_result_serialization(self):
        """
        Test serialization/deserialization for OfferingSearchResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rating_model = {} # Rating
        rating_model['one_star_count'] = 38
        rating_model['two_star_count'] = 38
        rating_model['three_star_count'] = 38
        rating_model['four_star_count'] = 38

        feature_model = {} # Feature
        feature_model['title'] = 'testString'
        feature_model['description'] = 'testString'

        configuration_model = {} # Configuration
        configuration_model['key'] = 'testString'
        configuration_model['type'] = 'testString'
        configuration_model['default_value'] = { 'foo': 'bar' }
        configuration_model['value_constraint'] = 'testString'
        configuration_model['description'] = 'testString'
        configuration_model['required'] = True
        configuration_model['options'] = [{ 'foo': 'bar' }]
        configuration_model['hidden'] = True

        validation_model = {} # Validation
        validation_model['validated'] = "2019-01-01T12:00:00Z"
        validation_model['requested'] = "2019-01-01T12:00:00Z"
        validation_model['state'] = 'testString'
        validation_model['last_operation'] = 'testString'
        validation_model['target'] = {}

        resource_model = {} # Resource
        resource_model['type'] = 'mem'
        resource_model['value'] = { 'foo': 'bar' }

        script_model = {} # Script
        script_model['instructions'] = 'testString'
        script_model['script'] = 'testString'
        script_model['script_permission'] = 'testString'
        script_model['delete_script'] = 'testString'
        script_model['scope'] = 'testString'

        version_entitlement_model = {} # VersionEntitlement
        version_entitlement_model['provider_name'] = 'testString'
        version_entitlement_model['provider_id'] = 'testString'
        version_entitlement_model['product_id'] = 'testString'
        version_entitlement_model['part_numbers'] = ['testString']
        version_entitlement_model['image_repo_name'] = 'testString'

        license_model = {} # License
        license_model['id'] = 'testString'
        license_model['name'] = 'testString'
        license_model['type'] = 'testString'
        license_model['url'] = 'testString'
        license_model['description'] = 'testString'

        state_model = {} # State
        state_model['current'] = 'testString'
        state_model['current_entered'] = "2019-01-01T12:00:00Z"
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = "2019-01-01T12:00:00Z"
        state_model['previous'] = 'testString'

        version_model = {} # Version
        version_model['id'] = 'testString'
        version_model['_rev'] = 'testString'
        version_model['crn'] = 'testString'
        version_model['version'] = 'testString'
        version_model['sha'] = 'testString'
        version_model['created'] = "2019-01-01T12:00:00Z"
        version_model['updated'] = "2019-01-01T12:00:00Z"
        version_model['offering_id'] = 'testString'
        version_model['catalog_id'] = 'testString'
        version_model['kind_id'] = 'testString'
        version_model['tags'] = ['testString']
        version_model['repo_url'] = 'testString'
        version_model['source_url'] = 'testString'
        version_model['tgz_url'] = 'testString'
        version_model['configuration'] = [configuration_model]
        version_model['metadata'] = {}
        version_model['validation'] = validation_model
        version_model['required_resources'] = [resource_model]
        version_model['single_instance'] = True
        version_model['install'] = script_model
        version_model['pre_install'] = [script_model]
        version_model['entitlement'] = version_entitlement_model
        version_model['licenses'] = [license_model]
        version_model['image_manifest_url'] = 'testString'
        version_model['deprecated'] = True
        version_model['package_version'] = 'testString'
        version_model['state'] = state_model
        version_model['version_locator'] = 'testString'
        version_model['console_url'] = 'testString'
        version_model['long_description'] = 'testString'
        version_model['whitelisted_accounts'] = ['testString']

        deployment_model = {} # Deployment
        deployment_model['id'] = 'testString'
        deployment_model['label'] = 'testString'
        deployment_model['name'] = 'testString'
        deployment_model['short_description'] = 'testString'
        deployment_model['long_description'] = 'testString'
        deployment_model['metadata'] = {}
        deployment_model['tags'] = ['testString']
        deployment_model['created'] = "2019-01-01T12:00:00Z"
        deployment_model['updated'] = "2019-01-01T12:00:00Z"

        plan_model = {} # Plan
        plan_model['id'] = 'testString'
        plan_model['label'] = 'testString'
        plan_model['name'] = 'testString'
        plan_model['short_description'] = 'testString'
        plan_model['long_description'] = 'testString'
        plan_model['metadata'] = {}
        plan_model['tags'] = ['testString']
        plan_model['additional_features'] = [feature_model]
        plan_model['created'] = "2019-01-01T12:00:00Z"
        plan_model['updated'] = "2019-01-01T12:00:00Z"
        plan_model['deployments'] = [deployment_model]

        kind_model = {} # Kind
        kind_model['id'] = 'testString'
        kind_model['format_kind'] = 'testString'
        kind_model['target_kind'] = 'testString'
        kind_model['metadata'] = {}
        kind_model['install_description'] = 'testString'
        kind_model['tags'] = ['testString']
        kind_model['additional_features'] = [feature_model]
        kind_model['created'] = "2019-01-01T12:00:00Z"
        kind_model['updated'] = "2019-01-01T12:00:00Z"
        kind_model['versions'] = [version_model]
        kind_model['plans'] = [plan_model]

        repo_info_model = {} # RepoInfo
        repo_info_model['token'] = 'testString'
        repo_info_model['type'] = 'testString'

        offering_model = {} # Offering
        offering_model['id'] = 'testString'
        offering_model['_rev'] = 'testString'
        offering_model['url'] = 'testString'
        offering_model['crn'] = 'testString'
        offering_model['label'] = 'testString'
        offering_model['name'] = 'testString'
        offering_model['offering_icon_url'] = 'testString'
        offering_model['offering_docs_url'] = 'testString'
        offering_model['offering_support_url'] = 'testString'
        offering_model['tags'] = ['testString']
        offering_model['keywords'] = ['testString']
        offering_model['rating'] = rating_model
        offering_model['created'] = "2019-01-01T12:00:00Z"
        offering_model['updated'] = "2019-01-01T12:00:00Z"
        offering_model['short_description'] = 'testString'
        offering_model['long_description'] = 'testString'
        offering_model['features'] = [feature_model]
        offering_model['kinds'] = [kind_model]
        offering_model['permit_request_ibm_public_publish'] = True
        offering_model['ibm_publish_approved'] = True
        offering_model['public_publish_approved'] = True
        offering_model['public_original_crn'] = 'testString'
        offering_model['publish_public_crn'] = 'testString'
        offering_model['portal_approval_record'] = 'testString'
        offering_model['portal_ui_url'] = 'testString'
        offering_model['catalog_id'] = 'testString'
        offering_model['catalog_name'] = 'testString'
        offering_model['metadata'] = {}
        offering_model['disclaimer'] = 'testString'
        offering_model['hidden'] = True
        offering_model['provider'] = 'testString'
        offering_model['repo_info'] = repo_info_model

        # Construct a json representation of a OfferingSearchResult model
        offering_search_result_model_json = {}
        offering_search_result_model_json['offset'] = 38
        offering_search_result_model_json['limit'] = 38
        offering_search_result_model_json['total_count'] = 38
        offering_search_result_model_json['resource_count'] = 38
        offering_search_result_model_json['first'] = 'testString'
        offering_search_result_model_json['last'] = 'testString'
        offering_search_result_model_json['prev'] = 'testString'
        offering_search_result_model_json['next'] = 'testString'
        offering_search_result_model_json['resources'] = [offering_model]

        # Construct a model instance of OfferingSearchResult by calling from_dict on the json representation
        offering_search_result_model = OfferingSearchResult.from_dict(offering_search_result_model_json)
        assert offering_search_result_model != False

        # Construct a model instance of OfferingSearchResult by calling from_dict on the json representation
        offering_search_result_model_dict = OfferingSearchResult.from_dict(offering_search_result_model_json).__dict__
        offering_search_result_model2 = OfferingSearchResult(**offering_search_result_model_dict)

        # Verify the model instances are equivalent
        assert offering_search_result_model == offering_search_result_model2

        # Convert model instance back to dict and verify no loss of data
        offering_search_result_model_json2 = offering_search_result_model.to_dict()
        assert offering_search_result_model_json2 == offering_search_result_model_json

class OperatorDeployResultUnitTests():
    """
    Test Class for OperatorDeployResult
    """

    def test_operator_deploy_result_serialization(self):
        """
        Test serialization/deserialization for OperatorDeployResult
        """

        # Construct a json representation of a OperatorDeployResult model
        operator_deploy_result_model_json = {}
        operator_deploy_result_model_json['phase'] = 'testString'
        operator_deploy_result_model_json['message'] = 'testString'
        operator_deploy_result_model_json['link'] = 'testString'
        operator_deploy_result_model_json['name'] = 'testString'
        operator_deploy_result_model_json['version'] = 'testString'
        operator_deploy_result_model_json['namespace'] = 'testString'
        operator_deploy_result_model_json['package_name'] = 'testString'
        operator_deploy_result_model_json['catalog_id'] = 'testString'

        # Construct a model instance of OperatorDeployResult by calling from_dict on the json representation
        operator_deploy_result_model = OperatorDeployResult.from_dict(operator_deploy_result_model_json)
        assert operator_deploy_result_model != False

        # Construct a model instance of OperatorDeployResult by calling from_dict on the json representation
        operator_deploy_result_model_dict = OperatorDeployResult.from_dict(operator_deploy_result_model_json).__dict__
        operator_deploy_result_model2 = OperatorDeployResult(**operator_deploy_result_model_dict)

        # Verify the model instances are equivalent
        assert operator_deploy_result_model == operator_deploy_result_model2

        # Convert model instance back to dict and verify no loss of data
        operator_deploy_result_model_json2 = operator_deploy_result_model.to_dict()
        assert operator_deploy_result_model_json2 == operator_deploy_result_model_json

class PlanUnitTests():
    """
    Test Class for Plan
    """

    def test_plan_serialization(self):
        """
        Test serialization/deserialization for Plan
        """

        # Construct dict forms of any model objects needed in order to build this model.

        feature_model = {} # Feature
        feature_model['title'] = 'testString'
        feature_model['description'] = 'testString'

        deployment_model = {} # Deployment
        deployment_model['id'] = 'testString'
        deployment_model['label'] = 'testString'
        deployment_model['name'] = 'testString'
        deployment_model['short_description'] = 'testString'
        deployment_model['long_description'] = 'testString'
        deployment_model['metadata'] = {}
        deployment_model['tags'] = ['testString']
        deployment_model['created'] = "2019-01-01T12:00:00Z"
        deployment_model['updated'] = "2019-01-01T12:00:00Z"

        # Construct a json representation of a Plan model
        plan_model_json = {}
        plan_model_json['id'] = 'testString'
        plan_model_json['label'] = 'testString'
        plan_model_json['name'] = 'testString'
        plan_model_json['short_description'] = 'testString'
        plan_model_json['long_description'] = 'testString'
        plan_model_json['metadata'] = {}
        plan_model_json['tags'] = ['testString']
        plan_model_json['additional_features'] = [feature_model]
        plan_model_json['created'] = "2019-01-01T12:00:00Z"
        plan_model_json['updated'] = "2019-01-01T12:00:00Z"
        plan_model_json['deployments'] = [deployment_model]

        # Construct a model instance of Plan by calling from_dict on the json representation
        plan_model = Plan.from_dict(plan_model_json)
        assert plan_model != False

        # Construct a model instance of Plan by calling from_dict on the json representation
        plan_model_dict = Plan.from_dict(plan_model_json).__dict__
        plan_model2 = Plan(**plan_model_dict)

        # Verify the model instances are equivalent
        assert plan_model == plan_model2

        # Convert model instance back to dict and verify no loss of data
        plan_model_json2 = plan_model.to_dict()
        assert plan_model_json2 == plan_model_json

class PublishObjectUnitTests():
    """
    Test Class for PublishObject
    """

    def test_publish_object_serialization(self):
        """
        Test serialization/deserialization for PublishObject
        """

        # Construct a json representation of a PublishObject model
        publish_object_model_json = {}
        publish_object_model_json['permit_ibm_public_publish'] = True
        publish_object_model_json['ibm_approved'] = True
        publish_object_model_json['public_approved'] = True
        publish_object_model_json['portal_approval_record'] = 'testString'
        publish_object_model_json['portal_url'] = 'testString'

        # Construct a model instance of PublishObject by calling from_dict on the json representation
        publish_object_model = PublishObject.from_dict(publish_object_model_json)
        assert publish_object_model != False

        # Construct a model instance of PublishObject by calling from_dict on the json representation
        publish_object_model_dict = PublishObject.from_dict(publish_object_model_json).__dict__
        publish_object_model2 = PublishObject(**publish_object_model_dict)

        # Verify the model instances are equivalent
        assert publish_object_model == publish_object_model2

        # Convert model instance back to dict and verify no loss of data
        publish_object_model_json2 = publish_object_model.to_dict()
        assert publish_object_model_json2 == publish_object_model_json

class RatingUnitTests():
    """
    Test Class for Rating
    """

    def test_rating_serialization(self):
        """
        Test serialization/deserialization for Rating
        """

        # Construct a json representation of a Rating model
        rating_model_json = {}
        rating_model_json['one_star_count'] = 38
        rating_model_json['two_star_count'] = 38
        rating_model_json['three_star_count'] = 38
        rating_model_json['four_star_count'] = 38

        # Construct a model instance of Rating by calling from_dict on the json representation
        rating_model = Rating.from_dict(rating_model_json)
        assert rating_model != False

        # Construct a model instance of Rating by calling from_dict on the json representation
        rating_model_dict = Rating.from_dict(rating_model_json).__dict__
        rating_model2 = Rating(**rating_model_dict)

        # Verify the model instances are equivalent
        assert rating_model == rating_model2

        # Convert model instance back to dict and verify no loss of data
        rating_model_json2 = rating_model.to_dict()
        assert rating_model_json2 == rating_model_json

class RepoInfoUnitTests():
    """
    Test Class for RepoInfo
    """

    def test_repo_info_serialization(self):
        """
        Test serialization/deserialization for RepoInfo
        """

        # Construct a json representation of a RepoInfo model
        repo_info_model_json = {}
        repo_info_model_json['token'] = 'testString'
        repo_info_model_json['type'] = 'testString'

        # Construct a model instance of RepoInfo by calling from_dict on the json representation
        repo_info_model = RepoInfo.from_dict(repo_info_model_json)
        assert repo_info_model != False

        # Construct a model instance of RepoInfo by calling from_dict on the json representation
        repo_info_model_dict = RepoInfo.from_dict(repo_info_model_json).__dict__
        repo_info_model2 = RepoInfo(**repo_info_model_dict)

        # Verify the model instances are equivalent
        assert repo_info_model == repo_info_model2

        # Convert model instance back to dict and verify no loss of data
        repo_info_model_json2 = repo_info_model.to_dict()
        assert repo_info_model_json2 == repo_info_model_json

class ResourceUnitTests():
    """
    Test Class for Resource
    """

    def test_resource_serialization(self):
        """
        Test serialization/deserialization for Resource
        """

        # Construct a json representation of a Resource model
        resource_model_json = {}
        resource_model_json['type'] = 'mem'
        resource_model_json['value'] = { 'foo': 'bar' }

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

class ScriptUnitTests():
    """
    Test Class for Script
    """

    def test_script_serialization(self):
        """
        Test serialization/deserialization for Script
        """

        # Construct a json representation of a Script model
        script_model_json = {}
        script_model_json['instructions'] = 'testString'
        script_model_json['script'] = 'testString'
        script_model_json['script_permission'] = 'testString'
        script_model_json['delete_script'] = 'testString'
        script_model_json['scope'] = 'testString'

        # Construct a model instance of Script by calling from_dict on the json representation
        script_model = Script.from_dict(script_model_json)
        assert script_model != False

        # Construct a model instance of Script by calling from_dict on the json representation
        script_model_dict = Script.from_dict(script_model_json).__dict__
        script_model2 = Script(**script_model_dict)

        # Verify the model instances are equivalent
        assert script_model == script_model2

        # Convert model instance back to dict and verify no loss of data
        script_model_json2 = script_model.to_dict()
        assert script_model_json2 == script_model_json

class StateUnitTests():
    """
    Test Class for State
    """

    def test_state_serialization(self):
        """
        Test serialization/deserialization for State
        """

        # Construct a json representation of a State model
        state_model_json = {}
        state_model_json['current'] = 'testString'
        state_model_json['current_entered'] = "2019-01-01T12:00:00Z"
        state_model_json['pending'] = 'testString'
        state_model_json['pending_requested'] = "2019-01-01T12:00:00Z"
        state_model_json['previous'] = 'testString'

        # Construct a model instance of State by calling from_dict on the json representation
        state_model = State.from_dict(state_model_json)
        assert state_model != False

        # Construct a model instance of State by calling from_dict on the json representation
        state_model_dict = State.from_dict(state_model_json).__dict__
        state_model2 = State(**state_model_dict)

        # Verify the model instances are equivalent
        assert state_model == state_model2

        # Convert model instance back to dict and verify no loss of data
        state_model_json2 = state_model.to_dict()
        assert state_model_json2 == state_model_json

class SyndicationAuthorizationUnitTests():
    """
    Test Class for SyndicationAuthorization
    """

    def test_syndication_authorization_serialization(self):
        """
        Test serialization/deserialization for SyndicationAuthorization
        """

        # Construct a json representation of a SyndicationAuthorization model
        syndication_authorization_model_json = {}
        syndication_authorization_model_json['token'] = 'testString'
        syndication_authorization_model_json['last_run'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of SyndicationAuthorization by calling from_dict on the json representation
        syndication_authorization_model = SyndicationAuthorization.from_dict(syndication_authorization_model_json)
        assert syndication_authorization_model != False

        # Construct a model instance of SyndicationAuthorization by calling from_dict on the json representation
        syndication_authorization_model_dict = SyndicationAuthorization.from_dict(syndication_authorization_model_json).__dict__
        syndication_authorization_model2 = SyndicationAuthorization(**syndication_authorization_model_dict)

        # Verify the model instances are equivalent
        assert syndication_authorization_model == syndication_authorization_model2

        # Convert model instance back to dict and verify no loss of data
        syndication_authorization_model_json2 = syndication_authorization_model.to_dict()
        assert syndication_authorization_model_json2 == syndication_authorization_model_json

class SyndicationClusterUnitTests():
    """
    Test Class for SyndicationCluster
    """

    def test_syndication_cluster_serialization(self):
        """
        Test serialization/deserialization for SyndicationCluster
        """

        # Construct a json representation of a SyndicationCluster model
        syndication_cluster_model_json = {}
        syndication_cluster_model_json['region'] = 'testString'
        syndication_cluster_model_json['id'] = 'testString'
        syndication_cluster_model_json['name'] = 'testString'
        syndication_cluster_model_json['resource_group_name'] = 'testString'
        syndication_cluster_model_json['type'] = 'testString'
        syndication_cluster_model_json['namespaces'] = ['testString']
        syndication_cluster_model_json['all_namespaces'] = True

        # Construct a model instance of SyndicationCluster by calling from_dict on the json representation
        syndication_cluster_model = SyndicationCluster.from_dict(syndication_cluster_model_json)
        assert syndication_cluster_model != False

        # Construct a model instance of SyndicationCluster by calling from_dict on the json representation
        syndication_cluster_model_dict = SyndicationCluster.from_dict(syndication_cluster_model_json).__dict__
        syndication_cluster_model2 = SyndicationCluster(**syndication_cluster_model_dict)

        # Verify the model instances are equivalent
        assert syndication_cluster_model == syndication_cluster_model2

        # Convert model instance back to dict and verify no loss of data
        syndication_cluster_model_json2 = syndication_cluster_model.to_dict()
        assert syndication_cluster_model_json2 == syndication_cluster_model_json

class SyndicationHistoryUnitTests():
    """
    Test Class for SyndicationHistory
    """

    def test_syndication_history_serialization(self):
        """
        Test serialization/deserialization for SyndicationHistory
        """

        # Construct dict forms of any model objects needed in order to build this model.

        syndication_cluster_model = {} # SyndicationCluster
        syndication_cluster_model['region'] = 'testString'
        syndication_cluster_model['id'] = 'testString'
        syndication_cluster_model['name'] = 'testString'
        syndication_cluster_model['resource_group_name'] = 'testString'
        syndication_cluster_model['type'] = 'testString'
        syndication_cluster_model['namespaces'] = ['testString']
        syndication_cluster_model['all_namespaces'] = True

        # Construct a json representation of a SyndicationHistory model
        syndication_history_model_json = {}
        syndication_history_model_json['namespaces'] = ['testString']
        syndication_history_model_json['clusters'] = [syndication_cluster_model]
        syndication_history_model_json['last_run'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of SyndicationHistory by calling from_dict on the json representation
        syndication_history_model = SyndicationHistory.from_dict(syndication_history_model_json)
        assert syndication_history_model != False

        # Construct a model instance of SyndicationHistory by calling from_dict on the json representation
        syndication_history_model_dict = SyndicationHistory.from_dict(syndication_history_model_json).__dict__
        syndication_history_model2 = SyndicationHistory(**syndication_history_model_dict)

        # Verify the model instances are equivalent
        assert syndication_history_model == syndication_history_model2

        # Convert model instance back to dict and verify no loss of data
        syndication_history_model_json2 = syndication_history_model.to_dict()
        assert syndication_history_model_json2 == syndication_history_model_json

class SyndicationResourceUnitTests():
    """
    Test Class for SyndicationResource
    """

    def test_syndication_resource_serialization(self):
        """
        Test serialization/deserialization for SyndicationResource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        syndication_cluster_model = {} # SyndicationCluster
        syndication_cluster_model['region'] = 'testString'
        syndication_cluster_model['id'] = 'testString'
        syndication_cluster_model['name'] = 'testString'
        syndication_cluster_model['resource_group_name'] = 'testString'
        syndication_cluster_model['type'] = 'testString'
        syndication_cluster_model['namespaces'] = ['testString']
        syndication_cluster_model['all_namespaces'] = True

        syndication_history_model = {} # SyndicationHistory
        syndication_history_model['namespaces'] = ['testString']
        syndication_history_model['clusters'] = [syndication_cluster_model]
        syndication_history_model['last_run'] = "2019-01-01T12:00:00Z"

        syndication_authorization_model = {} # SyndicationAuthorization
        syndication_authorization_model['token'] = 'testString'
        syndication_authorization_model['last_run'] = "2019-01-01T12:00:00Z"

        # Construct a json representation of a SyndicationResource model
        syndication_resource_model_json = {}
        syndication_resource_model_json['remove_related_components'] = True
        syndication_resource_model_json['clusters'] = [syndication_cluster_model]
        syndication_resource_model_json['history'] = syndication_history_model
        syndication_resource_model_json['authorization'] = syndication_authorization_model

        # Construct a model instance of SyndicationResource by calling from_dict on the json representation
        syndication_resource_model = SyndicationResource.from_dict(syndication_resource_model_json)
        assert syndication_resource_model != False

        # Construct a model instance of SyndicationResource by calling from_dict on the json representation
        syndication_resource_model_dict = SyndicationResource.from_dict(syndication_resource_model_json).__dict__
        syndication_resource_model2 = SyndicationResource(**syndication_resource_model_dict)

        # Verify the model instances are equivalent
        assert syndication_resource_model == syndication_resource_model2

        # Convert model instance back to dict and verify no loss of data
        syndication_resource_model_json2 = syndication_resource_model.to_dict()
        assert syndication_resource_model_json2 == syndication_resource_model_json

class ValidationUnitTests():
    """
    Test Class for Validation
    """

    def test_validation_serialization(self):
        """
        Test serialization/deserialization for Validation
        """

        # Construct a json representation of a Validation model
        validation_model_json = {}
        validation_model_json['validated'] = "2019-01-01T12:00:00Z"
        validation_model_json['requested'] = "2019-01-01T12:00:00Z"
        validation_model_json['state'] = 'testString'
        validation_model_json['last_operation'] = 'testString'
        validation_model_json['target'] = {}

        # Construct a model instance of Validation by calling from_dict on the json representation
        validation_model = Validation.from_dict(validation_model_json)
        assert validation_model != False

        # Construct a model instance of Validation by calling from_dict on the json representation
        validation_model_dict = Validation.from_dict(validation_model_json).__dict__
        validation_model2 = Validation(**validation_model_dict)

        # Verify the model instances are equivalent
        assert validation_model == validation_model2

        # Convert model instance back to dict and verify no loss of data
        validation_model_json2 = validation_model.to_dict()
        assert validation_model_json2 == validation_model_json

class VersionUnitTests():
    """
    Test Class for Version
    """

    def test_version_serialization(self):
        """
        Test serialization/deserialization for Version
        """

        # Construct dict forms of any model objects needed in order to build this model.

        configuration_model = {} # Configuration
        configuration_model['key'] = 'testString'
        configuration_model['type'] = 'testString'
        configuration_model['default_value'] = { 'foo': 'bar' }
        configuration_model['value_constraint'] = 'testString'
        configuration_model['description'] = 'testString'
        configuration_model['required'] = True
        configuration_model['options'] = [{ 'foo': 'bar' }]
        configuration_model['hidden'] = True

        validation_model = {} # Validation
        validation_model['validated'] = "2019-01-01T12:00:00Z"
        validation_model['requested'] = "2019-01-01T12:00:00Z"
        validation_model['state'] = 'testString'
        validation_model['last_operation'] = 'testString'
        validation_model['target'] = {}

        resource_model = {} # Resource
        resource_model['type'] = 'mem'
        resource_model['value'] = { 'foo': 'bar' }

        script_model = {} # Script
        script_model['instructions'] = 'testString'
        script_model['script'] = 'testString'
        script_model['script_permission'] = 'testString'
        script_model['delete_script'] = 'testString'
        script_model['scope'] = 'testString'

        version_entitlement_model = {} # VersionEntitlement
        version_entitlement_model['provider_name'] = 'testString'
        version_entitlement_model['provider_id'] = 'testString'
        version_entitlement_model['product_id'] = 'testString'
        version_entitlement_model['part_numbers'] = ['testString']
        version_entitlement_model['image_repo_name'] = 'testString'

        license_model = {} # License
        license_model['id'] = 'testString'
        license_model['name'] = 'testString'
        license_model['type'] = 'testString'
        license_model['url'] = 'testString'
        license_model['description'] = 'testString'

        state_model = {} # State
        state_model['current'] = 'testString'
        state_model['current_entered'] = "2019-01-01T12:00:00Z"
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = "2019-01-01T12:00:00Z"
        state_model['previous'] = 'testString'

        # Construct a json representation of a Version model
        version_model_json = {}
        version_model_json['id'] = 'testString'
        version_model_json['_rev'] = 'testString'
        version_model_json['crn'] = 'testString'
        version_model_json['version'] = 'testString'
        version_model_json['sha'] = 'testString'
        version_model_json['created'] = "2019-01-01T12:00:00Z"
        version_model_json['updated'] = "2019-01-01T12:00:00Z"
        version_model_json['offering_id'] = 'testString'
        version_model_json['catalog_id'] = 'testString'
        version_model_json['kind_id'] = 'testString'
        version_model_json['tags'] = ['testString']
        version_model_json['repo_url'] = 'testString'
        version_model_json['source_url'] = 'testString'
        version_model_json['tgz_url'] = 'testString'
        version_model_json['configuration'] = [configuration_model]
        version_model_json['metadata'] = {}
        version_model_json['validation'] = validation_model
        version_model_json['required_resources'] = [resource_model]
        version_model_json['single_instance'] = True
        version_model_json['install'] = script_model
        version_model_json['pre_install'] = [script_model]
        version_model_json['entitlement'] = version_entitlement_model
        version_model_json['licenses'] = [license_model]
        version_model_json['image_manifest_url'] = 'testString'
        version_model_json['deprecated'] = True
        version_model_json['package_version'] = 'testString'
        version_model_json['state'] = state_model
        version_model_json['version_locator'] = 'testString'
        version_model_json['console_url'] = 'testString'
        version_model_json['long_description'] = 'testString'
        version_model_json['whitelisted_accounts'] = ['testString']

        # Construct a model instance of Version by calling from_dict on the json representation
        version_model = Version.from_dict(version_model_json)
        assert version_model != False

        # Construct a model instance of Version by calling from_dict on the json representation
        version_model_dict = Version.from_dict(version_model_json).__dict__
        version_model2 = Version(**version_model_dict)

        # Verify the model instances are equivalent
        assert version_model == version_model2

        # Convert model instance back to dict and verify no loss of data
        version_model_json2 = version_model.to_dict()
        assert version_model_json2 == version_model_json

class VersionEntitlementUnitTests():
    """
    Test Class for VersionEntitlement
    """

    def test_version_entitlement_serialization(self):
        """
        Test serialization/deserialization for VersionEntitlement
        """

        # Construct a json representation of a VersionEntitlement model
        version_entitlement_model_json = {}
        version_entitlement_model_json['provider_name'] = 'testString'
        version_entitlement_model_json['provider_id'] = 'testString'
        version_entitlement_model_json['product_id'] = 'testString'
        version_entitlement_model_json['part_numbers'] = ['testString']
        version_entitlement_model_json['image_repo_name'] = 'testString'

        # Construct a model instance of VersionEntitlement by calling from_dict on the json representation
        version_entitlement_model = VersionEntitlement.from_dict(version_entitlement_model_json)
        assert version_entitlement_model != False

        # Construct a model instance of VersionEntitlement by calling from_dict on the json representation
        version_entitlement_model_dict = VersionEntitlement.from_dict(version_entitlement_model_json).__dict__
        version_entitlement_model2 = VersionEntitlement(**version_entitlement_model_dict)

        # Verify the model instances are equivalent
        assert version_entitlement_model == version_entitlement_model2

        # Convert model instance back to dict and verify no loss of data
        version_entitlement_model_json2 = version_entitlement_model.to_dict()
        assert version_entitlement_model_json2 == version_entitlement_model_json

class VersionUpdateDescriptorUnitTests():
    """
    Test Class for VersionUpdateDescriptor
    """

    def test_version_update_descriptor_serialization(self):
        """
        Test serialization/deserialization for VersionUpdateDescriptor
        """

        # Construct dict forms of any model objects needed in order to build this model.

        state_model = {} # State
        state_model['current'] = 'testString'
        state_model['current_entered'] = "2019-01-01T12:00:00Z"
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = "2019-01-01T12:00:00Z"
        state_model['previous'] = 'testString'

        resource_model = {} # Resource
        resource_model['type'] = 'mem'
        resource_model['value'] = { 'foo': 'bar' }

        # Construct a json representation of a VersionUpdateDescriptor model
        version_update_descriptor_model_json = {}
        version_update_descriptor_model_json['version_locator'] = 'testString'
        version_update_descriptor_model_json['version'] = 'testString'
        version_update_descriptor_model_json['state'] = state_model
        version_update_descriptor_model_json['required_resources'] = [resource_model]
        version_update_descriptor_model_json['package_version'] = 'testString'
        version_update_descriptor_model_json['can_update'] = True
        version_update_descriptor_model_json['messages'] = {}

        # Construct a model instance of VersionUpdateDescriptor by calling from_dict on the json representation
        version_update_descriptor_model = VersionUpdateDescriptor.from_dict(version_update_descriptor_model_json)
        assert version_update_descriptor_model != False

        # Construct a model instance of VersionUpdateDescriptor by calling from_dict on the json representation
        version_update_descriptor_model_dict = VersionUpdateDescriptor.from_dict(version_update_descriptor_model_json).__dict__
        version_update_descriptor_model2 = VersionUpdateDescriptor(**version_update_descriptor_model_dict)

        # Verify the model instances are equivalent
        assert version_update_descriptor_model == version_update_descriptor_model2

        # Convert model instance back to dict and verify no loss of data
        version_update_descriptor_model_json2 = version_update_descriptor_model.to_dict()
        assert version_update_descriptor_model_json2 == version_update_descriptor_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
