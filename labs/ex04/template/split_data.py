# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""


import numpy as np


def split_data(x, y, ratio, seed=1):
    """split the dataset based on the split ratio."""
    # set seed
    np.random.seed(seed)
    indices = np.arange(x.shape[0])
    np.random.shuffle(indices)
    # np.random.permutation

    number = int(x.shape[0]*ratio)
    trainingX = np.array([x[i] for i in indices[:number]])
    trainingY = np.array([y[i] for i in indices[:number]])

    testX = np.array([x[i] for i in indices[number:]])
    testY = np.array([y[i] for i in indices[number:]])
    assert(trainingX.shape[0] + testX.shape[0] == x.shape[0])
    
    return trainingX, trainingY, testX, testY
