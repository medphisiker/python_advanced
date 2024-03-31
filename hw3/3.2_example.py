import os

import numpy as np
from matrix import FunctionalArithmeticMatrix

if __name__ == "__main__":
    # Set the seed
    np.random.seed(0)

    # Set path to store artifacts
    artifacts_folder_path = "hw3/artifacts/3.2"

    # Создаем две матрицы
    matrix1_np = np.random.randint(0, 10, (10, 10))
    matrix1 = matrix1_np.tolist()
    matrix1 = FunctionalArithmeticMatrix(matrix1)

    matrix2_np = np.random.randint(0, 10, (10, 10))
    matrix2 = matrix2_np.tolist()
    matrix2 = FunctionalArithmeticMatrix(matrix2)

    print("\nМатрица 1:")
    print(matrix1)
    print("\nМатрица 2:")
    print(matrix2)

    print("\nПоэлементное сложение матриц:")
    print("Matrix module")
    element_wise_sum = matrix1 + matrix2
    print(element_wise_sum)
    file_path = os.path.join(artifacts_folder_path, "matrix+.txt")
    element_wise_sum.write_to_file(file_path)
    print("Numpy")
    print(matrix1_np + matrix2_np)

    print("\nПоэлементное умножение матриц:")
    print("Matrix module")
    element_wise_prod = matrix1 * matrix2
    print(element_wise_prod)
    file_path = os.path.join(artifacts_folder_path, "matrix*.txt")
    element_wise_prod.write_to_file(file_path)
    print("Numpy")
    print(matrix1_np * matrix2_np)

    print("\nУмножение матриц:")
    print("Matrix module")
    matrix_prod = matrix1 @ matrix2
    print(matrix_prod)
    file_path = os.path.join(artifacts_folder_path, "matrix@.txt")
    matrix_prod.write_to_file(file_path)
    print("Numpy")
    print(matrix1_np @ matrix2_np)
