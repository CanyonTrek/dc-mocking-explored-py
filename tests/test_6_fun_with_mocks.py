import unittest
from unittest.mock import MagicMock

class TestFunWithMocks(unittest.TestCase):
    def test_fun_with_mocks(self):
        """
        Demonstrates the behavior of mock objects:
        - If a method has not been configured with a return value, a default is returned.
        - In this case, we configure `size()` but not `is_empty()`.
        """
        # Arrange
        m_ints = MagicMock()
        m_ints.size.return_value = 4  # Explicitly stub `size()`

        # Act
        result = m_ints.is_empty()  # Not stubbed: returns a new MagicMock

        # Assert
        # Since result is a MagicMock instance, `assertTrue(result)` will fail.
        # We must explicitly define expected behavior for meaningful assertions.
        self.assertTrue(result, "The collection is empty")

        # To illustrate how mocking typically works in Python,
        # you might normally write:
        # m_ints.is_empty.return_value = True
        # and then assertTrue(m_ints.is_empty())


if __name__ == '__main__':
    unittest.main()
