# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    return np.array([[line**deg for deg in range(degree+1)] for line in x])
