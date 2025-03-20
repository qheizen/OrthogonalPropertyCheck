import numpy as np
from itertools import permutations, product
from typing import List

np.set_printoptions(precision=30, linewidth=200)

HIGH_PRECISION_DTYPE = np.float64


def generate_permutation_matrices() -> List[np.ndarray]:
    matrices = []
    for perm in permutations(range(3)):
        matrix = np.zeros((3, 3), dtype=HIGH_PRECISION_DTYPE)
        for row, col in enumerate(perm):
            matrix[row, col] = HIGH_PRECISION_DTYPE(1.0)
        matrices.append(matrix)
    return matrices


def generate_diagonal_matrices() -> List[np.ndarray]:
    diag_combinations = product([1.0, -1.0], repeat=3)
    matrices = []
    for combination in diag_combinations:
        matrix = np.diag([HIGH_PRECISION_DTYPE(v) for v in combination])
        matrices.append(matrix)
    return matrices


def random_matrix_calculate(size: int = 3) -> np.ndarray:
    matrix = np.random.rand(size, size).astype(HIGH_PRECISION_DTYPE)
    matrix *= np.random.randint(0,10000)
    return matrix


def calculate_determinant(matrix: np.ndarray) -> list:
    submatrix = np.array([[matrix[1, 1], matrix[1, 2]], [matrix[2, 1], matrix[2, 2]]], dtype=HIGH_PRECISION_DTYPE)
    submatrix1 = np.array([[matrix[1, 0], matrix[1, 2]], [matrix[2, 0], matrix[2, 2]]], dtype=HIGH_PRECISION_DTYPE)
    submatrix2 = np.array([[matrix[1, 0], matrix[1, 1]], [matrix[2, 0], matrix[2, 1]]], dtype=HIGH_PRECISION_DTYPE)
    return [np.linalg.det(submatrix), np.linalg.det(submatrix1), np.linalg.det(submatrix2)]


def is_equal(a: HIGH_PRECISION_DTYPE, b: HIGH_PRECISION_DTYPE) -> bool:
    rel_tol = 1e-14
    abs_tol = 1e-14
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def get_orthogonal_random_matrix() -> np.ndarray:
    random_matrix = random_matrix_calculate()
    Q, R = np.linalg.qr(random_matrix.astype(HIGH_PRECISION_DTYPE))
    det = np.linalg.det(Q)
    if det < 0:
        Q[:, 0] *= -1
    return Q


def matrix_product_combinations(matrix_list1: List[np.ndarray], matrix_list2: List[np.ndarray]) -> List[np.ndarray]:
    products = []
    for a in matrix_list1:
        for b in matrix_list2:
            product = np.dot(a.astype(HIGH_PRECISION_DTYPE), b.astype(HIGH_PRECISION_DTYPE))
            products.append(product)
    return products


def get_all_variation_transitive() -> List[np.ndarray]:
    diagonal_matrices = generate_diagonal_matrices()
    permutation_matrices = generate_permutation_matrices()
    return matrix_product_combinations(diagonal_matrices, permutation_matrices)
