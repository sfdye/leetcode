import importlib
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.s = importlib.import_module("..transpose-matrix").Solution()

    def test_two_by_two(self):
        self.assertEqual(self.s.transpose([[1, 2], [3, 4]]), [(1, 3), (2, 4)])

