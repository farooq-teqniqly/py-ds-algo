from unittest import TestCase
from binarysearch import binary_search


class BinarySearchTests(TestCase):
    def setUp(self):
        self.lst = [1, 2, 3, 4, 5]

    def test_binary_search(self):
        result = binary_search(self.lst, 4)
        self.assertEqual(3, result)

        result = binary_search(self.lst, 1)
        self.assertEqual(0, result)

    def test_binary_search_not_found(self):
        with self.assertRaises(ValueError):
            binary_search(self.lst, 6)

        with self.assertRaises(ValueError):
            binary_search(self.lst, 0)
