from app.text_file_source import TextFileSource
from app.basic_data_processor import BasicDataProcessor

def main():
    # Create the data source
    tfl = TextFileSource()

    # Set the filename
    fname = "data.txt" # "C:\\tmp\\KeyboardHandler.java.txt"

    # Define a lambda-like function to append the line to the list
    line_collector = lambda collection, line: collection + [line] 

    # Load data using the lambda functor
    lines = tfl.load_data(fname, line_collector)

    # Print each line prefixed with >>
    for element in lines:
        print(f">> {element}")

    # Process data using BasicDataProcessor
    processor = BasicDataProcessor(tfl)
    no_of_chars = processor.load_data(fname)

    print(f"No of characters in the file are: {no_of_chars}")



if __name__ == "__main__":
    main()

