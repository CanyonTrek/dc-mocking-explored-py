import logging

class TextFileLoader:
    def load_file(self, fname):
        """Loads a text file and returns a list of lines (stripped of newline characters)."""
        lines = []

        try:
            with open(fname, 'r', encoding='utf-8') as file:
                for line in file:
                    lines.append(line.strip())
        except IOError as ex:
            logging.error("Error reading file %s: %s", fname, ex)

        return lines

