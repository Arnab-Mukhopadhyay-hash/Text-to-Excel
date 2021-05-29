import os
import csv
import pandas


def txt_to_dict(key_lists):
    complete_data = []
    for file in os.listdir():
        if file.endswith("txt"):
            with open(file) as txt_file:
                file_dict = {}
                for key, line_value in zip(key_lists, txt_file):
                    file_dict[key] = line_value.strip("\n")
                complete_data.append(file_dict)
    return complete_data


def dict_to_csv(csv_filename, header_list, complete_data):
    with open(csv_filename, 'w', newline='') as file:
        csv_file = csv.DictWriter(file, fieldnames=header_list)
        csv_file.writeheader()
        csv_file.writerows(complete_data)


def csv_to_excel(csv_filename, excel_filename):
    csv_file = pandas.read_csv(csv_filename)
    excel_file = pandas.ExcelWriter(excel_filename)
    csv_file.to_excel(excel_filename, index=False)
    excel_file.save()


if __name__ == '__main__':
    key_list = ["name", "phone", "address"]
    data = txt_to_dict(key_list)
    print(data)
    dict_to_csv("Capstone.csv", key_list, data)
    csv_to_excel('Capstone.csv', 'Capstone.xlsx')
