import logging

def main():
    logging.basicConfig(level=logging.ERROR)
    file_name = "C:\\tmp\\KeyboardHandler.java.txt"

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                print(line.strip())
    except IOError as err:
        logging.error("File reading error: %s", err)

if __name__ == "__main__":
    main()

