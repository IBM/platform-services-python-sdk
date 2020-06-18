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

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
from ibm_platform_services.catalog_management_v1 import *


service = CatalogManagementV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://cm.globalcatalog.cloud.ibm.com/api/v1-beta'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Account
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_catalog_account
#-----------------------------------------------------------------------------
class TestGetCatalogAccount():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_catalog_account()
    #--------------------------------------------------------
    @responses.activate
    def test_get_catalog_account_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogaccount')
        mock_response = '{"id": "id", "account_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_catalog_account()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_catalog_account
#-----------------------------------------------------------------------------
class TestUpdateCatalogAccount():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_catalog_account()
    #--------------------------------------------------------
    @responses.activate
    def test_update_catalog_account_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogaccount')
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
        account_filters = filters_model

        # Invoke method
        response = service.update_catalog_account(
            id=id,
            account_filters=account_filters,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['account_filters'] == filters_model


    #--------------------------------------------------------
    # test_update_catalog_account_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_catalog_account_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogaccount')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Invoke method
        response = service.update_catalog_account()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_catalog_account_filters
#-----------------------------------------------------------------------------
class TestGetCatalogAccountFilters():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_catalog_account_filters()
    #--------------------------------------------------------
    @responses.activate
    def test_get_catalog_account_filters_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogaccount/filters')
        mock_response = '{"account_filters": [{"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}], "catalog_filters": [{"catalog": {"id": "id", "name": "name"}, "filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog = 'testString'

        # Invoke method
        response = service.get_catalog_account_filters(
            catalog=catalog,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'catalog={}'.format(catalog) in query_string


    #--------------------------------------------------------
    # test_get_catalog_account_filters_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_catalog_account_filters_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogaccount/filters')
        mock_response = '{"account_filters": [{"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}], "catalog_filters": [{"catalog": {"id": "id", "name": "name"}, "filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_catalog_account_filters()


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

#-----------------------------------------------------------------------------
# Test Class for list_catalogs
#-----------------------------------------------------------------------------
class TestListCatalogs():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_catalogs()
    #--------------------------------------------------------
    @responses.activate
    def test_list_catalogs_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00"}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_catalogs()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_catalog
#-----------------------------------------------------------------------------
class TestCreateCatalog():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_catalog()
    #--------------------------------------------------------
    @responses.activate
    def test_create_catalog_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs')
        mock_response = '{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00"}}}'
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

        # Construct a dict representation of a SyndicationAuthorization model
        syndication_authorization_model = {}
        syndication_authorization_model['token'] = 'testString'
        syndication_authorization_model['last_run'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a SyndicationHistory model
        syndication_history_model = {}
        syndication_history_model['namespaces'] = ['testString']
        syndication_history_model['clusters'] = [syndication_cluster_model]
        syndication_history_model['last_run'] = '2020-01-28T18:40:40.123456Z'

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
        url = 'testString'
        crn = 'testString'
        offerings_url = 'testString'
        features = [feature_model]
        disabled = True
        created = datetime.fromtimestamp(1580236840.123456, timezone.utc)
        updated = datetime.fromtimestamp(1580236840.123456, timezone.utc)
        resource_group_id = 'testString'
        owning_account = 'testString'
        catalog_filters = filters_model
        syndication_settings = syndication_resource_model

        # Invoke method
        response = service.create_catalog(
            id=id,
            rev=rev,
            label=label,
            short_description=short_description,
            catalog_icon_url=catalog_icon_url,
            tags=tags,
            url=url,
            crn=crn,
            offerings_url=offerings_url,
            features=features,
            disabled=disabled,
            created=created,
            updated=updated,
            resource_group_id=resource_group_id,
            owning_account=owning_account,
            catalog_filters=catalog_filters,
            syndication_settings=syndication_settings,
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
        assert req_body['url'] == 'testString'
        assert req_body['crn'] == 'testString'
        assert req_body['offerings_url'] == 'testString'
        assert req_body['features'] == [feature_model]
        assert req_body['disabled'] == True
        assert req_body['created'] == '2020-01-28T18:40:40.123456Z'
        assert req_body['updated'] == '2020-01-28T18:40:40.123456Z'
        assert req_body['resource_group_id'] == 'testString'
        assert req_body['owning_account'] == 'testString'
        assert req_body['catalog_filters'] == filters_model
        assert req_body['syndication_settings'] == syndication_resource_model


    #--------------------------------------------------------
    # test_create_catalog_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_catalog_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs')
        mock_response = '{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Invoke method
        response = service.create_catalog()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


#-----------------------------------------------------------------------------
# Test Class for get_catalog
#-----------------------------------------------------------------------------
class TestGetCatalog():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_catalog()
    #--------------------------------------------------------
    @responses.activate
    def test_get_catalog_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString')
        mock_response = '{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Invoke method
        response = service.get_catalog(
            catalog_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_catalog_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_catalog_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString')
        mock_response = '{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00"}}}'
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
                service.get_catalog(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for replace_catalog
#-----------------------------------------------------------------------------
class TestReplaceCatalog():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # replace_catalog()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_catalog_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString')
        mock_response = '{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00"}}}'
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

        # Construct a dict representation of a SyndicationAuthorization model
        syndication_authorization_model = {}
        syndication_authorization_model['token'] = 'testString'
        syndication_authorization_model['last_run'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a SyndicationHistory model
        syndication_history_model = {}
        syndication_history_model['namespaces'] = ['testString']
        syndication_history_model['clusters'] = [syndication_cluster_model]
        syndication_history_model['last_run'] = '2020-01-28T18:40:40.123456Z'

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
        url = 'testString'
        crn = 'testString'
        offerings_url = 'testString'
        features = [feature_model]
        disabled = True
        created = datetime.fromtimestamp(1580236840.123456, timezone.utc)
        updated = datetime.fromtimestamp(1580236840.123456, timezone.utc)
        resource_group_id = 'testString'
        owning_account = 'testString'
        catalog_filters = filters_model
        syndication_settings = syndication_resource_model

        # Invoke method
        response = service.replace_catalog(
            catalog_identifier,
            id=id,
            rev=rev,
            label=label,
            short_description=short_description,
            catalog_icon_url=catalog_icon_url,
            tags=tags,
            url=url,
            crn=crn,
            offerings_url=offerings_url,
            features=features,
            disabled=disabled,
            created=created,
            updated=updated,
            resource_group_id=resource_group_id,
            owning_account=owning_account,
            catalog_filters=catalog_filters,
            syndication_settings=syndication_settings,
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
        assert req_body['url'] == 'testString'
        assert req_body['crn'] == 'testString'
        assert req_body['offerings_url'] == 'testString'
        assert req_body['features'] == [feature_model]
        assert req_body['disabled'] == True
        assert req_body['created'] == '2020-01-28T18:40:40.123456Z'
        assert req_body['updated'] == '2020-01-28T18:40:40.123456Z'
        assert req_body['resource_group_id'] == 'testString'
        assert req_body['owning_account'] == 'testString'
        assert req_body['catalog_filters'] == filters_model
        assert req_body['syndication_settings'] == syndication_resource_model


    #--------------------------------------------------------
    # test_replace_catalog_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_catalog_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString')
        mock_response = '{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Invoke method
        response = service.replace_catalog(
            catalog_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_replace_catalog_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_catalog_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString')
        mock_response = '{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00"}}}'
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
                service.replace_catalog(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_catalog
#-----------------------------------------------------------------------------
class TestDeleteCatalog():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_catalog()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_catalog_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Invoke method
        response = service.delete_catalog(
            catalog_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_catalog_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_catalog_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString')
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
                service.delete_catalog(**req_copy)



# endregion
##############################################################################
# End of Service: Catalogs
##############################################################################

##############################################################################
# Start of Service: Enterprise
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_enterprise
#-----------------------------------------------------------------------------
class TestGetEnterprise():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_enterprise()
    #--------------------------------------------------------
    @responses.activate
    def test_get_enterprise_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/enterprises/testString')
        mock_response = '{"id": "id", "_rev": "rev", "account_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "account_groups": {"keys": {"id": "id", "account_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        enterprise_id = 'testString'

        # Invoke method
        response = service.get_enterprise(
            enterprise_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_enterprise_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_enterprise_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/enterprises/testString')
        mock_response = '{"id": "id", "_rev": "rev", "account_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "account_groups": {"keys": {"id": "id", "account_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        enterprise_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "enterprise_id": enterprise_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_enterprise(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for replace_enterprise
#-----------------------------------------------------------------------------
class TestReplaceEnterprise():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # replace_enterprise()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_enterprise_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/enterprises/testString')
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

        # Construct a dict representation of a AccountGroup model
        account_group_model = {}
        account_group_model['id'] = 'testString'
        account_group_model['account_filters'] = filters_model

        # Construct a dict representation of a EnterpriseAccountGroups model
        enterprise_account_groups_model = {}
        enterprise_account_groups_model['keys'] = account_group_model

        # Set up parameter values
        enterprise_id = 'testString'
        id = 'testString'
        rev = 'testString'
        account_filters = filters_model
        account_groups = enterprise_account_groups_model

        # Invoke method
        response = service.replace_enterprise(
            enterprise_id,
            id=id,
            rev=rev,
            account_filters=account_filters,
            account_groups=account_groups,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['_rev'] == 'testString'
        assert req_body['account_filters'] == filters_model
        assert req_body['account_groups'] == enterprise_account_groups_model


    #--------------------------------------------------------
    # test_replace_enterprise_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_enterprise_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/enterprises/testString')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        enterprise_id = 'testString'

        # Invoke method
        response = service.replace_enterprise(
            enterprise_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_replace_enterprise_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_enterprise_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/enterprises/testString')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        enterprise_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "enterprise_id": enterprise_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.replace_enterprise(**req_copy)



# endregion
##############################################################################
# End of Service: Enterprise
##############################################################################

##############################################################################
# Start of Service: Offerings
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_consumption_offerings
#-----------------------------------------------------------------------------
class TestGetConsumptionOfferings():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_consumption_offerings()
    #--------------------------------------------------------
    @responses.activate
    def test_get_consumption_offerings_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/offerings')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}]}'
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

        # Invoke method
        response = service.get_consumption_offerings(
            digest=digest,
            catalog=catalog,
            select=select,
            include_hidden=include_hidden,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'digest={}'.format('true' if digest else 'false') in query_string
        assert 'catalog={}'.format(catalog) in query_string
        assert 'select={}'.format(select) in query_string
        assert 'includeHidden={}'.format('true' if include_hidden else 'false') in query_string


    #--------------------------------------------------------
    # test_get_consumption_offerings_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_consumption_offerings_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/offerings')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_consumption_offerings()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for list_offerings
#-----------------------------------------------------------------------------
class TestListOfferings():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_offerings()
    #--------------------------------------------------------
    @responses.activate
    def test_list_offerings_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        digest = True

        # Invoke method
        response = service.list_offerings(
            catalog_identifier,
            digest=digest,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'digest={}'.format('true' if digest else 'false') in query_string


    #--------------------------------------------------------
    # test_list_offerings_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_offerings_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Invoke method
        response = service.list_offerings(
            catalog_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_offerings_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_offerings_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}]}'
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
                service.list_offerings(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_offering
#-----------------------------------------------------------------------------
class TestCreateOffering():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_offering()
    #--------------------------------------------------------
    @responses.activate
    def test_create_offering_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
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

        # Construct a dict representation of a Deployment model
        deployment_model = {}
        deployment_model['id'] = 'testString'
        deployment_model['label'] = 'testString'
        deployment_model['name'] = 'testString'
        deployment_model['short_description'] = 'testString'
        deployment_model['long_description'] = 'testString'
        deployment_model['metadata'] = { 'foo': 'bar' }
        deployment_model['tags'] = ['testString']
        deployment_model['created'] = '2020-01-28T18:40:40.123456Z'
        deployment_model['updated'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a License model
        license_model = {}
        license_model['id'] = 'testString'
        license_model['name'] = 'testString'
        license_model['type'] = 'testString'
        license_model['url'] = 'testString'
        license_model['description'] = 'testString'

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

        # Construct a dict representation of a State model
        state_model = {}
        state_model['current'] = 'testString'
        state_model['current_entered'] = '2020-01-28T18:40:40.123456Z'
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = '2020-01-28T18:40:40.123456Z'
        state_model['previous'] = 'testString'

        # Construct a dict representation of a Validation model
        validation_model = {}
        validation_model['validated'] = '2020-01-28T18:40:40.123456Z'
        validation_model['requested'] = '2020-01-28T18:40:40.123456Z'
        validation_model['state'] = 'testString'
        validation_model['last_operation'] = 'testString'
        validation_model['target'] = { 'foo': 'bar' }

        # Construct a dict representation of a VersionEntitlement model
        version_entitlement_model = {}
        version_entitlement_model['provider_name'] = 'testString'
        version_entitlement_model['provider_id'] = 'testString'
        version_entitlement_model['product_id'] = 'testString'
        version_entitlement_model['part_numbers'] = ['testString']
        version_entitlement_model['image_repo_name'] = 'testString'

        # Construct a dict representation of a Plan model
        plan_model = {}
        plan_model['id'] = 'testString'
        plan_model['label'] = 'testString'
        plan_model['name'] = 'testString'
        plan_model['short_description'] = 'testString'
        plan_model['long_description'] = 'testString'
        plan_model['metadata'] = { 'foo': 'bar' }
        plan_model['tags'] = ['testString']
        plan_model['additional_features'] = [feature_model]
        plan_model['created'] = '2020-01-28T18:40:40.123456Z'
        plan_model['updated'] = '2020-01-28T18:40:40.123456Z'
        plan_model['deployments'] = [deployment_model]

        # Construct a dict representation of a Version model
        version_model = {}
        version_model['id'] = 'testString'
        version_model['_rev'] = 'testString'
        version_model['crn'] = 'testString'
        version_model['version'] = 'testString'
        version_model['sha'] = 'testString'
        version_model['created'] = '2020-01-28T18:40:40.123456Z'
        version_model['updated'] = '2020-01-28T18:40:40.123456Z'
        version_model['offering_id'] = 'testString'
        version_model['catalog_id'] = 'testString'
        version_model['kind_id'] = 'testString'
        version_model['tags'] = ['testString']
        version_model['repo_url'] = 'testString'
        version_model['source_url'] = 'testString'
        version_model['tgz_url'] = 'testString'
        version_model['configuration'] = [configuration_model]
        version_model['metadata'] = { 'foo': 'bar' }
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

        # Construct a dict representation of a Kind model
        kind_model = {}
        kind_model['id'] = 'testString'
        kind_model['format_kind'] = 'testString'
        kind_model['target_kind'] = 'testString'
        kind_model['metadata'] = { 'foo': 'bar' }
        kind_model['install_description'] = 'testString'
        kind_model['tags'] = ['testString']
        kind_model['additional_features'] = [feature_model]
        kind_model['created'] = '2020-01-28T18:40:40.123456Z'
        kind_model['updated'] = '2020-01-28T18:40:40.123456Z'
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
        rating = rating_model
        created = datetime.fromtimestamp(1580236840.123456, timezone.utc)
        updated = datetime.fromtimestamp(1580236840.123456, timezone.utc)
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
        metadata = { 'foo': 'bar' }
        disclaimer = 'testString'
        hidden = True
        provider = 'testString'
        repo_info = repo_info_model

        # Invoke method
        response = service.create_offering(
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
        assert req_body['rating'] == rating_model
        assert req_body['created'] == '2020-01-28T18:40:40.123456Z'
        assert req_body['updated'] == '2020-01-28T18:40:40.123456Z'
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
        assert req_body['metadata'] == { 'foo': 'bar' }
        assert req_body['disclaimer'] == 'testString'
        assert req_body['hidden'] == True
        assert req_body['provider'] == 'testString'
        assert req_body['repo_info'] == repo_info_model


    #--------------------------------------------------------
    # test_create_offering_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_offering_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'

        # Invoke method
        response = service.create_offering(
            catalog_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    #--------------------------------------------------------
    # test_create_offering_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_offering_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
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
                service.create_offering(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for import_offering_version
#-----------------------------------------------------------------------------
class TestImportOfferingVersion():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # import_offering_version()
    #--------------------------------------------------------
    @responses.activate
    def test_import_offering_version_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings/testString/version')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        zipurl = 'testString'
        tags = ['testString']
        target_kinds = ['testString']
        target_version = 'testString'
        include_config = True
        repo_type = 'testString'
        x_auth_token = 'testString'

        # Invoke method
        response = service.import_offering_version(
            catalog_identifier,
            offering_id,
            zipurl,
            tags=tags,
            target_kinds=target_kinds,
            target_version=target_version,
            include_config=include_config,
            repo_type=repo_type,
            x_auth_token=x_auth_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'zipurl={}'.format(zipurl) in query_string
        assert 'targetVersion={}'.format(target_version) in query_string
        assert 'includeConfig={}'.format('true' if include_config else 'false') in query_string
        assert 'repoType={}'.format(repo_type) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['tags'] == ['testString']
        assert req_body['target_kinds'] == ['testString']


    #--------------------------------------------------------
    # test_import_offering_version_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_import_offering_version_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings/testString/version')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        zipurl = 'testString'

        # Invoke method
        response = service.import_offering_version(
            catalog_identifier,
            offering_id,
            zipurl,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'zipurl={}'.format(zipurl) in query_string


    #--------------------------------------------------------
    # test_import_offering_version_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_import_offering_version_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings/testString/version')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        zipurl = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "offering_id": offering_id,
            "zipurl": zipurl,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.import_offering_version(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for import_offering
#-----------------------------------------------------------------------------
class TestImportOffering():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # import_offering()
    #--------------------------------------------------------
    @responses.activate
    def test_import_offering_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/import/offerings')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        zipurl = 'testString'
        tags = ['testString']
        target_kinds = ['testString']
        offering_id = 'testString'
        include_config = True
        repo_type = 'testString'
        x_auth_token = 'testString'

        # Invoke method
        response = service.import_offering(
            catalog_identifier,
            zipurl,
            tags=tags,
            target_kinds=target_kinds,
            offering_id=offering_id,
            include_config=include_config,
            repo_type=repo_type,
            x_auth_token=x_auth_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'zipurl={}'.format(zipurl) in query_string
        assert 'offeringID={}'.format(offering_id) in query_string
        assert 'includeConfig={}'.format('true' if include_config else 'false') in query_string
        assert 'repoType={}'.format(repo_type) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['tags'] == ['testString']
        assert req_body['target_kinds'] == ['testString']


    #--------------------------------------------------------
    # test_import_offering_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_import_offering_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/import/offerings')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        zipurl = 'testString'

        # Invoke method
        response = service.import_offering(
            catalog_identifier,
            zipurl,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'zipurl={}'.format(zipurl) in query_string


    #--------------------------------------------------------
    # test_import_offering_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_import_offering_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/import/offerings')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        zipurl = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "zipurl": zipurl,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.import_offering(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for reload_offering
#-----------------------------------------------------------------------------
class TestReloadOffering():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # reload_offering()
    #--------------------------------------------------------
    @responses.activate
    def test_reload_offering_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings/testString/reload')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        zipurl = 'testString'
        target_version = 'testString'
        tags = ['testString']
        target_kinds = ['testString']
        repo_type = 'testString'
        x_auth_token = 'testString'

        # Invoke method
        response = service.reload_offering(
            catalog_identifier,
            offering_id,
            zipurl,
            target_version,
            tags=tags,
            target_kinds=target_kinds,
            repo_type=repo_type,
            x_auth_token=x_auth_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'zipurl={}'.format(zipurl) in query_string
        assert 'targetVersion={}'.format(target_version) in query_string
        assert 'repoType={}'.format(repo_type) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['tags'] == ['testString']
        assert req_body['target_kinds'] == ['testString']


    #--------------------------------------------------------
    # test_reload_offering_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_reload_offering_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings/testString/reload')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        zipurl = 'testString'
        target_version = 'testString'

        # Invoke method
        response = service.reload_offering(
            catalog_identifier,
            offering_id,
            zipurl,
            target_version,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'zipurl={}'.format(zipurl) in query_string
        assert 'targetVersion={}'.format(target_version) in query_string


    #--------------------------------------------------------
    # test_reload_offering_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_reload_offering_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings/testString/reload')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        zipurl = 'testString'
        target_version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_identifier": catalog_identifier,
            "offering_id": offering_id,
            "zipurl": zipurl,
            "target_version": target_version,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.reload_offering(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_offering
#-----------------------------------------------------------------------------
class TestGetOffering():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_offering()
    #--------------------------------------------------------
    @responses.activate
    def test_get_offering_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'

        # Invoke method
        response = service.get_offering(
            catalog_identifier,
            offering_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_offering_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_offering_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
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
                service.get_offering(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for replace_offering
#-----------------------------------------------------------------------------
class TestReplaceOffering():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # replace_offering()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_offering_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings/testString')
        mock_response = '{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00"}}}'
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

        # Construct a dict representation of a Deployment model
        deployment_model = {}
        deployment_model['id'] = 'testString'
        deployment_model['label'] = 'testString'
        deployment_model['name'] = 'testString'
        deployment_model['short_description'] = 'testString'
        deployment_model['long_description'] = 'testString'
        deployment_model['metadata'] = { 'foo': 'bar' }
        deployment_model['tags'] = ['testString']
        deployment_model['created'] = '2020-01-28T18:40:40.123456Z'
        deployment_model['updated'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a License model
        license_model = {}
        license_model['id'] = 'testString'
        license_model['name'] = 'testString'
        license_model['type'] = 'testString'
        license_model['url'] = 'testString'
        license_model['description'] = 'testString'

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

        # Construct a dict representation of a State model
        state_model = {}
        state_model['current'] = 'testString'
        state_model['current_entered'] = '2020-01-28T18:40:40.123456Z'
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = '2020-01-28T18:40:40.123456Z'
        state_model['previous'] = 'testString'

        # Construct a dict representation of a Validation model
        validation_model = {}
        validation_model['validated'] = '2020-01-28T18:40:40.123456Z'
        validation_model['requested'] = '2020-01-28T18:40:40.123456Z'
        validation_model['state'] = 'testString'
        validation_model['last_operation'] = 'testString'
        validation_model['target'] = { 'foo': 'bar' }

        # Construct a dict representation of a VersionEntitlement model
        version_entitlement_model = {}
        version_entitlement_model['provider_name'] = 'testString'
        version_entitlement_model['provider_id'] = 'testString'
        version_entitlement_model['product_id'] = 'testString'
        version_entitlement_model['part_numbers'] = ['testString']
        version_entitlement_model['image_repo_name'] = 'testString'

        # Construct a dict representation of a Plan model
        plan_model = {}
        plan_model['id'] = 'testString'
        plan_model['label'] = 'testString'
        plan_model['name'] = 'testString'
        plan_model['short_description'] = 'testString'
        plan_model['long_description'] = 'testString'
        plan_model['metadata'] = { 'foo': 'bar' }
        plan_model['tags'] = ['testString']
        plan_model['additional_features'] = [feature_model]
        plan_model['created'] = '2020-01-28T18:40:40.123456Z'
        plan_model['updated'] = '2020-01-28T18:40:40.123456Z'
        plan_model['deployments'] = [deployment_model]

        # Construct a dict representation of a Version model
        version_model = {}
        version_model['id'] = 'testString'
        version_model['_rev'] = 'testString'
        version_model['crn'] = 'testString'
        version_model['version'] = 'testString'
        version_model['sha'] = 'testString'
        version_model['created'] = '2020-01-28T18:40:40.123456Z'
        version_model['updated'] = '2020-01-28T18:40:40.123456Z'
        version_model['offering_id'] = 'testString'
        version_model['catalog_id'] = 'testString'
        version_model['kind_id'] = 'testString'
        version_model['tags'] = ['testString']
        version_model['repo_url'] = 'testString'
        version_model['source_url'] = 'testString'
        version_model['tgz_url'] = 'testString'
        version_model['configuration'] = [configuration_model]
        version_model['metadata'] = { 'foo': 'bar' }
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

        # Construct a dict representation of a Kind model
        kind_model = {}
        kind_model['id'] = 'testString'
        kind_model['format_kind'] = 'testString'
        kind_model['target_kind'] = 'testString'
        kind_model['metadata'] = { 'foo': 'bar' }
        kind_model['install_description'] = 'testString'
        kind_model['tags'] = ['testString']
        kind_model['additional_features'] = [feature_model]
        kind_model['created'] = '2020-01-28T18:40:40.123456Z'
        kind_model['updated'] = '2020-01-28T18:40:40.123456Z'
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
        rating = rating_model
        created = datetime.fromtimestamp(1580236840.123456, timezone.utc)
        updated = datetime.fromtimestamp(1580236840.123456, timezone.utc)
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
        metadata = { 'foo': 'bar' }
        disclaimer = 'testString'
        hidden = True
        provider = 'testString'
        repo_info = repo_info_model

        # Invoke method
        response = service.replace_offering(
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
        assert req_body['rating'] == rating_model
        assert req_body['created'] == '2020-01-28T18:40:40.123456Z'
        assert req_body['updated'] == '2020-01-28T18:40:40.123456Z'
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
        assert req_body['metadata'] == { 'foo': 'bar' }
        assert req_body['disclaimer'] == 'testString'
        assert req_body['hidden'] == True
        assert req_body['provider'] == 'testString'
        assert req_body['repo_info'] == repo_info_model


    #--------------------------------------------------------
    # test_replace_offering_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_offering_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings/testString')
        mock_response = '{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'

        # Invoke method
        response = service.replace_offering(
            catalog_identifier,
            offering_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_replace_offering_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_offering_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings/testString')
        mock_response = '{"id": "id", "_rev": "rev", "label": "label", "short_description": "short_description", "catalog_icon_url": "catalog_icon_url", "tags": ["tags"], "url": "url", "crn": "crn", "offerings_url": "offerings_url", "features": [{"title": "title", "description": "description"}], "disabled": true, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "resource_group_id": "resource_group_id", "owning_account": "owning_account", "catalog_filters": {"include_all": false, "category_filters": {"mapKey": {"include": false, "filter": {"filter_terms": ["filter_terms"]}}}, "id_filters": {"include": {"filter_terms": ["filter_terms"]}, "exclude": {"filter_terms": ["filter_terms"]}}}, "syndication_settings": {"remove_related_components": false, "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "history": {"namespaces": ["namespaces"], "clusters": [{"region": "region", "id": "id", "name": "name", "resource_group_name": "resource_group_name", "type": "type", "namespaces": ["namespaces"], "all_namespaces": true}], "last_run": "2019-01-01T12:00:00"}, "authorization": {"token": "token", "last_run": "2019-01-01T12:00:00"}}}'
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
                service.replace_offering(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_offering
#-----------------------------------------------------------------------------
class TestDeleteOffering():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_offering()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_offering_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'

        # Invoke method
        response = service.delete_offering(
            catalog_identifier,
            offering_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_offering_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_offering_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings/testString')
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
                service.delete_offering(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for replace_offering_icon
#-----------------------------------------------------------------------------
class TestReplaceOfferingIcon():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # replace_offering_icon()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_offering_icon_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings/testString/icon/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
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
        response = service.replace_offering_icon(
            catalog_identifier,
            offering_id,
            file_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_replace_offering_icon_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_offering_icon_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings/testString/icon/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
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
                service.replace_offering_icon(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_offering_ibm
#-----------------------------------------------------------------------------
class TestUpdateOfferingIbm():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_offering_ibm()
    #--------------------------------------------------------
    @responses.activate
    def test_update_offering_ibm_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings/testString/publish/ibm/true')
        mock_response = '{"ibm": false, "public": true, "changed": false}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        approval_type = 'ibm'
        approved = 'true'

        # Invoke method
        response = service.update_offering_ibm(
            catalog_identifier,
            offering_id,
            approval_type,
            approved,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_offering_ibm_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_offering_ibm_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/catalogs/testString/offerings/testString/publish/ibm/true')
        mock_response = '{"ibm": false, "public": true, "changed": false}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        catalog_identifier = 'testString'
        offering_id = 'testString'
        approval_type = 'ibm'
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
                service.update_offering_ibm(**req_copy)



# endregion
##############################################################################
# End of Service: Offerings
##############################################################################

##############################################################################
# Start of Service: Versions
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_version_about
#-----------------------------------------------------------------------------
class TestGetVersionAbout():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_version_about()
    #--------------------------------------------------------
    @responses.activate
    def test_get_version_about_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/about')
        mock_response = '"operation_response"'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='text/markdown',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = service.get_version_about(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_version_about_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_version_about_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/about')
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
                service.get_version_about(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_version_license
#-----------------------------------------------------------------------------
class TestGetVersionLicense():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_version_license()
    #--------------------------------------------------------
    @responses.activate
    def test_get_version_license_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/licenses/testString')
        responses.add(responses.GET,
                      url,
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'
        license_id = 'testString'

        # Invoke method
        response = service.get_version_license(
            version_loc_id,
            license_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_version_license_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_version_license_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/licenses/testString')
        responses.add(responses.GET,
                      url,
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
                service.get_version_license(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_version_container_images
#-----------------------------------------------------------------------------
class TestGetVersionContainerImages():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_version_container_images()
    #--------------------------------------------------------
    @responses.activate
    def test_get_version_container_images_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/containerImages')
        mock_response = '{"description": "description", "images": [{"image": "image"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = service.get_version_container_images(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_version_container_images_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_version_container_images_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/containerImages')
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
                service.get_version_container_images(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for deprecate_version
#-----------------------------------------------------------------------------
class TestDeprecateVersion():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # deprecate_version()
    #--------------------------------------------------------
    @responses.activate
    def test_deprecate_version_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/deprecate')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = service.deprecate_version(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    #--------------------------------------------------------
    # test_deprecate_version_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_deprecate_version_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/deprecate')
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
                service.deprecate_version(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for account_publish_version
#-----------------------------------------------------------------------------
class TestAccountPublishVersion():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # account_publish_version()
    #--------------------------------------------------------
    @responses.activate
    def test_account_publish_version_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/account-publish')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = service.account_publish_version(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    #--------------------------------------------------------
    # test_account_publish_version_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_account_publish_version_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/account-publish')
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
                service.account_publish_version(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for ibm_publish_version
#-----------------------------------------------------------------------------
class TestIbmPublishVersion():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # ibm_publish_version()
    #--------------------------------------------------------
    @responses.activate
    def test_ibm_publish_version_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/ibm-publish')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = service.ibm_publish_version(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    #--------------------------------------------------------
    # test_ibm_publish_version_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_ibm_publish_version_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/ibm-publish')
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
                service.ibm_publish_version(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for public_publish_version
#-----------------------------------------------------------------------------
class TestPublicPublishVersion():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # public_publish_version()
    #--------------------------------------------------------
    @responses.activate
    def test_public_publish_version_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/public-publish')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = service.public_publish_version(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    #--------------------------------------------------------
    # test_public_publish_version_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_public_publish_version_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/public-publish')
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
                service.public_publish_version(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for commit_version
#-----------------------------------------------------------------------------
class TestCommitVersion():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # commit_version()
    #--------------------------------------------------------
    @responses.activate
    def test_commit_version_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/commit')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = service.commit_version(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_commit_version_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_commit_version_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/commit')
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
                service.commit_version(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_version_working_copy
#-----------------------------------------------------------------------------
class TestGetVersionWorkingCopy():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_version_working_copy()
    #--------------------------------------------------------
    @responses.activate
    def test_get_version_working_copy_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/workingcopy')
        mock_response = '{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = service.get_version_working_copy(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_version_working_copy_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_version_working_copy_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/workingcopy')
        mock_response = '{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}'
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
                service.get_version_working_copy(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_version_updates
#-----------------------------------------------------------------------------
class TestGetVersionUpdates():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_version_updates()
    #--------------------------------------------------------
    @responses.activate
    def test_get_version_updates_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/updates')
        mock_response = '[{"version_locator": "version_locator", "version": "version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "package_version": "package_version", "can_update": true, "messages": {"anyKey": "anyValue"}}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'
        cluster_id = 'testString'
        region = 'testString'
        resource_group_id = 'testString'
        namespace = 'testString'

        # Invoke method
        response = service.get_version_updates(
            version_loc_id,
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
        query_string = requests.utils.unquote(query_string)
        assert 'cluster_id={}'.format(cluster_id) in query_string
        assert 'region={}'.format(region) in query_string
        assert 'resource_group_id={}'.format(resource_group_id) in query_string
        assert 'namespace={}'.format(namespace) in query_string


    #--------------------------------------------------------
    # test_get_version_updates_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_version_updates_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/updates')
        mock_response = '[{"version_locator": "version_locator", "version": "version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "package_version": "package_version", "can_update": true, "messages": {"anyKey": "anyValue"}}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = service.get_version_updates(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_version_updates_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_version_updates_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/updates')
        mock_response = '[{"version_locator": "version_locator", "version": "version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "package_version": "package_version", "can_update": true, "messages": {"anyKey": "anyValue"}}]'
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
                service.get_version_updates(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_version
#-----------------------------------------------------------------------------
class TestGetVersion():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_version()
    #--------------------------------------------------------
    @responses.activate
    def test_get_version_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = service.get_version(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_version_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_version_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString')
        mock_response = '{"id": "id", "_rev": "rev", "url": "url", "crn": "crn", "label": "label", "name": "name", "offering_icon_url": "offering_icon_url", "offering_docs_url": "offering_docs_url", "offering_support_url": "offering_support_url", "tags": ["tags"], "rating": {"one_star_count": 14, "two_star_count": 14, "three_star_count": 16, "four_star_count": 15}, "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "short_description": "short_description", "long_description": "long_description", "features": [{"title": "title", "description": "description"}], "kinds": [{"id": "id", "format_kind": "format_kind", "target_kind": "target_kind", "metadata": {"anyKey": "anyValue"}, "install_description": "install_description", "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "versions": [{"id": "id", "_rev": "rev", "crn": "crn", "version": "version", "sha": "sha", "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "offering_id": "offering_id", "catalog_id": "catalog_id", "kind_id": "kind_id", "tags": ["tags"], "repo_url": "repo_url", "source_url": "source_url", "tgz_url": "tgz_url", "configuration": [{"key": "key", "type": "type", "default_value": {"anyKey": "anyValue"}, "value_constraint": "value_constraint", "description": "description", "required": true, "options": [{"anyKey": "anyValue"}], "hidden": true}], "metadata": {"anyKey": "anyValue"}, "validation": {"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}, "required_resources": [{"type": "mem", "value": {"anyKey": "anyValue"}}], "single_instance": false, "install": {"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}, "pre_install": [{"instructions": "instructions", "script": "script", "script_permission": "script_permission", "delete_script": "delete_script", "scope": "scope"}], "entitlement": {"provider_name": "provider_name", "provider_id": "provider_id", "product_id": "product_id", "part_numbers": ["part_numbers"], "image_repo_name": "image_repo_name"}, "licenses": [{"id": "id", "name": "name", "type": "type", "url": "url", "description": "description"}], "image_manifest_url": "image_manifest_url", "deprecated": true, "package_version": "package_version", "state": {"current": "current", "current_entered": "2019-01-01T12:00:00", "pending": "pending", "pending_requested": "2019-01-01T12:00:00", "previous": "previous"}, "version_locator": "version_locator", "console_url": "console_url", "long_description": "long_description", "whitelisted_accounts": ["whitelisted_accounts"]}], "plans": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "additional_features": [{"title": "title", "description": "description"}], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00", "deployments": [{"id": "id", "label": "label", "name": "name", "short_description": "short_description", "long_description": "long_description", "metadata": {"anyKey": "anyValue"}, "tags": ["tags"], "created": "2019-01-01T12:00:00", "updated": "2019-01-01T12:00:00"}]}]}], "permit_request_ibm_public_publish": false, "ibm_publish_approved": true, "public_publish_approved": false, "public_original_crn": "public_original_crn", "publish_public_crn": "publish_public_crn", "portal_approval_record": "portal_approval_record", "portal_ui_url": "portal_ui_url", "catalog_id": "catalog_id", "catalog_name": "catalog_name", "metadata": {"anyKey": "anyValue"}, "disclaimer": "disclaimer", "hidden": true, "provider": "provider", "repo_info": {"token": "token", "type": "type"}}'
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
                service.get_version(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_version
#-----------------------------------------------------------------------------
class TestDeleteVersion():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_version()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_version_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = service.delete_version(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_version_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_version_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString')
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
                service.delete_version(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for list_versions
#-----------------------------------------------------------------------------
class TestListVersions():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_versions()
    #--------------------------------------------------------
    @responses.activate
    def test_list_versions_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions')
        responses.add(responses.GET,
                      url,
                      status=200)

        # Set up parameter values
        q = 'testString'

        # Invoke method
        response = service.list_versions(
            q,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'q={}'.format(q) in query_string


    #--------------------------------------------------------
    # test_list_versions_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_versions_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions')
        responses.add(responses.GET,
                      url,
                      status=200)

        # Set up parameter values
        q = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "q": q,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_versions(**req_copy)



# endregion
##############################################################################
# End of Service: Versions
##############################################################################

##############################################################################
# Start of Service: Repo
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_repos
#-----------------------------------------------------------------------------
class TestGetRepos():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_repos()
    #--------------------------------------------------------
    @responses.activate
    def test_get_repos_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/repo/testString/entries')
        mock_response = '{"chart": {"api_version": "api_version", "created": "2019-01-01T12:00:00", "description": "description", "deprecated": true, "digest": "digest", "home": "home", "icon": "icon", "keywords": ["keywords"], "maintainers": [{"email": "email", "name": "name"}], "name": "name", "tiller_version": "tiller_version", "urls": ["urls"], "sources": ["sources"], "version": "version", "appVersion": "app_version"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        type = 'testString'
        repourl = 'testString'

        # Invoke method
        response = service.get_repos(
            type,
            repourl,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'repourl={}'.format(repourl) in query_string


    #--------------------------------------------------------
    # test_get_repos_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_repos_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/repo/testString/entries')
        mock_response = '{"chart": {"api_version": "api_version", "created": "2019-01-01T12:00:00", "description": "description", "deprecated": true, "digest": "digest", "home": "home", "icon": "icon", "keywords": ["keywords"], "maintainers": [{"email": "email", "name": "name"}], "name": "name", "tiller_version": "tiller_version", "urls": ["urls"], "sources": ["sources"], "version": "version", "appVersion": "app_version"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        type = 'testString'
        repourl = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "type": type,
            "repourl": repourl,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_repos(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_repo
#-----------------------------------------------------------------------------
class TestGetRepo():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_repo()
    #--------------------------------------------------------
    @responses.activate
    def test_get_repo_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/repo/testString')
        mock_response = '{"chart": {"Chart.yaml": {"name": "name", "description": "description", "icon": "icon", "version": "version", "appVersion": "app_version"}, "sha": {"anyKey": "anyValue"}, "README.md": "readme_md", "values-metadata": {"anyKey": "anyValue"}, "license-metadata": {"anyKey": "anyValue"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        type = 'testString'
        charturl = 'testString'

        # Invoke method
        response = service.get_repo(
            type,
            charturl,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'charturl={}'.format(charturl) in query_string


    #--------------------------------------------------------
    # test_get_repo_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_repo_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/repo/testString')
        mock_response = '{"chart": {"Chart.yaml": {"name": "name", "description": "description", "icon": "icon", "version": "version", "appVersion": "app_version"}, "sha": {"anyKey": "anyValue"}, "README.md": "readme_md", "values-metadata": {"anyKey": "anyValue"}, "license-metadata": {"anyKey": "anyValue"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        type = 'testString'
        charturl = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "type": type,
            "charturl": charturl,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_repo(**req_copy)



# endregion
##############################################################################
# End of Service: Repo
##############################################################################

##############################################################################
# Start of Service: Deploy
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_clusters
#-----------------------------------------------------------------------------
class TestListClusters():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_clusters()
    #--------------------------------------------------------
    @responses.activate
    def test_list_clusters_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/kubernetes/clusters')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"resource_group_id": "resource_group_id", "resource_group_name": "resource_group_name", "id": "id", "name": "name", "region": "region"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        limit = 38
        offset = 38
        type = 'testString'

        # Invoke method
        response = service.list_clusters(
            limit=limit,
            offset=offset,
            type=type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'type={}'.format(type) in query_string


    #--------------------------------------------------------
    # test_list_clusters_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_clusters_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/kubernetes/clusters')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"resource_group_id": "resource_group_id", "resource_group_name": "resource_group_name", "id": "id", "name": "name", "region": "region"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_clusters()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_cluster
#-----------------------------------------------------------------------------
class TestGetCluster():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_cluster()
    #--------------------------------------------------------
    @responses.activate
    def test_get_cluster_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/kubernetes/clusters/testString')
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
        response = service.get_cluster(
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
        query_string = requests.utils.unquote(query_string)
        assert 'region={}'.format(region) in query_string


    #--------------------------------------------------------
    # test_get_cluster_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_cluster_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/kubernetes/clusters/testString')
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
                service.get_cluster(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_namespaces
#-----------------------------------------------------------------------------
class TestGetNamespaces():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_namespaces()
    #--------------------------------------------------------
    @responses.activate
    def test_get_namespaces_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/kubernetes/clusters/testString/namespaces')
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
        limit = 38
        offset = 38

        # Invoke method
        response = service.get_namespaces(
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
        query_string = requests.utils.unquote(query_string)
        assert 'region={}'.format(region) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string


    #--------------------------------------------------------
    # test_get_namespaces_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_namespaces_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/kubernetes/clusters/testString/namespaces')
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
        response = service.get_namespaces(
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
        query_string = requests.utils.unquote(query_string)
        assert 'region={}'.format(region) in query_string


    #--------------------------------------------------------
    # test_get_namespaces_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_namespaces_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/kubernetes/clusters/testString/namespaces')
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
                service.get_namespaces(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_operator
#-----------------------------------------------------------------------------
class TestCreateOperator():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_operator()
    #--------------------------------------------------------
    @responses.activate
    def test_create_operator_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/kubernetes/olm/operator')
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
        version_locator_id = 'testString'

        # Invoke method
        response = service.create_operator(
            x_auth_refresh_token,
            cluster_id=cluster_id,
            region=region,
            namespaces=namespaces,
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
        assert req_body['version_locator_id'] == 'testString'


    #--------------------------------------------------------
    # test_create_operator_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_operator_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/kubernetes/olm/operator')
        mock_response = '[{"phase": "phase", "message": "message", "link": "link", "name": "name", "version": "version", "namespace": "namespace", "package_name": "package_name", "catalog_id": "catalog_id"}]'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = service.create_operator(
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_create_operator_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_operator_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/kubernetes/olm/operator')
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
                service.create_operator(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for list_operators
#-----------------------------------------------------------------------------
class TestListOperators():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_operators()
    #--------------------------------------------------------
    @responses.activate
    def test_list_operators_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/kubernetes/olm/operator')
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
        response = service.list_operators(
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
        query_string = requests.utils.unquote(query_string)
        assert 'cluster_id={}'.format(cluster_id) in query_string
        assert 'region={}'.format(region) in query_string
        assert 'version_locator_id={}'.format(version_locator_id) in query_string


    #--------------------------------------------------------
    # test_list_operators_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_operators_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/kubernetes/olm/operator')
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
                service.list_operators(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for replace_operator
#-----------------------------------------------------------------------------
class TestReplaceOperator():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # replace_operator()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_operator_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/kubernetes/olm/operator')
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
        version_locator_id = 'testString'

        # Invoke method
        response = service.replace_operator(
            x_auth_refresh_token,
            cluster_id=cluster_id,
            region=region,
            namespaces=namespaces,
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
        assert req_body['version_locator_id'] == 'testString'


    #--------------------------------------------------------
    # test_replace_operator_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_operator_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/kubernetes/olm/operator')
        mock_response = '[{"phase": "phase", "message": "message", "link": "link", "name": "name", "version": "version", "namespace": "namespace", "package_name": "package_name", "catalog_id": "catalog_id"}]'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = service.replace_operator(
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_replace_operator_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_replace_operator_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/kubernetes/olm/operator')
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
                service.replace_operator(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_operator
#-----------------------------------------------------------------------------
class TestDeleteOperator():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_operator()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_operator_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/kubernetes/olm/operator')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        x_auth_refresh_token = 'testString'
        cluster_id = 'testString'
        region = 'testString'
        version_locator_id = 'testString'

        # Invoke method
        response = service.delete_operator(
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
        query_string = requests.utils.unquote(query_string)
        assert 'cluster_id={}'.format(cluster_id) in query_string
        assert 'region={}'.format(region) in query_string
        assert 'version_locator_id={}'.format(version_locator_id) in query_string


    #--------------------------------------------------------
    # test_delete_operator_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_operator_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/kubernetes/olm/operator')
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
                service.delete_operator(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for install_version
#-----------------------------------------------------------------------------
class TestInstallVersion():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # install_version()
    #--------------------------------------------------------
    @responses.activate
    def test_install_version_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/install')
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
        override_values = { 'foo': 'bar' }
        entitlement_apikey = 'testString'
        schematics = deploy_request_body_schematics_model
        script = 'testString'
        script_id = 'testString'
        version_locator_id = 'testString'
        vcenter_id = 'testString'
        vcenter_password = 'testString'
        vcenter_location = 'testString'

        # Invoke method
        response = service.install_version(
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
            vcenter_password=vcenter_password,
            vcenter_location=vcenter_location,
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
        assert req_body['override_values'] == { 'foo': 'bar' }
        assert req_body['entitlement_apikey'] == 'testString'
        assert req_body['schematics'] == deploy_request_body_schematics_model
        assert req_body['script'] == 'testString'
        assert req_body['script_id'] == 'testString'
        assert req_body['version_locator_id'] == 'testString'
        assert req_body['vcenter_id'] == 'testString'
        assert req_body['vcenter_password'] == 'testString'
        assert req_body['vcenter_location'] == 'testString'


    #--------------------------------------------------------
    # test_install_version_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_install_version_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/install')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = service.install_version(
            version_loc_id,
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    #--------------------------------------------------------
    # test_install_version_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_install_version_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/install')
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
                service.install_version(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for preinstall_version
#-----------------------------------------------------------------------------
class TestPreinstallVersion():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # preinstall_version()
    #--------------------------------------------------------
    @responses.activate
    def test_preinstall_version_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/preinstall')
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
        override_values = { 'foo': 'bar' }
        entitlement_apikey = 'testString'
        schematics = deploy_request_body_schematics_model
        script = 'testString'
        script_id = 'testString'
        version_locator_id = 'testString'
        vcenter_id = 'testString'
        vcenter_password = 'testString'
        vcenter_location = 'testString'

        # Invoke method
        response = service.preinstall_version(
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
            vcenter_password=vcenter_password,
            vcenter_location=vcenter_location,
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
        assert req_body['override_values'] == { 'foo': 'bar' }
        assert req_body['entitlement_apikey'] == 'testString'
        assert req_body['schematics'] == deploy_request_body_schematics_model
        assert req_body['script'] == 'testString'
        assert req_body['script_id'] == 'testString'
        assert req_body['version_locator_id'] == 'testString'
        assert req_body['vcenter_id'] == 'testString'
        assert req_body['vcenter_password'] == 'testString'
        assert req_body['vcenter_location'] == 'testString'


    #--------------------------------------------------------
    # test_preinstall_version_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_preinstall_version_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/preinstall')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = service.preinstall_version(
            version_loc_id,
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    #--------------------------------------------------------
    # test_preinstall_version_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_preinstall_version_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/preinstall')
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
                service.preinstall_version(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_preinstall
#-----------------------------------------------------------------------------
class TestGetPreinstall():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_preinstall()
    #--------------------------------------------------------
    @responses.activate
    def test_get_preinstall_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/preinstall')
        mock_response = '{"metadata": {"cluster_id": "cluster_id", "region": "region", "namespace": "namespace", "workspace_id": "workspace_id", "workspace_name": "workspace_name"}, "release": {"deployments": [{"anyKey": "anyValue"}], "replicasets": [{"anyKey": "anyValue"}], "statefulsets": [{"anyKey": "anyValue"}], "pods": [{"anyKey": "anyValue"}], "errors": [{"anyKey": "anyValue"}]}, "content_mgmt": {"pods": [{"anyKey": "anyValue"}], "errors": [{"anyKey": "anyValue"}]}}'
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
        response = service.get_preinstall(
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
        query_string = requests.utils.unquote(query_string)
        assert 'cluster_id={}'.format(cluster_id) in query_string
        assert 'region={}'.format(region) in query_string
        assert 'namespace={}'.format(namespace) in query_string


    #--------------------------------------------------------
    # test_get_preinstall_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_preinstall_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/preinstall')
        mock_response = '{"metadata": {"cluster_id": "cluster_id", "region": "region", "namespace": "namespace", "workspace_id": "workspace_id", "workspace_name": "workspace_name"}, "release": {"deployments": [{"anyKey": "anyValue"}], "replicasets": [{"anyKey": "anyValue"}], "statefulsets": [{"anyKey": "anyValue"}], "pods": [{"anyKey": "anyValue"}], "errors": [{"anyKey": "anyValue"}]}, "content_mgmt": {"pods": [{"anyKey": "anyValue"}], "errors": [{"anyKey": "anyValue"}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = service.get_preinstall(
            version_loc_id,
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_preinstall_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_preinstall_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/preinstall')
        mock_response = '{"metadata": {"cluster_id": "cluster_id", "region": "region", "namespace": "namespace", "workspace_id": "workspace_id", "workspace_name": "workspace_name"}, "release": {"deployments": [{"anyKey": "anyValue"}], "replicasets": [{"anyKey": "anyValue"}], "statefulsets": [{"anyKey": "anyValue"}], "pods": [{"anyKey": "anyValue"}], "errors": [{"anyKey": "anyValue"}]}, "content_mgmt": {"pods": [{"anyKey": "anyValue"}], "errors": [{"anyKey": "anyValue"}]}}'
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
                service.get_preinstall(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for validation_install
#-----------------------------------------------------------------------------
class TestValidationInstall():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # validation_install()
    #--------------------------------------------------------
    @responses.activate
    def test_validation_install_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/validation/install')
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
        override_values = { 'foo': 'bar' }
        entitlement_apikey = 'testString'
        schematics = deploy_request_body_schematics_model
        script = 'testString'
        script_id = 'testString'
        version_locator_id = 'testString'
        vcenter_id = 'testString'
        vcenter_password = 'testString'
        vcenter_location = 'testString'

        # Invoke method
        response = service.validation_install(
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
            vcenter_password=vcenter_password,
            vcenter_location=vcenter_location,
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
        assert req_body['override_values'] == { 'foo': 'bar' }
        assert req_body['entitlement_apikey'] == 'testString'
        assert req_body['schematics'] == deploy_request_body_schematics_model
        assert req_body['script'] == 'testString'
        assert req_body['script_id'] == 'testString'
        assert req_body['version_locator_id'] == 'testString'
        assert req_body['vcenter_id'] == 'testString'
        assert req_body['vcenter_password'] == 'testString'
        assert req_body['vcenter_location'] == 'testString'


    #--------------------------------------------------------
    # test_validation_install_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_validation_install_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/validation/install')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = service.validation_install(
            version_loc_id,
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    #--------------------------------------------------------
    # test_validation_install_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_validation_install_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/validation/install')
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
                service.validation_install(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_validation_status
#-----------------------------------------------------------------------------
class TestGetValidationStatus():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_validation_status()
    #--------------------------------------------------------
    @responses.activate
    def test_get_validation_status_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/validation/install')
        mock_response = '{"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = service.get_validation_status(
            version_loc_id,
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_validation_status_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_validation_status_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/validation/install')
        mock_response = '{"validated": "2019-01-01T12:00:00", "requested": "2019-01-01T12:00:00", "state": "state", "last_operation": "last_operation", "target": {"anyKey": "anyValue"}}'
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
                service.get_validation_status(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_override_values
#-----------------------------------------------------------------------------
class TestGetOverrideValues():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_override_values()
    #--------------------------------------------------------
    @responses.activate
    def test_get_override_values_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/validation/overridevalues')
        mock_response = '{"mapKey": {"anyKey": "anyValue"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'

        # Invoke method
        response = service.get_override_values(
            version_loc_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_override_values_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_override_values_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/validation/overridevalues')
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
                service.get_override_values(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_schematics_workspaces
#-----------------------------------------------------------------------------
class TestGetSchematicsWorkspaces():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_schematics_workspaces()
    #--------------------------------------------------------
    @responses.activate
    def test_get_schematics_workspaces_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/workspaces')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "name": "name", "type": ["type"], "description": "description", "tags": ["tags"], "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "status": "status", "workspace_status": {"frozen": true, "locked": true}, "template_ref": "template_ref", "template_repo": {"repo_url": "repo_url", "chart_name": "chart_name", "script_name": "script_name", "uninstall_script_name": "uninstall_script_name", "folder_name": "folder_name", "repo_sha_value": "repo_sha_value"}, "template_data": [{"anyKey": "anyValue"}], "runtime_data": {"id": "id", "engine_name": "engine_name", "engine_version": "engine_version", "state_store_url": "state_store_url", "log_store_url": "log_store_url"}, "shared_data": {"anyKey": "anyValue"}, "catalog_ref": {"item_id": "item_id", "item_name": "item_name", "item_url": "item_url"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'
        x_auth_refresh_token = 'testString'

        # Invoke method
        response = service.get_schematics_workspaces(
            version_loc_id,
            x_auth_refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_schematics_workspaces_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_schematics_workspaces_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/workspaces')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "name": "name", "type": ["type"], "description": "description", "tags": ["tags"], "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "status": "status", "workspace_status": {"frozen": true, "locked": true}, "template_ref": "template_ref", "template_repo": {"repo_url": "repo_url", "chart_name": "chart_name", "script_name": "script_name", "uninstall_script_name": "uninstall_script_name", "folder_name": "folder_name", "repo_sha_value": "repo_sha_value"}, "template_data": [{"anyKey": "anyValue"}], "runtime_data": {"id": "id", "engine_name": "engine_name", "engine_version": "engine_version", "state_store_url": "state_store_url", "log_store_url": "log_store_url"}, "shared_data": {"anyKey": "anyValue"}, "catalog_ref": {"item_id": "item_id", "item_name": "item_name", "item_url": "item_url"}}]}'
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
                service.get_schematics_workspaces(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for can_deploy_schematics
#-----------------------------------------------------------------------------
class TestCanDeploySchematics():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # can_deploy_schematics()
    #--------------------------------------------------------
    @responses.activate
    def test_can_deploy_schematics_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/candeploy')
        mock_response = '{"pre_install": {"anyKey": "anyValue"}, "install": {"anyKey": "anyValue"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'
        cluster_id = 'testString'
        region = 'testString'
        namespace = 'testString'
        resource_group_id = 'testString'

        # Invoke method
        response = service.can_deploy_schematics(
            version_loc_id,
            cluster_id,
            region,
            namespace=namespace,
            resource_group_id=resource_group_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'cluster_id={}'.format(cluster_id) in query_string
        assert 'region={}'.format(region) in query_string
        assert 'namespace={}'.format(namespace) in query_string
        assert 'resource_group_id={}'.format(resource_group_id) in query_string


    #--------------------------------------------------------
    # test_can_deploy_schematics_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_can_deploy_schematics_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/candeploy')
        mock_response = '{"pre_install": {"anyKey": "anyValue"}, "install": {"anyKey": "anyValue"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'
        cluster_id = 'testString'
        region = 'testString'

        # Invoke method
        response = service.can_deploy_schematics(
            version_loc_id,
            cluster_id,
            region,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'cluster_id={}'.format(cluster_id) in query_string
        assert 'region={}'.format(region) in query_string


    #--------------------------------------------------------
    # test_can_deploy_schematics_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_can_deploy_schematics_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/versions/testString/candeploy')
        mock_response = '{"pre_install": {"anyKey": "anyValue"}, "install": {"anyKey": "anyValue"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        version_loc_id = 'testString'
        cluster_id = 'testString'
        region = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "version_loc_id": version_loc_id,
            "cluster_id": cluster_id,
            "region": region,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.can_deploy_schematics(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_resource_groups
#-----------------------------------------------------------------------------
class TestGetResourceGroups():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_resource_groups()
    #--------------------------------------------------------
    @responses.activate
    def test_get_resource_groups_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/deploy/schematics/resourcegroups')
        mock_response = '{"offset": 6, "limit": 5, "total_count": 11, "resource_count": 14, "first": "first", "last": "last", "prev": "prev", "next": "next", "resources": [{"id": "id", "name": "name", "crn": "crn", "account_id": "account_id", "state": "state", "default": false}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_resource_groups()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Deploy
##############################################################################

##############################################################################
# Start of Service: Licensing
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_license_providers
#-----------------------------------------------------------------------------
class TestGetLicenseProviders():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_license_providers()
    #--------------------------------------------------------
    @responses.activate
    def test_get_license_providers_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/license/license_providers')
        mock_response = '{"total_results": 13, "total_pages": 11, "prev_url": "prev_url", "next_url": "next_url", "resources": [{"name": "name", "short_description": "short_description", "id": "id", "licence_type": "licence_type", "offering_type": "offering_type", "create_url": "create_url", "info_url": "info_url", "url": "url", "crn": "crn", "state": "state"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_license_providers()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for list_license_entitlements
#-----------------------------------------------------------------------------
class TestListLicenseEntitlements():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_license_entitlements()
    #--------------------------------------------------------
    @responses.activate
    def test_list_license_entitlements_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/license/entitlements')
        mock_response = '{"total_results": 13, "total_pages": 11, "prev_url": "prev_url", "next_url": "next_url", "resources": [{"name": "name", "id": "id", "crn": "crn", "url": "url", "offering_type": "offering_type", "state": "state", "effective_from": "effective_from", "effective_until": "effective_until", "account_id": "account_id", "owner_id": "owner_id", "version_id": "version_id", "license_offering_id": "license_offering_id", "license_id": "license_id", "license_owner_id": "license_owner_id", "license_type": "license_type", "license_provider_id": "license_provider_id", "license_provider_url": "license_provider_url", "license_product_id": "license_product_id", "namespace_repository": "namespace_repository", "apikey": "apikey", "create_by": "create_by", "update_by": "update_by", "create_at": "create_at", "updated_at": "updated_at", "history": [{"action": "action", "user": "user", "date": "date"}], "offering_list": [{"id": "id", "name": "name", "label": "label", "offering_icon_url": "offering_icon_url", "account_id": "account_id", "catalog_id": "catalog_id"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        license_product_id = 'testString'
        version_id = 'testString'
        state = 'testString'

        # Invoke method
        response = service.list_license_entitlements(
            account_id=account_id,
            license_product_id=license_product_id,
            version_id=version_id,
            state=state,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'license_product_id={}'.format(license_product_id) in query_string
        assert 'version_id={}'.format(version_id) in query_string
        assert 'state={}'.format(state) in query_string


    #--------------------------------------------------------
    # test_list_license_entitlements_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_license_entitlements_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/license/entitlements')
        mock_response = '{"total_results": 13, "total_pages": 11, "prev_url": "prev_url", "next_url": "next_url", "resources": [{"name": "name", "id": "id", "crn": "crn", "url": "url", "offering_type": "offering_type", "state": "state", "effective_from": "effective_from", "effective_until": "effective_until", "account_id": "account_id", "owner_id": "owner_id", "version_id": "version_id", "license_offering_id": "license_offering_id", "license_id": "license_id", "license_owner_id": "license_owner_id", "license_type": "license_type", "license_provider_id": "license_provider_id", "license_provider_url": "license_provider_url", "license_product_id": "license_product_id", "namespace_repository": "namespace_repository", "apikey": "apikey", "create_by": "create_by", "update_by": "update_by", "create_at": "create_at", "updated_at": "updated_at", "history": [{"action": "action", "user": "user", "date": "date"}], "offering_list": [{"id": "id", "name": "name", "label": "label", "offering_icon_url": "offering_icon_url", "account_id": "account_id", "catalog_id": "catalog_id"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_license_entitlements()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_license_entitlement
#-----------------------------------------------------------------------------
class TestCreateLicenseEntitlement():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_license_entitlement()
    #--------------------------------------------------------
    @responses.activate
    def test_create_license_entitlement_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/license/entitlements')
        mock_response = '{"name": "name", "id": "id", "crn": "crn", "url": "url", "offering_type": "offering_type", "state": "state", "effective_from": "effective_from", "effective_until": "effective_until", "account_id": "account_id", "owner_id": "owner_id", "version_id": "version_id", "license_offering_id": "license_offering_id", "license_id": "license_id", "license_owner_id": "license_owner_id", "license_type": "license_type", "license_provider_id": "license_provider_id", "license_provider_url": "license_provider_url", "license_product_id": "license_product_id", "namespace_repository": "namespace_repository", "apikey": "apikey", "create_by": "create_by", "update_by": "update_by", "create_at": "create_at", "updated_at": "updated_at", "history": [{"action": "action", "user": "user", "date": "date"}], "offering_list": [{"id": "id", "name": "name", "label": "label", "offering_icon_url": "offering_icon_url", "account_id": "account_id", "catalog_id": "catalog_id"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        name = 'testString'
        effective_from = 'testString'
        effective_until = 'testString'
        version_id = 'testString'
        license_id = 'testString'
        license_owner_id = 'testString'
        license_provider_id = 'testString'
        license_product_id = 'testString'
        account_id = 'testString'

        # Invoke method
        response = service.create_license_entitlement(
            name=name,
            effective_from=effective_from,
            effective_until=effective_until,
            version_id=version_id,
            license_id=license_id,
            license_owner_id=license_owner_id,
            license_provider_id=license_provider_id,
            license_product_id=license_product_id,
            account_id=account_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['effective_from'] == 'testString'
        assert req_body['effective_until'] == 'testString'
        assert req_body['version_id'] == 'testString'
        assert req_body['license_id'] == 'testString'
        assert req_body['license_owner_id'] == 'testString'
        assert req_body['license_provider_id'] == 'testString'
        assert req_body['license_product_id'] == 'testString'


    #--------------------------------------------------------
    # test_create_license_entitlement_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_license_entitlement_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/license/entitlements')
        mock_response = '{"name": "name", "id": "id", "crn": "crn", "url": "url", "offering_type": "offering_type", "state": "state", "effective_from": "effective_from", "effective_until": "effective_until", "account_id": "account_id", "owner_id": "owner_id", "version_id": "version_id", "license_offering_id": "license_offering_id", "license_id": "license_id", "license_owner_id": "license_owner_id", "license_type": "license_type", "license_provider_id": "license_provider_id", "license_provider_url": "license_provider_url", "license_product_id": "license_product_id", "namespace_repository": "namespace_repository", "apikey": "apikey", "create_by": "create_by", "update_by": "update_by", "create_at": "create_at", "updated_at": "updated_at", "history": [{"action": "action", "user": "user", "date": "date"}], "offering_list": [{"id": "id", "name": "name", "label": "label", "offering_icon_url": "offering_icon_url", "account_id": "account_id", "catalog_id": "catalog_id"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.create_license_entitlement()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_license_entitlements
#-----------------------------------------------------------------------------
class TestGetLicenseEntitlements():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_license_entitlements()
    #--------------------------------------------------------
    @responses.activate
    def test_get_license_entitlements_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/license/entitlements/productID/testString')
        mock_response = '{"total_results": 13, "total_pages": 11, "prev_url": "prev_url", "next_url": "next_url", "resources": [{"name": "name", "id": "id", "crn": "crn", "url": "url", "offering_type": "offering_type", "state": "state", "effective_from": "effective_from", "effective_until": "effective_until", "account_id": "account_id", "owner_id": "owner_id", "version_id": "version_id", "license_offering_id": "license_offering_id", "license_id": "license_id", "license_owner_id": "license_owner_id", "license_type": "license_type", "license_provider_id": "license_provider_id", "license_provider_url": "license_provider_url", "license_product_id": "license_product_id", "namespace_repository": "namespace_repository", "apikey": "apikey", "create_by": "create_by", "update_by": "update_by", "create_at": "create_at", "updated_at": "updated_at", "history": [{"action": "action", "user": "user", "date": "date"}], "offering_list": [{"id": "id", "name": "name", "label": "label", "offering_icon_url": "offering_icon_url", "account_id": "account_id", "catalog_id": "catalog_id"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        license_product_id = 'testString'
        account_id = 'testString'
        version_id = 'testString'

        # Invoke method
        response = service.get_license_entitlements(
            license_product_id,
            account_id=account_id,
            version_id=version_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'version_id={}'.format(version_id) in query_string


    #--------------------------------------------------------
    # test_get_license_entitlements_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_license_entitlements_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/license/entitlements/productID/testString')
        mock_response = '{"total_results": 13, "total_pages": 11, "prev_url": "prev_url", "next_url": "next_url", "resources": [{"name": "name", "id": "id", "crn": "crn", "url": "url", "offering_type": "offering_type", "state": "state", "effective_from": "effective_from", "effective_until": "effective_until", "account_id": "account_id", "owner_id": "owner_id", "version_id": "version_id", "license_offering_id": "license_offering_id", "license_id": "license_id", "license_owner_id": "license_owner_id", "license_type": "license_type", "license_provider_id": "license_provider_id", "license_provider_url": "license_provider_url", "license_product_id": "license_product_id", "namespace_repository": "namespace_repository", "apikey": "apikey", "create_by": "create_by", "update_by": "update_by", "create_at": "create_at", "updated_at": "updated_at", "history": [{"action": "action", "user": "user", "date": "date"}], "offering_list": [{"id": "id", "name": "name", "label": "label", "offering_icon_url": "offering_icon_url", "account_id": "account_id", "catalog_id": "catalog_id"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        license_product_id = 'testString'

        # Invoke method
        response = service.get_license_entitlements(
            license_product_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_license_entitlements_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_license_entitlements_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/license/entitlements/productID/testString')
        mock_response = '{"total_results": 13, "total_pages": 11, "prev_url": "prev_url", "next_url": "next_url", "resources": [{"name": "name", "id": "id", "crn": "crn", "url": "url", "offering_type": "offering_type", "state": "state", "effective_from": "effective_from", "effective_until": "effective_until", "account_id": "account_id", "owner_id": "owner_id", "version_id": "version_id", "license_offering_id": "license_offering_id", "license_id": "license_id", "license_owner_id": "license_owner_id", "license_type": "license_type", "license_provider_id": "license_provider_id", "license_provider_url": "license_provider_url", "license_product_id": "license_product_id", "namespace_repository": "namespace_repository", "apikey": "apikey", "create_by": "create_by", "update_by": "update_by", "create_at": "create_at", "updated_at": "updated_at", "history": [{"action": "action", "user": "user", "date": "date"}], "offering_list": [{"id": "id", "name": "name", "label": "label", "offering_icon_url": "offering_icon_url", "account_id": "account_id", "catalog_id": "catalog_id"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        license_product_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "license_product_id": license_product_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_license_entitlements(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_license_entitlement
#-----------------------------------------------------------------------------
class TestDeleteLicenseEntitlement():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_license_entitlement()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_license_entitlement_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/license/entitlements/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        entitlement_id = 'testString'
        account_id = 'testString'

        # Invoke method
        response = service.delete_license_entitlement(
            entitlement_id,
            account_id=account_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'account_id={}'.format(account_id) in query_string


    #--------------------------------------------------------
    # test_delete_license_entitlement_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_license_entitlement_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/license/entitlements/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        entitlement_id = 'testString'

        # Invoke method
        response = service.delete_license_entitlement(
            entitlement_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_license_entitlement_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_license_entitlement_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/license/entitlements/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        entitlement_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "entitlement_id": entitlement_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_license_entitlement(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_licenses
#-----------------------------------------------------------------------------
class TestGetLicenses():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_licenses()
    #--------------------------------------------------------
    @responses.activate
    def test_get_licenses_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/license/licenses')
        mock_response = '{"total_results": 13, "total_pages": 11, "prev_url": "prev_url", "next_url": "next_url", "resources": [{"name": "name", "offering_type": "offering_type", "seats_allowed": "seats_allowed", "seats_used": "seats_used", "owner_id": "owner_id", "license_offering_id": "license_offering_id", "license_id": "license_id", "license_owner_id": "license_owner_id", "license_type": "license_type", "license_provider_id": "license_provider_id", "license_product_id": "license_product_id", "license_provider_url": "license_provider_url", "effective_from": "effective_from", "effective_until": "effective_until", "internal": true, "offering_list": [{"id": "id", "name": "name", "label": "label", "offering_icon_url": "offering_icon_url", "account_id": "account_id", "catalog_id": "catalog_id"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        license_provider_id = 'testString'
        account_id = 'testString'
        name = 'testString'
        license_type = 'testString'
        license_product_id = 'testString'

        # Invoke method
        response = service.get_licenses(
            license_provider_id,
            account_id=account_id,
            name=name,
            license_type=license_type,
            license_product_id=license_product_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'license_provider_id={}'.format(license_provider_id) in query_string
        assert 'account_id={}'.format(account_id) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'license_type={}'.format(license_type) in query_string
        assert 'license_product_id={}'.format(license_product_id) in query_string


    #--------------------------------------------------------
    # test_get_licenses_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_licenses_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/license/licenses')
        mock_response = '{"total_results": 13, "total_pages": 11, "prev_url": "prev_url", "next_url": "next_url", "resources": [{"name": "name", "offering_type": "offering_type", "seats_allowed": "seats_allowed", "seats_used": "seats_used", "owner_id": "owner_id", "license_offering_id": "license_offering_id", "license_id": "license_id", "license_owner_id": "license_owner_id", "license_type": "license_type", "license_provider_id": "license_provider_id", "license_product_id": "license_product_id", "license_provider_url": "license_provider_url", "effective_from": "effective_from", "effective_until": "effective_until", "internal": true, "offering_list": [{"id": "id", "name": "name", "label": "label", "offering_icon_url": "offering_icon_url", "account_id": "account_id", "catalog_id": "catalog_id"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        license_provider_id = 'testString'

        # Invoke method
        response = service.get_licenses(
            license_provider_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'license_provider_id={}'.format(license_provider_id) in query_string


    #--------------------------------------------------------
    # test_get_licenses_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_licenses_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/license/licenses')
        mock_response = '{"total_results": 13, "total_pages": 11, "prev_url": "prev_url", "next_url": "next_url", "resources": [{"name": "name", "offering_type": "offering_type", "seats_allowed": "seats_allowed", "seats_used": "seats_used", "owner_id": "owner_id", "license_offering_id": "license_offering_id", "license_id": "license_id", "license_owner_id": "license_owner_id", "license_type": "license_type", "license_provider_id": "license_provider_id", "license_product_id": "license_product_id", "license_provider_url": "license_provider_url", "effective_from": "effective_from", "effective_until": "effective_until", "internal": true, "offering_list": [{"id": "id", "name": "name", "label": "label", "offering_icon_url": "offering_icon_url", "account_id": "account_id", "catalog_id": "catalog_id"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        license_provider_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "license_provider_id": license_provider_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_licenses(**req_copy)



# endregion
##############################################################################
# End of Service: Licensing
##############################################################################

##############################################################################
# Start of Service: CrossAccountSearch
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for search_license_versions
#-----------------------------------------------------------------------------
class TestSearchLicenseVersions():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # search_license_versions()
    #--------------------------------------------------------
    @responses.activate
    def test_search_license_versions_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/search/license/versions')
        responses.add(responses.GET,
                      url,
                      status=200)

        # Set up parameter values
        q = 'testString'

        # Invoke method
        response = service.search_license_versions(
            q,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'q={}'.format(q) in query_string


    #--------------------------------------------------------
    # test_search_license_versions_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_search_license_versions_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/search/license/versions')
        responses.add(responses.GET,
                      url,
                      status=200)

        # Set up parameter values
        q = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "q": q,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.search_license_versions(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for search_license_offerings
#-----------------------------------------------------------------------------
class TestSearchLicenseOfferings():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # search_license_offerings()
    #--------------------------------------------------------
    @responses.activate
    def test_search_license_offerings_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/search/license/offerings')
        responses.add(responses.GET,
                      url,
                      status=200)

        # Set up parameter values
        q = 'testString'

        # Invoke method
        response = service.search_license_offerings(
            q,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'q={}'.format(q) in query_string


    #--------------------------------------------------------
    # test_search_license_offerings_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_search_license_offerings_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/search/license/offerings')
        responses.add(responses.GET,
                      url,
                      status=200)

        # Set up parameter values
        q = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "q": q,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.search_license_offerings(**req_copy)



# endregion
##############################################################################
# End of Service: CrossAccountSearch
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for Account
#-----------------------------------------------------------------------------
class TestAccount():

    #--------------------------------------------------------
    # Test serialization/deserialization for Account
    #--------------------------------------------------------
    def test_account_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for AccountGroup
#-----------------------------------------------------------------------------
class TestAccountGroup():

    #--------------------------------------------------------
    # Test serialization/deserialization for AccountGroup
    #--------------------------------------------------------
    def test_account_group_serialization(self):

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

        # Construct a json representation of a AccountGroup model
        account_group_model_json = {}
        account_group_model_json['id'] = 'testString'
        account_group_model_json['account_filters'] = filters_model

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

#-----------------------------------------------------------------------------
# Test Class for AccumulatedFilters
#-----------------------------------------------------------------------------
class TestAccumulatedFilters():

    #--------------------------------------------------------
    # Test serialization/deserialization for AccumulatedFilters
    #--------------------------------------------------------
    def test_accumulated_filters_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        filter_terms_model = {} # FilterTerms
        filter_terms_model['filter_terms'] = ['testString']

        category_filter_model = {} # CategoryFilter
        category_filter_model['include'] = True
        category_filter_model['filter'] = filter_terms_model

        id_filter_model = {} # IDFilter
        id_filter_model['include'] = filter_terms_model
        id_filter_model['exclude'] = filter_terms_model

        accumulated_filters_catalog_filters_item_catalog_model = {} # AccumulatedFiltersCatalogFiltersItemCatalog
        accumulated_filters_catalog_filters_item_catalog_model['id'] = 'testString'
        accumulated_filters_catalog_filters_item_catalog_model['name'] = 'testString'

        filters_model = {} # Filters
        filters_model['include_all'] = True
        filters_model['category_filters'] = {}
        filters_model['id_filters'] = id_filter_model

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

#-----------------------------------------------------------------------------
# Test Class for AccumulatedFiltersCatalogFiltersItem
#-----------------------------------------------------------------------------
class TestAccumulatedFiltersCatalogFiltersItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for AccumulatedFiltersCatalogFiltersItem
    #--------------------------------------------------------
    def test_accumulated_filters_catalog_filters_item_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        filter_terms_model = {} # FilterTerms
        filter_terms_model['filter_terms'] = ['testString']

        category_filter_model = {} # CategoryFilter
        category_filter_model['include'] = True
        category_filter_model['filter'] = filter_terms_model

        id_filter_model = {} # IDFilter
        id_filter_model['include'] = filter_terms_model
        id_filter_model['exclude'] = filter_terms_model

        accumulated_filters_catalog_filters_item_catalog_model = {} # AccumulatedFiltersCatalogFiltersItemCatalog
        accumulated_filters_catalog_filters_item_catalog_model['id'] = 'testString'
        accumulated_filters_catalog_filters_item_catalog_model['name'] = 'testString'

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

#-----------------------------------------------------------------------------
# Test Class for AccumulatedFiltersCatalogFiltersItemCatalog
#-----------------------------------------------------------------------------
class TestAccumulatedFiltersCatalogFiltersItemCatalog():

    #--------------------------------------------------------
    # Test serialization/deserialization for AccumulatedFiltersCatalogFiltersItemCatalog
    #--------------------------------------------------------
    def test_accumulated_filters_catalog_filters_item_catalog_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for ApprovalResult
#-----------------------------------------------------------------------------
class TestApprovalResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for ApprovalResult
    #--------------------------------------------------------
    def test_approval_result_serialization(self):

        # Construct a json representation of a ApprovalResult model
        approval_result_model_json = {}
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

#-----------------------------------------------------------------------------
# Test Class for Catalog
#-----------------------------------------------------------------------------
class TestCatalog():

    #--------------------------------------------------------
    # Test serialization/deserialization for Catalog
    #--------------------------------------------------------
    def test_catalog_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        filter_terms_model = {} # FilterTerms
        filter_terms_model['filter_terms'] = ['testString']

        syndication_cluster_model = {} # SyndicationCluster
        syndication_cluster_model['region'] = 'testString'
        syndication_cluster_model['id'] = 'testString'
        syndication_cluster_model['name'] = 'testString'
        syndication_cluster_model['resource_group_name'] = 'testString'
        syndication_cluster_model['type'] = 'testString'
        syndication_cluster_model['namespaces'] = ['testString']
        syndication_cluster_model['all_namespaces'] = True

        category_filter_model = {} # CategoryFilter
        category_filter_model['include'] = True
        category_filter_model['filter'] = filter_terms_model

        id_filter_model = {} # IDFilter
        id_filter_model['include'] = filter_terms_model
        id_filter_model['exclude'] = filter_terms_model

        syndication_authorization_model = {} # SyndicationAuthorization
        syndication_authorization_model['token'] = 'testString'
        syndication_authorization_model['last_run'] = '2020-01-28T18:40:40.123456Z'

        syndication_history_model = {} # SyndicationHistory
        syndication_history_model['namespaces'] = ['testString']
        syndication_history_model['clusters'] = [syndication_cluster_model]
        syndication_history_model['last_run'] = '2020-01-28T18:40:40.123456Z'

        feature_model = {} # Feature
        feature_model['title'] = 'testString'
        feature_model['description'] = 'testString'

        filters_model = {} # Filters
        filters_model['include_all'] = True
        filters_model['category_filters'] = {}
        filters_model['id_filters'] = id_filter_model

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
        catalog_model_json['created'] = '2020-01-28T18:40:40.123456Z'
        catalog_model_json['updated'] = '2020-01-28T18:40:40.123456Z'
        catalog_model_json['resource_group_id'] = 'testString'
        catalog_model_json['owning_account'] = 'testString'
        catalog_model_json['catalog_filters'] = filters_model
        catalog_model_json['syndication_settings'] = syndication_resource_model

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

#-----------------------------------------------------------------------------
# Test Class for CatalogSearchResult
#-----------------------------------------------------------------------------
class TestCatalogSearchResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for CatalogSearchResult
    #--------------------------------------------------------
    def test_catalog_search_result_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        filter_terms_model = {} # FilterTerms
        filter_terms_model['filter_terms'] = ['testString']

        syndication_cluster_model = {} # SyndicationCluster
        syndication_cluster_model['region'] = 'testString'
        syndication_cluster_model['id'] = 'testString'
        syndication_cluster_model['name'] = 'testString'
        syndication_cluster_model['resource_group_name'] = 'testString'
        syndication_cluster_model['type'] = 'testString'
        syndication_cluster_model['namespaces'] = ['testString']
        syndication_cluster_model['all_namespaces'] = True

        category_filter_model = {} # CategoryFilter
        category_filter_model['include'] = True
        category_filter_model['filter'] = filter_terms_model

        id_filter_model = {} # IDFilter
        id_filter_model['include'] = filter_terms_model
        id_filter_model['exclude'] = filter_terms_model

        syndication_authorization_model = {} # SyndicationAuthorization
        syndication_authorization_model['token'] = 'testString'
        syndication_authorization_model['last_run'] = '2020-01-28T18:40:40.123456Z'

        syndication_history_model = {} # SyndicationHistory
        syndication_history_model['namespaces'] = ['testString']
        syndication_history_model['clusters'] = [syndication_cluster_model]
        syndication_history_model['last_run'] = '2020-01-28T18:40:40.123456Z'

        feature_model = {} # Feature
        feature_model['title'] = 'testString'
        feature_model['description'] = 'testString'

        filters_model = {} # Filters
        filters_model['include_all'] = True
        filters_model['category_filters'] = {}
        filters_model['id_filters'] = id_filter_model

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
        catalog_model['created'] = '2020-01-28T18:40:40.123456Z'
        catalog_model['updated'] = '2020-01-28T18:40:40.123456Z'
        catalog_model['resource_group_id'] = 'testString'
        catalog_model['owning_account'] = 'testString'
        catalog_model['catalog_filters'] = filters_model
        catalog_model['syndication_settings'] = syndication_resource_model

        # Construct a json representation of a CatalogSearchResult model
        catalog_search_result_model_json = {}
        catalog_search_result_model_json['offset'] = 38
        catalog_search_result_model_json['limit'] = 38
        catalog_search_result_model_json['total_count'] = 38
        catalog_search_result_model_json['resource_count'] = 38
        catalog_search_result_model_json['first'] = 'testString'
        catalog_search_result_model_json['last'] = 'testString'
        catalog_search_result_model_json['prev'] = 'testString'
        catalog_search_result_model_json['next'] = 'testString'
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

#-----------------------------------------------------------------------------
# Test Class for CategoryFilter
#-----------------------------------------------------------------------------
class TestCategoryFilter():

    #--------------------------------------------------------
    # Test serialization/deserialization for CategoryFilter
    #--------------------------------------------------------
    def test_category_filter_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for ClusterInfo
#-----------------------------------------------------------------------------
class TestClusterInfo():

    #--------------------------------------------------------
    # Test serialization/deserialization for ClusterInfo
    #--------------------------------------------------------
    def test_cluster_info_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for ClusterSearchResult
#-----------------------------------------------------------------------------
class TestClusterSearchResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for ClusterSearchResult
    #--------------------------------------------------------
    def test_cluster_search_result_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        cluster_info_model = {} # ClusterInfo
        cluster_info_model['resource_group_id'] = 'testString'
        cluster_info_model['resource_group_name'] = 'testString'
        cluster_info_model['id'] = 'testString'
        cluster_info_model['name'] = 'testString'
        cluster_info_model['region'] = 'testString'

        # Construct a json representation of a ClusterSearchResult model
        cluster_search_result_model_json = {}
        cluster_search_result_model_json['offset'] = 38
        cluster_search_result_model_json['limit'] = 38
        cluster_search_result_model_json['total_count'] = 38
        cluster_search_result_model_json['resource_count'] = 38
        cluster_search_result_model_json['first'] = 'testString'
        cluster_search_result_model_json['last'] = 'testString'
        cluster_search_result_model_json['prev'] = 'testString'
        cluster_search_result_model_json['next'] = 'testString'
        cluster_search_result_model_json['resources'] = [cluster_info_model]

        # Construct a model instance of ClusterSearchResult by calling from_dict on the json representation
        cluster_search_result_model = ClusterSearchResult.from_dict(cluster_search_result_model_json)
        assert cluster_search_result_model != False

        # Construct a model instance of ClusterSearchResult by calling from_dict on the json representation
        cluster_search_result_model_dict = ClusterSearchResult.from_dict(cluster_search_result_model_json).__dict__
        cluster_search_result_model2 = ClusterSearchResult(**cluster_search_result_model_dict)

        # Verify the model instances are equivalent
        assert cluster_search_result_model == cluster_search_result_model2

        # Convert model instance back to dict and verify no loss of data
        cluster_search_result_model_json2 = cluster_search_result_model.to_dict()
        assert cluster_search_result_model_json2 == cluster_search_result_model_json

#-----------------------------------------------------------------------------
# Test Class for Configuration
#-----------------------------------------------------------------------------
class TestConfiguration():

    #--------------------------------------------------------
    # Test serialization/deserialization for Configuration
    #--------------------------------------------------------
    def test_configuration_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for DeployRequestBodySchematics
#-----------------------------------------------------------------------------
class TestDeployRequestBodySchematics():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeployRequestBodySchematics
    #--------------------------------------------------------
    def test_deploy_request_body_schematics_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for DeployRequirementsCheck
#-----------------------------------------------------------------------------
class TestDeployRequirementsCheck():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeployRequirementsCheck
    #--------------------------------------------------------
    def test_deploy_requirements_check_serialization(self):

        # Construct a json representation of a DeployRequirementsCheck model
        deploy_requirements_check_model_json = {}
        deploy_requirements_check_model_json['pre_install'] = { 'foo': 'bar' }
        deploy_requirements_check_model_json['install'] = { 'foo': 'bar' }

        # Construct a model instance of DeployRequirementsCheck by calling from_dict on the json representation
        deploy_requirements_check_model = DeployRequirementsCheck.from_dict(deploy_requirements_check_model_json)
        assert deploy_requirements_check_model != False

        # Construct a model instance of DeployRequirementsCheck by calling from_dict on the json representation
        deploy_requirements_check_model_dict = DeployRequirementsCheck.from_dict(deploy_requirements_check_model_json).__dict__
        deploy_requirements_check_model2 = DeployRequirementsCheck(**deploy_requirements_check_model_dict)

        # Verify the model instances are equivalent
        assert deploy_requirements_check_model == deploy_requirements_check_model2

        # Convert model instance back to dict and verify no loss of data
        deploy_requirements_check_model_json2 = deploy_requirements_check_model.to_dict()
        assert deploy_requirements_check_model_json2 == deploy_requirements_check_model_json

#-----------------------------------------------------------------------------
# Test Class for Deployment
#-----------------------------------------------------------------------------
class TestDeployment():

    #--------------------------------------------------------
    # Test serialization/deserialization for Deployment
    #--------------------------------------------------------
    def test_deployment_serialization(self):

        # Construct a json representation of a Deployment model
        deployment_model_json = {}
        deployment_model_json['id'] = 'testString'
        deployment_model_json['label'] = 'testString'
        deployment_model_json['name'] = 'testString'
        deployment_model_json['short_description'] = 'testString'
        deployment_model_json['long_description'] = 'testString'
        deployment_model_json['metadata'] = { 'foo': 'bar' }
        deployment_model_json['tags'] = ['testString']
        deployment_model_json['created'] = '2020-01-28T18:40:40.123456Z'
        deployment_model_json['updated'] = '2020-01-28T18:40:40.123456Z'

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

#-----------------------------------------------------------------------------
# Test Class for Enterprise
#-----------------------------------------------------------------------------
class TestEnterprise():

    #--------------------------------------------------------
    # Test serialization/deserialization for Enterprise
    #--------------------------------------------------------
    def test_enterprise_serialization(self):

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

        account_group_model = {} # AccountGroup
        account_group_model['id'] = 'testString'
        account_group_model['account_filters'] = filters_model

        enterprise_account_groups_model = {} # EnterpriseAccountGroups
        enterprise_account_groups_model['keys'] = account_group_model

        # Construct a json representation of a Enterprise model
        enterprise_model_json = {}
        enterprise_model_json['id'] = 'testString'
        enterprise_model_json['_rev'] = 'testString'
        enterprise_model_json['account_filters'] = filters_model
        enterprise_model_json['account_groups'] = enterprise_account_groups_model

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

#-----------------------------------------------------------------------------
# Test Class for EnterpriseAccountGroups
#-----------------------------------------------------------------------------
class TestEnterpriseAccountGroups():

    #--------------------------------------------------------
    # Test serialization/deserialization for EnterpriseAccountGroups
    #--------------------------------------------------------
    def test_enterprise_account_groups_serialization(self):

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

        account_group_model = {} # AccountGroup
        account_group_model['id'] = 'testString'
        account_group_model['account_filters'] = filters_model

        # Construct a json representation of a EnterpriseAccountGroups model
        enterprise_account_groups_model_json = {}
        enterprise_account_groups_model_json['keys'] = account_group_model

        # Construct a model instance of EnterpriseAccountGroups by calling from_dict on the json representation
        enterprise_account_groups_model = EnterpriseAccountGroups.from_dict(enterprise_account_groups_model_json)
        assert enterprise_account_groups_model != False

        # Construct a model instance of EnterpriseAccountGroups by calling from_dict on the json representation
        enterprise_account_groups_model_dict = EnterpriseAccountGroups.from_dict(enterprise_account_groups_model_json).__dict__
        enterprise_account_groups_model2 = EnterpriseAccountGroups(**enterprise_account_groups_model_dict)

        # Verify the model instances are equivalent
        assert enterprise_account_groups_model == enterprise_account_groups_model2

        # Convert model instance back to dict and verify no loss of data
        enterprise_account_groups_model_json2 = enterprise_account_groups_model.to_dict()
        assert enterprise_account_groups_model_json2 == enterprise_account_groups_model_json

#-----------------------------------------------------------------------------
# Test Class for Feature
#-----------------------------------------------------------------------------
class TestFeature():

    #--------------------------------------------------------
    # Test serialization/deserialization for Feature
    #--------------------------------------------------------
    def test_feature_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for FilterTerms
#-----------------------------------------------------------------------------
class TestFilterTerms():

    #--------------------------------------------------------
    # Test serialization/deserialization for FilterTerms
    #--------------------------------------------------------
    def test_filter_terms_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for Filters
#-----------------------------------------------------------------------------
class TestFilters():

    #--------------------------------------------------------
    # Test serialization/deserialization for Filters
    #--------------------------------------------------------
    def test_filters_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for HelmChart
#-----------------------------------------------------------------------------
class TestHelmChart():

    #--------------------------------------------------------
    # Test serialization/deserialization for HelmChart
    #--------------------------------------------------------
    def test_helm_chart_serialization(self):

        # Construct a json representation of a HelmChart model
        helm_chart_model_json = {}
        helm_chart_model_json['name'] = 'testString'
        helm_chart_model_json['description'] = 'testString'
        helm_chart_model_json['icon'] = 'testString'
        helm_chart_model_json['version'] = 'testString'
        helm_chart_model_json['appVersion'] = 'testString'

        # Construct a model instance of HelmChart by calling from_dict on the json representation
        helm_chart_model = HelmChart.from_dict(helm_chart_model_json)
        assert helm_chart_model != False

        # Construct a model instance of HelmChart by calling from_dict on the json representation
        helm_chart_model_dict = HelmChart.from_dict(helm_chart_model_json).__dict__
        helm_chart_model2 = HelmChart(**helm_chart_model_dict)

        # Verify the model instances are equivalent
        assert helm_chart_model == helm_chart_model2

        # Convert model instance back to dict and verify no loss of data
        helm_chart_model_json2 = helm_chart_model.to_dict()
        assert helm_chart_model_json2 == helm_chart_model_json

#-----------------------------------------------------------------------------
# Test Class for HelmPackage
#-----------------------------------------------------------------------------
class TestHelmPackage():

    #--------------------------------------------------------
    # Test serialization/deserialization for HelmPackage
    #--------------------------------------------------------
    def test_helm_package_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        helm_chart_model = {} # HelmChart
        helm_chart_model['name'] = 'testString'
        helm_chart_model['description'] = 'testString'
        helm_chart_model['icon'] = 'testString'
        helm_chart_model['version'] = 'testString'
        helm_chart_model['appVersion'] = 'testString'

        helm_package_chart_model = {} # HelmPackageChart
        helm_package_chart_model['Chart.yaml'] = helm_chart_model
        helm_package_chart_model['sha'] = { 'foo': 'bar' }
        helm_package_chart_model['README.md'] = 'testString'
        helm_package_chart_model['values-metadata'] = { 'foo': 'bar' }
        helm_package_chart_model['license-metadata'] = { 'foo': 'bar' }

        # Construct a json representation of a HelmPackage model
        helm_package_model_json = {}
        helm_package_model_json['chart'] = helm_package_chart_model

        # Construct a model instance of HelmPackage by calling from_dict on the json representation
        helm_package_model = HelmPackage.from_dict(helm_package_model_json)
        assert helm_package_model != False

        # Construct a model instance of HelmPackage by calling from_dict on the json representation
        helm_package_model_dict = HelmPackage.from_dict(helm_package_model_json).__dict__
        helm_package_model2 = HelmPackage(**helm_package_model_dict)

        # Verify the model instances are equivalent
        assert helm_package_model == helm_package_model2

        # Convert model instance back to dict and verify no loss of data
        helm_package_model_json2 = helm_package_model.to_dict()
        assert helm_package_model_json2 == helm_package_model_json

#-----------------------------------------------------------------------------
# Test Class for HelmPackageChart
#-----------------------------------------------------------------------------
class TestHelmPackageChart():

    #--------------------------------------------------------
    # Test serialization/deserialization for HelmPackageChart
    #--------------------------------------------------------
    def test_helm_package_chart_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        helm_chart_model = {} # HelmChart
        helm_chart_model['name'] = 'testString'
        helm_chart_model['description'] = 'testString'
        helm_chart_model['icon'] = 'testString'
        helm_chart_model['version'] = 'testString'
        helm_chart_model['appVersion'] = 'testString'

        # Construct a json representation of a HelmPackageChart model
        helm_package_chart_model_json = {}
        helm_package_chart_model_json['Chart.yaml'] = helm_chart_model
        helm_package_chart_model_json['sha'] = { 'foo': 'bar' }
        helm_package_chart_model_json['README.md'] = 'testString'
        helm_package_chart_model_json['values-metadata'] = { 'foo': 'bar' }
        helm_package_chart_model_json['license-metadata'] = { 'foo': 'bar' }

        # Construct a model instance of HelmPackageChart by calling from_dict on the json representation
        helm_package_chart_model = HelmPackageChart.from_dict(helm_package_chart_model_json)
        assert helm_package_chart_model != False

        # Construct a model instance of HelmPackageChart by calling from_dict on the json representation
        helm_package_chart_model_dict = HelmPackageChart.from_dict(helm_package_chart_model_json).__dict__
        helm_package_chart_model2 = HelmPackageChart(**helm_package_chart_model_dict)

        # Verify the model instances are equivalent
        assert helm_package_chart_model == helm_package_chart_model2

        # Convert model instance back to dict and verify no loss of data
        helm_package_chart_model_json2 = helm_package_chart_model.to_dict()
        assert helm_package_chart_model_json2 == helm_package_chart_model_json

#-----------------------------------------------------------------------------
# Test Class for HelmRepoList
#-----------------------------------------------------------------------------
class TestHelmRepoList():

    #--------------------------------------------------------
    # Test serialization/deserialization for HelmRepoList
    #--------------------------------------------------------
    def test_helm_repo_list_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        maintainers_model = {} # Maintainers
        maintainers_model['email'] = 'testString'
        maintainers_model['name'] = 'testString'

        helm_repo_list_chart_model = {} # HelmRepoListChart
        helm_repo_list_chart_model['api_version'] = 'testString'
        helm_repo_list_chart_model['created'] = '2020-01-28T18:40:40.123456Z'
        helm_repo_list_chart_model['description'] = 'testString'
        helm_repo_list_chart_model['deprecated'] = True
        helm_repo_list_chart_model['digest'] = 'testString'
        helm_repo_list_chart_model['home'] = 'testString'
        helm_repo_list_chart_model['icon'] = 'testString'
        helm_repo_list_chart_model['keywords'] = ['testString']
        helm_repo_list_chart_model['maintainers'] = [maintainers_model]
        helm_repo_list_chart_model['name'] = 'testString'
        helm_repo_list_chart_model['tiller_version'] = 'testString'
        helm_repo_list_chart_model['urls'] = ['testString']
        helm_repo_list_chart_model['sources'] = ['testString']
        helm_repo_list_chart_model['version'] = 'testString'
        helm_repo_list_chart_model['appVersion'] = 'testString'

        # Construct a json representation of a HelmRepoList model
        helm_repo_list_model_json = {}
        helm_repo_list_model_json['chart'] = helm_repo_list_chart_model

        # Construct a model instance of HelmRepoList by calling from_dict on the json representation
        helm_repo_list_model = HelmRepoList.from_dict(helm_repo_list_model_json)
        assert helm_repo_list_model != False

        # Construct a model instance of HelmRepoList by calling from_dict on the json representation
        helm_repo_list_model_dict = HelmRepoList.from_dict(helm_repo_list_model_json).__dict__
        helm_repo_list_model2 = HelmRepoList(**helm_repo_list_model_dict)

        # Verify the model instances are equivalent
        assert helm_repo_list_model == helm_repo_list_model2

        # Convert model instance back to dict and verify no loss of data
        helm_repo_list_model_json2 = helm_repo_list_model.to_dict()
        assert helm_repo_list_model_json2 == helm_repo_list_model_json

#-----------------------------------------------------------------------------
# Test Class for HelmRepoListChart
#-----------------------------------------------------------------------------
class TestHelmRepoListChart():

    #--------------------------------------------------------
    # Test serialization/deserialization for HelmRepoListChart
    #--------------------------------------------------------
    def test_helm_repo_list_chart_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        maintainers_model = {} # Maintainers
        maintainers_model['email'] = 'testString'
        maintainers_model['name'] = 'testString'

        # Construct a json representation of a HelmRepoListChart model
        helm_repo_list_chart_model_json = {}
        helm_repo_list_chart_model_json['api_version'] = 'testString'
        helm_repo_list_chart_model_json['created'] = '2020-01-28T18:40:40.123456Z'
        helm_repo_list_chart_model_json['description'] = 'testString'
        helm_repo_list_chart_model_json['deprecated'] = True
        helm_repo_list_chart_model_json['digest'] = 'testString'
        helm_repo_list_chart_model_json['home'] = 'testString'
        helm_repo_list_chart_model_json['icon'] = 'testString'
        helm_repo_list_chart_model_json['keywords'] = ['testString']
        helm_repo_list_chart_model_json['maintainers'] = [maintainers_model]
        helm_repo_list_chart_model_json['name'] = 'testString'
        helm_repo_list_chart_model_json['tiller_version'] = 'testString'
        helm_repo_list_chart_model_json['urls'] = ['testString']
        helm_repo_list_chart_model_json['sources'] = ['testString']
        helm_repo_list_chart_model_json['version'] = 'testString'
        helm_repo_list_chart_model_json['appVersion'] = 'testString'

        # Construct a model instance of HelmRepoListChart by calling from_dict on the json representation
        helm_repo_list_chart_model = HelmRepoListChart.from_dict(helm_repo_list_chart_model_json)
        assert helm_repo_list_chart_model != False

        # Construct a model instance of HelmRepoListChart by calling from_dict on the json representation
        helm_repo_list_chart_model_dict = HelmRepoListChart.from_dict(helm_repo_list_chart_model_json).__dict__
        helm_repo_list_chart_model2 = HelmRepoListChart(**helm_repo_list_chart_model_dict)

        # Verify the model instances are equivalent
        assert helm_repo_list_chart_model == helm_repo_list_chart_model2

        # Convert model instance back to dict and verify no loss of data
        helm_repo_list_chart_model_json2 = helm_repo_list_chart_model.to_dict()
        assert helm_repo_list_chart_model_json2 == helm_repo_list_chart_model_json

#-----------------------------------------------------------------------------
# Test Class for IDFilter
#-----------------------------------------------------------------------------
class TestIDFilter():

    #--------------------------------------------------------
    # Test serialization/deserialization for IDFilter
    #--------------------------------------------------------
    def test_id_filter_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for Image
#-----------------------------------------------------------------------------
class TestImage():

    #--------------------------------------------------------
    # Test serialization/deserialization for Image
    #--------------------------------------------------------
    def test_image_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for ImageManifest
#-----------------------------------------------------------------------------
class TestImageManifest():

    #--------------------------------------------------------
    # Test serialization/deserialization for ImageManifest
    #--------------------------------------------------------
    def test_image_manifest_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for InstallStatus
#-----------------------------------------------------------------------------
class TestInstallStatus():

    #--------------------------------------------------------
    # Test serialization/deserialization for InstallStatus
    #--------------------------------------------------------
    def test_install_status_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        install_status_content_mgmt_model = {} # InstallStatusContentMgmt
        install_status_content_mgmt_model['pods'] = [{ 'foo': 'bar' }]
        install_status_content_mgmt_model['errors'] = [{ 'foo': 'bar' }]

        install_status_metadata_model = {} # InstallStatusMetadata
        install_status_metadata_model['cluster_id'] = 'testString'
        install_status_metadata_model['region'] = 'testString'
        install_status_metadata_model['namespace'] = 'testString'
        install_status_metadata_model['workspace_id'] = 'testString'
        install_status_metadata_model['workspace_name'] = 'testString'

        install_status_release_model = {} # InstallStatusRelease
        install_status_release_model['deployments'] = [{ 'foo': 'bar' }]
        install_status_release_model['replicasets'] = [{ 'foo': 'bar' }]
        install_status_release_model['statefulsets'] = [{ 'foo': 'bar' }]
        install_status_release_model['pods'] = [{ 'foo': 'bar' }]
        install_status_release_model['errors'] = [{ 'foo': 'bar' }]

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

#-----------------------------------------------------------------------------
# Test Class for InstallStatusContentMgmt
#-----------------------------------------------------------------------------
class TestInstallStatusContentMgmt():

    #--------------------------------------------------------
    # Test serialization/deserialization for InstallStatusContentMgmt
    #--------------------------------------------------------
    def test_install_status_content_mgmt_serialization(self):

        # Construct a json representation of a InstallStatusContentMgmt model
        install_status_content_mgmt_model_json = {}
        install_status_content_mgmt_model_json['pods'] = [{ 'foo': 'bar' }]
        install_status_content_mgmt_model_json['errors'] = [{ 'foo': 'bar' }]

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

#-----------------------------------------------------------------------------
# Test Class for InstallStatusMetadata
#-----------------------------------------------------------------------------
class TestInstallStatusMetadata():

    #--------------------------------------------------------
    # Test serialization/deserialization for InstallStatusMetadata
    #--------------------------------------------------------
    def test_install_status_metadata_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for InstallStatusRelease
#-----------------------------------------------------------------------------
class TestInstallStatusRelease():

    #--------------------------------------------------------
    # Test serialization/deserialization for InstallStatusRelease
    #--------------------------------------------------------
    def test_install_status_release_serialization(self):

        # Construct a json representation of a InstallStatusRelease model
        install_status_release_model_json = {}
        install_status_release_model_json['deployments'] = [{ 'foo': 'bar' }]
        install_status_release_model_json['replicasets'] = [{ 'foo': 'bar' }]
        install_status_release_model_json['statefulsets'] = [{ 'foo': 'bar' }]
        install_status_release_model_json['pods'] = [{ 'foo': 'bar' }]
        install_status_release_model_json['errors'] = [{ 'foo': 'bar' }]

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

#-----------------------------------------------------------------------------
# Test Class for Kind
#-----------------------------------------------------------------------------
class TestKind():

    #--------------------------------------------------------
    # Test serialization/deserialization for Kind
    #--------------------------------------------------------
    def test_kind_serialization(self):

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

        deployment_model = {} # Deployment
        deployment_model['id'] = 'testString'
        deployment_model['label'] = 'testString'
        deployment_model['name'] = 'testString'
        deployment_model['short_description'] = 'testString'
        deployment_model['long_description'] = 'testString'
        deployment_model['metadata'] = { 'foo': 'bar' }
        deployment_model['tags'] = ['testString']
        deployment_model['created'] = '2020-01-28T18:40:40.123456Z'
        deployment_model['updated'] = '2020-01-28T18:40:40.123456Z'

        feature_model = {} # Feature
        feature_model['title'] = 'testString'
        feature_model['description'] = 'testString'

        license_model = {} # License
        license_model['id'] = 'testString'
        license_model['name'] = 'testString'
        license_model['type'] = 'testString'
        license_model['url'] = 'testString'
        license_model['description'] = 'testString'

        resource_model = {} # Resource
        resource_model['type'] = 'mem'
        resource_model['value'] = { 'foo': 'bar' }

        script_model = {} # Script
        script_model['instructions'] = 'testString'
        script_model['script'] = 'testString'
        script_model['script_permission'] = 'testString'
        script_model['delete_script'] = 'testString'
        script_model['scope'] = 'testString'

        state_model = {} # State
        state_model['current'] = 'testString'
        state_model['current_entered'] = '2020-01-28T18:40:40.123456Z'
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = '2020-01-28T18:40:40.123456Z'
        state_model['previous'] = 'testString'

        validation_model = {} # Validation
        validation_model['validated'] = '2020-01-28T18:40:40.123456Z'
        validation_model['requested'] = '2020-01-28T18:40:40.123456Z'
        validation_model['state'] = 'testString'
        validation_model['last_operation'] = 'testString'
        validation_model['target'] = { 'foo': 'bar' }

        version_entitlement_model = {} # VersionEntitlement
        version_entitlement_model['provider_name'] = 'testString'
        version_entitlement_model['provider_id'] = 'testString'
        version_entitlement_model['product_id'] = 'testString'
        version_entitlement_model['part_numbers'] = ['testString']
        version_entitlement_model['image_repo_name'] = 'testString'

        plan_model = {} # Plan
        plan_model['id'] = 'testString'
        plan_model['label'] = 'testString'
        plan_model['name'] = 'testString'
        plan_model['short_description'] = 'testString'
        plan_model['long_description'] = 'testString'
        plan_model['metadata'] = { 'foo': 'bar' }
        plan_model['tags'] = ['testString']
        plan_model['additional_features'] = [feature_model]
        plan_model['created'] = '2020-01-28T18:40:40.123456Z'
        plan_model['updated'] = '2020-01-28T18:40:40.123456Z'
        plan_model['deployments'] = [deployment_model]

        version_model = {} # Version
        version_model['id'] = 'testString'
        version_model['_rev'] = 'testString'
        version_model['crn'] = 'testString'
        version_model['version'] = 'testString'
        version_model['sha'] = 'testString'
        version_model['created'] = '2020-01-28T18:40:40.123456Z'
        version_model['updated'] = '2020-01-28T18:40:40.123456Z'
        version_model['offering_id'] = 'testString'
        version_model['catalog_id'] = 'testString'
        version_model['kind_id'] = 'testString'
        version_model['tags'] = ['testString']
        version_model['repo_url'] = 'testString'
        version_model['source_url'] = 'testString'
        version_model['tgz_url'] = 'testString'
        version_model['configuration'] = [configuration_model]
        version_model['metadata'] = { 'foo': 'bar' }
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

        # Construct a json representation of a Kind model
        kind_model_json = {}
        kind_model_json['id'] = 'testString'
        kind_model_json['format_kind'] = 'testString'
        kind_model_json['target_kind'] = 'testString'
        kind_model_json['metadata'] = { 'foo': 'bar' }
        kind_model_json['install_description'] = 'testString'
        kind_model_json['tags'] = ['testString']
        kind_model_json['additional_features'] = [feature_model]
        kind_model_json['created'] = '2020-01-28T18:40:40.123456Z'
        kind_model_json['updated'] = '2020-01-28T18:40:40.123456Z'
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

#-----------------------------------------------------------------------------
# Test Class for License
#-----------------------------------------------------------------------------
class TestLicense():

    #--------------------------------------------------------
    # Test serialization/deserialization for License
    #--------------------------------------------------------
    def test_license_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for LicenseEntitlement
#-----------------------------------------------------------------------------
class TestLicenseEntitlement():

    #--------------------------------------------------------
    # Test serialization/deserialization for LicenseEntitlement
    #--------------------------------------------------------
    def test_license_entitlement_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        license_entitlement_history_item_model = {} # LicenseEntitlementHistoryItem
        license_entitlement_history_item_model['action'] = 'testString'
        license_entitlement_history_item_model['user'] = 'testString'
        license_entitlement_history_item_model['date'] = 'testString'

        license_offering_reference_model = {} # LicenseOfferingReference
        license_offering_reference_model['id'] = 'testString'
        license_offering_reference_model['name'] = 'testString'
        license_offering_reference_model['label'] = 'testString'
        license_offering_reference_model['offering_icon_url'] = 'testString'
        license_offering_reference_model['account_id'] = 'testString'
        license_offering_reference_model['catalog_id'] = 'testString'

        # Construct a json representation of a LicenseEntitlement model
        license_entitlement_model_json = {}
        license_entitlement_model_json['name'] = 'testString'
        license_entitlement_model_json['id'] = 'testString'
        license_entitlement_model_json['crn'] = 'testString'
        license_entitlement_model_json['url'] = 'testString'
        license_entitlement_model_json['offering_type'] = 'testString'
        license_entitlement_model_json['state'] = 'testString'
        license_entitlement_model_json['effective_from'] = 'testString'
        license_entitlement_model_json['effective_until'] = 'testString'
        license_entitlement_model_json['account_id'] = 'testString'
        license_entitlement_model_json['owner_id'] = 'testString'
        license_entitlement_model_json['version_id'] = 'testString'
        license_entitlement_model_json['license_offering_id'] = 'testString'
        license_entitlement_model_json['license_id'] = 'testString'
        license_entitlement_model_json['license_owner_id'] = 'testString'
        license_entitlement_model_json['license_type'] = 'testString'
        license_entitlement_model_json['license_provider_id'] = 'testString'
        license_entitlement_model_json['license_provider_url'] = 'testString'
        license_entitlement_model_json['license_product_id'] = 'testString'
        license_entitlement_model_json['namespace_repository'] = 'testString'
        license_entitlement_model_json['apikey'] = 'testString'
        license_entitlement_model_json['create_by'] = 'testString'
        license_entitlement_model_json['update_by'] = 'testString'
        license_entitlement_model_json['create_at'] = 'testString'
        license_entitlement_model_json['updated_at'] = 'testString'
        license_entitlement_model_json['history'] = [license_entitlement_history_item_model]
        license_entitlement_model_json['offering_list'] = [license_offering_reference_model]

        # Construct a model instance of LicenseEntitlement by calling from_dict on the json representation
        license_entitlement_model = LicenseEntitlement.from_dict(license_entitlement_model_json)
        assert license_entitlement_model != False

        # Construct a model instance of LicenseEntitlement by calling from_dict on the json representation
        license_entitlement_model_dict = LicenseEntitlement.from_dict(license_entitlement_model_json).__dict__
        license_entitlement_model2 = LicenseEntitlement(**license_entitlement_model_dict)

        # Verify the model instances are equivalent
        assert license_entitlement_model == license_entitlement_model2

        # Convert model instance back to dict and verify no loss of data
        license_entitlement_model_json2 = license_entitlement_model.to_dict()
        assert license_entitlement_model_json2 == license_entitlement_model_json

#-----------------------------------------------------------------------------
# Test Class for LicenseEntitlementHistoryItem
#-----------------------------------------------------------------------------
class TestLicenseEntitlementHistoryItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for LicenseEntitlementHistoryItem
    #--------------------------------------------------------
    def test_license_entitlement_history_item_serialization(self):

        # Construct a json representation of a LicenseEntitlementHistoryItem model
        license_entitlement_history_item_model_json = {}
        license_entitlement_history_item_model_json['action'] = 'testString'
        license_entitlement_history_item_model_json['user'] = 'testString'
        license_entitlement_history_item_model_json['date'] = 'testString'

        # Construct a model instance of LicenseEntitlementHistoryItem by calling from_dict on the json representation
        license_entitlement_history_item_model = LicenseEntitlementHistoryItem.from_dict(license_entitlement_history_item_model_json)
        assert license_entitlement_history_item_model != False

        # Construct a model instance of LicenseEntitlementHistoryItem by calling from_dict on the json representation
        license_entitlement_history_item_model_dict = LicenseEntitlementHistoryItem.from_dict(license_entitlement_history_item_model_json).__dict__
        license_entitlement_history_item_model2 = LicenseEntitlementHistoryItem(**license_entitlement_history_item_model_dict)

        # Verify the model instances are equivalent
        assert license_entitlement_history_item_model == license_entitlement_history_item_model2

        # Convert model instance back to dict and verify no loss of data
        license_entitlement_history_item_model_json2 = license_entitlement_history_item_model.to_dict()
        assert license_entitlement_history_item_model_json2 == license_entitlement_history_item_model_json

#-----------------------------------------------------------------------------
# Test Class for LicenseEntitlements
#-----------------------------------------------------------------------------
class TestLicenseEntitlements():

    #--------------------------------------------------------
    # Test serialization/deserialization for LicenseEntitlements
    #--------------------------------------------------------
    def test_license_entitlements_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        license_entitlement_history_item_model = {} # LicenseEntitlementHistoryItem
        license_entitlement_history_item_model['action'] = 'testString'
        license_entitlement_history_item_model['user'] = 'testString'
        license_entitlement_history_item_model['date'] = 'testString'

        license_offering_reference_model = {} # LicenseOfferingReference
        license_offering_reference_model['id'] = 'testString'
        license_offering_reference_model['name'] = 'testString'
        license_offering_reference_model['label'] = 'testString'
        license_offering_reference_model['offering_icon_url'] = 'testString'
        license_offering_reference_model['account_id'] = 'testString'
        license_offering_reference_model['catalog_id'] = 'testString'

        license_entitlement_model = {} # LicenseEntitlement
        license_entitlement_model['name'] = 'testString'
        license_entitlement_model['id'] = 'testString'
        license_entitlement_model['crn'] = 'testString'
        license_entitlement_model['url'] = 'testString'
        license_entitlement_model['offering_type'] = 'testString'
        license_entitlement_model['state'] = 'testString'
        license_entitlement_model['effective_from'] = 'testString'
        license_entitlement_model['effective_until'] = 'testString'
        license_entitlement_model['account_id'] = 'testString'
        license_entitlement_model['owner_id'] = 'testString'
        license_entitlement_model['version_id'] = 'testString'
        license_entitlement_model['license_offering_id'] = 'testString'
        license_entitlement_model['license_id'] = 'testString'
        license_entitlement_model['license_owner_id'] = 'testString'
        license_entitlement_model['license_type'] = 'testString'
        license_entitlement_model['license_provider_id'] = 'testString'
        license_entitlement_model['license_provider_url'] = 'testString'
        license_entitlement_model['license_product_id'] = 'testString'
        license_entitlement_model['namespace_repository'] = 'testString'
        license_entitlement_model['apikey'] = 'testString'
        license_entitlement_model['create_by'] = 'testString'
        license_entitlement_model['update_by'] = 'testString'
        license_entitlement_model['create_at'] = 'testString'
        license_entitlement_model['updated_at'] = 'testString'
        license_entitlement_model['history'] = [license_entitlement_history_item_model]
        license_entitlement_model['offering_list'] = [license_offering_reference_model]

        # Construct a json representation of a LicenseEntitlements model
        license_entitlements_model_json = {}
        license_entitlements_model_json['total_results'] = 38
        license_entitlements_model_json['total_pages'] = 38
        license_entitlements_model_json['prev_url'] = 'testString'
        license_entitlements_model_json['next_url'] = 'testString'
        license_entitlements_model_json['resources'] = [license_entitlement_model]

        # Construct a model instance of LicenseEntitlements by calling from_dict on the json representation
        license_entitlements_model = LicenseEntitlements.from_dict(license_entitlements_model_json)
        assert license_entitlements_model != False

        # Construct a model instance of LicenseEntitlements by calling from_dict on the json representation
        license_entitlements_model_dict = LicenseEntitlements.from_dict(license_entitlements_model_json).__dict__
        license_entitlements_model2 = LicenseEntitlements(**license_entitlements_model_dict)

        # Verify the model instances are equivalent
        assert license_entitlements_model == license_entitlements_model2

        # Convert model instance back to dict and verify no loss of data
        license_entitlements_model_json2 = license_entitlements_model.to_dict()
        assert license_entitlements_model_json2 == license_entitlements_model_json

#-----------------------------------------------------------------------------
# Test Class for LicenseObject
#-----------------------------------------------------------------------------
class TestLicenseObject():

    #--------------------------------------------------------
    # Test serialization/deserialization for LicenseObject
    #--------------------------------------------------------
    def test_license_object_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        license_offering_reference_model = {} # LicenseOfferingReference
        license_offering_reference_model['id'] = 'testString'
        license_offering_reference_model['name'] = 'testString'
        license_offering_reference_model['label'] = 'testString'
        license_offering_reference_model['offering_icon_url'] = 'testString'
        license_offering_reference_model['account_id'] = 'testString'
        license_offering_reference_model['catalog_id'] = 'testString'

        # Construct a json representation of a LicenseObject model
        license_object_model_json = {}
        license_object_model_json['name'] = 'testString'
        license_object_model_json['offering_type'] = 'testString'
        license_object_model_json['seats_allowed'] = 'testString'
        license_object_model_json['seats_used'] = 'testString'
        license_object_model_json['owner_id'] = 'testString'
        license_object_model_json['license_offering_id'] = 'testString'
        license_object_model_json['license_id'] = 'testString'
        license_object_model_json['license_owner_id'] = 'testString'
        license_object_model_json['license_type'] = 'testString'
        license_object_model_json['license_provider_id'] = 'testString'
        license_object_model_json['license_product_id'] = 'testString'
        license_object_model_json['license_provider_url'] = 'testString'
        license_object_model_json['effective_from'] = 'testString'
        license_object_model_json['effective_until'] = 'testString'
        license_object_model_json['internal'] = True
        license_object_model_json['offering_list'] = [license_offering_reference_model]

        # Construct a model instance of LicenseObject by calling from_dict on the json representation
        license_object_model = LicenseObject.from_dict(license_object_model_json)
        assert license_object_model != False

        # Construct a model instance of LicenseObject by calling from_dict on the json representation
        license_object_model_dict = LicenseObject.from_dict(license_object_model_json).__dict__
        license_object_model2 = LicenseObject(**license_object_model_dict)

        # Verify the model instances are equivalent
        assert license_object_model == license_object_model2

        # Convert model instance back to dict and verify no loss of data
        license_object_model_json2 = license_object_model.to_dict()
        assert license_object_model_json2 == license_object_model_json

#-----------------------------------------------------------------------------
# Test Class for LicenseOfferingReference
#-----------------------------------------------------------------------------
class TestLicenseOfferingReference():

    #--------------------------------------------------------
    # Test serialization/deserialization for LicenseOfferingReference
    #--------------------------------------------------------
    def test_license_offering_reference_serialization(self):

        # Construct a json representation of a LicenseOfferingReference model
        license_offering_reference_model_json = {}
        license_offering_reference_model_json['id'] = 'testString'
        license_offering_reference_model_json['name'] = 'testString'
        license_offering_reference_model_json['label'] = 'testString'
        license_offering_reference_model_json['offering_icon_url'] = 'testString'
        license_offering_reference_model_json['account_id'] = 'testString'
        license_offering_reference_model_json['catalog_id'] = 'testString'

        # Construct a model instance of LicenseOfferingReference by calling from_dict on the json representation
        license_offering_reference_model = LicenseOfferingReference.from_dict(license_offering_reference_model_json)
        assert license_offering_reference_model != False

        # Construct a model instance of LicenseOfferingReference by calling from_dict on the json representation
        license_offering_reference_model_dict = LicenseOfferingReference.from_dict(license_offering_reference_model_json).__dict__
        license_offering_reference_model2 = LicenseOfferingReference(**license_offering_reference_model_dict)

        # Verify the model instances are equivalent
        assert license_offering_reference_model == license_offering_reference_model2

        # Convert model instance back to dict and verify no loss of data
        license_offering_reference_model_json2 = license_offering_reference_model.to_dict()
        assert license_offering_reference_model_json2 == license_offering_reference_model_json

#-----------------------------------------------------------------------------
# Test Class for LicenseProvider
#-----------------------------------------------------------------------------
class TestLicenseProvider():

    #--------------------------------------------------------
    # Test serialization/deserialization for LicenseProvider
    #--------------------------------------------------------
    def test_license_provider_serialization(self):

        # Construct a json representation of a LicenseProvider model
        license_provider_model_json = {}
        license_provider_model_json['name'] = 'testString'
        license_provider_model_json['short_description'] = 'testString'
        license_provider_model_json['id'] = 'testString'
        license_provider_model_json['licence_type'] = 'testString'
        license_provider_model_json['offering_type'] = 'testString'
        license_provider_model_json['create_url'] = 'testString'
        license_provider_model_json['info_url'] = 'testString'
        license_provider_model_json['url'] = 'testString'
        license_provider_model_json['crn'] = 'testString'
        license_provider_model_json['state'] = 'testString'

        # Construct a model instance of LicenseProvider by calling from_dict on the json representation
        license_provider_model = LicenseProvider.from_dict(license_provider_model_json)
        assert license_provider_model != False

        # Construct a model instance of LicenseProvider by calling from_dict on the json representation
        license_provider_model_dict = LicenseProvider.from_dict(license_provider_model_json).__dict__
        license_provider_model2 = LicenseProvider(**license_provider_model_dict)

        # Verify the model instances are equivalent
        assert license_provider_model == license_provider_model2

        # Convert model instance back to dict and verify no loss of data
        license_provider_model_json2 = license_provider_model.to_dict()
        assert license_provider_model_json2 == license_provider_model_json

#-----------------------------------------------------------------------------
# Test Class for LicenseProviders
#-----------------------------------------------------------------------------
class TestLicenseProviders():

    #--------------------------------------------------------
    # Test serialization/deserialization for LicenseProviders
    #--------------------------------------------------------
    def test_license_providers_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        license_provider_model = {} # LicenseProvider
        license_provider_model['name'] = 'testString'
        license_provider_model['short_description'] = 'testString'
        license_provider_model['id'] = 'testString'
        license_provider_model['licence_type'] = 'testString'
        license_provider_model['offering_type'] = 'testString'
        license_provider_model['create_url'] = 'testString'
        license_provider_model['info_url'] = 'testString'
        license_provider_model['url'] = 'testString'
        license_provider_model['crn'] = 'testString'
        license_provider_model['state'] = 'testString'

        # Construct a json representation of a LicenseProviders model
        license_providers_model_json = {}
        license_providers_model_json['total_results'] = 38
        license_providers_model_json['total_pages'] = 38
        license_providers_model_json['prev_url'] = 'testString'
        license_providers_model_json['next_url'] = 'testString'
        license_providers_model_json['resources'] = [license_provider_model]

        # Construct a model instance of LicenseProviders by calling from_dict on the json representation
        license_providers_model = LicenseProviders.from_dict(license_providers_model_json)
        assert license_providers_model != False

        # Construct a model instance of LicenseProviders by calling from_dict on the json representation
        license_providers_model_dict = LicenseProviders.from_dict(license_providers_model_json).__dict__
        license_providers_model2 = LicenseProviders(**license_providers_model_dict)

        # Verify the model instances are equivalent
        assert license_providers_model == license_providers_model2

        # Convert model instance back to dict and verify no loss of data
        license_providers_model_json2 = license_providers_model.to_dict()
        assert license_providers_model_json2 == license_providers_model_json

#-----------------------------------------------------------------------------
# Test Class for Licenses
#-----------------------------------------------------------------------------
class TestLicenses():

    #--------------------------------------------------------
    # Test serialization/deserialization for Licenses
    #--------------------------------------------------------
    def test_licenses_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        license_offering_reference_model = {} # LicenseOfferingReference
        license_offering_reference_model['id'] = 'testString'
        license_offering_reference_model['name'] = 'testString'
        license_offering_reference_model['label'] = 'testString'
        license_offering_reference_model['offering_icon_url'] = 'testString'
        license_offering_reference_model['account_id'] = 'testString'
        license_offering_reference_model['catalog_id'] = 'testString'

        license_object_model = {} # LicenseObject
        license_object_model['name'] = 'testString'
        license_object_model['offering_type'] = 'testString'
        license_object_model['seats_allowed'] = 'testString'
        license_object_model['seats_used'] = 'testString'
        license_object_model['owner_id'] = 'testString'
        license_object_model['license_offering_id'] = 'testString'
        license_object_model['license_id'] = 'testString'
        license_object_model['license_owner_id'] = 'testString'
        license_object_model['license_type'] = 'testString'
        license_object_model['license_provider_id'] = 'testString'
        license_object_model['license_product_id'] = 'testString'
        license_object_model['license_provider_url'] = 'testString'
        license_object_model['effective_from'] = 'testString'
        license_object_model['effective_until'] = 'testString'
        license_object_model['internal'] = True
        license_object_model['offering_list'] = [license_offering_reference_model]

        # Construct a json representation of a Licenses model
        licenses_model_json = {}
        licenses_model_json['total_results'] = 38
        licenses_model_json['total_pages'] = 38
        licenses_model_json['prev_url'] = 'testString'
        licenses_model_json['next_url'] = 'testString'
        licenses_model_json['resources'] = [license_object_model]

        # Construct a model instance of Licenses by calling from_dict on the json representation
        licenses_model = Licenses.from_dict(licenses_model_json)
        assert licenses_model != False

        # Construct a model instance of Licenses by calling from_dict on the json representation
        licenses_model_dict = Licenses.from_dict(licenses_model_json).__dict__
        licenses_model2 = Licenses(**licenses_model_dict)

        # Verify the model instances are equivalent
        assert licenses_model == licenses_model2

        # Convert model instance back to dict and verify no loss of data
        licenses_model_json2 = licenses_model.to_dict()
        assert licenses_model_json2 == licenses_model_json

#-----------------------------------------------------------------------------
# Test Class for Maintainers
#-----------------------------------------------------------------------------
class TestMaintainers():

    #--------------------------------------------------------
    # Test serialization/deserialization for Maintainers
    #--------------------------------------------------------
    def test_maintainers_serialization(self):

        # Construct a json representation of a Maintainers model
        maintainers_model_json = {}
        maintainers_model_json['email'] = 'testString'
        maintainers_model_json['name'] = 'testString'

        # Construct a model instance of Maintainers by calling from_dict on the json representation
        maintainers_model = Maintainers.from_dict(maintainers_model_json)
        assert maintainers_model != False

        # Construct a model instance of Maintainers by calling from_dict on the json representation
        maintainers_model_dict = Maintainers.from_dict(maintainers_model_json).__dict__
        maintainers_model2 = Maintainers(**maintainers_model_dict)

        # Verify the model instances are equivalent
        assert maintainers_model == maintainers_model2

        # Convert model instance back to dict and verify no loss of data
        maintainers_model_json2 = maintainers_model.to_dict()
        assert maintainers_model_json2 == maintainers_model_json

#-----------------------------------------------------------------------------
# Test Class for NamespaceSearchResult
#-----------------------------------------------------------------------------
class TestNamespaceSearchResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for NamespaceSearchResult
    #--------------------------------------------------------
    def test_namespace_search_result_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for Offering
#-----------------------------------------------------------------------------
class TestOffering():

    #--------------------------------------------------------
    # Test serialization/deserialization for Offering
    #--------------------------------------------------------
    def test_offering_serialization(self):

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

        deployment_model = {} # Deployment
        deployment_model['id'] = 'testString'
        deployment_model['label'] = 'testString'
        deployment_model['name'] = 'testString'
        deployment_model['short_description'] = 'testString'
        deployment_model['long_description'] = 'testString'
        deployment_model['metadata'] = { 'foo': 'bar' }
        deployment_model['tags'] = ['testString']
        deployment_model['created'] = '2020-01-28T18:40:40.123456Z'
        deployment_model['updated'] = '2020-01-28T18:40:40.123456Z'

        feature_model = {} # Feature
        feature_model['title'] = 'testString'
        feature_model['description'] = 'testString'

        license_model = {} # License
        license_model['id'] = 'testString'
        license_model['name'] = 'testString'
        license_model['type'] = 'testString'
        license_model['url'] = 'testString'
        license_model['description'] = 'testString'

        resource_model = {} # Resource
        resource_model['type'] = 'mem'
        resource_model['value'] = { 'foo': 'bar' }

        script_model = {} # Script
        script_model['instructions'] = 'testString'
        script_model['script'] = 'testString'
        script_model['script_permission'] = 'testString'
        script_model['delete_script'] = 'testString'
        script_model['scope'] = 'testString'

        state_model = {} # State
        state_model['current'] = 'testString'
        state_model['current_entered'] = '2020-01-28T18:40:40.123456Z'
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = '2020-01-28T18:40:40.123456Z'
        state_model['previous'] = 'testString'

        validation_model = {} # Validation
        validation_model['validated'] = '2020-01-28T18:40:40.123456Z'
        validation_model['requested'] = '2020-01-28T18:40:40.123456Z'
        validation_model['state'] = 'testString'
        validation_model['last_operation'] = 'testString'
        validation_model['target'] = { 'foo': 'bar' }

        version_entitlement_model = {} # VersionEntitlement
        version_entitlement_model['provider_name'] = 'testString'
        version_entitlement_model['provider_id'] = 'testString'
        version_entitlement_model['product_id'] = 'testString'
        version_entitlement_model['part_numbers'] = ['testString']
        version_entitlement_model['image_repo_name'] = 'testString'

        plan_model = {} # Plan
        plan_model['id'] = 'testString'
        plan_model['label'] = 'testString'
        plan_model['name'] = 'testString'
        plan_model['short_description'] = 'testString'
        plan_model['long_description'] = 'testString'
        plan_model['metadata'] = { 'foo': 'bar' }
        plan_model['tags'] = ['testString']
        plan_model['additional_features'] = [feature_model]
        plan_model['created'] = '2020-01-28T18:40:40.123456Z'
        plan_model['updated'] = '2020-01-28T18:40:40.123456Z'
        plan_model['deployments'] = [deployment_model]

        version_model = {} # Version
        version_model['id'] = 'testString'
        version_model['_rev'] = 'testString'
        version_model['crn'] = 'testString'
        version_model['version'] = 'testString'
        version_model['sha'] = 'testString'
        version_model['created'] = '2020-01-28T18:40:40.123456Z'
        version_model['updated'] = '2020-01-28T18:40:40.123456Z'
        version_model['offering_id'] = 'testString'
        version_model['catalog_id'] = 'testString'
        version_model['kind_id'] = 'testString'
        version_model['tags'] = ['testString']
        version_model['repo_url'] = 'testString'
        version_model['source_url'] = 'testString'
        version_model['tgz_url'] = 'testString'
        version_model['configuration'] = [configuration_model]
        version_model['metadata'] = { 'foo': 'bar' }
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

        kind_model = {} # Kind
        kind_model['id'] = 'testString'
        kind_model['format_kind'] = 'testString'
        kind_model['target_kind'] = 'testString'
        kind_model['metadata'] = { 'foo': 'bar' }
        kind_model['install_description'] = 'testString'
        kind_model['tags'] = ['testString']
        kind_model['additional_features'] = [feature_model]
        kind_model['created'] = '2020-01-28T18:40:40.123456Z'
        kind_model['updated'] = '2020-01-28T18:40:40.123456Z'
        kind_model['versions'] = [version_model]
        kind_model['plans'] = [plan_model]

        rating_model = {} # Rating
        rating_model['one_star_count'] = 38
        rating_model['two_star_count'] = 38
        rating_model['three_star_count'] = 38
        rating_model['four_star_count'] = 38

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
        offering_model_json['rating'] = rating_model
        offering_model_json['created'] = '2020-01-28T18:40:40.123456Z'
        offering_model_json['updated'] = '2020-01-28T18:40:40.123456Z'
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
        offering_model_json['metadata'] = { 'foo': 'bar' }
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

#-----------------------------------------------------------------------------
# Test Class for OfferingSearchResult
#-----------------------------------------------------------------------------
class TestOfferingSearchResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for OfferingSearchResult
    #--------------------------------------------------------
    def test_offering_search_result_serialization(self):

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

        deployment_model = {} # Deployment
        deployment_model['id'] = 'testString'
        deployment_model['label'] = 'testString'
        deployment_model['name'] = 'testString'
        deployment_model['short_description'] = 'testString'
        deployment_model['long_description'] = 'testString'
        deployment_model['metadata'] = { 'foo': 'bar' }
        deployment_model['tags'] = ['testString']
        deployment_model['created'] = '2020-01-28T18:40:40.123456Z'
        deployment_model['updated'] = '2020-01-28T18:40:40.123456Z'

        feature_model = {} # Feature
        feature_model['title'] = 'testString'
        feature_model['description'] = 'testString'

        license_model = {} # License
        license_model['id'] = 'testString'
        license_model['name'] = 'testString'
        license_model['type'] = 'testString'
        license_model['url'] = 'testString'
        license_model['description'] = 'testString'

        resource_model = {} # Resource
        resource_model['type'] = 'mem'
        resource_model['value'] = { 'foo': 'bar' }

        script_model = {} # Script
        script_model['instructions'] = 'testString'
        script_model['script'] = 'testString'
        script_model['script_permission'] = 'testString'
        script_model['delete_script'] = 'testString'
        script_model['scope'] = 'testString'

        state_model = {} # State
        state_model['current'] = 'testString'
        state_model['current_entered'] = '2020-01-28T18:40:40.123456Z'
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = '2020-01-28T18:40:40.123456Z'
        state_model['previous'] = 'testString'

        validation_model = {} # Validation
        validation_model['validated'] = '2020-01-28T18:40:40.123456Z'
        validation_model['requested'] = '2020-01-28T18:40:40.123456Z'
        validation_model['state'] = 'testString'
        validation_model['last_operation'] = 'testString'
        validation_model['target'] = { 'foo': 'bar' }

        version_entitlement_model = {} # VersionEntitlement
        version_entitlement_model['provider_name'] = 'testString'
        version_entitlement_model['provider_id'] = 'testString'
        version_entitlement_model['product_id'] = 'testString'
        version_entitlement_model['part_numbers'] = ['testString']
        version_entitlement_model['image_repo_name'] = 'testString'

        plan_model = {} # Plan
        plan_model['id'] = 'testString'
        plan_model['label'] = 'testString'
        plan_model['name'] = 'testString'
        plan_model['short_description'] = 'testString'
        plan_model['long_description'] = 'testString'
        plan_model['metadata'] = { 'foo': 'bar' }
        plan_model['tags'] = ['testString']
        plan_model['additional_features'] = [feature_model]
        plan_model['created'] = '2020-01-28T18:40:40.123456Z'
        plan_model['updated'] = '2020-01-28T18:40:40.123456Z'
        plan_model['deployments'] = [deployment_model]

        version_model = {} # Version
        version_model['id'] = 'testString'
        version_model['_rev'] = 'testString'
        version_model['crn'] = 'testString'
        version_model['version'] = 'testString'
        version_model['sha'] = 'testString'
        version_model['created'] = '2020-01-28T18:40:40.123456Z'
        version_model['updated'] = '2020-01-28T18:40:40.123456Z'
        version_model['offering_id'] = 'testString'
        version_model['catalog_id'] = 'testString'
        version_model['kind_id'] = 'testString'
        version_model['tags'] = ['testString']
        version_model['repo_url'] = 'testString'
        version_model['source_url'] = 'testString'
        version_model['tgz_url'] = 'testString'
        version_model['configuration'] = [configuration_model]
        version_model['metadata'] = { 'foo': 'bar' }
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

        kind_model = {} # Kind
        kind_model['id'] = 'testString'
        kind_model['format_kind'] = 'testString'
        kind_model['target_kind'] = 'testString'
        kind_model['metadata'] = { 'foo': 'bar' }
        kind_model['install_description'] = 'testString'
        kind_model['tags'] = ['testString']
        kind_model['additional_features'] = [feature_model]
        kind_model['created'] = '2020-01-28T18:40:40.123456Z'
        kind_model['updated'] = '2020-01-28T18:40:40.123456Z'
        kind_model['versions'] = [version_model]
        kind_model['plans'] = [plan_model]

        rating_model = {} # Rating
        rating_model['one_star_count'] = 38
        rating_model['two_star_count'] = 38
        rating_model['three_star_count'] = 38
        rating_model['four_star_count'] = 38

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
        offering_model['rating'] = rating_model
        offering_model['created'] = '2020-01-28T18:40:40.123456Z'
        offering_model['updated'] = '2020-01-28T18:40:40.123456Z'
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
        offering_model['metadata'] = { 'foo': 'bar' }
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

#-----------------------------------------------------------------------------
# Test Class for OperatorDeployResult
#-----------------------------------------------------------------------------
class TestOperatorDeployResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for OperatorDeployResult
    #--------------------------------------------------------
    def test_operator_deploy_result_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for Plan
#-----------------------------------------------------------------------------
class TestPlan():

    #--------------------------------------------------------
    # Test serialization/deserialization for Plan
    #--------------------------------------------------------
    def test_plan_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        deployment_model = {} # Deployment
        deployment_model['id'] = 'testString'
        deployment_model['label'] = 'testString'
        deployment_model['name'] = 'testString'
        deployment_model['short_description'] = 'testString'
        deployment_model['long_description'] = 'testString'
        deployment_model['metadata'] = { 'foo': 'bar' }
        deployment_model['tags'] = ['testString']
        deployment_model['created'] = '2020-01-28T18:40:40.123456Z'
        deployment_model['updated'] = '2020-01-28T18:40:40.123456Z'

        feature_model = {} # Feature
        feature_model['title'] = 'testString'
        feature_model['description'] = 'testString'

        # Construct a json representation of a Plan model
        plan_model_json = {}
        plan_model_json['id'] = 'testString'
        plan_model_json['label'] = 'testString'
        plan_model_json['name'] = 'testString'
        plan_model_json['short_description'] = 'testString'
        plan_model_json['long_description'] = 'testString'
        plan_model_json['metadata'] = { 'foo': 'bar' }
        plan_model_json['tags'] = ['testString']
        plan_model_json['additional_features'] = [feature_model]
        plan_model_json['created'] = '2020-01-28T18:40:40.123456Z'
        plan_model_json['updated'] = '2020-01-28T18:40:40.123456Z'
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

#-----------------------------------------------------------------------------
# Test Class for Rating
#-----------------------------------------------------------------------------
class TestRating():

    #--------------------------------------------------------
    # Test serialization/deserialization for Rating
    #--------------------------------------------------------
    def test_rating_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for RepoInfo
#-----------------------------------------------------------------------------
class TestRepoInfo():

    #--------------------------------------------------------
    # Test serialization/deserialization for RepoInfo
    #--------------------------------------------------------
    def test_repo_info_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for ResourceGroup
#-----------------------------------------------------------------------------
class TestResourceGroup():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceGroup
    #--------------------------------------------------------
    def test_resource_group_serialization(self):

        # Construct a json representation of a ResourceGroup model
        resource_group_model_json = {}
        resource_group_model_json['id'] = 'testString'
        resource_group_model_json['name'] = 'testString'
        resource_group_model_json['crn'] = 'testString'
        resource_group_model_json['account_id'] = 'testString'
        resource_group_model_json['state'] = 'testString'
        resource_group_model_json['default'] = True

        # Construct a model instance of ResourceGroup by calling from_dict on the json representation
        resource_group_model = ResourceGroup.from_dict(resource_group_model_json)
        assert resource_group_model != False

        # Construct a model instance of ResourceGroup by calling from_dict on the json representation
        resource_group_model_dict = ResourceGroup.from_dict(resource_group_model_json).__dict__
        resource_group_model2 = ResourceGroup(**resource_group_model_dict)

        # Verify the model instances are equivalent
        assert resource_group_model == resource_group_model2

        # Convert model instance back to dict and verify no loss of data
        resource_group_model_json2 = resource_group_model.to_dict()
        assert resource_group_model_json2 == resource_group_model_json

#-----------------------------------------------------------------------------
# Test Class for ResourceGroups
#-----------------------------------------------------------------------------
class TestResourceGroups():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceGroups
    #--------------------------------------------------------
    def test_resource_groups_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        resource_group_model = {} # ResourceGroup
        resource_group_model['id'] = 'testString'
        resource_group_model['name'] = 'testString'
        resource_group_model['crn'] = 'testString'
        resource_group_model['account_id'] = 'testString'
        resource_group_model['state'] = 'testString'
        resource_group_model['default'] = True

        # Construct a json representation of a ResourceGroups model
        resource_groups_model_json = {}
        resource_groups_model_json['offset'] = 38
        resource_groups_model_json['limit'] = 38
        resource_groups_model_json['total_count'] = 38
        resource_groups_model_json['resource_count'] = 38
        resource_groups_model_json['first'] = 'testString'
        resource_groups_model_json['last'] = 'testString'
        resource_groups_model_json['prev'] = 'testString'
        resource_groups_model_json['next'] = 'testString'
        resource_groups_model_json['resources'] = [resource_group_model]

        # Construct a model instance of ResourceGroups by calling from_dict on the json representation
        resource_groups_model = ResourceGroups.from_dict(resource_groups_model_json)
        assert resource_groups_model != False

        # Construct a model instance of ResourceGroups by calling from_dict on the json representation
        resource_groups_model_dict = ResourceGroups.from_dict(resource_groups_model_json).__dict__
        resource_groups_model2 = ResourceGroups(**resource_groups_model_dict)

        # Verify the model instances are equivalent
        assert resource_groups_model == resource_groups_model2

        # Convert model instance back to dict and verify no loss of data
        resource_groups_model_json2 = resource_groups_model.to_dict()
        assert resource_groups_model_json2 == resource_groups_model_json

#-----------------------------------------------------------------------------
# Test Class for SchematicsWorkspace
#-----------------------------------------------------------------------------
class TestSchematicsWorkspace():

    #--------------------------------------------------------
    # Test serialization/deserialization for SchematicsWorkspace
    #--------------------------------------------------------
    def test_schematics_workspace_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        schematics_workspace_catalog_ref_model = {} # SchematicsWorkspaceCatalogRef
        schematics_workspace_catalog_ref_model['item_id'] = 'testString'
        schematics_workspace_catalog_ref_model['item_name'] = 'testString'
        schematics_workspace_catalog_ref_model['item_url'] = 'testString'

        schematics_workspace_runtime_data_model = {} # SchematicsWorkspaceRuntimeData
        schematics_workspace_runtime_data_model['id'] = 'testString'
        schematics_workspace_runtime_data_model['engine_name'] = 'testString'
        schematics_workspace_runtime_data_model['engine_version'] = 'testString'
        schematics_workspace_runtime_data_model['state_store_url'] = 'testString'
        schematics_workspace_runtime_data_model['log_store_url'] = 'testString'

        schematics_workspace_template_repo_model = {} # SchematicsWorkspaceTemplateRepo
        schematics_workspace_template_repo_model['repo_url'] = 'testString'
        schematics_workspace_template_repo_model['chart_name'] = 'testString'
        schematics_workspace_template_repo_model['script_name'] = 'testString'
        schematics_workspace_template_repo_model['uninstall_script_name'] = 'testString'
        schematics_workspace_template_repo_model['folder_name'] = 'testString'
        schematics_workspace_template_repo_model['repo_sha_value'] = 'testString'

        schematics_workspace_workspace_status_model = {} # SchematicsWorkspaceWorkspaceStatus
        schematics_workspace_workspace_status_model['frozen'] = True
        schematics_workspace_workspace_status_model['locked'] = True

        # Construct a json representation of a SchematicsWorkspace model
        schematics_workspace_model_json = {}
        schematics_workspace_model_json['id'] = 'testString'
        schematics_workspace_model_json['name'] = 'testString'
        schematics_workspace_model_json['type'] = ['testString']
        schematics_workspace_model_json['description'] = 'testString'
        schematics_workspace_model_json['tags'] = ['testString']
        schematics_workspace_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        schematics_workspace_model_json['created_by'] = 'testString'
        schematics_workspace_model_json['status'] = 'testString'
        schematics_workspace_model_json['workspace_status'] = schematics_workspace_workspace_status_model
        schematics_workspace_model_json['template_ref'] = 'testString'
        schematics_workspace_model_json['template_repo'] = schematics_workspace_template_repo_model
        schematics_workspace_model_json['template_data'] = [{ 'foo': 'bar' }]
        schematics_workspace_model_json['runtime_data'] = schematics_workspace_runtime_data_model
        schematics_workspace_model_json['shared_data'] = { 'foo': 'bar' }
        schematics_workspace_model_json['catalog_ref'] = schematics_workspace_catalog_ref_model

        # Construct a model instance of SchematicsWorkspace by calling from_dict on the json representation
        schematics_workspace_model = SchematicsWorkspace.from_dict(schematics_workspace_model_json)
        assert schematics_workspace_model != False

        # Construct a model instance of SchematicsWorkspace by calling from_dict on the json representation
        schematics_workspace_model_dict = SchematicsWorkspace.from_dict(schematics_workspace_model_json).__dict__
        schematics_workspace_model2 = SchematicsWorkspace(**schematics_workspace_model_dict)

        # Verify the model instances are equivalent
        assert schematics_workspace_model == schematics_workspace_model2

        # Convert model instance back to dict and verify no loss of data
        schematics_workspace_model_json2 = schematics_workspace_model.to_dict()
        assert schematics_workspace_model_json2 == schematics_workspace_model_json

#-----------------------------------------------------------------------------
# Test Class for SchematicsWorkspaceCatalogRef
#-----------------------------------------------------------------------------
class TestSchematicsWorkspaceCatalogRef():

    #--------------------------------------------------------
    # Test serialization/deserialization for SchematicsWorkspaceCatalogRef
    #--------------------------------------------------------
    def test_schematics_workspace_catalog_ref_serialization(self):

        # Construct a json representation of a SchematicsWorkspaceCatalogRef model
        schematics_workspace_catalog_ref_model_json = {}
        schematics_workspace_catalog_ref_model_json['item_id'] = 'testString'
        schematics_workspace_catalog_ref_model_json['item_name'] = 'testString'
        schematics_workspace_catalog_ref_model_json['item_url'] = 'testString'

        # Construct a model instance of SchematicsWorkspaceCatalogRef by calling from_dict on the json representation
        schematics_workspace_catalog_ref_model = SchematicsWorkspaceCatalogRef.from_dict(schematics_workspace_catalog_ref_model_json)
        assert schematics_workspace_catalog_ref_model != False

        # Construct a model instance of SchematicsWorkspaceCatalogRef by calling from_dict on the json representation
        schematics_workspace_catalog_ref_model_dict = SchematicsWorkspaceCatalogRef.from_dict(schematics_workspace_catalog_ref_model_json).__dict__
        schematics_workspace_catalog_ref_model2 = SchematicsWorkspaceCatalogRef(**schematics_workspace_catalog_ref_model_dict)

        # Verify the model instances are equivalent
        assert schematics_workspace_catalog_ref_model == schematics_workspace_catalog_ref_model2

        # Convert model instance back to dict and verify no loss of data
        schematics_workspace_catalog_ref_model_json2 = schematics_workspace_catalog_ref_model.to_dict()
        assert schematics_workspace_catalog_ref_model_json2 == schematics_workspace_catalog_ref_model_json

#-----------------------------------------------------------------------------
# Test Class for SchematicsWorkspaceRuntimeData
#-----------------------------------------------------------------------------
class TestSchematicsWorkspaceRuntimeData():

    #--------------------------------------------------------
    # Test serialization/deserialization for SchematicsWorkspaceRuntimeData
    #--------------------------------------------------------
    def test_schematics_workspace_runtime_data_serialization(self):

        # Construct a json representation of a SchematicsWorkspaceRuntimeData model
        schematics_workspace_runtime_data_model_json = {}
        schematics_workspace_runtime_data_model_json['id'] = 'testString'
        schematics_workspace_runtime_data_model_json['engine_name'] = 'testString'
        schematics_workspace_runtime_data_model_json['engine_version'] = 'testString'
        schematics_workspace_runtime_data_model_json['state_store_url'] = 'testString'
        schematics_workspace_runtime_data_model_json['log_store_url'] = 'testString'

        # Construct a model instance of SchematicsWorkspaceRuntimeData by calling from_dict on the json representation
        schematics_workspace_runtime_data_model = SchematicsWorkspaceRuntimeData.from_dict(schematics_workspace_runtime_data_model_json)
        assert schematics_workspace_runtime_data_model != False

        # Construct a model instance of SchematicsWorkspaceRuntimeData by calling from_dict on the json representation
        schematics_workspace_runtime_data_model_dict = SchematicsWorkspaceRuntimeData.from_dict(schematics_workspace_runtime_data_model_json).__dict__
        schematics_workspace_runtime_data_model2 = SchematicsWorkspaceRuntimeData(**schematics_workspace_runtime_data_model_dict)

        # Verify the model instances are equivalent
        assert schematics_workspace_runtime_data_model == schematics_workspace_runtime_data_model2

        # Convert model instance back to dict and verify no loss of data
        schematics_workspace_runtime_data_model_json2 = schematics_workspace_runtime_data_model.to_dict()
        assert schematics_workspace_runtime_data_model_json2 == schematics_workspace_runtime_data_model_json

#-----------------------------------------------------------------------------
# Test Class for SchematicsWorkspaceSearchResult
#-----------------------------------------------------------------------------
class TestSchematicsWorkspaceSearchResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for SchematicsWorkspaceSearchResult
    #--------------------------------------------------------
    def test_schematics_workspace_search_result_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        schematics_workspace_catalog_ref_model = {} # SchematicsWorkspaceCatalogRef
        schematics_workspace_catalog_ref_model['item_id'] = 'testString'
        schematics_workspace_catalog_ref_model['item_name'] = 'testString'
        schematics_workspace_catalog_ref_model['item_url'] = 'testString'

        schematics_workspace_runtime_data_model = {} # SchematicsWorkspaceRuntimeData
        schematics_workspace_runtime_data_model['id'] = 'testString'
        schematics_workspace_runtime_data_model['engine_name'] = 'testString'
        schematics_workspace_runtime_data_model['engine_version'] = 'testString'
        schematics_workspace_runtime_data_model['state_store_url'] = 'testString'
        schematics_workspace_runtime_data_model['log_store_url'] = 'testString'

        schematics_workspace_template_repo_model = {} # SchematicsWorkspaceTemplateRepo
        schematics_workspace_template_repo_model['repo_url'] = 'testString'
        schematics_workspace_template_repo_model['chart_name'] = 'testString'
        schematics_workspace_template_repo_model['script_name'] = 'testString'
        schematics_workspace_template_repo_model['uninstall_script_name'] = 'testString'
        schematics_workspace_template_repo_model['folder_name'] = 'testString'
        schematics_workspace_template_repo_model['repo_sha_value'] = 'testString'

        schematics_workspace_workspace_status_model = {} # SchematicsWorkspaceWorkspaceStatus
        schematics_workspace_workspace_status_model['frozen'] = True
        schematics_workspace_workspace_status_model['locked'] = True

        schematics_workspace_model = {} # SchematicsWorkspace
        schematics_workspace_model['id'] = 'testString'
        schematics_workspace_model['name'] = 'testString'
        schematics_workspace_model['type'] = ['testString']
        schematics_workspace_model['description'] = 'testString'
        schematics_workspace_model['tags'] = ['testString']
        schematics_workspace_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        schematics_workspace_model['created_by'] = 'testString'
        schematics_workspace_model['status'] = 'testString'
        schematics_workspace_model['workspace_status'] = schematics_workspace_workspace_status_model
        schematics_workspace_model['template_ref'] = 'testString'
        schematics_workspace_model['template_repo'] = schematics_workspace_template_repo_model
        schematics_workspace_model['template_data'] = [{ 'foo': 'bar' }]
        schematics_workspace_model['runtime_data'] = schematics_workspace_runtime_data_model
        schematics_workspace_model['shared_data'] = { 'foo': 'bar' }
        schematics_workspace_model['catalog_ref'] = schematics_workspace_catalog_ref_model

        # Construct a json representation of a SchematicsWorkspaceSearchResult model
        schematics_workspace_search_result_model_json = {}
        schematics_workspace_search_result_model_json['offset'] = 38
        schematics_workspace_search_result_model_json['limit'] = 38
        schematics_workspace_search_result_model_json['total_count'] = 38
        schematics_workspace_search_result_model_json['resource_count'] = 38
        schematics_workspace_search_result_model_json['first'] = 'testString'
        schematics_workspace_search_result_model_json['last'] = 'testString'
        schematics_workspace_search_result_model_json['prev'] = 'testString'
        schematics_workspace_search_result_model_json['next'] = 'testString'
        schematics_workspace_search_result_model_json['resources'] = [schematics_workspace_model]

        # Construct a model instance of SchematicsWorkspaceSearchResult by calling from_dict on the json representation
        schematics_workspace_search_result_model = SchematicsWorkspaceSearchResult.from_dict(schematics_workspace_search_result_model_json)
        assert schematics_workspace_search_result_model != False

        # Construct a model instance of SchematicsWorkspaceSearchResult by calling from_dict on the json representation
        schematics_workspace_search_result_model_dict = SchematicsWorkspaceSearchResult.from_dict(schematics_workspace_search_result_model_json).__dict__
        schematics_workspace_search_result_model2 = SchematicsWorkspaceSearchResult(**schematics_workspace_search_result_model_dict)

        # Verify the model instances are equivalent
        assert schematics_workspace_search_result_model == schematics_workspace_search_result_model2

        # Convert model instance back to dict and verify no loss of data
        schematics_workspace_search_result_model_json2 = schematics_workspace_search_result_model.to_dict()
        assert schematics_workspace_search_result_model_json2 == schematics_workspace_search_result_model_json

#-----------------------------------------------------------------------------
# Test Class for SchematicsWorkspaceTemplateRepo
#-----------------------------------------------------------------------------
class TestSchematicsWorkspaceTemplateRepo():

    #--------------------------------------------------------
    # Test serialization/deserialization for SchematicsWorkspaceTemplateRepo
    #--------------------------------------------------------
    def test_schematics_workspace_template_repo_serialization(self):

        # Construct a json representation of a SchematicsWorkspaceTemplateRepo model
        schematics_workspace_template_repo_model_json = {}
        schematics_workspace_template_repo_model_json['repo_url'] = 'testString'
        schematics_workspace_template_repo_model_json['chart_name'] = 'testString'
        schematics_workspace_template_repo_model_json['script_name'] = 'testString'
        schematics_workspace_template_repo_model_json['uninstall_script_name'] = 'testString'
        schematics_workspace_template_repo_model_json['folder_name'] = 'testString'
        schematics_workspace_template_repo_model_json['repo_sha_value'] = 'testString'

        # Construct a model instance of SchematicsWorkspaceTemplateRepo by calling from_dict on the json representation
        schematics_workspace_template_repo_model = SchematicsWorkspaceTemplateRepo.from_dict(schematics_workspace_template_repo_model_json)
        assert schematics_workspace_template_repo_model != False

        # Construct a model instance of SchematicsWorkspaceTemplateRepo by calling from_dict on the json representation
        schematics_workspace_template_repo_model_dict = SchematicsWorkspaceTemplateRepo.from_dict(schematics_workspace_template_repo_model_json).__dict__
        schematics_workspace_template_repo_model2 = SchematicsWorkspaceTemplateRepo(**schematics_workspace_template_repo_model_dict)

        # Verify the model instances are equivalent
        assert schematics_workspace_template_repo_model == schematics_workspace_template_repo_model2

        # Convert model instance back to dict and verify no loss of data
        schematics_workspace_template_repo_model_json2 = schematics_workspace_template_repo_model.to_dict()
        assert schematics_workspace_template_repo_model_json2 == schematics_workspace_template_repo_model_json

#-----------------------------------------------------------------------------
# Test Class for SchematicsWorkspaceWorkspaceStatus
#-----------------------------------------------------------------------------
class TestSchematicsWorkspaceWorkspaceStatus():

    #--------------------------------------------------------
    # Test serialization/deserialization for SchematicsWorkspaceWorkspaceStatus
    #--------------------------------------------------------
    def test_schematics_workspace_workspace_status_serialization(self):

        # Construct a json representation of a SchematicsWorkspaceWorkspaceStatus model
        schematics_workspace_workspace_status_model_json = {}
        schematics_workspace_workspace_status_model_json['frozen'] = True
        schematics_workspace_workspace_status_model_json['locked'] = True

        # Construct a model instance of SchematicsWorkspaceWorkspaceStatus by calling from_dict on the json representation
        schematics_workspace_workspace_status_model = SchematicsWorkspaceWorkspaceStatus.from_dict(schematics_workspace_workspace_status_model_json)
        assert schematics_workspace_workspace_status_model != False

        # Construct a model instance of SchematicsWorkspaceWorkspaceStatus by calling from_dict on the json representation
        schematics_workspace_workspace_status_model_dict = SchematicsWorkspaceWorkspaceStatus.from_dict(schematics_workspace_workspace_status_model_json).__dict__
        schematics_workspace_workspace_status_model2 = SchematicsWorkspaceWorkspaceStatus(**schematics_workspace_workspace_status_model_dict)

        # Verify the model instances are equivalent
        assert schematics_workspace_workspace_status_model == schematics_workspace_workspace_status_model2

        # Convert model instance back to dict and verify no loss of data
        schematics_workspace_workspace_status_model_json2 = schematics_workspace_workspace_status_model.to_dict()
        assert schematics_workspace_workspace_status_model_json2 == schematics_workspace_workspace_status_model_json

#-----------------------------------------------------------------------------
# Test Class for Script
#-----------------------------------------------------------------------------
class TestScript():

    #--------------------------------------------------------
    # Test serialization/deserialization for Script
    #--------------------------------------------------------
    def test_script_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for State
#-----------------------------------------------------------------------------
class TestState():

    #--------------------------------------------------------
    # Test serialization/deserialization for State
    #--------------------------------------------------------
    def test_state_serialization(self):

        # Construct a json representation of a State model
        state_model_json = {}
        state_model_json['current'] = 'testString'
        state_model_json['current_entered'] = '2020-01-28T18:40:40.123456Z'
        state_model_json['pending'] = 'testString'
        state_model_json['pending_requested'] = '2020-01-28T18:40:40.123456Z'
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

#-----------------------------------------------------------------------------
# Test Class for SyndicationAuthorization
#-----------------------------------------------------------------------------
class TestSyndicationAuthorization():

    #--------------------------------------------------------
    # Test serialization/deserialization for SyndicationAuthorization
    #--------------------------------------------------------
    def test_syndication_authorization_serialization(self):

        # Construct a json representation of a SyndicationAuthorization model
        syndication_authorization_model_json = {}
        syndication_authorization_model_json['token'] = 'testString'
        syndication_authorization_model_json['last_run'] = '2020-01-28T18:40:40.123456Z'

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

#-----------------------------------------------------------------------------
# Test Class for SyndicationCluster
#-----------------------------------------------------------------------------
class TestSyndicationCluster():

    #--------------------------------------------------------
    # Test serialization/deserialization for SyndicationCluster
    #--------------------------------------------------------
    def test_syndication_cluster_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for SyndicationHistory
#-----------------------------------------------------------------------------
class TestSyndicationHistory():

    #--------------------------------------------------------
    # Test serialization/deserialization for SyndicationHistory
    #--------------------------------------------------------
    def test_syndication_history_serialization(self):

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
        syndication_history_model_json['last_run'] = '2020-01-28T18:40:40.123456Z'

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

#-----------------------------------------------------------------------------
# Test Class for SyndicationResource
#-----------------------------------------------------------------------------
class TestSyndicationResource():

    #--------------------------------------------------------
    # Test serialization/deserialization for SyndicationResource
    #--------------------------------------------------------
    def test_syndication_resource_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        syndication_cluster_model = {} # SyndicationCluster
        syndication_cluster_model['region'] = 'testString'
        syndication_cluster_model['id'] = 'testString'
        syndication_cluster_model['name'] = 'testString'
        syndication_cluster_model['resource_group_name'] = 'testString'
        syndication_cluster_model['type'] = 'testString'
        syndication_cluster_model['namespaces'] = ['testString']
        syndication_cluster_model['all_namespaces'] = True

        syndication_authorization_model = {} # SyndicationAuthorization
        syndication_authorization_model['token'] = 'testString'
        syndication_authorization_model['last_run'] = '2020-01-28T18:40:40.123456Z'

        syndication_history_model = {} # SyndicationHistory
        syndication_history_model['namespaces'] = ['testString']
        syndication_history_model['clusters'] = [syndication_cluster_model]
        syndication_history_model['last_run'] = '2020-01-28T18:40:40.123456Z'

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

#-----------------------------------------------------------------------------
# Test Class for Validation
#-----------------------------------------------------------------------------
class TestValidation():

    #--------------------------------------------------------
    # Test serialization/deserialization for Validation
    #--------------------------------------------------------
    def test_validation_serialization(self):

        # Construct a json representation of a Validation model
        validation_model_json = {}
        validation_model_json['validated'] = '2020-01-28T18:40:40.123456Z'
        validation_model_json['requested'] = '2020-01-28T18:40:40.123456Z'
        validation_model_json['state'] = 'testString'
        validation_model_json['last_operation'] = 'testString'
        validation_model_json['target'] = { 'foo': 'bar' }

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

#-----------------------------------------------------------------------------
# Test Class for Version
#-----------------------------------------------------------------------------
class TestVersion():

    #--------------------------------------------------------
    # Test serialization/deserialization for Version
    #--------------------------------------------------------
    def test_version_serialization(self):

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

        license_model = {} # License
        license_model['id'] = 'testString'
        license_model['name'] = 'testString'
        license_model['type'] = 'testString'
        license_model['url'] = 'testString'
        license_model['description'] = 'testString'

        resource_model = {} # Resource
        resource_model['type'] = 'mem'
        resource_model['value'] = { 'foo': 'bar' }

        script_model = {} # Script
        script_model['instructions'] = 'testString'
        script_model['script'] = 'testString'
        script_model['script_permission'] = 'testString'
        script_model['delete_script'] = 'testString'
        script_model['scope'] = 'testString'

        state_model = {} # State
        state_model['current'] = 'testString'
        state_model['current_entered'] = '2020-01-28T18:40:40.123456Z'
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = '2020-01-28T18:40:40.123456Z'
        state_model['previous'] = 'testString'

        validation_model = {} # Validation
        validation_model['validated'] = '2020-01-28T18:40:40.123456Z'
        validation_model['requested'] = '2020-01-28T18:40:40.123456Z'
        validation_model['state'] = 'testString'
        validation_model['last_operation'] = 'testString'
        validation_model['target'] = { 'foo': 'bar' }

        version_entitlement_model = {} # VersionEntitlement
        version_entitlement_model['provider_name'] = 'testString'
        version_entitlement_model['provider_id'] = 'testString'
        version_entitlement_model['product_id'] = 'testString'
        version_entitlement_model['part_numbers'] = ['testString']
        version_entitlement_model['image_repo_name'] = 'testString'

        # Construct a json representation of a Version model
        version_model_json = {}
        version_model_json['id'] = 'testString'
        version_model_json['_rev'] = 'testString'
        version_model_json['crn'] = 'testString'
        version_model_json['version'] = 'testString'
        version_model_json['sha'] = 'testString'
        version_model_json['created'] = '2020-01-28T18:40:40.123456Z'
        version_model_json['updated'] = '2020-01-28T18:40:40.123456Z'
        version_model_json['offering_id'] = 'testString'
        version_model_json['catalog_id'] = 'testString'
        version_model_json['kind_id'] = 'testString'
        version_model_json['tags'] = ['testString']
        version_model_json['repo_url'] = 'testString'
        version_model_json['source_url'] = 'testString'
        version_model_json['tgz_url'] = 'testString'
        version_model_json['configuration'] = [configuration_model]
        version_model_json['metadata'] = { 'foo': 'bar' }
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

#-----------------------------------------------------------------------------
# Test Class for VersionEntitlement
#-----------------------------------------------------------------------------
class TestVersionEntitlement():

    #--------------------------------------------------------
    # Test serialization/deserialization for VersionEntitlement
    #--------------------------------------------------------
    def test_version_entitlement_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for VersionUpdateDescriptor
#-----------------------------------------------------------------------------
class TestVersionUpdateDescriptor():

    #--------------------------------------------------------
    # Test serialization/deserialization for VersionUpdateDescriptor
    #--------------------------------------------------------
    def test_version_update_descriptor_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        resource_model = {} # Resource
        resource_model['type'] = 'mem'
        resource_model['value'] = { 'foo': 'bar' }

        state_model = {} # State
        state_model['current'] = 'testString'
        state_model['current_entered'] = '2020-01-28T18:40:40.123456Z'
        state_model['pending'] = 'testString'
        state_model['pending_requested'] = '2020-01-28T18:40:40.123456Z'
        state_model['previous'] = 'testString'

        # Construct a json representation of a VersionUpdateDescriptor model
        version_update_descriptor_model_json = {}
        version_update_descriptor_model_json['version_locator'] = 'testString'
        version_update_descriptor_model_json['version'] = 'testString'
        version_update_descriptor_model_json['state'] = state_model
        version_update_descriptor_model_json['required_resources'] = [resource_model]
        version_update_descriptor_model_json['package_version'] = 'testString'
        version_update_descriptor_model_json['can_update'] = True
        version_update_descriptor_model_json['messages'] = { 'foo': 'bar' }

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
