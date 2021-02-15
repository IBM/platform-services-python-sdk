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

import os
import pytest
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.case_management_v1 import *

# Config file name
config_file = 'case_management_v1.env'

case_management_service = None

config = None


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
            config = read_external_sources(CaseManagementV1.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_cases_example(self):
        """
        get_cases request example
        """
        try:
            # begin-getCases

            case_list = case_management_service.get_cases().get_result()

            print(json.dumps(case_list, indent=2))

            # end-getCases

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_case_example(self):
        """
        create_case request example
        """
        try:
            # begin-createCase

            case = case_management_service.create_case(
                type='technical',
                subject='testString',
                description='testString'
            ).get_result()

            print(json.dumps(case, indent=2))

            # end-createCase

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_case_example(self):
        """
        get_case request example
        """
        try:
            # begin-getCase

            case = case_management_service.get_case(
                case_number='testString'
            ).get_result()

            print(json.dumps(case, indent=2))

            # end-getCase

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_case_status_example(self):
        """
        update_case_status request example
        """
        try:
            # begin-updateCaseStatus

            status_payload_model = {
                'action': 'resolve',
                'comment': 'It was actually a mistake',
                'resolution_code': 1
            }

            case = case_management_service.update_case_status(
                case_number='testString',
                status_payload=status_payload_model
            ).get_result()

            print(json.dumps(case, indent=2))

            # end-updateCaseStatus

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_add_comment_example(self):
        """
        add_comment request example
        """
        try:
            # begin-addComment

            comment = case_management_service.add_comment(
                case_number='testString',
                comment='This is a test comment'
            ).get_result()

            print(json.dumps(comment, indent=2))

            # end-addComment

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_add_watchlist_example(self):
        """
        add_watchlist request example
        """
        try:
            # begin-addWatchlist

            watchlist_add_response = case_management_service.add_watchlist(
                case_number='testString',
            ).get_result()

            print(json.dumps(watchlist_add_response, indent=2))

            # end-addWatchlist

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_add_resource_example(self):
        """
        add_resource request example
        """
        try:
            # begin-addResource

            resource = case_management_service.add_resource(
                case_number='testString',
            ).get_result()

            print(json.dumps(resource, indent=2))

            # end-addResource

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_upload_file_example(self):
        """
        upload_file request example
        """
        try:
            # begin-uploadFile

            file_with_metadata_model = {
                'data': io.BytesIO(b'This is a mock file.').getvalue()
            }

            attachment = case_management_service.upload_file(
                case_number='testString',
                file=[file_with_metadata_model]
            ).get_result()

            print(json.dumps(attachment, indent=2))

            # end-uploadFile

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_download_file_example(self):
        """
        download_file request example
        """
        try:
            # begin-downloadFile

            result = case_management_service.download_file(
                case_number='testString',
                file_id='testString'
            ).get_result()

            with open('/tmp/result.out', 'wb') as fp:
                fp.write(result)

            # end-downloadFile

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_remove_watchlist_example(self):
        """
        remove_watchlist request example
        """
        try:
            # begin-removeWatchlist

            watchlist = case_management_service.remove_watchlist(
                case_number='testString',
            ).get_result()

            print(json.dumps(watchlist, indent=2))

            # end-removeWatchlist

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_file_example(self):
        """
        delete_file request example
        """
        try:
            # begin-deleteFile

            attachment_list = case_management_service.delete_file(
                case_number='testString',
                file_id='testString'
            ).get_result()

            print(json.dumps(attachment_list, indent=2))

            # end-deleteFile

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: CaseManagementV1
##############################################################################
