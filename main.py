from math import factorial

import numpy
import KoshiDerivation.Derivation as ksh
import os
ROUND_COEF = 4
STAT_COUNT = 10000

def print_all_about_matrix(dets, elems, matrix, num):
    print("#" * 70)
    print(f"Номер матрицы - {num + 1}".center(60))
    print("Матрица после перемножения:")
    print(matrix)
    print("Элементы матрицы первой строки (модуль):", list(map(float, elems)))
    print("Детерминанты миноров (модуль):", list(map(float, dets)))


def print_abnormal_matrix(dets, matrix, matrix1, t, matrix2, num):
    print("#" * 70)
    print(f"Номер матрицы - {num+1}".center(60))
    print("Q1: det(Q1) = ", numpy.linalg.det(matrix1))
    print(matrix1.round(ROUND_COEF))
    print("P: det(P) = ", numpy.linalg.det(t))
    print(t)
    print("Q2: det(Q2) = ", numpy.linalg.det(matrix2))
    print(matrix2.round(ROUND_COEF))
    print("Матрица после перемножения:")
    print(matrix.round(ROUND_COEF))
    print("Детерминанты миноров (модуль):", list(map(float,dets)))


def check_is_matrix_abnormal(det):
    return min(det) >= 1/(factorial(ksh.MATRIX_SIZE) * (2**(ksh.MATRIX_SIZE-1)))

# для 4 порядка - 1/8*24
# для 5 1/5факториал*2^4

def set_matrix_size():
    print(f"Укажите значение типа int")
    ksh.MATRIX_SIZE = int(input())

def set_stat_size():
    print(f"Укажите значение типа int")
    STAT_COUNT = int(input())

def calc_single_pe_abs(): #1
    transitive_matrices = ksh.get_all_variations_of_pe()
    matrix1 = ksh.get_orthogonal_random_matrix()
    matrix2 = ksh.get_orthogonal_random_matrix()

    variants = [matrix1 @ t @ matrix2 for t in transitive_matrices]

    counter = 0
    for i, v in enumerate(variants):
        det = ksh.calculate_determinant(v)

        if check_is_matrix_abnormal(list(map(abs,det))):
            print_abnormal_matrix(det, v, matrix1, transitive_matrices[i], matrix2, i)
            counter += 1
    print("Количество матриц - ", counter)

def calc_single_p_abs(): #2
    transitive_matrices = ksh.generate_permutation_matrices()
    matrix1 = ksh.get_orthogonal_random_matrix()
    matrix2 = ksh.get_orthogonal_random_matrix()

    variants = [matrix1 @ t @ matrix2 for t in transitive_matrices]

    counter = 0
    for i, v in enumerate(variants):
        det = ksh.calculate_determinant(v)

        if check_is_matrix_abnormal(list(map(abs,det))):
            print_abnormal_matrix(det, v, matrix1, transitive_matrices[i], matrix2, i)
            counter += 1
    print("Количество матриц - ", counter)

def calc_single_pe(): #3
    transitive_matrices = ksh.get_all_variations_of_pe()
    matrix1 = ksh.get_orthogonal_random_matrix()
    matrix2 = ksh.get_orthogonal_random_matrix()

    variants = [matrix1 @ t @ matrix2 for t in transitive_matrices]

    counter = 0
    for i, v in enumerate(variants):
        det = ksh.calculate_determinant(v)

        if check_is_matrix_abnormal(det):
            print_abnormal_matrix(det, v, matrix1, transitive_matrices[i], matrix2, i)
            counter += 1
    print("Количество матриц - ", counter)

def calc_single_p(): #4
    transitive_matrices = ksh.generate_permutation_matrices()
    matrix1 = ksh.get_orthogonal_random_matrix()
    matrix2 = ksh.get_orthogonal_random_matrix()

    variants = [matrix1 @ t @ matrix2 for t in transitive_matrices]

    counter = 0
    for i, v in enumerate(variants):
        det = ksh.calculate_determinant(v)

        if check_is_matrix_abnormal(det):
            print_abnormal_matrix(det, v, matrix1, transitive_matrices[i], matrix2, i)
            counter += 1
    print("Количество матриц - ", counter)

def calc_many_pe_abs():
    transitive_matrices = ksh.get_all_variations_of_pe()
    index_stat = [0] * (len(transitive_matrices) + 1)
    counter_anti = 0
    for k in range(STAT_COUNT):
        matrix1 = ksh.get_orthogonal_random_matrix()
        matrix2 = ksh.get_orthogonal_random_matrix()

        variants = [matrix1 @ t @ matrix2 for t in transitive_matrices]
        counter = 0


        for i, v in enumerate(variants):
            det = ksh.calculate_determinant(v)

            if check_is_matrix_abnormal(list(map(abs,det))):
                index_stat[i] += 1
                counter += 1
        print("Количество матриц - ",  counter)

        if counter == 0:
            print("Нет удовлетворяющих матриц")
            print(matrix1)
            print(numpy.linalg.det(matrix1))
            print(matrix2)
            print(numpy.linalg.det(matrix2))
            counter_anti += 1
            index_stat[len(transitive_matrices)] += 1

        del matrix1
        del matrix2

    print("Количество удовлетворяющих - ", counter_anti)
    print("Статистика по индексам - ", index_stat)


