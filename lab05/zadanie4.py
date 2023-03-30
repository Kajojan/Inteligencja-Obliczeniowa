import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
)
sns.set()


df = pd.read_csv('./iris.csv')
X = pd.DataFrame(df, columns=df.columns)
X = X[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]

y = df["species"]
# y = pd.get_dummies(y, drop_first=True)


X_train, X_test, y_train, y_test = train_test_split(X, y,train_size=0.7, random_state=278892)

# k_range= [3,5,11]

# for i in k_range:
#     knn=KNeighborsClassifier(n_neighbors=i)
#     knn.fit(X_train,y_train)
#     y_pred=knn.predict(X_test)
#     print(i , " - "  ,metrics.accuracy_score(y_test,y_pred)*100)
#     y_pred_labels = np.argmax(y_pred, axis=1)
#     y_test_labels = np.argmax(y_test.values, axis=1)
#     cm = confusion_matrix(y_test_labels, y_pred_labels)
#     print(cm,"\n")






model = GaussianNB()


model.fit(X_train, y_train)



y_pred = model.predict(X_test)
accuray = accuracy_score(y_pred, y_test)
f1 = f1_score(y_pred, y_test, average="weighted")

print("Accuracy:", accuray)
print("F1 Score:", f1)

print(1/(1+np.exp(-0.79853419159)))


