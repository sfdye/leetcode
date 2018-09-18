
import unittest
import importlib


class TestCases(unittest.TestCase):
    def setUp(self):
        self.s = importlib.import_module("..two-sum").Solution()

    def test_two_nums(self):
        self.assertEqual(self.s.twoSum([1, 2], 3), [0, 1])

    def test_three_nums(self):
        self.assertEqual(self.s.twoSum([1, 2, 3], 5), [1, 2])
