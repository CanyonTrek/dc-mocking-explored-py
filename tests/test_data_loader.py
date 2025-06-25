import unittest
from app.text_file_source import TextFileSource
from app.data_loader import DataLoader

class DataLoaderTest(unittest.TestCase):
    def test_count_chars_in_data_source_no_mocking(self):
        # arrange
        tfl = TextFileSource()
        fname = "data.txt" #"C:/tmp/KeyboardHandler.txt"
        dl = DataLoader(tfl)
        expected = 11 #1383

        # act
        result = dl.load_data(fname)

        # assert
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

