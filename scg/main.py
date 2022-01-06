from prettytable import PrettyTable

from scg.csvreader import CSVReader


def show_csv_content(csv):
    # Row count
    table = PrettyTable()

    csv_file = CSVReader.CSVReader(csv)
    print(f"CSV Rows Count: {csv_file.get_count()}\n")
    table.field_names = csv_file.get_row_dict_keys()

    for item in csv_file.get_rows_dict():
        temp_list = []
        for index in range(0, csv_file.get_count()):
            temp_list.append(item[table.field_names[index]])
        table.add_row(temp_list)
        temp_list.clear()

    print(table)


def main(csv_file):
    show_csv_content(csv_file)


if __name__ == "__main__":
    main()
