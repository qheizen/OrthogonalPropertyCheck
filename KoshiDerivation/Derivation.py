import numpy as np
from itertools import permutations, product
from typing import List

np.set_printoptions(precision=30, linewidth=200)

HIGH_PRECISION_DTYPE = np.float64
MATRIX_SIZE = 3

def generate_permutation_matrices() -> List[np.ndarray]:
    matrices = []
    for perm in permutations(range(MATRIX_SIZE)):
        matrix = np.zeros((MATRIX_SIZE, MATRIX_SIZE), dtype=HIGH_PRECISION_DTYPE)
        for row, col in enumerate(perm):
            matrix[row, col] = HIGH_PRECISION_DTYPE(1.0)
        matrices.append(matrix)
    return matrices


def generate_refraction_matrices() -> List[np.ndarray]:
    diag_combinations = product([1.0, -1.0], repeat=MATRIX_SIZE)
    matrices = []
    for combination in diag_combinations:
        matrix = np.diag([HIGH_PRECISION_DTYPE(v) for v in combination])
        matrices.append(matrix)
    return matrices


def random_matrix_calculate(size: int = MATRIX_SIZE) -> np.ndarray:
    matrix = np.random.rand(size, size).astype(HIGH_PRECISION_DTYPE)
    matrix *= np.random.randint(0,10000)
    return matrix


def calculate_determinant(matrix: np.ndarray) -> list:
    rows, cols = matrix.shape
    max_k = min(rows, cols)
    determinants = []
    for k in range(1, max_k + 1):
        minor = matrix[:k, :k]
        det = np.linalg.det(minor)
        determinants.append(det)
    return determinants


def is_equal(a: HIGH_PRECISION_DTYPE, b: HIGH_PRECISION_DTYPE) -> bool:
    rel_tol = 1e-14
    abs_tol = 1e-14
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def get_orthogonal_random_matrix() -> np.ndarray:
    random_matrix = random_matrix_calculate(MATRIX_SIZE)
    Q, R = np.linalg.qr(random_matrix.astype(HIGH_PRECISION_DTYPE))
    return Q


def matrix_product_combinations(matrix_list1: List[np.ndarray], matrix_list2: List[np.ndarray]) -> List[np.ndarray]:
    products = []
    for a in matrix_list1:
        for b in matrix_list2:
            product = np.dot(a.astype(HIGH_PRECISION_DTYPE), b.astype(HIGH_PRECISION_DTYPE))
            products.append(product)
    return products


def get_all_variations_of_pe() -> List[np.ndarray]:
    diagonal_matrices = generate_refraction_matrices()
    permutation_matrices = generate_permutation_matrices()
    return matrix_product_combinations(diagonal_matrices, permutation_matrices)
