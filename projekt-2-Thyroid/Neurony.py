from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.activations import relu, sigmoid, tanh
from keras.utils import plot_model
from sklearn.metrics import accuracy_score, confusion_matrix



import pandas as pd
from Data import data, data2

from sklearn import preprocessing
le = preprocessing.LabelEncoder()

data['target'] = le.fit_transform(data['target'])

all_inputs = data.drop('target',axis=1).values
all_classes = data['target'].values

all_inputs2 = data2.drop('target', axis=1).values
all_classes2 = data2['target'].values


# (train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=278892)
# (train_inputs2, test_inputs2, train_classes2, test_classes2) = train_test_split(all_inputs2, all_classes2, train_size=0.7, random_state=278892)

datasets = train_test_split(all_inputs, all_classes, test_size=0.3, random_state=278892)
train_data, test_data, train_labels, test_labels = datasets

scaler = StandardScaler()
scaler.fit(train_data)
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)

model = Sequential()
model.add(Dense(6, activation='relu', input_dim=train_data.shape[1]))
model.add(Dense(6, activation='relu'))
model.add(Dense(2, activation='relu'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# compile the keras model
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
# model.fit(X, y, epochs=150, batch_size=10)
# evaluate the keras model


model.fit(train_data, train_labels, epochs=500, batch_size=32, verbose=0, validation_data=(test_data, test_labels))

# predictions_test_probs = model.predict(test_data)
# predictions_test_probs = predictions_test_probs.flatten()

# threshold = 0.5
# predictions_test = [1 if prob > threshold else 0 for prob in predictions_test_probs]

# accuracy = accuracy_score(test_labels, predictions_test)

# print("Accuracy: " + str(round(accuracy*100,2)) + "%")

_, accuracy = model.evaluate(test_labels, test_data)
print('Accuracy: %.2f' % (accuracy*100))

