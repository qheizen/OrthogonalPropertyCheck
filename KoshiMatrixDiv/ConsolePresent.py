import numpy as np

ROUND_COEF = 4


def print_all_about_matrix(matrix, elems, dets, num):
    print("#" * 70)
    print(f"Номер матрицы - {num + 1}".center(60))
    print("Матрица после перемножения:")
    print(matrix)
    print("Элементы матрицы первой строки (модуль):", list(map(float, elems)))
    print("Детерминанты миноров (модуль):", list(map(float, dets)))


def print_abnormal_matrix(dets, matrix, q1_matrix, t, q2_matrix, num):
    print("#" * 70)
    print(f"Номер матрицы - {num + 1}".center(60))
    print("Q1: det(Q1) = ", np.linalg.det(q1_matrix))
    print(q1_matrix.round(ROUND_COEF))
    print("P: det(P) = ", np.linalg.det(t))
    print(t)
    print("Q2: det(Q2) = ", np.linalg.det(q2_matrix))
    print(q2_matrix.round(ROUND_COEF))
    print("Матрица после перемножения:")
    print(matrix.round(ROUND_COEF))
    print("Детерминанты миноров (модуль):", list(map(float, dets)))
