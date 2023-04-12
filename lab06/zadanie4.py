import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from keras.models import Sequential
from keras.layers import Dense
from keras.activations import relu, sigmoid, tanh
from keras.utils import plot_model


diab = pd.read_csv("diabetes.csv")

diab['class'] = diab['class'].replace({'tested_positive': 1.0, 'tested_negative': 0.0})

all_inputs = diab[['pregnant-times','glucose-concentr','blood-pressure','skin-thickness','insulin','mass-index','pedigree-func','age']].values
all_classes = diab['class'].values

datasets = train_test_split(all_inputs, all_classes, test_size=0.3, random_state=278892)
train_data, test_data, train_labels, test_labels = datasets

scaler = StandardScaler()
scaler.fit(train_data)
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)

print(train_data[:3])

model = Sequential()
model.add(Dense(6, activation='relu', input_dim=train_data.shape[1]))
model.add(Dense(3, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(train_data, train_labels, epochs=500, batch_size=32, verbose=0, validation_data=(test_data, test_labels))

predictions_test_probs = model.predict(test_data)
predictions_test_probs = predictions_test_probs.flatten()

threshold = 0.5
predictions_test = [1 if prob > threshold else 0 for prob in predictions_test_probs]

accuracy = accuracy_score(test_labels, predictions_test)
print("Accuracy: " + str(round(accuracy*100,2)) + "%")



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




def create_model(optimizer='adam', activation='relu'):
    model = Sequential()
    model.add(Dense(6, activation=activation, input_dim=train_data.shape[1]))
    model.add(Dense(3, activation=activation))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
    return model

optimizers = ['adam', 'sgd', 'rmsprop']
activations = [relu, sigmoid, tanh]

plt.figure(figsize=(18, 12))

for i, optimizer in enumerate(optimizers):
    for j, activation in enumerate(activations):
        plt.subplot(len(optimizers), len(activations), i * len(activations) + j + 1)
        model = create_model(optimizer=optimizer, activation=activation)
        history = model.fit(train_data, train_labels, epochs=500, batch_size=32, verbose=0, validation_data=(test_data, test_labels))
        train_loss = history.history['loss']
        val_loss = history.history['val_loss']
        plt.plot(train_loss, label='Train')
        plt.plot(val_loss, label='Test')
        plt.title('Optimizer: {}, Activation: {}'.format(optimizer, activation.__name__))
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()

plt.tight_layout()
plt.show()