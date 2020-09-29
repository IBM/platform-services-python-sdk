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
Examples for IamIdentityV1
"""

import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.iam_identity_v1 import *

# Config file name
config_file = 'iam_identity.env'

iam_identity_service = None

config = None

apikeyName = 'Python-SDK-IT-ApiKey'
serviceIDName = 'Python-SDK-IT-ServiceId'
newDescription = 'This is an updated description'

accountId = None
iamId = None
apikey = None



##############################################################################
# Start of Examples for Service: IamIdentityV1
##############################################################################
# region
class TestIamIdentityV1Examples():
    """
    Example Test Class for IamIdentityV1
    """

    @classmethod
    def setup_class(cls):
        global iam_identity_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            iam_identity_service = IamIdentityV1.new_instance()
            
            # end-common
            assert iam_identity_service is not None

            # Load the configuration
            global config
            config = read_external_sources(IamIdentityV1.DEFAULT_SERVICE_NAME)

            accountId = config['ACCOUNT_ID']
            iamId = config['IAM_ID']
            apikey = config['APIKEY']
        
        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_api_key_example(self):
        """
        create_api_key request example
        """
        try:
            # begin-create_api_key

            api_key = iam_identity_service.create_api_key(
                name= apikeyName,
                iam_id= iamId
             ).get_result()

            print(json.dumps(api_key, indent=2))

            # end-create_api_key

            global apikeyId
            apikeyId = api_key['id']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_api_key_example(self):
        """
        get_api_key request example
        """
        try:
            # begin-get_api_key

            api_key = iam_identity_service.get_api_key(
                id= apikeyId
            ).get_result()

            print(json.dumps(api_key, indent=2))

            # end-get_api_key

            global apikeyEtag
            apikeyEtag = api_key['entity_tag']

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_get_api_keys_details_example(self):
        """
        get_api_keys_details request example
        """
        try:
            # begin-get_api_keys_details

            api_key = iam_identity_service.get_api_keys_details(
                iam_api_key= apikey
            ).get_result()

            print(json.dumps(api_key, indent=2))

            # end-get_api_keys_details

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_api_keys_example(self):
        """
        list_api_keys request example
        """
        try:
            # begin-list_api_keys

            api_key_list = iam_identity_service.list_api_keys(
                account_id= accountId,
                iam_id= iamId
            ).get_result()

            print(json.dumps(api_key_list, indent=2))

            # end-list_api_keys

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_api_key_example(self):
        """
        update_api_key request example
        """
        try:
            # begin-update_api_key

            api_key = iam_identity_service.update_api_key(
                id= apikeyId,
                if_match= apikeyEtag,
            ).get_result()

            print(json.dumps(api_key, indent=2))

            # end-update_api_key

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_lock_api_key_example(self):
        """
        lock_api_key request example
        """
        try:
            # begin-lock_api_key

            response = iam_identity_service.lock_api_key(
                id= apikeyId
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-lock_api_key

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_unlock_api_key_example(self):
        """
        unlock_api_key request example
        """
        try:
            # begin-unlock_api_key

            response = iam_identity_service.unlock_api_key(
                id= apikeyId
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-unlock_api_key

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_delete_api_key_example(self):
        """
        delete_api_key request example
        """
        try:
            # begin-delete_api_key

            response = iam_identity_service.delete_api_key(
                id= apikeyId
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_api_key

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_service_id_example(self):
        """
        create_service_id request example
        """
        try:
            # begin-create_service_id

            service_id = iam_identity_service.create_service_id(
                account_id= accountId,
                name= serviceIDName
            ).get_result()

            print(json.dumps(service_id, indent=2))

            # end-create_service_id

            global serviceId
            serviceId = service_id['id']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_service_id_example(self):
        """
        get_service_id request example
        """
        try:
            # begin-get_service_id

            service_id = iam_identity_service.get_service_id(
                id= serviceId
            ).get_result()

            print(json.dumps(service_id, indent=2))

            # end-get_service_id

            global serviceIDEtag
            serviceIDEtag = service_id['entity_tag']

        except ApiException as e:
            pytest.fail(str(e))
    
    @needscredentials
    def test_list_service_ids_example(self):
        """
        list_service_ids request example
        """
        try:
            # begin-list_service_ids

            service_id_list = iam_identity_service.list_service_ids(
                account_id= accountId,
                name= serviceIDName,
                pagesize= 100
            ).get_result()

            print(json.dumps(service_id_list, indent=2))

            # end-list_service_ids

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_service_id_example(self):
        """
        update_service_id request example
        """
        try:
            # begin-update_service_id

            service_id = iam_identity_service.update_service_id(
                id= serviceId,
                if_match= serviceIDEtag,
            ).get_result()

            print(json.dumps(service_id, indent=2))

            # end-update_service_id

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_lock_service_id_example(self):
        """
        lock_service_id request example
        """
        try:
            # begin-lock_service_id

            service_id = iam_identity_service.lock_service_id(
                id= serviceId
            ).get_result()

            print(json.dumps(service_id, indent=2))

            # end-lock_service_id

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_unlock_service_id_example(self):
        """
        unlock_service_id request example
        """
        try:
            # begin-unlock_service_id

            service_id = iam_identity_service.unlock_service_id(
                id= serviceId
            ).get_result()

            print(json.dumps(service_id, indent=2))

            # end-unlock_service_id

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_service_id_example(self):
        """
        delete_service_id request example
        """
        try:
            # begin-delete_service_id

            response = iam_identity_service.delete_service_id(
                id= serviceId
            ).get_result()

            print(json.dumps(response, indent=2))

            # end-delete_service_id

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: IamIdentityV1
##############################################################################
