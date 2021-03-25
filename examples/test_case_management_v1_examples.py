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
Examples for CaseManagementV1
"""

import io
import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.case_management_v1 import *

#
# This file provides an example of how to use the Case Management service.
#
# The following configuration properties are assumed to be defined:
#
# CASE_MANAGEMENT_URL=<service url>
# CASE_MANAGEMENT_AUTH_TYPE=iam
# CASE_MANAGEMENT_AUTH_URL=<IAM token service URL - omit this if using the production environment>
# CASE_MANAGEMENT_APIKEY=<IAM apikey>
# CASE_MANAGEMENT_RESOURCE_CRN=<CRN of resource to use in examples>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'case_management.env'

case_management_service = None
config = None
case_number = None
attachment_id = None
resource_crn = None


##############################################################################
# Start of Examples for Service: CaseManagementV1
##############################################################################
# region
class TestCaseManagementV1Examples():
    """
    Example Test Class for CaseManagementV1
    """

    @classmethod
    def setup_class(cls):
        global case_management_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            case_management_service = CaseManagementV1.new_instance(
            )

            # end-common
            assert case_management_service is not None

            # Load the configuration
            global config
            config = read_external_sources(
                CaseManagementV1.DEFAULT_SERVICE_NAME)

            global resource_crn
            resource_crn = config['RESOURCE_CRN']

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason='External configuration not available, skipping...'
    )

    @needscredentials
    def test_create_case_example(self):
        """
        create_case request example
        """
        try:
            # begin-createCase

            offering_type = OfferingType(
                group='crn_service_name',
                key='cloud-object-storage'
            )
            offering_payload = Offering(
                name='Cloud Object Storage',
                type=offering_type
            )

            case = case_management_service.create_case(
                type='technical',
                subject='Example technical case',
                description='This is an example case description. This is where the problem would be described.',
                offering=offering_payload,
                severity=4,
            ).get_result()

            print('\ncreate_case() result:\n' + json.dumps(case, indent=2))

            # end-createCase

            assert case is not None
            assert case['number'] is not None

            global case_number
            case_number = case['number']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_case_example(self):
        """
        get_case request example
        """
        assert case_number is not None

        try:
            # begin-getCase

            fields_to_return = [
                GetCaseEnums.Fields.DESCRIPTION,
                GetCaseEnums.Fields.STATUS,
                GetCaseEnums.Fields.SEVERITY,
                GetCaseEnums.Fields.CREATED_BY,
            ]

            case = case_management_service.get_case(
                case_number=case_number,
                fields=fields_to_return
            ).get_result()

            print('\nget_case() result:\n' + json.dumps(case, indent=2))

            # end-getCase

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_cases_example(self):
        """
        get_cases request example
        """
        try:
            # begin-getCases

            case_list = case_management_service.get_cases(
                offset=0,
                limit=100,
                search='blocker',
                sort=GetCasesEnums.Fields.UPDATED_AT,
            ).get_result()

            print('\nget_cases() result:\n' + json.dumps(case_list, indent=2))

            # end-getCases

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_add_comment_example(self):
        """
        add_comment request example
        """
        assert case_number is not None

        try:
            # begin-addComment

            comment = case_management_service.add_comment(
                case_number=case_number,
                comment='This is an example comment.'
            ).get_result()

            print('\nadd_comment() result:\n' + json.dumps(comment, indent=2))

            # end-addComment

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_add_watchlist_example(self):
        """
        add_watchlist request example
        """
        assert case_number is not None

        try:
            # begin-addWatchlist

            watchlist_users = [
                User(realm='IBMid', user_id='abc@ibm.com')
            ]

            watchlist_add_response = case_management_service.add_watchlist(
                case_number=case_number,
                watchlist=watchlist_users,
            ).get_result()

            print('\nadd_watchlist() result:\n' + json.dumps(watchlist_add_response, indent=2))

            # end-addWatchlist

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_remove_watchlist_example(self):
        """
        remove_watchlist request example
        """
        assert case_number is not None

        try:
            # begin-removeWatchlist

            watchlist_users = [
                User(realm='IBMid', user_id='abc@ibm.com')
            ]

            watchlist = case_management_service.remove_watchlist(
                case_number=case_number,
                watchlist=watchlist_users,
            ).get_result()

            print('\nremove_watchlist() result:\n' + json.dumps(watchlist, indent=2))

            # end-removeWatchlist

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_add_resource_example(self):
        """
        add_resource request example
        """
        assert case_number is not None
        assert resource_crn is not None

        try:
            # begin-addResource

            resource = case_management_service.add_resource(
                case_number=case_number,
                crn=resource_crn,
                note='This resource is the service that is having the problem.',
            ).get_result()

            print('\nadd_resource() result:\n' + json.dumps(resource, indent=2))

            # end-addResource

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_upload_file_example(self):
        """
        upload_file request example
        """
        assert case_number is not None

        try:
            # begin-uploadFile

            example_file_content = b'This is the content of the file to upload.'

            file_with_metadata_model = {
                'data': io.BytesIO(example_file_content).getvalue(),
                'filename': 'example.log',
                'content_type': 'application/octet-stream',
            }

            files_to_upload = [file_with_metadata_model]

            attachment = case_management_service.upload_file(
                case_number=case_number,
                file=files_to_upload,
            ).get_result()

            print('\nupload_file() result:\n' + json.dumps(attachment, indent=2))

            # end-uploadFile

            assert attachment is not None
            assert attachment['id'] is not None

            global attachment_id
            attachment_id = attachment['id']

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_download_file_example(self):
        """
        download_file request example
        """
        assert case_number is not None
        assert attachment_id is not None

        try:
            # begin-downloadFile

            response = case_management_service.download_file(
                case_number=case_number,
                file_id=attachment_id,
            )

            file = response.get_result()

            print('\ndownload_file() result:\n')
            print('Attachment content-type:', response.get_headers()['content-type'])
            print('Attachment contents:', file.content)

            # end-downloadFile

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_file_example(self):
        """
        delete_file request example
        """
        assert case_number is not None
        assert attachment_id is not None

        try:
            # begin-deleteFile

            attachment_list = case_management_service.delete_file(
                case_number=case_number,
                file_id=attachment_id
            ).get_result()

            print('\ndelete_file() result:\n' + json.dumps(attachment_list, indent=2))

            # end-deleteFile

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_case_status_example(self):
        """
        update_case_status request example
        """
        assert case_number is not None

        try:
            # begin-updateCaseStatus

            status_payload_model = {
                'action': 'resolve',
                'comment': 'The problem has been resolved.',
                'resolution_code': 1,
            }

            case = case_management_service.update_case_status(
                case_number=case_number,
                status_payload=status_payload_model
            ).get_result()

            print('\nupdate_case_status() result:\n' + json.dumps(case, indent=2))

            # end-updateCaseStatus

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: CaseManagementV1
##############################################################################
