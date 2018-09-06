import unittest

from listutil import count_unique

"""
Tests of the count_unique methods.
"""

class test_unique(unittest.TestCase):

    def test_null(self):
        list = [ ]
        self.assertEquals(0, count_unique(list))

    def test_multiple_unique(self):
        list = ['a', 'b', 'b', 'b', 'a', 'c', 'c']
        self.assertEquals(3, count_unique(list))

    def test_one_unique(self):
        list = ['a', 'a', 'a', 'a']
        self.assertEquals(1, count_unique(list))