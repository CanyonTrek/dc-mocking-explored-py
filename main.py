from app.text_file_loader import TextFileLoader

def main():
    tfl = TextFileLoader()

    # Define a lambda-like function to append the line to the list
    line_collector = lambda collection, line: collection.append(line)

    # Load the file with the processing function
    lines = tfl.load_file("C:/tmp/KeyboardHandler.txt", line_collector)

    # Print the lines with a prefix
    for element in lines:
        print(f">> {element}")

if __name__ == "__main__":
    main()

