import logging

def load_file():
    file_name = "C:\\tmp\\KeyboardHandler.txt"
    lines = []

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                lines.append(line.strip())
    except IOError as ex:
        logging.error("File reading error: %s", ex)

    return lines

def main():
    lines = load_file()

    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
