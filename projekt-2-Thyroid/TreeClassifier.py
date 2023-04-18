import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from Data import data, data2


all_inputs = data.drop('target',axis=1).values
all_classes = data['target'].values

all_inputs2 = data2.drop('target', axis=1).values
all_classes2 = data2['target'].values

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=92)
(train_inputs2, test_inputs2, train_classes2, test_classes2) = train_test_split(all_inputs2, all_classes2, train_size=0.7, random_state=92)


# wiersze, kolumny = np.where(data == "f")
# for i in range(len(wiersze)):
#     print(f"Wartość f znajduje się w wierszu {wiersze[i]} i kolumnie {kolumny[i]}")
dtc = DecisionTreeClassifier()
dtc.fit(train_inputs, train_classes)
dtc.score(test_inputs, test_classes)
print(dtc.score(test_inputs, test_classes))
tree.plot_tree(dtc)
plt.show()

dtc2 = DecisionTreeClassifier()
dtc2.fit(train_inputs2, train_classes2)
dtc2.score(test_inputs2, test_classes2)
print(dtc2.score(test_inputs2, test_classes2))
tree.plot_tree(dtc2)
plt.show()


