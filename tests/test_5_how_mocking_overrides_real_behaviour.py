"""
Demonstration of how mocking overrides real behavior.

This does not reflect actual list behavior, but shows how mocks can be configured
to return fixed values regardless of real method logic.
"""

import unittest
from unittest.mock import MagicMock

class TestMockingList(unittest.TestCase):
    def test_how_mocking_overrides_real_behavior(self):
        # Standard list
        ints = []
        ints.append(1)
        ints.append(2)
        ints.append(3)
        self.assertEqual(len(ints), 3, "This should work")

        # Mocked list using MagicMock to support special methods like __len__
        mocked_ints = MagicMock()
        mocked_ints.__len__.return_value = 4

        # len(mocked_ints) will always return 4
        self.assertEqual(len(mocked_ints), 4, "This is mocked - len is faked")

        # Even after 'adding', len doesn't change
        mocked_ints.append(3)
        mocked_ints.append(7)
        self.assertNotEqual(len(mocked_ints), 2, "This is still mocked")

if __name__ == '__main__':
    unittest.main()

