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
Examples for GlobalTaggingV1
"""

import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.global_tagging_v1 import *

#
# This file provides an example of how to use the Global Tagging service.
#
# The following configuration properties are assumed to be defined:
#
# GLOBAL_TAGGING_URL=<service url>
# GLOBAL_TAGGING_AUTHTYPE=iam
# GLOBAL_TAGGING_APIKEY=<IAM api key>
# GLOBAL_TAGGING_AUTH_URL=<IAM token service URL - omit this if using the production environment>
# GLOBAL_TAGGING_RESOURCE_CRN=<the crn of the resource to be used in the examples>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'global_tagging.env'

global_tagging_service = None

config = None
resource_crn = None


##############################################################################
# Start of Examples for Service: GlobalTaggingV1
##############################################################################
# region
class TestGlobalTaggingV1Examples:
    """
    Example Test Class for GlobalTaggingV1
    """

    @classmethod
    def setup_class(cls):
        global global_tagging_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            global_tagging_service = GlobalTaggingV1.new_instance()

            # end-common
            assert global_tagging_service is not None

            # Load the configuration
            global config
            config = read_external_sources(GlobalTaggingV1.DEFAULT_SERVICE_NAME)

            global resource_crn
            resource_crn = config.get("RESOURCE_CRN")

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_tag_example(self):
        """
        create_tag request example
        """
        try:
            print('\ncreate_tag() result:')
            # begin-create_tag

            create_tag_results = global_tagging_service.create_tag(
                tag_names=['env:example-access-tag'], tag_type='access'
            ).get_result()

            print(json.dumps(create_tag_results, indent=2))

            # end-create_tag

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_tags_example(self):
        """
        list_tags request example
        """
        try:
            print('\nlist_tags() result:')
            # begin-list_tags

            tag_list = global_tagging_service.list_tags(
                tag_type='user', attached_only=True, full_data=True, providers=['ghost'], order_by_name='asc'
            ).get_result()

            print(json.dumps(tag_list, indent=2))

            # end-list_tags

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_attach_tag_example(self):
        """
        attach_tag request example
        """
        try:
            print('\nattach_tag() result:')
            # begin-attach_tag

            resource_model = {'resource_id': resource_crn}

            tag_results = global_tagging_service.attach_tag(
                tag_names=['tag_test_1', 'tag_test_2'], tag_type='user'
            ).get_result()

            print(json.dumps(tag_results, indent=2))

            # end-attach_tag

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_detach_tag_example(self):
        """
        detach_tag request example
        """
        try:
            print('\ndetach_tag() result:')
            # begin-detach_tag

            resource_model = {'resource_id': resource_crn}

            tag_results = global_tagging_service.detach_tag(
                tag_names=['tag_test_1', 'tag_test_2'], tag_type='user'
            ).get_result()

            print(json.dumps(tag_results, indent=2))

            # end-detach_tag

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_tag_example(self):
        """
        delete_tag request example
        """
        try:
            print('\ndelete_tag() result:')
            # begin-delete_tag

            delete_tag_results = global_tagging_service.delete_tag(
                tag_name='env:example-access-tag', tag_type='access'
            ).get_result()

            print(json.dumps(delete_tag_results, indent=2))

            # end-delete_tag

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_tag_all_example(self):
        """
        delete_tag_all request example
        """
        try:
            print('\ndelete_tag_all() result:')
            # begin-delete_tag_all

            delete_tags_result = global_tagging_service.delete_tag_all(tag_type='user').get_result()

            print(json.dumps(delete_tags_result, indent=2))

            # end-delete_tag_all

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: GlobalTaggingV1
##############################################################################
