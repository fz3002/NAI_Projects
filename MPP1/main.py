import csv

def read_file(file_name):
    list = []
    with open(file_name, newline='') as f:
        lines = csv.reader(f, delimiter=";")
        for row in lines:
            list.append(row)
    f.close()
    return list

def knn(k, vector, space):
    closest = []
    for v in space:
        closest.sort()
        sum = 0;
        for i in range(len(vector)-1):
            sum += (vector[i] - v[i])**2
        if(closest.length < k):
            closest.append((sum, v[v.length-1]))
        else:
            if(closest[closest.length-1][0] > sum):
                closest[closest.length-1] = (sum, v[v.length-1])
                  
k = int(input("Podaj k: "))
train_list = read_file("train_set.csv")
test_list = read_file("test_set.csv")