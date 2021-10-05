import time

import numpy as np
import src.resol_matrix as rslv


class QR:

    def __init__(self, A):
        self.A = A
        self.n, self.m = np.shape(self.A)
        self.Q = np.zeros((self.n, self.n))
        self.R = np.zeros((self.n, self.n))

    # Question #1
    def DecompositionGS(self):

        for j in range(self.n):
            w = self.A[:, j]
            for k in range(j):
                self.R[k, j] = self.Q[:, k] @ self.A[:, j]
                w = w - (self.R[k, j] * self.Q[:, k])
            self.R[j, j] = np.sqrt(sum(w) ** 2)
            self.Q[:, j] = w / (self.R[j, j])

        return self.Q, self.R

    def ResolGS(self, B, q=None, r=None):
        if q is not None:
            self.R = r
            self.Q = q

        X = rslv.ResolTriSup(self.R, np.transpose(self.Q) @ B)
        return X

# ========================================
