"""
Demonstrates loose coupling using duck typing instead of explicit interfaces.

Any object that provides a `do_something(x, y)` method can be used.
This mirrors Java's use of an interface (IB), but in a more natural Pythonic way.
"""

import unittest

class B:
    def do_something(self, x, y):
        return x + y

class X:
    def do_something(self, x, y):
        return x * 1 + y * 1

class A:
    def __init__(self, b_like):
        self.b = b_like

    def do_something(self, x, y, z):
        return self.b.do_something(x, y) + z

class TestInterfaceLike(unittest.TestCase):
    def test_loosely_coupled_with_duck_typing(self):
        # arrange
        child = X()  # could be B(), X(), or a mock
        cut = A(child)
        x, y, z = 3, 6, 9
        expected = 18

        # act
        result = cut.do_something(x, y, z)

        # assert
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

