import unittest
from app.text_file_source import TextFileSource

class TestTextFileSource(unittest.TestCase):
    def test_how_to_use_load_data_method_with_single_param(self):
        """
        Demonstrates usage of TextFileSource.load_data() with a single filename parameter.
        """
        tfl = TextFileSource()
        fname = "data.txt" # "C:\\tmp\\KeyboardHandler.java.txt"
        lines = tfl.load_data(fname)

        for element in lines:
            print(f">> {element}")

    def test_how_to_use_load_data_method_with_3_params(self):
        """
        Demonstrates usage of TextFileSource.load_data() with a filename, collection, 
        and line processor function.
        """
        tfl = TextFileSource()
        fname = "data.txt" # "C:\\tmp\\KeyboardHandler.java.txt"
        data = []

        # Define lambda equivalent for line processor
        line_processor = lambda col, line: col + [line]

        lines = tfl.load_data(fname, data, line_processor)

        for element in lines:
            print(f">> {element}")


if __name__ == "__main__":
    unittest.main()

