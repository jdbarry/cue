# Copyright 2013 Red Hat, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from cue.tests import api


class TestRootController(api.FunctionalTest):

    def test_get_root(self):
        """test case for get in root controller."""
        data = self.get_json('/')
        self.assertEqual('v1', data['default_version']['id'])
        self.assertEqual('STABLE', data['default_version']['status'])
        # Check fields are not empty
        [self.assertNotIn(f, ['', []]) for f in data.keys()]