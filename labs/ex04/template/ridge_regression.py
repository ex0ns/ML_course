# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np


def ridge_regression(y, tx, lamb):
    """implement ridge regression."""
    ident = np.eye(tx.shape[1])*lamb
    return np.linalg.inv(tx.T.dot(tx)+ident).dot(tx.T).dot(y)
