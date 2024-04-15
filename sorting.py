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

def selection_sort(cisla):
    for i in range (len(cisla)):
        min_index = i
        for j in range(i+1, len(cisla)):
            if cisla [j]< cisla[min_index]:
                min_index = j
        #prohození čísel
        cisla[i], cisla[min_index] = cisla[min_index], cisla [i]
    return cisla


def main():
    data = read_data("numbers.csv")
    print(data)
    sort = selection_sort(data["series_1"])
    print (sort)


if __name__ == '__main__':
    main()
