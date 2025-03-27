import numpy as np
from itertools import permutations, product
from typing import List, Optional, Union
from math import factorial

np.set_printoptions(precision=30, linewidth=200)
HIGH_PRECISION_DTYPE = np.float64


def matrix_product_combinations(matrix_list1: List[np.ndarray],
                                matrix_list2: List[np.ndarray],
                                index: Optional[int] = None) -> Union[List[np.ndarray], np.ndarray]:
    if index is not None:
        n = len(matrix_list2)
        i = index // n
        j = index % n

        if i < 0 or i >= len(matrix_list1) or j < 0 or j >= len(matrix_list2):
            raise IndexError(f"Index {index} is out of bounds")

        a = matrix_list1[i].astype(HIGH_PRECISION_DTYPE, copy=False)
        b = matrix_list2[j].astype(HIGH_PRECISION_DTYPE, copy=False)
        return np.dot(a, b)

    class LazyProductGenerator:
        def __iter__(self):
            for a in matrix_list1:
                for b in matrix_list2:
                    yield np.dot(
                        a.astype(HIGH_PRECISION_DTYPE, copy=False),
                        b.astype(HIGH_PRECISION_DTYPE, copy=False))

    return list(LazyProductGenerator())

def generate_pe_matrix() -> tuple:
    p_matrix = koshi.generate_permutation_matrices()
    e_matrix = koshi.generate_refraction_matrices()
    return p_matrix, e_matrix


def check_is_matrix_abnormal(det):
    derivator = (factorial(koshi.matrix_size) * (2 ** (koshi.matrix_size - 1)))
    return min(det) >= 1 / derivator


class MatrixOperation:

    def __init__(self, size, amount):
        self._matrix_size = size
        self._statistic_amount = amount

    @property
    def matrix_size(self):
        return self._matrix_size

    @matrix_size.setter
    def matrix_size(self, value):
        self._matrix_size = value

    @property
    def amount(self):
        return self._statistic_amount

    @amount.setter
    def amount(self, value):
        self._statistic_amount = value

    def generate_permutation_matrices(self) -> List[np.ndarray]:
        matrices = []
        for perm in permutations(range(self._matrix_size)):
            matrix = np.zeros((self._matrix_size, self._matrix_size), dtype=float)
            for row, col in enumerate(perm):
                matrix[row, col] = float(1.0)
            matrices.append(matrix)
        return matrices

    def generate_refraction_matrices(self) -> List[np.ndarray]:
        diag_combinations = product([1.0, -1.0], repeat=self._matrix_size)
        matrices = []
        for combination in diag_combinations:
            matrix = np.diag([float(v) for v in combination])
            matrices.append(matrix)
        return matrices

    def calculate_minor_determinants(self, matrix: np.ndarray) -> list:
        rows, cols = matrix.shape
        max_k = min(rows, cols)
        determinants = []
        for k in range(1, max_k + 1):
            minor = matrix[:k, :k]
            det = np.linalg.det(minor)
            determinants.append(det)
        return determinants

    def get_orthogonal_random_matrix(self) -> np.ndarray:
        random_matrix = self.random_matrix_calculate()
        Q, R = np.linalg.qr(random_matrix.astype(HIGH_PRECISION_DTYPE))

        # Отражаем ортогональную матрицу
        if np.random.rand() > 0.5:
            col = np.random.randint(0, self._matrix_size)
            Q[:, col] *= -1

        return Q

    def random_matrix_calculate(self) -> np.ndarray:
        matrix = np.random.rand(self._matrix_size, self._matrix_size).astype(HIGH_PRECISION_DTYPE)
        matrix *= np.random.randint(-10000, 10000)
        return matrix

    def is_equal(a: HIGH_PRECISION_DTYPE, b: HIGH_PRECISION_DTYPE) -> bool:
        rel_tol = 1e-14
        abs_tol = 1e-14
        return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


koshi = MatrixOperation(3, 100)
