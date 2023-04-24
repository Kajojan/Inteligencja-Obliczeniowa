import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics, tree
from Data import data, data2


all_inputs = data.drop('target',axis=1).values
all_classes = data['target'].values

all_inputs2 = data2.drop('target', axis=1).values
all_classes2 = data2['target'].values
all_classes = pd.get_dummies(all_classes, drop_first=True)
all_classes2 = pd.get_dummies(all_classes2, drop_first=True)



(X_train, X_test, y_train, y_test) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=92)
(X_train2, X_test2, y_train2, y_test2) = train_test_split(all_inputs2, all_classes2, train_size=0.7, random_state=92)


k_range= [3,5,11]

for i in k_range:
    knn=KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    y_pred=knn.predict(X_test)
    print(i , " - "  ,metrics.accuracy_score(y_test,y_pred)*100)
    y_pred_labels = np.argmax(y_pred, axis=1)
    y_test_labels = np.argmax(y_test.values, axis=1)
    cm = metrics.confusion_matrix(y_test_labels, y_pred_labels)
    disp = metrics.ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.show()

for i in k_range:
    knn=KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train2,y_train2)
    y_pred=knn.predict(X_test2)
    print(i , " - "  ,metrics.accuracy_score(y_test2,y_pred)*100)
    y_pred_labels = np.argmax(y_pred, axis=1)
    y_test_labels = np.argmax(y_test2.values, axis=1)
    cm = metrics.confusion_matrix(y_test_labels, y_pred_labels)
    disp.plot()
    plt.show()
