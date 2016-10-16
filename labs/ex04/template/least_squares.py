# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np

def least_squares(y, tx):
    w = np.linalg.pinv(tx).dot(y) # np.linalg.inv(tx.T.dot(tx)).dot(tx.T).dot(y)
    #return w, compute_loss(y, tx, w)
    return w
