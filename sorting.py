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

#Selection Sort
def selection_sort(cisla, direction):
    #první for cyklus si pamatuje indexy čísel
    for i in range (len(cisla)):
        min_index = i
        if direction == True:
            for j in range(min_index+1, len(cisla)):
                if cisla[j]< cisla[min_index]:
                    min_index = j
        elif direction == False:
            for j in range(min_index+1, len(cisla)):
                if cisla[j]> cisla[min_index]:
                    min_index = j
        # prohození čísel
        cisla[i], cisla[min_index] = cisla[min_index], cisla[i]
    return cisla

# Bubble Sort
def bubble_sort(cisla):
    for i in range(len(cisla)):
        for j in range(0, len(cisla)-i-1):
            if cisla[j] > cisla [j+1]:
                cisla[j], cisla[j+1] = cisla[j+1], cisla[j]
    return cisla


def main():
    data = read_data("numbers.csv")
    print(data)
    sort_s = selection_sort(data["series_1"], False)
    print (sort_s)
    sort_b = bubble_sort(data["series_2"])
    print (sort_b)



if __name__ == '__main__':
    main()
