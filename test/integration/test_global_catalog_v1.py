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
Test the platform service Global Catalog API operations
"""

import unittest
import os
from ibm_platform_services import GlobalCatalogV1
from ibm_cloud_sdk_core import *
import pytest

configFile = 'global_catalog.env'
configLoaded = None

if os.path.exists(configFile):
    os.environ['IBM_CREDENTIALS_FILE'] = configFile
    configLoaded = True
else:
    print('External configuration was not found, skipping tests...')

class TestGlobalCatalogV1(unittest.TestCase):

    @classmethod
    def setUp(self):
        if not configLoaded:
            raise unittest.SkipTest('External configuration not available, skipping...')

        self.service = GlobalCatalogV1.new_instance()
        assert self.service is not None

        self.defaultEntry = {
            'name': 'someName',
            'id': 'someId',
            'active': False,
            'kind': 'service',
            'disabled': False,
            'tags': ['a', 'b', 'c'],
            'overview_ui': {
                'en': {
                   'display_name': 'display',
                   'long_description': 'longDesc',
                   'description': 'desc'
               }
           },
           'images': {
             'image': 'image',
             'small_image': 'small',
             'medium_image': 'medium',
             'feature_image': 'feature'
            },
           'provider': {
             'email': 'bogus@us.ibm.com',
             'name': 'someName'
            },
            'restrictions': 'private',
            'metadata': {
                'pricing': {
                    'origin': 'global_catalog'
                }
            },
            'artifactId': 'someArtifactId.json',
            'artifact': {
                'someKey': 'someValue'
            }
        }

        self.defaultChildEntry = {
            'name': 'someChildName',
            'id': 'someChildId',
            'parent_id': self.defaultEntry['id'],
            'active': False,
            'kind': 'service',
            'disabled': False,
            'tags': ['a', 'b', 'c'],
            'overview_ui': {
                'en': {
                   'display_name': 'display',
                   'long_description': 'longDesc',
                   'description': 'desc'
               }
           },
           'images': {
             'image': 'image',
             'small_image': 'small',
             'medium_image': 'medium',
             'feature_image': 'feature'
            },
           'provider': {
             'email': 'bogus@us.ibm.com',
             'name': 'someName'
            }
        }

        self.updatedEntry = {
            'name': 'someNameUpdated',
            'id': 'someId',
            'active': False,
            'kind': 'template',
            'disabled': False,
            'tags': ['x', 'y', 'z'],                            # tags are case-sensitive
            'overview_ui': {
                'en': {
                   'display_name': 'displayUpdated',
                   'long_description': 'longDescUpdated',
                   'description': 'descUpdated'
               }
           },
           'images': {
             'image': 'imageUpdated',
             'small_image': 'smallUpdated',
             'medium_image': 'mediumUpdated',
             'feature_image': 'featureUpdated'
            },
           'provider': {
             'email': 'bogus@us.ibm.com',
             'name': 'someNameUpdated'
            }
        }

        self.service.delete_catalog_entry(id=self.defaultEntry['id'])

    @classmethod
    def tearDown(self):
        self.service.delete_catalog_entry(id=self.defaultEntry['id'])

    def test_create_catalog_entry(self):
        env = self.service.create_catalog_entry(id=self.defaultEntry['id'],
            name=self.defaultEntry['name'],
            overview_ui=self.defaultEntry['overview_ui'],
            kind=self.defaultEntry['kind'],
            images=self.defaultEntry['images'],
            disabled=self.defaultEntry['disabled'],
            tags=self.defaultEntry['tags'],
            provider=self.defaultEntry['provider'])
        assert env is not None
        assert env.get_status_code() == 201

        results = env.get_result()
        assert results.get('id') == self.defaultEntry['id']
        assert results.get('name') == self.defaultEntry['name']
        assert results.get('active') == self.defaultEntry['active']
        assert results.get('disabled') == self.defaultEntry['disabled']
        assert results.get('kind') == self.defaultEntry['kind']
        assert results.get('images') == self.defaultEntry['images']
        assert results.get('provider') == self.defaultEntry['provider']
        assert results.get('tags') == self.defaultEntry['tags']

    def test_get_catalog_entry(self):
        self.service.create_catalog_entry(id=self.defaultEntry['id'],
            name=self.defaultEntry['name'],
            overview_ui=self.defaultEntry['overview_ui'],
            kind=self.defaultEntry['kind'],
            images=self.defaultEntry['images'],
            disabled=self.defaultEntry['disabled'],
            tags=self.defaultEntry['tags'],
            provider=self.defaultEntry['provider'])

        env = self.service.get_catalog_entry(id=self.defaultEntry['id'])
        assert env is not None
        assert env.get_status_code() == 200

        results = env.get_result()
        assert results.get('id') == self.defaultEntry['id']
        assert results.get('name') == self.defaultEntry['name']
        assert results.get('active') == self.defaultEntry['active']
        assert results.get('disabled') == self.defaultEntry['disabled']
        assert results.get('kind') == self.defaultEntry['kind']
        assert results.get('images') == self.defaultEntry['images']
        assert results.get('provider') == self.defaultEntry['provider']
        assert results.get('tags') == self.defaultEntry['tags']

    def test_update_catalog_entry(self):
        self.service.create_catalog_entry(id=self.defaultEntry['id'],
            name=self.defaultEntry['name'],
            overview_ui=self.defaultEntry['overview_ui'],
            kind=self.defaultEntry['kind'],
            images=self.defaultEntry['images'],
            disabled=self.defaultEntry['disabled'],
            tags=self.defaultEntry['tags'],
            provider=self.defaultEntry['provider'])

        env = self.service.update_catalog_entry(id=self.updatedEntry['id'],
            name=self.updatedEntry['name'],
            overview_ui=self.updatedEntry['overview_ui'],
            kind=self.updatedEntry['kind'],
            images=self.updatedEntry['images'],
            disabled=self.updatedEntry['disabled'],
            tags=self.updatedEntry['tags'],
            provider=self.updatedEntry['provider'])
        assert env is not None
        assert env.get_status_code() == 200

        results = env.get_result()
        assert results.get('id') == self.updatedEntry['id']
        assert results.get('name') == self.updatedEntry['name']
        assert results.get('active') == self.updatedEntry['active']
        assert results.get('disabled') == self.updatedEntry['disabled']
        assert results.get('kind') == self.updatedEntry['kind']
        assert results.get('images') == self.updatedEntry['images']
        assert results.get('provider') == self.updatedEntry['provider']
        assert results.get('tags') == self.updatedEntry['tags']

    def test_delete_catalog_entry(self):
        self.service.create_catalog_entry(id=self.defaultEntry['id'],
            name=self.defaultEntry['name'],
            overview_ui=self.defaultEntry['overview_ui'],
            kind=self.defaultEntry['kind'],
            images=self.defaultEntry['images'],
            disabled=self.defaultEntry['disabled'],
            tags=self.defaultEntry['tags'],
            provider=self.defaultEntry['provider'])

        env = self.service.delete_catalog_entry(id=self.defaultEntry['id'])
        assert env is not None
        assert env.get_status_code() == 200

        results = env.get_result()
        assert results is not None

    def test_get_catalog_entry_after_delete_failure(self):
        self.service.create_catalog_entry(id=self.defaultEntry['id'],
            name=self.defaultEntry['name'],
            overview_ui=self.defaultEntry['overview_ui'],
            kind=self.defaultEntry['kind'],
            images=self.defaultEntry['images'],
            disabled=self.defaultEntry['disabled'],
            tags=self.defaultEntry['tags'],
            provider=self.defaultEntry['provider'])
        self.service.delete_catalog_entry(id=self.defaultEntry['id'])

        with pytest.raises(ApiException) as e:
            self.service.get_catalog_entry(id=self.defaultEntry['id'])
        assert e.value.code == 404

    def test_get_catalog_entry_failure(self):
        with pytest.raises(ApiException) as e:
            self.service.get_catalog_entry(id='bogus')
        assert e.value.code == 404

    def test_archive_catalog_entry_failure(self):
        env = self.service.delete_catalog_entry(id='bogus')
        assert env is not None
        assert env.get_status_code() == 200

        results = env.get_result()
        assert results is not None

    def test_update_catalog_entry_failure(self):
        with pytest.raises(ApiException) as e:
            self.service.update_catalog_entry(id='bogus',
                name=self.updatedEntry['name'],
                overview_ui=self.updatedEntry['overview_ui'],
                kind=self.updatedEntry['kind'],
                images=self.updatedEntry['images'],
                disabled=self.updatedEntry['disabled'],
                tags=self.updatedEntry['tags'],
                provider=self.updatedEntry['provider'])
        assert e.value.code == 404

    def test_create_catalog_entry_failure(self):
        self.service.create_catalog_entry(id=self.defaultEntry['id'],
            name=self.defaultEntry['name'],
            overview_ui=self.defaultEntry['overview_ui'],
            kind=self.defaultEntry['kind'],
            images=self.defaultEntry['images'],
            disabled=self.defaultEntry['disabled'],
            tags=self.defaultEntry['tags'],
            provider=self.defaultEntry['provider'])

        with pytest.raises(ApiException) as e:
            self.service.create_catalog_entry(id=self.defaultEntry['id'],
                name=self.defaultEntry['name'],
                overview_ui=self.defaultEntry['overview_ui'],
                kind=self.defaultEntry['kind'],
                images=self.defaultEntry['images'],
                disabled=self.defaultEntry['disabled'],
                tags=self.defaultEntry['tags'],
                provider=self.defaultEntry['provider'])
        assert e.value.code == 409

    def test_list_catalog_entries(self):
        env = self.service.list_catalog_entries(account=None)
        assert env is not None
        assert env.get_status_code() == 200

        results = env.get_result()
        assert results is not None

        resources = results.get('resources')
        assert resources is not None
        assert len(resources) > 0

    def test_get_child_catalog_entry(self):
        self.service.create_catalog_entry(id=self.defaultEntry['id'],
            name=self.defaultEntry['name'],
            overview_ui=self.defaultEntry['overview_ui'],
            kind=self.defaultEntry['kind'],
            images=self.defaultEntry['images'],
            disabled=self.defaultEntry['disabled'],
            tags=self.defaultEntry['tags'],
            provider=self.defaultEntry['provider'])
        self.service.create_catalog_entry(id=self.defaultChildEntry['id'],
            parent_id=self.defaultChildEntry['parent_id'],
            name=self.defaultChildEntry['name'],
            overview_ui=self.defaultChildEntry['overview_ui'],
            kind=self.defaultChildEntry['kind'],
            images=self.defaultChildEntry['images'],
            disabled=self.defaultChildEntry['disabled'],
            tags=self.defaultChildEntry['tags'],
            provider=self.defaultChildEntry['provider'])

        env = self.service.get_child_objects(id=self.defaultEntry['id'], kind=self.defaultEntry['kind'])
        assert env is not None
        assert env.get_status_code() == 200

        results = env.get_result()
        assert results.get('offset') == 0
        assert results.get('count') == 1
        assert results.get('resource_count') == 1

        resources = results.get('resources')
        assert resources is not None
        assert len(resources) == 1
        assert resources[0].get('id') == self.defaultChildEntry['id']
        assert resources[0].get('name') == self.defaultChildEntry['name']
        assert resources[0].get('active') == self.defaultChildEntry['active']
        assert resources[0].get('disabled') == self.defaultChildEntry['disabled']
        assert resources[0].get('kind') == self.defaultChildEntry['kind']
        assert resources[0].get('images') == self.defaultChildEntry['images']
        assert resources[0].get('provider') == self.defaultChildEntry['provider']
        assert resources[0].get('tags') == self.defaultChildEntry['tags']

    def test_get_child_catalog_entry_failure(self):
        with pytest.raises(ApiException) as e:
            self.service.get_child_objects(id='bogus', kind='bogus')
        assert e.value.code == 404

    def test_restore_catalog_entry(self):
        self.service.create_catalog_entry(id=self.defaultEntry['id'],
            name=self.defaultEntry['name'],
            overview_ui=self.defaultEntry['overview_ui'],
            kind=self.defaultEntry['kind'],
            images=self.defaultEntry['images'],
            disabled=self.defaultEntry['disabled'],
            tags=self.defaultEntry['tags'],
            provider=self.defaultEntry['provider'])
        self.service.delete_catalog_entry(id=self.defaultEntry['id'])

        env = self.service.restore_catalog_entry(self.defaultEntry['id'])
        assert env is not None
        assert env.get_status_code() == 200

        env = self.service.get_catalog_entry(id=self.defaultEntry['id'])
        assert env is not None
        assert env.get_status_code() == 200

        results = env.get_result()
        assert results is not None
        assert results.get('id') == self.defaultEntry['id']
        assert results.get('name') == self.defaultEntry['name']
        assert results.get('active') == self.defaultEntry['active']
        assert results.get('disabled') == self.defaultEntry['disabled']
        assert results.get('kind') == self.defaultEntry['kind']
        assert results.get('images') == self.defaultEntry['images']
        assert results.get('provider') == self.defaultEntry['provider']
        assert results.get('tags') == self.defaultEntry['tags']

    def test_restore_catalog_entry_failure(self):
        with pytest.raises(ApiException) as e:
            self.service.restore_catalog_entry('bogus')
        assert e.value.code == 404

    def test_get_visibility(self):
        self.service.create_catalog_entry(id=self.defaultEntry['id'],
            name=self.defaultEntry['name'],
            overview_ui=self.defaultEntry['overview_ui'],
            kind=self.defaultEntry['kind'],
            images=self.defaultEntry['images'],
            disabled=self.defaultEntry['disabled'],
            tags=self.defaultEntry['tags'],
            provider=self.defaultEntry['provider'])

        env = self.service.get_visibility(self.defaultEntry['id'])
        assert env is not None
        assert env.get_status_code() == 200

        results = env.get_result()
        assert results is not None
        assert results.get('restrictions') == self.defaultEntry['restrictions']

    def test_get_visibility_failure(self):
        with pytest.raises(ApiException) as e:
            self.service.get_visibility('bogus')
        assert e.value.code == 404

    def test_update_visibility(self):
        self.service.create_catalog_entry(id=self.defaultEntry['id'],
            name=self.defaultEntry['name'],
            overview_ui=self.defaultEntry['overview_ui'],
            kind=self.defaultEntry['kind'],
            images=self.defaultEntry['images'],
            disabled=self.defaultEntry['disabled'],
            tags=self.defaultEntry['tags'],
            provider=self.defaultEntry['provider'])

        with pytest.raises(ApiException) as e:
            self.service.update_visibility(id=self.defaultEntry['id'])
        assert e.value.code == 403

    def test_update_visibility_failure(self):
        with pytest.raises(ApiException) as e:
            self.service.update_visibility('bogus')
        assert e.value.code == 404

    def test_get_pricing(self):
        env = self.service.create_catalog_entry(id=self.defaultEntry['id'],
            name=self.defaultEntry['name'],
            overview_ui=self.defaultEntry['overview_ui'],
            kind=self.defaultEntry['kind'],
            images=self.defaultEntry['images'],
            disabled=self.defaultEntry['disabled'],
            tags=self.defaultEntry['tags'],
            provider=self.defaultEntry['provider'],
            metadata=self.defaultEntry['metadata'])

        env = self.service.get_visibility(self.defaultEntry['id'])
        assert env is not None
        assert env.get_status_code() == 200

        results = env.get_result()
        assert results is not None
        assert results.get('restrictions') == self.defaultEntry['restrictions']

    def test_get_pricing_failure(self):
        self.service.create_catalog_entry(id=self.defaultEntry['id'],
            name=self.defaultEntry['name'],
            overview_ui=self.defaultEntry['overview_ui'],
            kind=self.defaultEntry['kind'],
            images=self.defaultEntry['images'],
            disabled=self.defaultEntry['disabled'],
            tags=self.defaultEntry['tags'],
            provider=self.defaultEntry['provider'])

        
        with pytest.raises(ApiException) as e:
            self.service.get_pricing(self.defaultEntry['id'])
        assert e.value.code == 404
        
        with pytest.raises(ApiException) as e:
            self.service.get_pricing('bogus')
        assert e.value.code == 404

    def test_list_artifacts(self):
        self.service.create_catalog_entry(id=self.defaultEntry['id'],
          name=self.defaultEntry['name'],
          overview_ui=self.defaultEntry['overview_ui'],
          kind=self.defaultEntry['kind'],
          images=self.defaultEntry['images'],
          disabled=self.defaultEntry['disabled'],
          tags=self.defaultEntry['tags'],
          provider=self.defaultEntry['provider'])
        self.service.upload_artifact(object_id=self.defaultEntry['id'],
         artifact_id=self.defaultEntry['artifactId'],
         artifact=self.defaultEntry['artifact'])

        env = self.service.list_artifacts(object_id=self.defaultEntry['id'],
          artifact_id=self.defaultEntry['artifactId'])
        assert env is not None
        assert env.get_status_code() == 200

        results = env.get_result()
        assert results is not None
        assert results.get('count') == 1

        resources = results.get('resources')
        assert resources is not None
        assert len(resources) == 1
        assert resources[0].get('name') == self.defaultEntry['artifactId']
        assert resources[0].get('url') == '{}/{}/artifacts/{}'.format(self.service.service_url,
          self.defaultEntry['id'],
          self.defaultEntry['artifactId'])
        assert resources[0].get('size') == 24

    def test_list_artifacts_failure(self):
        env = self.service.list_artifacts('bogus')
        assert env is not None
        assert env.get_status_code() == 200

        results = env.get_result()
        assert results is not None
        assert results.get('count') == 0

    def test_get_artifact(self):
        self.service.create_catalog_entry(id=self.defaultEntry['id'],
          name=self.defaultEntry['name'],
          overview_ui=self.defaultEntry['overview_ui'],
          kind=self.defaultEntry['kind'],
          images=self.defaultEntry['images'],
          disabled=self.defaultEntry['disabled'],
          tags=self.defaultEntry['tags'],
          provider=self.defaultEntry['provider'])
        self.service.upload_artifact(object_id=self.defaultEntry['id'],
         artifact_id=self.defaultEntry['artifactId'],
         artifact=self.defaultEntry['artifact'])

        env = self.service.get_artifact(object_id=self.defaultEntry['id'], artifact_id=self.defaultEntry['artifactId'])
        assert env is not None
        assert env.get_status_code() == 200

        results = env.get_result()
        assert results is not None
        assert results == self.defaultEntry['artifact']

    def test_get_artifact_failure(self):
        self.service.create_catalog_entry(id=self.defaultEntry['id'],
          name=self.defaultEntry['name'],
          overview_ui=self.defaultEntry['overview_ui'],
          kind=self.defaultEntry['kind'],
          images=self.defaultEntry['images'],
          disabled=self.defaultEntry['disabled'],
          tags=self.defaultEntry['tags'],
          provider=self.defaultEntry['provider'])

        with pytest.raises(ApiException) as e:
            self.service.get_artifact(object_id=self.defaultEntry['id'], artifact_id='bogus')
        assert e.value.code == 404

        with pytest.raises(ApiException) as e:
            self.service.get_artifact('bogus', 'bogus')
        assert e.value.code == 404

    def test_upload_artifact(self):
        self.service.create_catalog_entry(id=self.defaultEntry['id'],
          name=self.defaultEntry['name'],
          overview_ui=self.defaultEntry['overview_ui'],
          kind=self.defaultEntry['kind'],
          images=self.defaultEntry['images'],
          disabled=self.defaultEntry['disabled'],
          tags=self.defaultEntry['tags'],
          provider=self.defaultEntry['provider'])

        env = self.service.upload_artifact(object_id=self.defaultEntry['id'],
            artifact_id=self.defaultEntry['artifactId'],
            artifact=self.defaultEntry['artifact'])
        assert env is not None
        assert env.get_status_code() == 200

        results = env.get_result()
        assert results is not None

    def test_upload_artifact_failure(self):
        with pytest.raises(ApiException) as e:
            self.service.upload_artifact('bogus', 'bogus')
        assert e.value.code == 404

    def test_delete_artifact(self):
        self.service.create_catalog_entry(id=self.defaultEntry['id'],
          name=self.defaultEntry['name'],
          overview_ui=self.defaultEntry['overview_ui'],
          kind=self.defaultEntry['kind'],
          images=self.defaultEntry['images'],
          disabled=self.defaultEntry['disabled'],
          tags=self.defaultEntry['tags'],
          provider=self.defaultEntry['provider'])

        env = self.service.delete_artifact(object_id=self.defaultEntry['id'], artifact_id='bogus')
        assert env is not None
        assert env.get_status_code() == 200

        results = env.get_result()
        assert results is not None

    def test_delete_artifact_failure(self):
        self.service.create_catalog_entry(id=self.defaultEntry['id'],
          name=self.defaultEntry['name'],
          overview_ui=self.defaultEntry['overview_ui'],
          kind=self.defaultEntry['kind'],
          images=self.defaultEntry['images'],
          disabled=self.defaultEntry['disabled'],
          tags=self.defaultEntry['tags'],
          provider=self.defaultEntry['provider'])

        env = self.service.delete_artifact(object_id=self.defaultEntry['id'], artifact_id='bogus')
        assert env is not None
        assert env.get_status_code() == 200

        results = env.get_result()
        assert results is not None

        with pytest.raises(ApiException) as e:
            self.service.delete_artifact('bogus', 'bogus')
        assert e.value.code == 404

if __name__ == '__main__':
    unittest.main()
