#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:17:52 2024

@author: imtaeyeon
"""


import numpy as np
import tensorflow as tf
import tensorflow.keras.datasets as ds
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD, Adam
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = ds.mnist.load_data()
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype(np.float32) / 255.0
x_test = x_test.astype(np.float32) / 255.0
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# Model with SGD optimizer
dmlp = Sequential()
dmlp.add(Dense(units=1024, activation="relu", input_shape=(784,)))
dmlp.add(Dense(units=512, activation="relu"))
dmlp.add(Dense(units=512, activation="relu"))
dmlp.add(Dense(units=10, activation="softmax"))
dmlp.compile(loss="categorical_crossentropy", optimizer=Adam(learning_rate=0.001), metrics=["accuracy"])
hist = dmlp.fit(x_train, y_train, batch_size=128, epochs=50, validation_data=(x_test, y_test), verbose=2)
print("정확률: ", dmlp.evaluate(x_test, y_test, verbose=0)[1] * 100)

dmlp.save("dmpl_save.h5")

plt.plot(hist.history['accuracy'], 'r--', label='SGD Training Accuracy')
plt.plot(hist.history['val_accuracy'], 'r', label='SGD Validation Accuracy')
plt.title("Accuracy Comparison")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend(['train', 'test'])
plt.grid()
plt.show()

plt.plot(hist.history['loss'], 'r--', label='SGD Training Accuracy')
plt.plot(hist.history['val_loss'], 'r', label='SGD Validation Accuracy')
plt.title("loss Comparison")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend(['train', 'test'])
plt.grid()
plt.show()