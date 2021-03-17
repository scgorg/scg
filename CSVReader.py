import csv


class CSVReader:

    def __init__(self, csv_filename):
        self.filename = csv_filename

    def get_rows(self):
        with open(self.filename, newline='') as csv_file:
            rows = csv.reader(csv_file)

            for row in rows:
                # yield for name and gmail
                yield row[0], row[1]

# Usage

# reviewer_list = CSVReader("some_email_list.csv")
#
# for name, mail in reviewer_list.get_rows():
#     print(name, mail)
