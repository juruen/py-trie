#! /usr/bin/env python
# Copyright (c) 2011 Javier Uruen (juruen@warp.es)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import unittest
import trie


class TestTrie(unittest.TestCase):
    """Test unit for trie class"""

    TEST_VALUES = {"A": 15, "to": 7, "tea": 3, "ted": 4,
        "ten": 12, "i": 11, "in": 5,  "inn": 9}

    def setUp(self):
        """Populate trie with TEST_VALUES"""
        self.trie = trie.Trie(self.TEST_VALUES)

    def test_lookup(self):
        """Test we can lookup existing keys. Also test nonexistent keys will
           throw proper exception"""
        for i in self.TEST_VALUES:
            self.trie.assertEqual(self.TEST_VALUES[i], self.trie.lookup(i))
        self.asserRaises(self.trie.KeyNotFound, self.trie.lookup("foobar"))
