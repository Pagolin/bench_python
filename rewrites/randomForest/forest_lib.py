from sklearn.tree import DecisionTreeClassifier

def train_tree(i, data, labels):
    tree = DecisionTreeClassifier()
    tree.fit(data, labels)

