from matplotlib import pyplot as plt
import numpy as np
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense , Flatten
from keras.activations import relu, sigmoid, tanh
from keras.utils import plot_model, normalize
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, confusion_matrix
from ann_visualizer.visualize import ann_viz;


import pandas as pd
import tensorflow as tf
from Data import data, data2

from sklearn import preprocessing
le = preprocessing.LabelEncoder()

data['target'] = le.fit_transform(data['target'])
data2['target'] = le.fit_transform(data2['target'])

all_inputs = data.drop('target',axis=1).values
print(len(all_inputs))
all_classes = data['target'].values

all_inputs2 = data2.drop('target', axis=1).values

all_classes2 = data2['target'].values


(train_data, test_data, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=278892)

scaler = StandardScaler()
scaler.fit(train_data)
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)


model = Sequential()
model.add(Dense(3, activation='relu'))
model.add(Dense(8, activation='selu'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy' , metrics=['accuracy'])

#sigmoid-spoko
#relu -słabiej
#softplus -nawet ok
#softsign -super 
#tanh -super



# Sgd -spoko --- słabo
#RMSprop - słabo  -- słabo 
# adam -spoko -spoko pardzo podobnie
    # Adamax-fajnie --gorzej 
    # Nadam-spoko -- owiele gorzej 
    # Ftrl-spoko  --spoko 



history= model.fit(train_data, train_classes, epochs=30, batch_size=2, validation_data=(test_data, test_classes))
_, accuracy = model.evaluate(test_data, test_classes)
print('Accuracy: %.2f' % (accuracy*100))


ann_viz(model, title="My first neural network")

# threshold = 0.5
# predictions_test = [1 if prob > threshold else 0 for prob in predictions_test_probs]

# y_pred_labels = np.argmax(model.predict(test_data), axis=1)
# cm = confusion_matrix(test_classes, y_pred_labels)
# disp = ConfusionMatrixDisplay(confusion_matrix=cm)
# disp.plot()


train_loss = history.history['loss']
val_loss = history.history['val_loss']

plt.figure(figsize=(10, 6))
plt.plot(train_loss, label='Train')
plt.plot(val_loss, label='Test')
plt.title('Loss Curve')
plt.xlabel('Epoch') 
plt.ylabel('Loss')
plt.legend()
plt.show()


## data2 

(train_data2, test_data2, train_classes2, test_classes2) = train_test_split(all_inputs2, all_classes2, train_size=0.6, random_state=278892)

scaler2 = StandardScaler()
scaler2.fit(train_data2)
train_data2 = scaler2.transform(train_data2)
test_data2 = scaler2.transform(test_data2)


model2 = Sequential()
model2.add(Dense(3, activation='relu'))
model2.add(Dense(3, activation='relu'))
model2.add(Dense(8, activation='softmax'))
model2.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

history2 = model2.fit(train_data2, train_classes2, epochs=30, batch_size=16,verbose=0, validation_data=(test_data2, test_classes2))
_, accuracy = model2.evaluate(test_data2, test_classes2)
print('Accuracy: %.2f' % (accuracy*100))

ann_viz(model2, title="My first neural network")


y_pred_labels = np.argmax(model2.predict(test_data2), axis=1)
cm = confusion_matrix(test_classes2, y_pred_labels)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()


train_loss = history2.history['loss']
val_loss = history2.history['val_loss']

plt.figure(figsize=(10, 6))
plt.plot(train_loss, label='Train')
plt.plot(val_loss, label='Test')
plt.title('Loss Curve')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()

