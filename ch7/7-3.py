#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:50:06 2024

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
mlp_sgd = Sequential()
mlp_sgd.add(Dense(units=512, activation="tanh", input_shape=(784,)))
mlp_sgd.add(Dense(units=10, activation="softmax"))
mlp_sgd.compile(loss="MSE", optimizer=SGD(learning_rate=0.001), metrics=["accuracy"])
hist_sgd = mlp_sgd.fit(x_train, y_train, batch_size=128, epochs=50, validation_data=(x_test, y_test), verbose=2)
print("SGD 정확률: ", mlp_sgd.evaluate(x_test, y_test, verbose=0)[1] * 100)

# Model with Adam optimizer
mlp_adam = Sequential()
mlp_adam.add(Dense(units=512, activation="tanh", input_shape=(784,)))
mlp_adam.add(Dense(units=10, activation="softmax"))
mlp_adam.compile(loss="MSE", optimizer=Adam(learning_rate=0.001), metrics=["accuracy"])
hist_adam = mlp_adam.fit(x_train, y_train, batch_size=128, epochs=50, validation_data=(x_test, y_test), verbose=2)
print("Adam 정확률: ", mlp_adam.evaluate(x_test, y_test, verbose=0)[1] * 100)

# Plotting
plt.plot(hist_sgd.history['accuracy'], 'r--', label='SGD Training Accuracy')
plt.plot(hist_sgd.history['val_accuracy'], 'r', label='SGD Validation Accuracy')
plt.plot(hist_adam.history['accuracy'], 'b--', label='Adam Training Accuracy')
plt.plot(hist_adam.history['val_accuracy'], 'b', label='Adam Validation Accuracy')
plt.title("Accuracy Comparison")
plt.ylim(0.7, 1.0)
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid()
plt.show()