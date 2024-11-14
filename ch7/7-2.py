#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:46:02 2024

@author: imtaeyeon
"""

import numpy as np
import tensorflow as tf
import tensorflow.keras.datasets as ds

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD, Adam

(x_train, y_train), (x_test, y_test) = ds.mnist.load_data()
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype(np.float32) / 255.0
x_test = x_test.astype(np.float32) / 255.0
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

mlp_sgd = Sequential()
mlp_sgd.add(Dense(units=512, activation="tanh", input_shape=(784,)))
mlp_sgd.add(Dense(units=10, activation="softmax"))

mlp_sgd.compile(loss="MSE", optimizer=Adam(learning_rate=0.001), metrics=["accuracy"])
mlp_sgd.fit(x_train, y_train, batch_size=128, epochs=50, validation_data=(x_test, y_test), verbose=2)

res = mlp_sgd.evaluate(x_test, y_test, verbose=0)
print("정확률 = ", res[1] * 100)