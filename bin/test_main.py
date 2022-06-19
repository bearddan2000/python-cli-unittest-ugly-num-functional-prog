import unittest

import main

class TestMain(unittest.TestCase):
    """docstring for TestMain."""
    def test_max_divide(self):
        self.assertEqual(main.max_divide(10, 5), 2)

    def test_is_ugly(self):
        self.assertTrue(main.is_ugly(0, [2,3,5], 12))

    def test_find_ugly(self):
        self.assertEqual(main.find_ugly(10, 1, 1, [2,3,5]), 12)
