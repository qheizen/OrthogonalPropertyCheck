import KoshiMatrixDiv
import numpy as np
import os

from KoshiMatrixDiv.MatrixOperation import koshi, generate_pe_matrix, matrix_product_combinations, check_is_matrix_abnormal
from KoshiMatrixDiv.ConsolePresent import print_abnormal_matrix

def calc_single_pe_abs(): #1
    p_m, e_m = generate_pe_matrix()
    matrix1 = np.array([])
    matrix2 = np.array([])

    checker = False
    while not checker:
        matrix1 = koshi.get_orthogonal_random_matrix()
        matrix2 = koshi.get_orthogonal_random_matrix()
        if np.linalg.det(matrix1) * np.linalg.det(matrix2) > 0:
            checker = True

    variants = len(p_m) * len(e_m)

    counter = 0
    for i in range(variants):
        transitive = matrix_product_combinations(p_m, e_m, i)
        v = matrix1 @ transitive @ matrix2
        det = koshi.calculate_minor_determinants(v)

        if check_is_matrix_abnormal(list(map(abs,det))):
            print_abnormal_matrix(det, v, matrix1, transitive, matrix2, i)
            counter += 1
    print("Количество матриц - ", counter)

def calc_single_p_abs(): #2
    p_m, e_m = generate_pe_matrix()
    matrix1 = np.array([])
    matrix2 = np.array([])

    checker = False
    while not checker:
        matrix1 = koshi.get_orthogonal_random_matrix()
        matrix2 = koshi.get_orthogonal_random_matrix()
        if np.linalg.det(matrix1) * np.linalg.det(matrix2) > 0:
            checker = True

    variants = len(p_m)

    counter = 0
    for i in range(variants):
        transitive = p_m[i]
        v = matrix1 @ transitive @ matrix2
        det = koshi.calculate_minor_determinants(v)

        if check_is_matrix_abnormal(list(map(abs, det))):
            print_abnormal_matrix(det, v, matrix1, transitive, matrix2, i)
            counter += 1
    print("Количество матриц - ", counter)

def calc_single_pe(): #3
    p_m, e_m = generate_pe_matrix()
    matrix1 = np.array([])
    matrix2 = np.array([])

    checker = False
    while not checker:
        matrix1 = koshi.get_orthogonal_random_matrix()
        matrix2 = koshi.get_orthogonal_random_matrix()
        if np.linalg.det(matrix1) * np.linalg.det(matrix2) > 0:
            checker = True

    variants = len(p_m) * len(e_m)

    counter = 0
    for i in range(variants):
        transitive = matrix_product_combinations(p_m, e_m, i)
        v = matrix1 @ transitive @ matrix2
        det = koshi.calculate_minor_determinants(v)

        if check_is_matrix_abnormal(det):
            print_abnormal_matrix(det, v, matrix1, transitive, matrix2, i)
            counter += 1
    print("Количество матриц - ", counter)

def calc_single_p(): #4
    p_m, e_m = generate_pe_matrix()
    matrix1 = np.array([])
    matrix2 = np.array([])

    checker = False
    while not checker:
        matrix1 = koshi.get_orthogonal_random_matrix()
        matrix2 = koshi.get_orthogonal_random_matrix()
        if np.linalg.det(matrix1) * np.linalg.det(matrix2) > 0:
            checker = True

    variants = len(p_m)

    counter = 0
    for i in range(variants):
        transitive = p_m[i]
        v = matrix1 @ transitive @ matrix2
        det = koshi.calculate_minor_determinants(v)

        if check_is_matrix_abnormal(det):
            print_abnormal_matrix(det, v, matrix1, transitive, matrix2, i)
            counter += 1
    print("Количество матриц - ", counter)


def main():
    while True:
        os.system('cls')
        print(f"Для указания размерности матрицы введите -> size")
        print(f"Для указания количества просчитываемых матриц в режиме статистики -> stat")
        print(f"Прогонки с матрицей {koshi.matrix_size} перестановок и отражения P @ E и взятия детерминанта по модулю -> 1")
        print(f"Прогонки с матрицей {koshi.matrix_size} перестановок P и взятия детерминанта по модулю -> 2")
        print(f"Прогонки с матрицей {koshi.matrix_size} перестановок и отражения P @ E -> 3")
        print(f"Прогонки с матрицей {koshi.matrix_size} перестановок P -> 4")
        input_string: str = input()

        if input_string == "size":
            koshi.matrix_size = int(input("Укажите значение типа int"))
        elif input_string == "stat":
            koshi.amount = int(input("Укажите значение типа int"))
        elif input_string == "1":
            calc_single_pe_abs()
        elif input_string == "2":
            calc_single_p_abs()
        elif input_string == "3":
            calc_single_pe()
        elif input_string == "4":
            calc_single_p()

        input("Нажмите enter")

if __name__ == "__main__":
    main()
