import logging

class TextFileSource:
    """
    A data source class that loads data from a text file and allows external logic
    to process each line using a provided function.

    This abstracts away the file reading mechanism and decouples it from how
    the data is processed.
    """

    def load_data(self, fname, line_processor):
        """
        Loads lines from the given file and applies the line_processor to each line.

        Parameters:
        - fname: Path to the file to be read.
        - line_processor: A function that accepts (list, line) to process each line.

        Returns:
        - A list of processed lines.
        """
        lines = []
        try:
            with open(fname, "r", encoding="utf-8") as file:
                for line in file:
                    lines = line_processor(lines, line.strip())
        except IOError as ex:
            logging.error("Error reading file %s: %s", fname, ex)
        return lines

