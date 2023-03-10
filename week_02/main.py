import numpy as np
from collections.abc import Iterable

#
def transpose(mat):#sf
    if not isinstance(mat, np.ndarray):
        return None
    return np.transpose(mat)


def product(mat_a, mat_b):
    if mat_a.shape == mat_b.shape:
        return np.dot(mat_a, mat_b), np.multiply(mat_a, mat_b)
    elif len(mat_a[0]) == len(mat_b):
        return np.dot(mat_a, mat_b)
    else:
        return "Khong co tich ma tran"


def replace_col(mat, col_ind):
    for row_ind in range(len(mat)):
        mat[row_ind][col_ind] = 1
    return mat


if __name__ == "__main__":
    print(product(np.array([[1, 2, 3], [4, 5, 6],[2,3,4]]), np.array([[9, 10,12], [11, 12,14]])))

