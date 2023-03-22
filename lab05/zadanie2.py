import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7, 
random_state=92)
# print("set",train_set[0, 0:4])
# test_set[:, 4]

def classify_iris(a):
    # print(a
    if a[3] < 1:
        return("setosa")
    elif a[2] >= 5.2 or ( a[2] < 5.2 and a[3] > 1.6 and a[0] >= 4.8):
        return("virginica")
    else:
        return("versicolor")
    

good_predictions = 0
len = test_set.shape[0]
for i in range(len):
    if classify_iris(test_set[i, 0:4]) == test_set[i, 4]:
        good_predictions = good_predictions + 1

print(good_predictions)

print(good_predictions/len*100, "%")
