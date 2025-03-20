import KoshiDerivation.KoshiDerivation as ksh


def main():
    transitive_matrices = ksh.get_all_variation_transitive()

    while True:
        matrix1 = ksh.get_orthogonal_random_matrix()
        matrix2 = ksh.get_orthogonal_random_matrix()

        variants = [matrix1 @ t @ matrix2 for t in transitive_matrices]

        for v in variants:
            det = abs(ksh.calculate_determinant(v))
            elem = abs(v[0][0])

            if not ksh.is_equal(det, elem):
                print(f"Совпадение: det={det} != elem[0][0]={elem}")
                print("Матрица:\n", v)


if __name__ == "__main__":
    main()
