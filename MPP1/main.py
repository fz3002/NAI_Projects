def main(k,train_set,test_set):
    train_list = []
    test_list = []
    print(train_set)
    with open(train_set, 'r') as f:
        lines = f.readlines();
        print(len(lines))
        for line in lines:
            attributes = line.split(";")
            new_iris = iris(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4])
            train_list.append(new_iris)
    f.close()
    with open(test_set, 'r') as f:
        lines = f.readlines();
        for line in lines:
            attributes = line.split(";")
            new_iris = iris(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4])
            test_list.append(new_iris)
    f.close()
    print(len(train_list))
    print(len(test_list))

class iris:
    def __init__(self, first, second, third, fourth, verdict):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.verdict = verdict


k = int(input("Podaj k"))
main(k, "train_set.csv", "test_set.csv")
