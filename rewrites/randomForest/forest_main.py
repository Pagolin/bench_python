from forest_lib import *
from collections import Counter
from sklearn.tree import DecisionTreeClassifier

def train_tree(i, data, labels):
    tree = DecisionTreeClassifier()
    tree.fit(data, labels)


def train_forest(data, labels, count, sample):
    forest = []
    for i in range(count):
        tree = train_tree(i, data, labels)
        forest.append(tree)
    predictions = []
    for tree in forest:
        prediction = tree.predict(sample)
        first = prediction.__getitem__(0)
        predictions.append(first)
    return Counter(predictions).most_common(1)

