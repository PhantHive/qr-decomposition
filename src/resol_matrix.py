#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Dans ce document, les accents ont ete volontairement
# omis pour eviter un eventuel probleme de compatibilite d'encodage.
#

import numpy as np


def ResolTriSup(T, b):
    """ Resolution d'un systeme Tx=b
    avec T triangulaire superieure et b un vecteur.
    La solution x est rendue de meme format que b """

    frm = b.shape
    n, m = T.shape
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        S = T[i, i + 1:] @ x[i + 1:]
        x[i] = (b[i] - S) / T[i, i]
    return x.reshape(frm)


def ResolTriInf(T, b):
    """ Resolution d'un systeme Tx=b
    avec T triangulaire inferieure et b un vecteur.
    La solution x est rendue de meme format que b """

    frm = b.shape
    n, m = T.shape
    x = np.zeros(n)
    for i in range(n):
        S = T[i, :i] @ x[:i]
        x[i] = (b[i] - S) / T[i, i]
    return x.reshape(frm)


def DecompositionLU(A):
    """ Calcul de la decomposition LU d'une matrice carree A"""
    U = np.array(A, float)
    n, m = U.shape
    if n != m:
        raise Exception('Pas une matrice carree')
    L = np.eye(n)
    for i in range(n - 1):
        if U[i, i] == 0:
            raise Exception('Un pivot est nul')
        for j in range(i + 1, n):
            g = U[j, i] / U[i, i]
            L[j, i] = g
            U[j, :] = U[j, :] - g * U[i, :]
    return L, U
