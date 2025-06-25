class DataLoader:
    """
    DataLoader is responsible for loading data via a provided data source (e.g., a file)
    and calculating the total number of characters across all lines.

    It delegates line-collection logic to the data source and processes the final result.
    """

    def __init__(self, data_source):
        self.data_source = data_source

    def load_data(self, fname):
        # Define the lambda to append lines (similar to Java's functor)
        functor = lambda col, line: col + [line]

        data = self.data_source.load_data(fname, functor)
        count = sum(len(line) for line in data)

        return count

