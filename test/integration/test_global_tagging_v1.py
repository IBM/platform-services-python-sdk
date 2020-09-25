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


class TestGlobalTaggingV1():
    """
    Integration Test Class for GlobalTaggingV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.global_tagging_service = GlobalTaggingV1.new_instance()
            assert cls.global_tagging_service is not None

            cls.config = read_external_sources(
                GlobalTaggingV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.resource_crn = cls.config.get("RESOURCE_CRN")
            assert cls.resource_crn is not None

            assert cls.config["URL"] == cls.global_tagging_service.service_url

            cls.tag_name = 'python-sdk-' + str(randint(0, 100000))

            print('Service URL: ', cls.global_tagging_service.service_url)
            print('Resource CRN: ', cls.resource_crn)
            print('Test tag: ', cls.tag_name)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_list_tags(self):

        list_tags_response = self.global_tagging_service.list_tags(
            offset=0, limit=1000)

        assert list_tags_response.get_status_code() == 200
        tag_list = list_tags_response.get_result()
        assert tag_list is not None
        # print('\nlist_tags result: ', json.dumps(tag_list, indent=2))
        items = tag_list.get('items')
        assert items is not None

    @needscredentials
    def test_attach_tag(self):

        # Construct a dict representation of a Resource model
        resource_model = {
            'resource_id': self.resource_crn,
        }

        attach_tag_response = self.global_tagging_service.attach_tag(
            resources=[resource_model],
            tag_names=[self.tag_name]
        )

        assert attach_tag_response.get_status_code() == 200
        tag_results = attach_tag_response.get_result()
        assert tag_results is not None
        # print('\nattach_tag() result: ', json.dumps(tag_results, indent=2))

        # Make sure the tag is in fact attached to the resource
        tag_names = self.get_tag_names_for_resource(
            resource_id=self.resource_crn)
        assert self.tag_name in tag_names

    @needscredentials
    def test_detach_tag(self):

        # Construct a dict representation of a Resource model
        resource_model = {
            'resource_id': self.resource_crn
        }

        detach_tag_response = self.global_tagging_service.detach_tag(
            resources=[resource_model],
            tag_names=[self.tag_name]
        )

        assert detach_tag_response.get_status_code() == 200
        tag_results = detach_tag_response.get_result()
        assert tag_results is not None
        # print('\ndetach_tag() result: ', json.dumps(tag_results, indent=2))

        # Make sure the tag is in fact attached to the resource
        tag_names = self.get_tag_names_for_resource(
            resource_id=self.resource_crn)
        assert self.tag_name not in tag_names

    @needscredentials
    def test_delete_tag(self):

        delete_tag_response = self.global_tagging_service.delete_tag(
            tag_name=self.tag_name
        )

        assert delete_tag_response.get_status_code() == 200
        delete_tag_results = delete_tag_response.get_result()
        assert delete_tag_results is not None
        # print('\ndelete_tag() result: ', json.dumps(
        #     delete_tag_results, indent=2))

    @needscredentials
    def test_delete_tag_all(self):
        delete_tag_all_response = self.global_tagging_service.delete_tag_all()

        assert delete_tag_all_response.get_status_code() == 200
        delete_tags_result = delete_tag_all_response.get_result()
        assert delete_tags_result is not None
        # print('\ndelete_tag_all() result: ', json.dumps(
        #     delete_tags_result, indent=2))

    def get_tag_names_for_resource(self, resource_id):
        tag_names = []
        response = self.global_tagging_service.list_tags(
            offset=0, limit=1000, attached_to=resource_id)
        tag_list = response.get_result()
        items = tag_list.get('items')
        if items is not None:
            for item in items:
                tag_names.append(item.get('name'))

        return tag_names
