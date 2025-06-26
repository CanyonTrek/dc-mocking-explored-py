"""
Demonstrates using mocking to isolate dependencies during testing.

In this example, class A depends on a collaborator (b) with a `do_something(x, y)` method.
We inject a mock instead of a real implementation to isolate the test logic.
"""

import unittest
from unittest.mock import Mock

class A:
    def __init__(self, b_like):
        self.b = b_like

    def do_something(self, x, y, z):
        return self.b.do_something(x, y) + z

class TestMocking(unittest.TestCase):
    def test_introducing_mocking_to_replace_dependency(self):
        # arrange
        mock_b = Mock()
        cut = A(mock_b)
        x, y, z = 3, 6, 9
        expected = 18

        # setup the mock expectation
        mock_b.do_something.return_value = 9

        # act
        result = cut.do_something(x, y, z)

        # assert
        self.assertEqual(expected, result)
        mock_b.do_something.assert_called_once_with(3, 6)

if __name__ == '__main__':
    unittest.main()

