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

class Trie():
    """This class implements a data structure known as trie or prefix tree"""
    def __init__(self, data=None):
        pass

    def lookup(self, key):
        """Search key in trie and return its value if it is found. Otherwise
            throw KeyNotFound exception"""
        pass

class KeyNotFound(Exception):
    """Key not found in trie"""
    def __init__(self, key):
        self.key = key
    def __str__(self):
        return "key %s not found in trie" % (self.key)
