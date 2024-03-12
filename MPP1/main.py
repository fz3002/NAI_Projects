import csv

def read_file(file_name):
    list = []
    with open(file_name, newline='') as f:
        lines = csv.reader(f, delimiter=";")
        for row in lines:
            list.append(row)
    f.close()
    return list

k = int(input("Podaj k: "))
train_list = read_file("train_set.csv")
test_list = read_file("test_set.csv")