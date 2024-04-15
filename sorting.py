import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """

    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open (file_path, "r") as f:
        reader = csv.DictReader(f)
        dict = {}
        for row in reader:
            for header, value in row.items():
                if header not in dict:
                    dict[header] = [int(value)]
                else:
                    dict [header].append(int(value))
    return dict



def main():
    data = read_data("numbers.csv")
    print(data)


if __name__ == '__main__':
    main()
