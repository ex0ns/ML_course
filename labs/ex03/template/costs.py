# -*- coding: utf-8 -*-
"""a function used to compute the loss."""

import numpy as np


def compute_loss(y, tx, w, mae = False):
    loss = 0
    N = y.shape[0]
    e = y-np.dot(tx,w)
    
    if mae:
        loss = 1/N * np.sum(np.absolute(e))
    else:
        loss = 1/(2*N) * (np.dot(np.transpose(e),e))

    return loss
