import time
import numpy as np
from qr_decomposition import *
import src.curves as crv


def getMatrixA(n):
    a_matrix = np.random.randn(n, n)
    return a_matrix


def getMatrixB(n):
    b_matrix = np.random.rand(n, 1)
    return b_matrix


if __name__ == '__main__':
    # Q1
    matrixSize = []

    # 1st method
    errorList = []
    timeList = []

    # 2nd method
    timeNp = []
    errorNp = []

    # 3rd method
    timeNpQr = []
    errorNpQr = []

    labels = ["Gram-Schmidt", "Numpy Solve", "Numpy Householder"]

    for n in range(1, 1000, 10):
        print(f"Matrice de taille {n}")

        matA = getMatrixA(n)
        matB = getMatrixB(n)

        qr_essai = QR(matA)

        # first method
        start = time.process_time()
        Q, R = qr_essai.DecompositionGS()
        X = qr_essai.ResolGS(matB)
        stop = time.process_time()
        error = np.linalg.norm(matA @ X - matB)

        totalTime = stop - start

        # 2nd method
        startNumpy = time.process_time()
        XNumpy = np.linalg.solve(matA, matB)
        stopNumpy = time.process_time()
        errorNumpy = np.linalg.norm(matA @ XNumpy - matB)

        totalNumpy = stopNumpy - startNumpy

        # 3rd method
        startNumpy2 = time.process_time()
        Q2, R2 = np.linalg.qr(matA)
        X2 = qr_essai.ResolGS(matB, Q2, R2)
        stopNumpy2 = time.process_time()
        errorNp2 = np.linalg.norm(matA @ X2 - matB)

        totalNumpy2 = stopNumpy2 - startNumpy2

        # list completion
        matrixSize.append(n)

        errorList.append(error)
        timeList.append(totalTime)

        errorNp.append(errorNumpy)
        timeNp.append(totalNumpy)

        errorNpQr.append(errorNp2)
        timeNpQr.append(totalNumpy2)
        # ===

    # time
    crvShow = crv.Curve("Temps de résolution d'une matrice par Gram Schmidt\n en fonction de la taille d'une matrice",
                        "taille de la matrice (n)", "temps de résolution (en ms)", labels)

    # error
    crvShow2 = crv.Curve("Erreur en fonction de la taille d'une matrice",
                         "taille de la matrice (n)", "erreurs (en puissance de 10)", labels)

    crvShow.plot_data(matrixSize, timeList, timeNp, timeNpQr, False)
    crvShow2.plot_data(matrixSize, errorList, errorNp, errorNpQr, True)
