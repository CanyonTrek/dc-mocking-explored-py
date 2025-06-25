import logging

def main():
    file_name = "C:\\tmp\\KeyboardHandler.txt"

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                # process the line
                print(line.strip())
    except IOError as ex:
        logging.error("File reading error: %s", ex)


if __name__ == "__main__":
    main()
