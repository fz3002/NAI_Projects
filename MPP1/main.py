import csv
import math
import random

#read csv file into list
def read_file(file_name):
    list = []
    with open(file_name, newline='') as f:
        lines = csv.reader(f, delimiter=";")
        for row in lines:
            list.append(row)
    f.close()
    return list

def normilize(dataset):
    attributes_values = []

    #get values for each attribute in dataset
    for i in range(len(dataset[0])-1):
        attributes_values.append([])
    for row in dataset:
        for i in range(len(row)-1):
            attributes_values[i].append(float(row[i]))

    max_attributes = []
    min_attributes = []

    #get max and min value for each attribute in dataset
    for attribute in attributes_values:
        max_attributes.append(max(attribute))
        min_attributes.append(min(attribute))

    #normalize every value
    for row in dataset:
        for i in range(len(row)-1):
            row[i] = round((float(row[i]) - min_attributes[i])/(max_attributes[i] - min_attributes[i]),3)
    
    return dataset

#function finding k closest vectors to a given one
def knn(k, vector, space):
    closest = []
    most_frequent = {}
    distance_vector_atribute = []
    
    #finding k nearest neighbors
    for v in space:
        sum = 0;
        for i in range(len(vector)):
            sum += round(((vector[i] - v[i])**2),3)
        distance_vector_atribute.append((math.sqrt(sum), v[len(v) - 1]))
    distance_vector_atribute.sort()
    closest = distance_vector_atribute[:k]
    
    #counting neighbors
    for e in closest:
        if(e[1] not in list(most_frequent.keys())):
            most_frequent.update({e[1]:1})
        else:
            most_frequent[e[1]] += 1

    #finding max freq
    max_frequent = max(most_frequent.values())
    
    #find and return most freq class
    for e in list(most_frequent.keys()):
        if (most_frequent[e] == max_frequent):
            return e
        
#print out accuracy for k from range 1 to 45        
def accuracy_for_each_k(test_list, train_list):
    for i in range(1,46):
        good_results = 0
        for e in test_list:
            vector = e[:-1]
            test_result = e[-1]
            knn_result = knn(i, vector, train_list)
            if(knn_result == test_result):
                good_results += 1
        print("k:", i, "accuracy: ", good_results/len(test_list))     


##########################################Testing and interface


k = int(input("Podaj k: "))
full_dataset = read_file("iris.csv")
train_list = read_file("train_set.csv")
test_list = read_file("test_set.csv")
train_list = normilize(train_list)
test_list = normilize(test_list)
full_dataset = normilize(full_dataset)
test_list_2 = random.sample(test_list, 35)
train_list_2 = [element for element in full_dataset if element not in test_list_2]
good_results = 0
number_of_coords = len(train_list[0])-1

#testing on test_set.csv
for e in test_list:
    vector = e[:-1]
    test_result = e[-1]
    knn_result = knn(k, vector, train_list)
    if(knn_result == test_result):
        good_results += 1
    print("result: ", knn_result, "from test_set: ", test_result)
    
#print out accuracy of testing for given k
print("accuracy: ", good_results/len(test_list))

accuracy_for_each_k(test_list, train_list)

print("Randomized data")

accuracy_for_each_k(train_list_2, test_list_2)

#Looped vector testing
while(True):
    input_vec = []
    for i in range(number_of_coords):
        input_vec.append(float(input("Podaj współrzędną: ")))
    print(knn(k, input_vec, train_list))
