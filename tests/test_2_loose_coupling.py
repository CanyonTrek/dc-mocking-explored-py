"""
This test shows how to loosen coupling using dependency injection.

Class A accepts an instance of B through its constructor rather than 
creating it internally. This allows A to work with any compatible object, 
making it easier to test or replace B with a mock if needed.

This approach improves modularity and testability.
"""

import unittest

class B:
    def do_something(self, x, y):
        return x + y

class A:
    def __init__(self, b):
        self.b = b

    def do_something(self, x, y, z):
        return self.b.do_something(x, y) + z

class TestLooseCoupling(unittest.TestCase):
    def test_loosely_coupled(self):
        # arrange
        b = B()
        cut = A(b)
        x, y, z = 3, 6, 9
        expected = 18

        # act
        result = cut.do_something(x, y, z)

        # assert
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

