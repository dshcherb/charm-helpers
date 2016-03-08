# Copyright 2016 Canonical Limited.
#
# This file is part of charm-helpers.
#
# charm-helpers is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3 as
# published by the Free Software Foundation.
#
# charm-helpers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with charm-helpers.  If not, see <http://www.gnu.org/licenses/>.
import os
import glob
import yaml

from unittest import TestCase

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'defaults')


class DefaultsTestCase(TestCase):

    def setUp(self):
        super(DefaultsTestCase, self).setUp()

    def test_defaults(self):
        defaults_paths = glob.glob('%s/*.yaml' % TEMPLATES_DIR)
        for defaults in defaults_paths:
            schema = "%s.schema" % defaults
            self.assertTrue(os.path.exists(schema))
            a = yaml.safe_load(open(schema))
            b = yaml.safe_load(open(defaults))
            if not a and not b:
                continue

            # Test that all keys in default are present in their associated
            # schema.
            b.update(a)
            self.assertEqual(b, a)
