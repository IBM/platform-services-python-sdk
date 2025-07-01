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
Integration Tests for GlobalTaggingV1
"""

import os
import pytest
from ibm_cloud_sdk_core import *
from ibm_platform_services.global_tagging_v1 import *
from random import randint

# Config file name
config_file = 'global_tagging.env'


class TestGlobalTaggingV1:
    """
    Integration Test Class for GlobalTaggingV1
    """

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @classmethod
    def setup_class(cls):
        print('\nStarting setup...')
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.global_tagging_service = GlobalTaggingV1.new_instance()
            assert cls.global_tagging_service is not None

            cls.config = read_external_sources(GlobalTaggingV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.resource_crn = cls.config.get("RESOURCE_CRN")
            assert cls.resource_crn is not None

            assert cls.config["URL"] == cls.global_tagging_service.service_url

            cls.sdk_label = 'python-sdk'
            cls.user_tag_1 = cls.sdk_label + '-user-test1'
            cls.user_tag_2 = cls.sdk_label + '-user-test2'
            cls.access_tag_1 = 'env:' + cls.sdk_label + '-public'
            cls.access_tag_2 = 'region:' + cls.sdk_label + '-us-south'

            print('Service URL: ', cls.global_tagging_service.service_url)
            print('Resource CRN: ', cls.resource_crn)

            cls.clean_tags(cls)

        print('Setup complete.')

    @classmethod
    def teardown_class(cls):
        print('\nStarting teardown...')
        cls.clean_tags(cls)
        print('\nTeardown complete.')

    def clean_tags(self):
        print('\nStarted cleaning tags...')
        # Detach all user and access tags that contain our label.
        tag_names = self.get_tag_names_for_resource(self, self.resource_crn, 'user')
        for tag_name in tag_names:
            if self.sdk_label in tag_name:
                print('Detaching user tag {0} from resource {1}'.format(tag_name, self.resource_crn))
                self.detach_tag(self, self.resource_crn, tag_name, 'user')
        tag_names = self.get_tag_names_for_resource(self, self.resource_crn, 'user')
        print('Resource now has these user tags: {0}'.format(tag_names))

        tag_names = self.get_tag_names_for_resource(self, self.resource_crn, 'access')
        for tag_name in tag_names:
            if self.sdk_label in tag_name:
                print('Detaching access tag {0} from resource {1}'.format(tag_name, self.resource_crn))
                self.detach_tag(self, self.resource_crn, tag_name, 'access')
        tag_names = self.get_tag_names_for_resource(self, self.resource_crn, 'access')
        print('Resource now has these access tags: {0}'.format(tag_names))

        # Delete all user and access tags that contain our label.
        tag_names = self.list_tags_with_label(self, 'user', self.sdk_label)
        print('Found {0} user tag(s) that contain our label.'.format(len(tag_names)))
        for tag_name in tag_names:
            print('Deleting user tag: {0}'.format(tag_name))
            self.delete_tag(self, tag_name, 'user')

        tag_names = self.list_tags_with_label(self, 'access', self.sdk_label)
        print('Found {0} access tag(s) that contain our label.'.format(len(tag_names)))
        for tag_name in tag_names:
            print('Deleting access tag: {0}'.format(tag_name))
            self.delete_tag(self, tag_name, 'access')

        print('\nFinished cleaning tags...')

    def delete_tag(self, tag_name, tag_type):
        response = self.global_tagging_service.delete_tag(tag_name=tag_name, tag_type=tag_type)
        assert response.get_status_code() == 200
        assert response.get_result() is not None
        delete_tag_results = DeleteTagResults.from_dict(response.get_result())
        assert delete_tag_results is not None
        for elem in delete_tag_results.results:
            assert elem.is_error is False

    def detach_tag(self, resource_id, tag_name, tag_type):
        resource_model = {'resource_id': resource_id}
        response = self.global_tagging_service.detach_tag(
            resources=[resource_model], tag_names=[tag_name], tag_type=tag_type
        )
        assert response.get_status_code() == 200
        assert response.get_result() is not None
        tag_results = TagResults.from_dict(response.get_result())
        assert tag_results is not None
        for elem in tag_results.results:
            assert elem.is_error is False

    def get_tag_names_for_resource(self, resource_id, tag_type):
        tag_names = []
        response = self.global_tagging_service.list_tags(attached_to=resource_id, tag_type=tag_type)
        tag_list = TagList.from_dict(response.get_result())
        if tag_list.items is not None:
            for item in tag_list.items:
                tag_names.append(item.name)
        return tag_names

    def list_tags_with_label(self, tag_type, label):
        tag_names = []
        offset = 0
        more_results = True
        while more_results:
            list_tags_response = self.global_tagging_service.list_tags(offset=offset, limit=500, tag_type=tag_type)
            assert list_tags_response.get_status_code() == 200
            assert list_tags_response.get_result() is not None

            tag_list = TagList.from_dict(list_tags_response.get_result())
            assert tag_list is not None
            if len(tag_list.items) > 0:
                for tag in tag_list.items:
                    if self.sdk_label in tag.name:
                        tag_names.append(tag.name)
                offset += len(tag_list.items)
            else:
                more_results = False
        return tag_names

    @needscredentials
    def test_create_tag(self):
        create_tag_response = self.global_tagging_service.create_tag(
            tag_names=[self.access_tag_1, self.access_tag_2], tag_type='access'
        )

        assert create_tag_response.get_status_code() == 200
        assert create_tag_response.get_result() is not None
        create_tag_results = CreateTagResults.from_dict(create_tag_response.get_result())
        assert create_tag_results is not None
        print('\ncreate_tag() result: ', json.dumps(create_tag_results.to_dict(), indent=2))
        assert create_tag_results.results is not None
        for result in create_tag_results.results:
            assert result.is_error is False

    @needscredentials
    def test_attach_tag_user(self):
        # Construct a dict representation of a Resource model
        resource_model = {
            'resource_id': self.resource_crn,
        }

        attach_tag_response = self.global_tagging_service.attach_tag(
            resources=[resource_model], tag_names=[self.user_tag_1, self.user_tag_2], tag_type='user'
        )

        assert attach_tag_response.get_status_code() == 200
        assert attach_tag_response.get_result() is not None
        tag_results = TagResults.from_dict(attach_tag_response.get_result())
        assert tag_results is not None
        print('\nattach_tag(user) result: ', json.dumps(tag_results.to_dict(), indent=2))

        for elem in tag_results.results:
            assert elem.is_error is False

        # Make sure the tags are in fact attached to the resource.
        tag_names = self.get_tag_names_for_resource(resource_id=self.resource_crn, tag_type='user')
        assert self.user_tag_1 in tag_names
        assert self.user_tag_2 in tag_names

    @needscredentials
    def test_attach_tag_access(self):
        # Construct a dict representation of a Resource model
        resource_model = {
            'resource_id': self.resource_crn,
        }

        attach_tag_response = self.global_tagging_service.attach_tag(
            resources=[resource_model], tag_names=[self.access_tag_1, self.access_tag_2], tag_type='access'
        )

        assert attach_tag_response.get_status_code() == 200
        assert attach_tag_response.get_result() is not None
        tag_results = TagResults.from_dict(attach_tag_response.get_result())
        assert tag_results is not None
        print('\nattach_tag(access) result: ', json.dumps(tag_results.to_dict(), indent=2))

        for elem in tag_results.results:
            assert elem.is_error is False

        # Make sure the tags are in fact attached to the resource.
        tag_names = self.get_tag_names_for_resource(resource_id=self.resource_crn, tag_type='access')
        assert self.access_tag_1 in tag_names
        assert self.access_tag_2 in tag_names

    @needscredentials
    def test_list_tags_user(self):
        tags = []
        offset = 0
        more_results = True
        while more_results:
            list_tags_response = self.global_tagging_service.list_tags(offset=offset, limit=500, tag_type='user')
            assert list_tags_response.get_status_code() == 200
            assert list_tags_response.get_result() is not None

            tag_list = TagList.from_dict(list_tags_response.get_result())
            assert tag_list is not None
            if len(tag_list.items) > 0:
                for item in tag_list.items:
                    tags.append(item)
                offset += len(tag_list.items)
            else:
                more_results = False

        print('\nRetrieved a total of {0} user tags.'.format(len(tags)))
        matches = []
        for tag in tags:
            if self.sdk_label in tag.name:
                matches.append(tag.name)
        print('Found {0} user tags containing our label: {1}'.format(len(matches), matches))

    @needscredentials
    def test_list_tags_access(self):
        tags = []
        offset = 0
        more_results = True
        while more_results:
            list_tags_response = self.global_tagging_service.list_tags(offset=offset, limit=500, tag_type='access')
            assert list_tags_response.get_status_code() == 200
            assert list_tags_response.get_result() is not None

            tag_list = TagList.from_dict(list_tags_response.get_result())
            assert tag_list is not None
            if len(tag_list.items) > 0:
                for item in tag_list.items:
                    tags.append(item)
                offset += len(tag_list.items)
            else:
                more_results = False

        print('\nRetrieved a total of {0} access tags.'.format(len(tags)))
        matches = []
        for tag in tags:
            if self.sdk_label in tag.name:
                matches.append(tag.name)
        print('Found {0} access tags containing our label: {1}'.format(len(matches), matches))

    @needscredentials
    def test_detach_tag_user(self):
        # Construct a dict representation of a Resource model
        resource_model = {'resource_id': self.resource_crn}

        detach_tag_response = self.global_tagging_service.detach_tag(
            resources=[resource_model], tag_names=[self.user_tag_1, self.user_tag_2], tag_type='user'
        )

        assert detach_tag_response.get_status_code() == 200
        assert detach_tag_response.get_result() is not None
        tag_results = TagResults.from_dict(detach_tag_response.get_result())
        assert tag_results is not None
        print('\ndetach_tag(user) result: ', json.dumps(tag_results.to_dict(), indent=2))

        for elem in tag_results.results:
            assert elem.is_error is False

        # Make sure the tag is in fact attached to the resource
        tag_names = self.get_tag_names_for_resource(self.resource_crn, 'user')
        assert self.user_tag_1 not in tag_names
        assert self.user_tag_2 not in tag_names

    @needscredentials
    def test_detach_tag_access(self):
        # Construct a dict representation of a Resource model
        resource_model = {'resource_id': self.resource_crn}

        detach_tag_response = self.global_tagging_service.detach_tag(
            resources=[resource_model], tag_names=[self.access_tag_1, self.access_tag_2], tag_type='access'
        )

        assert detach_tag_response.get_status_code() == 200
        assert detach_tag_response.get_result() is not None
        tag_results = TagResults.from_dict(detach_tag_response.get_result())
        assert tag_results is not None
        print('\ndetach_tag(access) result: ', json.dumps(tag_results.to_dict(), indent=2))

        for elem in tag_results.results:
            assert elem.is_error is False

        # Make sure the tag is in fact attached to the resource
        tag_names = self.get_tag_names_for_resource(self.resource_crn, 'access')
        assert self.access_tag_1 not in tag_names
        assert self.access_tag_2 not in tag_names

    @needscredentials
    def test_delete_tag_user(self):
        delete_tag_response = self.global_tagging_service.delete_tag(tag_name=self.user_tag_1, tag_type='user')

        assert delete_tag_response.get_status_code() == 200
        assert delete_tag_response.get_result() is not None
        delete_tag_results = DeleteTagResults.from_dict(delete_tag_response.get_result())
        assert delete_tag_results is not None
        print('\ndelete_tag(user) result: ', json.dumps(delete_tag_results.to_dict(), indent=2))

        for item in delete_tag_results.results:
            assert item.is_error is False

    @needscredentials
    def test_delete_tag_access(self):
        delete_tag_response = self.global_tagging_service.delete_tag(tag_name=self.access_tag_1, tag_type='access')

        assert delete_tag_response.get_status_code() == 200
        assert delete_tag_response.get_result() is not None
        delete_tag_results = DeleteTagResults.from_dict(delete_tag_response.get_result())
        assert delete_tag_results is not None
        print('\ndelete_tag(access) result: ', json.dumps(delete_tag_results.to_dict(), indent=2))

        for item in delete_tag_results.results:
            assert item.is_error is False

    @needscredentials
    def test_delete_tag_all_user(self):
        delete_tag_all_response = self.global_tagging_service.delete_tag_all(tag_type='user')

        assert delete_tag_all_response.get_status_code() == 200
        assert delete_tag_all_response.get_result() is not None
        delete_tags_result = DeleteTagsResult.from_dict(delete_tag_all_response.get_result())
        assert delete_tags_result is not None
        print('\ndelete_tag_all(user) result: ', json.dumps(delete_tags_result.to_dict(), indent=2))

        for item in delete_tags_result.items:
            assert item.is_error is False

    @needscredentials
    def test_delete_tag_all_access(self):
        delete_tag_all_response = self.global_tagging_service.delete_tag_all(tag_type='access')

        assert delete_tag_all_response.get_status_code() == 200
        assert delete_tag_all_response.get_result() is not None
        delete_tags_result = DeleteTagsResult.from_dict(delete_tag_all_response.get_result())
        assert delete_tags_result is not None
        print('\ndelete_tag_all(access) result: ', json.dumps(delete_tags_result.to_dict(), indent=2))

        for item in delete_tags_result.items:
            assert item.is_error is False
