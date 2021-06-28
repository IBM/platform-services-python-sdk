# # -*- coding: utf-8 -*-
# # (C) Copyright IBM Corp. 2020.
# #
# # Licensed under the Apache License, Version 2.0 (the 'License');
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# #      http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an 'AS IS' BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.
# """
# Integration Tests for CatalogManagementV1
# """
#
# import unittest
# import os
# from ibm_cloud_sdk_core import *
# from ibm_platform_services.catalog_management_v1 import *
# import pytest
# import time
#
# config_file = 'catalog_mgmt.env'
#
# sdk_label_prefix = 'python-sdk-IT'
#
# timestamp = int(time.time())
# expectedAccount = '67d27f28d43948b2b3bda9138f251a13'
# expectedLabel = '{}-{}'.format(sdk_label_prefix, timestamp)
# expectedShortDesc = 'test'
# expectedURL = 'https://cm.globalcatalog.test.cloud.ibm.com/api/v1-beta/catalogs/{}'
# expectedOfferingsURL = 'https://cm.globalcatalog.test.cloud.ibm.com/api/v1-beta/catalogs/{}/offerings'
# fakeName = 'bogus'
# fakeVersionLocator = 'bogus.bogus'
# expectedOfferingName = "test-offering"
# expectedOfferingURL = "https://cm.globalcatalog.test.cloud.ibm.com/api/v1-beta/catalogs/{}/offerings/{}"
#
#
# class TestCatalogManagementV1(unittest.TestCase):
#     """
#     Integration Test Class for CaatalogManagementV1
#     """
#     @classmethod
#     def setup_class(cls):
#         if os.path.exists(config_file):
#             os.environ['IBM_CREDENTIALS_FILE'] = config_file
#
#             cls.service = CatalogManagementV1.new_instance()
#
#             cls.config = read_external_sources(
#                 CatalogManagementV1.DEFAULT_SERVICE_NAME)
#             assert cls.config is not None
#
#             cls.gitToken = cls.config.get('GIT_TOKEN')
#             assert cls.gitToken is not None
#
#             cls.clean_catalogs(cls, expectedLabel)
#
#             print('Finished setup.')
#
#     @classmethod
#     def teardown_class(cls):
#         cls.clean_catalogs(cls, expectedLabel)
#
#     needscredentials = pytest.mark.skipif(
#         not os.path.exists(config_file),
#         reason="External configuration not available, skipping...")
#
#     def clean_catalogs(self, label):
#         print('Cleaning catalogs...')
#         result = self.service.list_catalogs().get_result()
#         if result is not None:
#             resources = result.get('resources')
#             # print("Catalogs to clean up: ", json.dumps(resources, indent=2))
#             for resource in resources:
#                 label = resource.get('label')
#                 if label.startswith(sdk_label_prefix):
#                     catalog_id = resource.get('id')
#                     print('Deleting catalog id={}, label={}'.format(
#                         catalog_id, label))
#                     self.service.delete_catalog(catalog_identifier=catalog_id)
#         print('Finished cleaning catalogs.')
#
#     def test_get_catalog_account(self):
#         response = self.service.get_catalog_account()
#
#         assert response is not None
#         assert response.get_status_code() == 200
#
#         result = response.get_result()
#         assert result.get('id') == expectedAccount
#         assert result.get('account_filters').get('include_all') is True
#         assert result.get('account_filters').get('category_filters') is None
#         assert result.get('account_filters').get('id_filters').get(
#             'include') is None
#         assert result.get('account_filters').get('id_filters').get(
#             'exclude') is None
#
#     def test_get_catalog_account_filters(self):
#         response = self.service.get_catalog_account_filters()
#
#         assert response is not None
#         assert response.get_status_code() == 200
#
#         result = response.get_result()
#         assert result.get('account_filters')[0].get('include_all') is True
#         assert result.get('account_filters')[0].get('category_filters') is None
#         assert result.get('account_filters')[0].get('id_filters').get(
#             'include') is None
#         assert result.get('account_filters')[0].get('id_filters').get(
#             'exclude') is None
#
#     def test_list_catalogs(self):
#         catalogCount = 0
#         catalogIndex = -1
#
#         createResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         createResult = createResponse.get_result()
#
#         listResponse = self.service.list_catalogs()
#
#         self.service.delete_catalog(catalog_identifier=createResult.get('id'))
#
#         if listResponse.get_result() is not None:
#             for i, resource in enumerate(
#                     listResponse.get_result().get('resources')):
#                 if resource.get('label') == expectedLabel:
#                     catalogCount = catalogCount + 1
#                     catalogIndex = i
#
#         assert listResponse is not None
#         assert listResponse.get_status_code() == 200
#
#         listResult = listResponse.get_result()
#         assert listResult.get('offset') == 0
#         assert listResult.get('limit') == 0
#         assert catalogCount == 1
#         assert listResult.get('last') is None
#         assert listResult.get('prev') is None
#         assert listResult.get('next') is None
#
#         resources = listResult.get('resources')
#         assert resources is not None
#         assert resources[catalogIndex].get('label') == expectedLabel
#         assert resources[catalogIndex].get(
#             'short_description') == expectedShortDesc
#         assert resources[catalogIndex].get('url') == expectedURL.format(
#             createResult.get('id'))
#         assert resources[catalogIndex].get(
#             'offerings_url') == expectedOfferingsURL.format(
#                 createResult.get('id'))
#         assert resources[catalogIndex].get('owning_account') == expectedAccount
#         assert resources[catalogIndex].get('catalog_filters').get(
#             'include_all') is False
#         assert resources[catalogIndex].get('catalog_filters').get(
#             'category_filters') is None
#         assert resources[catalogIndex].get('catalog_filters').get(
#             'id_filters').get('include') is None
#         assert resources[catalogIndex].get('catalog_filters').get(
#             'id_filters').get('exclude') is None
#
#     def test_create_catalog(self):
#         response = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#
#         assert response is not None
#         assert response.get_status_code() == 201
#
#         result = response.get_result()
#
#         self.service.delete_catalog(catalog_identifier=result.get('id'))
#
#         assert result.get('label') == expectedLabel
#         assert result.get('short_description') == expectedShortDesc
#         assert result.get('url') == expectedURL.format(result.get('id'))
#         assert result.get('offerings_url') == expectedOfferingsURL.format(
#             result.get('id'))
#         assert result.get('owning_account') == expectedAccount
#         assert result.get('catalog_filters').get('include_all') is False
#         assert result.get('catalog_filters').get('category_filters') is None
#         assert result.get('catalog_filters').get('id_filters').get(
#             'include') is None
#         assert result.get('catalog_filters').get('id_filters').get(
#             'exclude') is None
#
#     def test_get_catalog(self):
#         createResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         createResult = createResponse.get_result()
#
#         getResponse = self.service.get_catalog(
#             catalog_identifier=createResult.get('id'))
#         getResult = getResponse.get_result()
#
#         assert getResponse is not None
#         assert getResponse.get_status_code() == 200
#
#         self.service.delete_catalog(catalog_identifier=createResult.get('id'))
#
#         assert getResult.get('label') == expectedLabel
#         assert getResult.get('short_description') == expectedShortDesc
#         assert getResult.get('url') == expectedURL.format(getResult.get('id'))
#         assert getResult.get('offerings_url') == expectedOfferingsURL.format(
#             getResult.get('id'))
#         assert getResult.get('owning_account') == expectedAccount
#         assert getResult.get('catalog_filters').get('include_all') is False
#         assert getResult.get('catalog_filters').get('category_filters') is None
#         assert getResult.get('catalog_filters').get('id_filters').get(
#             'include') is None
#         assert getResult.get('catalog_filters').get('id_filters').get(
#             'exclude') is None
#
#     def test_get_catalog_failure(self):
#         with pytest.raises(ApiException) as e:
#             self.service.get_catalog(catalog_identifier=fakeName)
#         assert e.value.code == 404
#
#     def test_update_catalog(self):
#         expectedLabelUpdated = "test2"
#         expectedShortDescUpdated = "integration-test-update"
#
#         createResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         createResult = createResponse.get_result()
#
#         updateResponse = self.service.replace_catalog(
#             catalog_identifier=createResult.get('id'),
#             id=createResult.get('id'),
#             label=expectedLabelUpdated,
#             short_description=expectedShortDescUpdated)
#         updateResult = updateResponse.get_result()
#
#         self.service.delete_catalog(catalog_identifier=createResult.get('id'))
#
#         assert updateResponse is not None
#         assert updateResponse.get_status_code() == 200
#
#         assert updateResult.get('label') == expectedLabelUpdated
#         assert updateResult.get(
#             'short_description') == expectedShortDescUpdated
#         # assert updateResult.get('url') == expectedURL.format(createResult.get('id'))
#         # assert updateResult.get('offerings_url') == expectedOfferingsURL.format(createResult.get('id'))
#         # assert updateResult.get('owning_account') == expectedAccount
#         assert updateResult.get('catalog_filters').get('include_all') is True
#         assert updateResult.get('catalog_filters').get(
#             'category_filters') is None
#         assert updateResult.get('catalog_filters').get('id_filters').get(
#             'include') is None
#         assert updateResult.get('catalog_filters').get('id_filters').get(
#             'exclude') is None
#
#     def test_update_catalog_failure(self):
#         with pytest.raises(ApiException) as e:
#             self.service.replace_catalog(catalog_identifier=fakeName,
#                                          id=fakeName)
#         assert e.value.code == 404
#
#     def test_delete_catalog(self):
#         createResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         createResult = createResponse.get_result()
#
#         deleteResponse = self.service.delete_catalog(
#             catalog_identifier=createResult.get('id'),
#             id=createResult.get('id'))
#
#         assert deleteResponse is not None
#         assert deleteResponse.get_status_code() == 200
#
#     def test_delete_catalog_failure(self):
#         deleteResponse = self.service.delete_catalog(
#             catalog_identifier=fakeName, id=fakeName)
#
#         assert deleteResponse is not None
#         assert deleteResponse.get_status_code() == 200
#
#     def test_create_offering(self):
#         catalogResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         catalogResult = catalogResponse.get_result()
#
#         offeringResponse = self.service.create_offering(
#             catalog_identifier=catalogResult.get('id'),
#             name=expectedOfferingName,
#             label=expectedLabel)
#         offeringResult = offeringResponse.get_result()
#
#         self.service.delete_catalog(catalog_identifier=catalogResult.get('id'))
#
#         assert offeringResponse is not None
#         assert offeringResponse.get_status_code() == 201
#         assert offeringResult.get('name') == expectedOfferingName
#         assert offeringResult.get('url') == expectedOfferingURL.format(
#             catalogResult.get('id'), offeringResult.get('id'))
#         assert offeringResult.get('label') == expectedLabel
#
#     def test_get_offering(self):
#         catalogResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         catalogResult = catalogResponse.get_result()
#
#         offeringResponse = self.service.create_offering(
#             catalog_identifier=catalogResult.get('id'),
#             name=expectedOfferingName,
#             label=expectedLabel)
#         offeringResult = offeringResponse.get_result()
#
#         getResponse = self.service.get_offering(
#             catalog_identifier=catalogResult.get('id'),
#             offering_id=offeringResult.get('id'))
#         getResult = getResponse.get_result()
#
#         self.service.delete_catalog(catalog_identifier=catalogResult.get('id'))
#
#         assert getResponse is not None
#         assert getResponse.get_status_code() == 200
#         assert getResult.get('name') == expectedOfferingName
#         assert getResult.get('url') == expectedOfferingURL.format(
#             catalogResult.get('id'), offeringResult.get('id'))
#         assert getResult.get('label') == expectedLabel
#
#     def test_get_offering_failure(self):
#         createResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         createResult = createResponse.get_result()
#
#         with pytest.raises(ApiException) as e:
#             self.service.get_offering(
#                 catalog_identifier=createResult.get('id'),
#                 offering_id=fakeName)
#         assert e.value.code == 404
#
#         self.service.delete_catalog(catalog_identifier=createResult.get('id'))
#
#         with pytest.raises(ApiException) as e:
#             self.service.get_offering(
#                 catalog_identifier=createResult.get('id'),
#                 offering_id=fakeName)
#         assert e.value.code == 403
#
#     def test_list_offerings(self):
#         expectedFirst = "/api/v1-beta/catalogs/{}/offerings?limit=100&sort=label"
#         expectedLast = "/api/v1-beta/catalogs/{}/offerings?limit=100&sort=label"
#
#         catalogResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         catalogResult = catalogResponse.get_result()
#
#         offeringResponse = self.service.create_offering(
#             catalog_identifier=catalogResult.get('id'),
#             name=expectedOfferingName,
#             label=expectedLabel)
#         offeringResult = offeringResponse.get_result()
#
#         listResponse = self.service.list_offerings(
#             catalog_identifier=catalogResult.get('id'))
#         listResult = listResponse.get_result()
#
#         self.service.delete_catalog(catalog_identifier=catalogResult.get('id'))
#
#         assert listResponse is not None
#         assert listResponse.get_status_code() == 200
#         assert listResult.get('offset') == 0
#         assert listResult.get('limit') == 100
#         assert listResult.get('total_count') == 1
#         assert listResult.get('resource_count') == 1
#         assert listResult.get('first') == expectedFirst.format(
#             catalogResult.get('id'))
#         assert listResult.get('last') == expectedLast.format(
#             catalogResult.get('id'))
#
#         resources = listResult.get('resources')
#         assert resources is not None
#         assert resources[0].get('id') == offeringResult.get('id')
#         assert resources[0].get('url') == expectedOfferingURL.format(
#             catalogResult.get('id'), offeringResult.get('id'))
#         assert resources[0].get('label') == expectedLabel
#         assert resources[0].get('name') == expectedOfferingName
#         assert resources[0].get('catalog_id') == catalogResult.get('id')
#         assert resources[0].get('catalog_name') == expectedLabel
#
#     def test_delete_offering(self):
#         catalogResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         catalogResult = catalogResponse.get_result()
#
#         offeringResponse = self.service.create_offering(
#             catalog_identifier=catalogResult.get('id'),
#             name=expectedOfferingName,
#             label=expectedLabel)
#         offeringResult = offeringResponse.get_result()
#
#         deleteResponse = self.service.delete_offering(
#             catalog_identifier=catalogResult.get('id'),
#             offering_id=offeringResult.get('id'))
#
#         self.service.delete_catalog(catalog_identifier=catalogResult.get('id'))
#
#         assert deleteResponse is not None
#         assert deleteResponse.get_status_code() == 200
#
#     def test_delete_offering_failure(self):
#         catalogResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         catalogResult = catalogResponse.get_result()
#
#         deleteResponse = self.service.delete_offering(
#             catalog_identifier=catalogResult.get('id'), offering_id=fakeName)
#
#         self.service.delete_catalog(catalog_identifier=catalogResult.get('id'))
#
#         assert deleteResponse is not None
#         assert deleteResponse.get_status_code() == 200
#
#         with pytest.raises(ApiException) as e:
#             self.service.delete_offering(
#                 catalog_identifier=catalogResult.get('id'),
#                 offering_id=fakeName)
#         assert e.value.code == 403
#
#     def test_update_offering(self):
#         expectedLabelUpdate = "test-update"
#         expectedShortDescUpdate = "test-desc-update"
#
#         catalogResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         catalogResult = catalogResponse.get_result()
#
#         offeringResponse = self.service.create_offering(
#             catalog_identifier=catalogResult.get('id'),
#             name=expectedOfferingName,
#             label=expectedLabel)
#         offeringResult = offeringResponse.get_result()
#
#         updateResponse = self.service.replace_offering(
#             catalog_identifier=catalogResult.get('id'),
#             offering_id=offeringResult.get('id'),
#             id=offeringResult.get('id'),
#             rev=offeringResult.get('_rev'),
#             label=expectedLabelUpdate,
#             short_description=expectedShortDescUpdate)
#         updateResult = updateResponse.get_result()
#
#         self.service.delete_catalog(catalog_identifier=catalogResult.get('id'))
#
#         assert updateResponse is not None
#         assert updateResponse.get_status_code() == 200
#         assert updateResult.get('short_description') == expectedShortDescUpdate
#         assert updateResult.get('url') == expectedOfferingURL.format(
#             catalogResult.get('id'), offeringResult.get('id'))
#         assert updateResult.get('label') == expectedLabelUpdate
#
#     def test_update_offering_failure(self):
#         createResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         createResult = createResponse.get_result()
#
#         with pytest.raises(ApiException) as e:
#             self.service.replace_offering(
#                 catalog_identifier=createResult.get('id'),
#                 offering_id=fakeName,
#                 id=fakeName,
#                 rev=fakeName)
#         assert e.value.code == 404
#
#         self.service.delete_catalog(catalog_identifier=createResult.get('id'))
#
#         with pytest.raises(ApiException) as e:
#             self.service.replace_offering(
#                 catalog_identifier=createResult.get('id'),
#                 offering_id=fakeName,
#                 id=fakeName,
#                 rev=fakeName)
#         assert e.value.code == 403
#
#     def test_get_consumption_offerings(self):
#         getResponse = self.service.get_consumption_offerings()
#         assert getResponse is not None
#         assert getResponse.get_status_code() == 200
#
#         getResult = getResponse.get_result()
#         assert getResult.get('offset') == 0
#         assert getResult.get('limit') > 0
#         assert getResult.get('total_count') > 0
#         assert getResult.get('last') is not None
#         assert getResult.get('prev') is None
#         assert getResult.get('next') is not None
#         assert getResult.get('resources') is not None
#
#     def test_import_offering(self):
#         expectedOfferingZipURL = 'https://github.com/operator-framework/community-operators/blob/master/community-operators/jenkins-operator/0.4.0/jenkins-operator.v0.4.0.clusterserviceversion.yaml'
#         expectedOfferingTargetKind = 'roks'
#         expectedOfferingVersion = "0.4.0"
#         expectedJenkinsOfferingName = 'jenkins-operator'
#         expectedJenkinsOfferingLabel = 'Jenkins Operator'
#         expectedJenkinsOfferingShortDesc = 'Kubernetes native operator which fully manages Jenkins on Openshift.'
#
#         catalogResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         catalogResult = catalogResponse.get_result()
#
#         offeringResponse = self.service.import_offering(
#             catalog_identifier=catalogResult.get('id'),
#             zipurl=expectedOfferingZipURL,
#             x_auth_token=self.gitToken)
#         offeringResult = offeringResponse.get_result()
#
#         self.service.delete_catalog(catalog_identifier=catalogResult.get('id'))
#
#         assert offeringResponse is not None
#         assert offeringResponse.get_status_code() == 201
#         assert offeringResult.get('name') == expectedJenkinsOfferingName
#         assert offeringResult.get('url') == expectedOfferingURL.format(
#             catalogResult.get('id'), offeringResult.get('id'))
#         assert offeringResult.get('label') == expectedJenkinsOfferingLabel
#         assert offeringResult.get(
#             'short_description') == expectedJenkinsOfferingShortDesc
#         assert offeringResult.get('catalog_name') == expectedLabel
#         assert offeringResult.get('catalog_id') == catalogResult.get('id')
#         assert offeringResult.get('kinds') is not None
#         assert offeringResult.get('kinds')[0].get(
#             'target_kind') == expectedOfferingTargetKind
#         assert offeringResult.get('kinds')[0].get('versions') is not None
#         assert offeringResult.get('kinds')[0].get('versions')[0].get(
#             'version') == expectedOfferingVersion
#         assert offeringResult.get('kinds')[0].get('versions')[0].get(
#             'tgz_url') == expectedOfferingZipURL
#
#     def test_import_offering_version(self):
#         expectedOfferingZipURL = 'https://github.com/operator-framework/community-operators/blob/master/community-operators/jenkins-operator/0.3.31/jenkins-operator.v0.3.31.clusterserviceversion.yaml'
#         expectedOfferingZipURLUpdate = "https://github.com/operator-framework/community-operators/blob/master/community-operators/jenkins-operator/0.4.0/jenkins-operator.v0.4.0.clusterserviceversion.yaml"
#         expectedOfferingTargetKind = 'roks'
#         expectedOfferingVersion = "0.3.31"
#         expectedOfferingVersionUpdate = "0.4.0"
#         expectedJenkinsOfferingName = 'jenkins-operator'
#         expectedJenkinsOfferingLabel = 'Jenkins Operator'
#         expectedJenkinsOfferingShortDesc = 'Kubernetes native operator which fully manages Jenkins on Openshift.'
#
#         catalogResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         catalogResult = catalogResponse.get_result()
#
#         offeringResponse = self.service.import_offering(
#             catalog_identifier=catalogResult.get('id'),
#             zipurl=expectedOfferingZipURL,
#             x_auth_token=self.gitToken)
#         offeringResult = offeringResponse.get_result()
#
#         versionResponse = self.service.import_offering_version(
#             catalog_identifier=catalogResult.get('id'),
#             offering_id=offeringResult.get('id'),
#             zipurl=expectedOfferingZipURLUpdate,
#             x_auth_token=self.gitToken)
#         versionResult = versionResponse.get_result()
#
#         self.service.delete_catalog(catalog_identifier=catalogResult.get('id'))
#
#         assert versionResponse is not None
#         assert versionResponse.get_status_code() == 201
#         assert versionResult.get('name') == expectedJenkinsOfferingName
#         assert versionResult.get('url') == expectedOfferingURL.format(
#             catalogResult.get('id'), offeringResult.get('id'))
#         assert versionResult.get('label') == expectedJenkinsOfferingLabel
#         assert versionResult.get(
#             'short_description') == expectedJenkinsOfferingShortDesc
#         assert versionResult.get('catalog_name') == expectedLabel
#         assert versionResult.get('catalog_id') == catalogResult.get('id')
#         assert versionResult.get('kinds') is not None
#         assert versionResult.get('kinds')[0].get(
#             'target_kind') == expectedOfferingTargetKind
#         assert versionResult.get('kinds')[0].get('versions') is not None
#         assert versionResult.get('kinds')[0].get('versions')[0].get(
#             'version') == expectedOfferingVersion
#         assert versionResult.get('kinds')[0].get('versions')[0].get(
#             'tgz_url') == expectedOfferingZipURL
#         assert versionResult.get('kinds')[0].get('versions')[1].get(
#             'version') == expectedOfferingVersionUpdate
#         assert versionResult.get('kinds')[0].get('versions')[1].get(
#             'tgz_url') == expectedOfferingZipURLUpdate
#
#     def test_import_offering_version_failure(self):
#         expectedOfferingZipURL = 'https://github.com/operator-framework/community-operators/blob/master/community-operators/jenkins-operator/0.3.31/jenkins-operator.v0.3.31.clusterserviceversion.yaml'
#
#         createResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         createResult = createResponse.get_result()
#
#         with pytest.raises(ApiException) as e:
#             self.service.import_offering_version(
#                 catalog_identifier=createResult.get('id'),
#                 offering_id=fakeName,
#                 zipurl=expectedOfferingZipURL,
#                 x_auth_token=self.gitToken)
#         assert e.value.code == 404
#
#         self.service.delete_catalog(catalog_identifier=createResult.get('id'))
#
#         with pytest.raises(ApiException) as e:
#             self.service.import_offering_version(
#                 catalog_identifier=createResult.get('id'),
#                 offering_id=fakeName,
#                 zipurl=expectedOfferingZipURL,
#                 x_auth_token=self.gitToken)
#         assert e.value.code == 403
#
#     def test_reload_offering(self):
#         expectedOfferingZipURL = "https://github.com/operator-framework/community-operators/blob/master/community-operators/jenkins-operator/0.4.0/jenkins-operator.v0.4.0.clusterserviceversion.yaml"
#         expectedOfferingTargetKind = 'roks'
#         expectedOfferingVersion = "0.4.0"
#         expectedJenkinsOfferingName = 'jenkins-operator'
#         expectedJenkinsOfferingLabel = 'Jenkins Operator'
#         expectedJenkinsOfferingShortDesc = 'Kubernetes native operator which fully manages Jenkins on Openshift.'
#
#         catalogResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         catalogResult = catalogResponse.get_result()
#
#         offeringResponse = self.service.import_offering(
#             catalog_identifier=catalogResult.get('id'),
#             zipurl=expectedOfferingZipURL,
#             x_auth_token=self.gitToken)
#         offeringResult = offeringResponse.get_result()
#
#         reloadResponse = self.service.reload_offering(
#             catalog_identifier=catalogResult.get('id'),
#             offering_id=offeringResult.get('id'),
#             zipurl=expectedOfferingZipURL,
#             target_version=expectedOfferingVersion,
#             x_auth_token=self.gitToken)
#         reloadResult = reloadResponse.get_result()
#
#         self.service.delete_catalog(catalog_identifier=catalogResult.get('id'))
#
#         assert reloadResponse is not None
#         assert reloadResponse.get_status_code() == 200
#         assert reloadResult.get('name') == expectedJenkinsOfferingName
#         assert reloadResult.get('url') == expectedOfferingURL.format(
#             catalogResult.get('id'), offeringResult.get('id'))
#         assert reloadResult.get('label') == expectedJenkinsOfferingLabel
#         assert reloadResult.get(
#             'short_description') == expectedJenkinsOfferingShortDesc
#         assert reloadResult.get('catalog_name') == expectedLabel
#         assert reloadResult.get('catalog_id') == catalogResult.get('id')
#         assert reloadResult.get('kinds') is not None
#         assert reloadResult.get('kinds')[0].get(
#             'target_kind') == expectedOfferingTargetKind
#         assert reloadResult.get('kinds')[0].get('versions') is not None
#         assert reloadResult.get('kinds')[0].get('versions')[0].get(
#             'version') == expectedOfferingVersion
#         assert reloadResult.get('kinds')[0].get('versions')[0].get(
#             'tgz_url') == expectedOfferingZipURL
#
#     def test_reload_offering_failure(self):
#         expectedOfferingZipURL = 'https://github.com/operator-framework/community-operators/blob/master/community-operators/jenkins-operator/0.3.31/jenkins-operator.v0.3.31.clusterserviceversion.yaml'
#         expectedOfferingVersion = "0.4.0"
#
#         createResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         createResult = createResponse.get_result()
#
#         with pytest.raises(ApiException) as e:
#             self.service.reload_offering(
#                 catalog_identifier=createResult.get('id'),
#                 offering_id=fakeName,
#                 zipurl=expectedOfferingZipURL,
#                 target_version=expectedOfferingVersion)
#         assert e.value.code == 404
#
#         self.service.delete_catalog(catalog_identifier=createResult.get('id'))
#
#         with pytest.raises(ApiException) as e:
#             self.service.reload_offering(
#                 catalog_identifier=createResult.get('id'),
#                 offering_id=fakeName,
#                 zipurl=expectedOfferingZipURL,
#                 target_version=expectedOfferingVersion)
#         assert e.value.code == 403
#
#     def test_get_version(self):
#         expectedOfferingZipURL = "https://github.com/operator-framework/community-operators/blob/master/community-operators/jenkins-operator/0.4.0/jenkins-operator.v0.4.0.clusterserviceversion.yaml"
#         expectedOfferingTargetKind = 'roks'
#         expectedOfferingVersion = "0.4.0"
#         expectedJenkinsOfferingName = 'jenkins-operator'
#         expectedJenkinsOfferingLabel = 'Jenkins Operator'
#         expectedJenkinsOfferingShortDesc = 'Kubernetes native operator which fully manages Jenkins on Openshift.'
#
#         catalogResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         catalogResult = catalogResponse.get_result()
#
#         offeringResponse = self.service.import_offering(
#             catalog_identifier=catalogResult.get('id'),
#             zipurl=expectedOfferingZipURL,
#             x_auth_token=self.gitToken)
#         offeringResult = offeringResponse.get_result()
#
#         reloadResponse = self.service.get_version(
#             version_loc_id=offeringResult.get('kinds')[0].get(
#                 'versions')[0].get('version_locator'))
#         reloadResult = reloadResponse.get_result()
#
#         self.service.delete_catalog(catalog_identifier=catalogResult.get('id'))
#
#         assert reloadResponse is not None
#         assert reloadResponse.get_status_code() == 200
#         assert reloadResult.get('name') == expectedJenkinsOfferingName
#         assert reloadResult.get('url') == expectedOfferingURL.format(
#             catalogResult.get('id'), offeringResult.get('id'))
#         assert reloadResult.get('label') == expectedJenkinsOfferingLabel
#         assert reloadResult.get(
#             'short_description') == expectedJenkinsOfferingShortDesc
#         assert reloadResult.get('catalog_name') == expectedLabel
#         assert reloadResult.get('catalog_id') == catalogResult.get('id')
#         assert reloadResult.get('kinds') is not None
#         assert reloadResult.get('kinds')[0].get(
#             'target_kind') == expectedOfferingTargetKind
#         assert reloadResult.get('kinds')[0].get('versions') is not None
#         assert reloadResult.get('kinds')[0].get('versions')[0].get(
#             'version') == expectedOfferingVersion
#         assert reloadResult.get('kinds')[0].get('versions')[0].get(
#             'tgz_url') == expectedOfferingZipURL
#
#     def test_get_version_failure(self):
#         with pytest.raises(ApiException) as e:
#             self.service.get_version(version_loc_id=fakeVersionLocator)
#         assert e.value.code == 404
#
#     def test_delete_version(self):
#         expectedOfferingZipURL = "https://github.com/operator-framework/community-operators/blob/master/community-operators/jenkins-operator/0.4.0/jenkins-operator.v0.4.0.clusterserviceversion.yaml"
#
#         catalogResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         catalogResult = catalogResponse.get_result()
#
#         offeringResponse = self.service.import_offering(
#             catalog_identifier=catalogResult.get('id'),
#             zipurl=expectedOfferingZipURL,
#             x_auth_token=self.gitToken)
#         offeringResult = offeringResponse.get_result()
#
#         reloadResponse = self.service.delete_version(
#             version_loc_id=offeringResult.get('kinds')[0].get(
#                 'versions')[0].get('version_locator'))
#
#         self.service.delete_catalog(catalog_identifier=catalogResult.get('id'))
#
#         assert reloadResponse is not None
#         assert reloadResponse.get_status_code() == 200
#
#     def test_delete_version_failure(self):
#         with pytest.raises(ApiException) as e:
#             self.service.delete_version(version_loc_id=fakeVersionLocator)
#         assert e.value.code == 404
#
#     def test_get_version_about(self):
#         expectedOfferingZipURL = "https://github.com/operator-framework/community-operators/blob/master/community-operators/jenkins-operator/0.4.0/jenkins-operator.v0.4.0.clusterserviceversion.yaml"
#
#         catalogResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         catalogResult = catalogResponse.get_result()
#
#         offeringResponse = self.service.import_offering(
#             catalog_identifier=catalogResult.get('id'),
#             zipurl=expectedOfferingZipURL,
#             x_auth_token=self.gitToken)
#         offeringResult = offeringResponse.get_result()
#
#         getResponse = self.service.get_version_about(
#             version_loc_id=offeringResult.get('kinds')[0].get(
#                 'versions')[0].get('version_locator'))
#         getResult = getResponse.get_result()
#
#         self.service.delete_catalog(catalog_identifier=catalogResult.get('id'))
#
#         assert getResponse is not None
#         assert getResponse.get_status_code() == 200
#         assert getResult is not None
#
#     def test_get_version_about_failure(self):
#         with pytest.raises(ApiException) as e:
#             self.service.get_version_about(version_loc_id=fakeVersionLocator)
#         assert e.value.code == 404
#
#     def test_get_version_updates(self):
#         expectedOfferingZipURL = 'https://github.com/operator-framework/community-operators/blob/master/community-operators/jenkins-operator/0.3.31/jenkins-operator.v0.3.31.clusterserviceversion.yaml'
#         expectedOfferingZipURLUpdate = "https://github.com/operator-framework/community-operators/blob/master/community-operators/jenkins-operator/0.4.0/jenkins-operator.v0.4.0.clusterserviceversion.yaml"
#         expectedOfferingVersionUpdate = "0.4.0"
#
#         catalogResponse = self.service.create_catalog(
#             label=expectedLabel, short_description=expectedShortDesc)
#         catalogResult = catalogResponse.get_result()
#
#         offeringResponse = self.service.import_offering(
#             catalog_identifier=catalogResult.get('id'),
#             zipurl=expectedOfferingZipURL,
#             x_auth_token=self.gitToken)
#         offeringResult = offeringResponse.get_result()
#
#         versionResponse = self.service.import_offering_version(
#             catalog_identifier=catalogResult.get('id'),
#             offering_id=offeringResult.get('id'),
#             zipurl=expectedOfferingZipURLUpdate,
#             x_auth_token=self.gitToken)
#         versionResult = versionResponse.get_result()
#
#         updateResponse = self.service.get_version_updates(
#             version_loc_id=offeringResult.get('kinds')[0].get(
#                 'versions')[0].get('version_locator'))
#         updateResult = updateResponse.get_result()
#
#         self.service.delete_catalog(catalog_identifier=catalogResult.get('id'))
#
#         assert updateResponse is not None
#         assert updateResponse.get_status_code() == 200
#         assert updateResult is not None
#         assert updateResult[0].get('version_locator') == versionResult.get(
#             'kinds')[0].get('versions')[1].get('version_locator')
#         assert updateResult[0].get('version') == expectedOfferingVersionUpdate
#         assert updateResult[0].get(
#             'package_version') == expectedOfferingVersionUpdate
#         assert updateResult[0].get('can_update') is True
#
#     def test_get_version_updates_failure(self):
#         with pytest.raises(ApiException) as e:
#             self.service.get_version_updates(version_loc_id=fakeVersionLocator)
#         assert e.value.code == 404
#
#     def test_get_license_providers(self):
#         expectedTotalResults = 1
#         expectedTotalPages = 1
#         expectedName = "IBM Passport Advantage"
#         expectedOfferingType = "content"
#         expectedCreateURL = "https://www.ibm.com/software/passportadvantage/aboutpassport.html"
#         expectedInfoURL = "https://www.ibm.com/software/passportadvantage/"
#         expectedURL = "/v1/licensing/license_providers/11cabc37-c4a7-410b-894d-8cb3586423f1"
#         expectedState = "active"
#
#         listResponse = self.service.get_license_providers()
#
#         assert listResponse is not None
#         assert listResponse.get_status_code() == 200
#
#         listResult = listResponse.get_result()
#         assert listResult.get('total_results') == expectedTotalResults
#         assert listResult.get('total_pages') == expectedTotalPages
#
#         resources = listResult.get('resources')
#         assert resources is not None
#         assert len(resources) == 1
#         assert resources[0].get('name') == expectedName
#         assert resources[0].get('offering_type') == expectedOfferingType
#         assert resources[0].get('create_url') == expectedCreateURL
#         assert resources[0].get('info_url') == expectedInfoURL
#         assert resources[0].get('url') == expectedURL
#         assert resources[0].get('state') == expectedState
#
#     def test_list_license_entitlements(self):
#         expectedResourceCount = 0
#         expectedTotalResults = 0
#         expectedTotalPages = 1
#
#         listResponse = self.service.list_license_entitlements()
#
#         assert listResponse is not None
#         assert listResponse.get_status_code() == 200
#
#         listResult = listResponse.get_result()
#         assert listResult.get('total_results') == expectedTotalResults
#         assert listResult.get('total_pages') == expectedTotalPages
#
#         resources = listResult.get('resources')
#         assert len(resources) == expectedResourceCount
#
#     def test_search_license_versions(self):
#         with pytest.raises(ApiException) as e:
#             self.service.search_license_versions(q=fakeName)
#         assert e.value.code == 403
#
#     def test_search_license_offerings(self):
#         with pytest.raises(ApiException) as e:
#             self.service.search_license_offerings(q=fakeName)
#         assert e.value.code == 403
#
#
# if __name__ == '__main__':
#     unittest.main()
