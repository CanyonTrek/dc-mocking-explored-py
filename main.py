from app.text_file_loader import TextFileLoader

def main():
    tfl = TextFileLoader()
    lines = tfl.load_file("C:/tmp/KeyboardHandler.java.txt")

    for line in lines:
        print(line)

if __name__ == "__main__":
    main()

