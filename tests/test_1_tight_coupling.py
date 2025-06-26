"""
This test demonstrates the problem of tight coupling.

Class A directly creates an instance of class B and calls its method.
This makes it impossible to substitute B during testing, and any change
in B or its dependencies (e.g., file access) could cause this test to fail.

This is typical of tightly coupled code that is hard to test or isolate.
"""

import unittest

class B:
    def do_something(self, x, y):
        return x + y

class A:
    def __init__(self):
        self.b = B()

    def do_something(self, x, y, z):
        return self.b.do_something(x, y) + z

class TestTightCoupling(unittest.TestCase):
    def test_whats_the_problem_we_are_trying_to_solve(self):
        # arrange
        # A creates its own instance of B, tightly coupling the code.
        # If B accessed a file that was missing, the test could fail.
        cut = A()
        x = 3
        y = 6
        z = 9
        expected = 18

        # act
        result = cut.do_something(x, y, z)

        # assert
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

