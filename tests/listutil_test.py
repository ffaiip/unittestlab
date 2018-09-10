import unittest

from listutil import count_unique, binary_search


class test_unique(unittest.TestCase):
    """Tests of the count_unique function."""

    def test_none(self):
        list = [None]
        self.assertRaises(TypeError, count_unique(list))

    def test_empty(self):
        list = [ ]
        self.assertEqual(0, count_unique(list))

    def test_multiple_unique(self):
        list = ['a', 'b', 'b', 'b', 'a', 'c', 'c']
        self.assertEqual(3, count_unique(list))

    def test_one_unique(self):
        list = ['a', 'a', 'a', 'a']
        self.assertEqual(1, count_unique(list))

    def test_add_none(self):
        list = ['a', 'a', 'a', 'a', None]
        self.assertEqual(2, count_unique(list))


class test_binary_seach(unittest.TestCase):
    """Tests of the binary_search function."""

    def test_none(self):
        list, element = [None], None
        self.assertRaises(TypeError, binary_search(list, element))

    def test_empty(self):
        list, element = [' ', 'e', 'f', 'u', 'l', 't'], ' '
        self.assertEqual(0, binary_search(list, element))

    def test_character(self):
        list, element = ['d', 'e', 'f', 'u', 'l', 't'], 'f'
        self.assertEqual(2, binary_search(list, element))

    def test_out_of_list(self):
        list, element = ['d', 'e', 'f', 'u', 'l', 't'], 'a'
        self.assertEqual(-1, binary_search(list, element))

    def test_number(self):
        list, element = [7, 3, 8, 1, 5], 3
        self.assertEqual(1, binary_search(list, element))
