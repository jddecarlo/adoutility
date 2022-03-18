"""The test_dummy module contains unit tests for the adoutility.dummy module."""

# ---------------- TESTS ----------------
import unittest

from adoutility.dummy import *


class TestDummy(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(add_one(5), 6)
        self.assertNotEqual(add_one(1), 1)


if __name__ == "__main__":
    unittest.main()
