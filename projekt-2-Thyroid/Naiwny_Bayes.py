import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import seaborn as sns
from Data import data, data2
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
)
sns.set()




all_inputs = data.drop('target',axis=1).values
all_classes = data['target'].values

all_inputs2 = data2.drop('target', axis=1).values
all_classes2 = data2['target'].values



(X_train, X_test, y_train, y_test) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=278892)

(X_train2, X_test2, y_train2, y_test2) = train_test_split(all_inputs2, all_classes2, train_size=0.7, random_state=278892)


#data

model = GaussianNB()


model.fit(X_train, y_train)



y_pred = model.predict(X_test)
accuray = accuracy_score(y_pred, y_test)
f1 = f1_score(y_pred, y_test, average="weighted")

print("Accuracy:", accuray)
print("F1 Score:", f1)


#data2

model2 = GaussianNB()


model2.fit(X_train2, y_train2)


y_pred2 = model2.predict(X_test2)
accuray = accuracy_score(y_pred2, y_test2)
f1 = f1_score(y_pred2, y_test2, average="weighted")

print("Accuracy:", accuray)
print("F1 Score:", f1)
