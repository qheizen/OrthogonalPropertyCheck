import KoshiDerivation.Derivation as ksh

ROUND = 4

def unlimit_checker(transitive_matrices: list):
    while True:
        matrix1 = ksh.get_orthogonal_random_matrix()
        matrix2 = ksh.get_orthogonal_random_matrix()

        variants = [matrix1 @ t @ matrix2 for t in transitive_matrices]

        for i, v in enumerate(variants):
            det = map(abs, ksh.calculate_determinant(v))
            elem = map(abs, [v[0][0], v[0][1], v[0][2]])

            if check_is_matrix_abnormal(det):
                print_abnormal_matrix(det, elem, v, matrix1, transitive_matrices[i], matrix2, i)


def single_matrix_gen(transitive_matrices: list):
    matrix1 = ksh.get_orthogonal_random_matrix()
    matrix2 = ksh.get_orthogonal_random_matrix()

    variants = [matrix1 @ t @ matrix2 for t in transitive_matrices]

    for i, v in enumerate(variants):
        det = list(map(abs, ksh.calculate_determinant(v)))
        elem = list(map(abs, [v[0][0], v[0][1], v[0][2]]))

        if check_is_matrix_abnormal(det):
            print_abnormal_matrix(det, elem, v, matrix1, transitive_matrices[i], matrix2, i)
        else:
            print_all_about_matrix(det, elem, v, i)


def print_all_about_matrix(dets, elems, matrix, num):
    print("\033[37m#" * 70)
    print(f"Номер матрицы - {num + 1}".center(60))
    print("Матрица после перемножения:")
    print(matrix)
    print("Элементы матрицы первой строки (модуль):", list(map(float, elems)))
    print("Детерминанты миноров (модуль):", list(map(float, dets)))


def print_abnormal_matrix(dets, elems, matrix, matrix1, t, matrix2, num):
    print("\033[36m#" * 70)
    print(f"Номер матрицы - {num+1}".center(60))
    print("Q1:")
    print(matrix1.round(ROUND))
    print("P:")
    print(t)
    print("Q2:")
    print(matrix2.round(ROUND))
    print("Матрица после перемножения:")
    print(matrix.round(ROUND))
    print("Элементы матрицы первой строки (модуль):", list(map(float, elems)))
    print("Детерминанты миноров (модуль):", list(map(float,dets)))
    print("\033[37m")


def check_is_matrix_abnormal(det):
    return min(det) >= 1/24


def main():
    transitive_matrices = ksh.get_all_variation_transitive()
    print(len(transitive_matrices))
    print("Введите 1 - работа в бесконечном режиме с отслеживанием условия.")
    print("Введите 2 - вывести все транзитивные матрицы.")
    print("Иначе нажмите Enter")

    inputStr: str = input()

    if inputStr == "1":
        unlimit_checker(transitive_matrices)
    elif inputStr == "2":
        for matrix in transitive_matrices:
            print(matrix)
    else:
        single_matrix_gen(transitive_matrices)


if __name__ == "__main__":
    main()
