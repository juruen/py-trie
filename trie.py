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

import pickle


class TrieNode():
    """Node of a trie"""
    def __init__(self, letter, color, value=None):
        self.letter = letter
        self.value = value
        # White nodes contain the end of a string. Conversely,
        # black nodes contain inner characters of a string.
        self.color = color
        self.children = {}

    def to_str(self):
        str = "letter: %s value %s color %s children %s " % (self.letter,
                self.value, self.color, self.children.keys())
        return str

    def child_num(self):
        return len(self.children.keys())


class Trie():
    """This class implements a data structure known as trie or prefix tree"""

    def __init__(self, data=None):
        self.root = TrieNode("", "black")
        if data:
            for i in data:
                self.insert(i, data[i])

    def insert(self, key, value):
        node = self.root
        for index, l in enumerate(key):
            if index == len(key) - 1:
                col = "white"
                val = value
            else:
                col = "black"
                val = None
            if l in node.children:
                node = node.children[l]
                if col == "white":
                    node.color = col
                    node.value = val
            else:
                node.children[l] = TrieNode(letter=l, color=col, value=val)
                node = node.children[l]

    def lookup(self, key):
        """Search key in trie and return its value if it is found. Otherwise
            throw KeyNotFound exception"""
        node = self.root
        for index, l in enumerate(key):
            if l in node.children:
                node = node.children[l]
            else:
                raise KeyNotFound(key)
            if (index == (len(key) - 1) and node.color == "white"):
                return node.value
        raise KeyNotFound(key)

    def delete(self, key):
        """Delete a given key from trie"""
        self.__delete(self.root, key)

    def save(self, path):
        """Dump trie to path"""
        pickle.dump(self.root, open(path, "wb"))

    def load(self, path):
        self.root = pickle.load(open(path))

    def __delete(self, node, key, index=0):
        """Delete a given key. Recursive approach"""
        if index != len(key):
            if key[index] not in node.children:
                raise KeyNotFound(key)
            if self.__delete(node.children[key[index]], key, index + 1):
                del(node.children[key[index]])
                return node.color == "black" and node.child_num() == 0
            else:
                return False
        else:
            if node.color == "black":
                raise KeyNotFound(key)
            else:
                node.color = "black"
            return node.child_num() == 0


class KeyNotFound(Exception):
    """Key not found in trie"""
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return "key '%s' not found in trie" % (self.key)