def calc_many_p_abs():
    transitive_matrices = ksh.generate_permutation_matrices()
    index_stat = [0] * (len(transitive_matrices) + 1)
    counter_anti = 0
    for k in range(STAT_COUNT):
        matrix1 = ksh.get_orthogonal_random_matrix()
        matrix2 = ksh.get_orthogonal_random_matrix()

        variants = [matrix1 @ t @ matrix2 for t in transitive_matrices]
        counter = 0

        for i, v in enumerate(variants):
            det = ksh.calculate_determinant(v)

            if check_is_matrix_abnormal(list(map(abs,det))):
                index_stat[i] += 1
                counter += 1
        print("Количество матриц - ", counter)

        if counter == 0:
            print("Нет удовлетворяющих матриц")
            print(matrix1)
            print(numpy.linalg.det(matrix1))
            print(matrix2)
            print(numpy.linalg.det(matrix2))
            counter_anti += 1
            index_stat[len(transitive_matrices)] += 1

        del matrix1
        del matrix2
    print("Количество удовлетворяющих - ", counter_anti)
    print("Статистика по индексам - ", index_stat)


def calc_many_pe():
    transitive_matrices = ksh.get_all_variations_of_pe()
    index_stat = [0] * (len(transitive_matrices) + 1)
    counter_anti = 0
    for k in range(STAT_COUNT):
        matrix1 = ksh.get_orthogonal_random_matrix()
        matrix2 = ksh.get_orthogonal_random_matrix()

        variants = [matrix1 @ t @ matrix2 for t in transitive_matrices]
        counter = 0

        for i, v in enumerate(variants):
            det = ksh.calculate_determinant(v)

            if check_is_matrix_abnormal(det):
                index_stat[i] += 1
                counter += 1
        print("Количество матриц - ", counter)

        if counter == 0:
            print("Нет удовлетворяющих матриц")
            print(matrix1)
            print(numpy.linalg.det(matrix1))
            print(matrix2)
            print(numpy.linalg.det(matrix2))
            counter_anti += 1
            index_stat[len(transitive_matrices)] += 1

        del matrix1
        del matrix2
    print("Количество удовлетворяющих - ", counter_anti)
    print("Статистика по индексам - ", index_stat)

def calc_many_p():
    transitive_matrices = ksh.generate_permutation_matrices()
    index_stat = [0] * (len(transitive_matrices) + 1)
    counter_anti = 0
    for k in range(STAT_COUNT):
        matrix1 = ksh.get_orthogonal_random_matrix()
        matrix2 = ksh.get_orthogonal_random_matrix()

        variants = [matrix1 @ t @ matrix2 for t in transitive_matrices]
        counter = 0

        for i, v in enumerate(variants):
            det = ksh.calculate_determinant(v)

            if check_is_matrix_abnormal(det):
                index_stat[i] += 1
                counter += 1
        print("Количество матриц - ", counter)

        if counter == 0:
            print("Нет удовлетворяющих матриц")
            print(matrix1)
            print(numpy.linalg.det(matrix1))
            print(matrix2)
            print(numpy.linalg.det(matrix2))
            counter_anti += 1
            index_stat[len(transitive_matrices)] += 1

        del matrix1
        del matrix2
    print("Количество удовлетворяющих - ", counter_anti)
    print("Статистика по индексам - ", index_stat)

def main():
    while True:
        os.system('cls')
        print(f"Для указания размерности матрицы введите -> size")
        print(f"Для указания количества просчитываемых матриц в режиме статистики -> stat")
        print(f"Прогонки с матрицей {ksh.MATRIX_SIZE} перестановок и отражения P @ E и взятия детерминанта по модулю -> 1")
        print(f"Прогонки с матрицей {ksh.MATRIX_SIZE} перестановок P и взятия детерминанта по модулю -> 2")
        print(f"Прогонки с матрицей {ksh.MATRIX_SIZE} перестановок и отражения P @ E -> 3")
        print(f"Прогонки с матрицей {ksh.MATRIX_SIZE} перестановок P -> 4")
        print(f"Просчет {STAT_COUNT} матриц с P @ E и взятия детерминанта по модулю -> 5")
        print(f"Просчет {STAT_COUNT} матриц с P и взятия детерминанта по модулю -> 6")
        print(f"Просчет {STAT_COUNT} матриц с P @ E -> 7")
        print(f"Просчет {STAT_COUNT} матриц с P -> 8")

        input_string: str = input()

        if input_string == "size":
            set_matrix_size()
        elif input_string == "stat":
            set_stat_size()
        elif input_string == "1":
            calc_single_pe_abs()
        elif input_string == "2":
            calc_single_p_abs()
        elif input_string == "3":
            calc_single_pe()
        elif input_string == "4":
            calc_single_p()
        elif input_string == "5":
            calc_many_pe_abs()
        elif input_string == "6":
            calc_many_p_abs()
        elif input_string == "7":
            calc_many_pe()
        elif input_string == "8":
            calc_many_p()

        input("Нажмите enter")
        input()



if __name__ == "__main__":
    main()


