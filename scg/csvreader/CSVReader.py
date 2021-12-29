import csv


class CSVReader:
    def __init__(self, csv_filename):
        self.filename = csv_filename

    def get_count(self):
        """
        Return the total number of CSV rows through the given CSV file
        :return: int
        """
        count = 0
        with open(self.filename, newline="") as csv_file:
            rows = csv.reader(csv_file)
            for row in rows:
                # the type of row is a list
                count = len(row)
                break
        return count

    def get_rows_list(self):
        """
        Return CSV data, the type is list
        :return:
        """
        with open(self.filename, newline="") as csv_file:
            rows = csv.reader(csv_file)
            for row in rows:
                yield row

    def get_rows_dict(self):
        """
        Return CSV data, the type is Dict
        :return:
        """
        with open(self.filename, newline="") as csv_file:
            rows = csv.DictReader(csv_file)
            for row in rows:
                yield row


# Usage


if __name__ == "__main__":
    reviewer_list = CSVReader("../../tests/list.csv")

    print(reviewer_list.get_count())
    for item in reviewer_list.get_rows_list():
        print(item)
    for item in reviewer_list.get_rows_dict():
        print(item)
