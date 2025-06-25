from app.text_file_source import TextFileSource
from app.data_loader import DataLoader

def main():
    # Create a TextFileSource instance
    tfl = TextFileSource()

    # Set file name
    fname = "data.txt" # "C:\\tmp\\KeyboardHandler.txt"

    # Define a lambda-like function to append the line to the list
    line_collector = lambda collection, line: collection + [line] 

    # Load data using the source and line processor
    lines = tfl.load_data(fname, line_collector)

    # Print each line
    for element in lines:
        print(f">> {element}")

    # Use the DataLoader to count characters
    dl = DataLoader(tfl)
    no_of_chars = dl.load_data(fname)

    print(f"No of characters in the file are: {no_of_chars}")

if __name__ == "__main__":
    main()

