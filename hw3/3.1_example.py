from matrix import Matrix
import numpy as np

if __name__ == "__main__":
    # Set the seed
    np.random.seed(0)

    # Создаем две матрицы
    matrix1_np = np.random.randint(0, 10, (10, 10))
    matrix1 = matrix1_np.tolist()
    matrix1 = Matrix(matrix1)

    matrix2_np = np.random.randint(0, 10, (10, 10)) 
    matrix2 = matrix2_np.tolist()
    matrix2 = Matrix(matrix2)

    print("\nМатрица 1:")
    print(matrix1)
    print("\nМатрица 2:")
    print(matrix2)

    print("\nПоэлементное сложение матриц:")
    print("Matrix module")
    element_wise_sum = matrix1 + matrix2
    print(element_wise_sum)
    element_wise_sum.write_to_file('hw3/artifacts/3.1/matrix+.txt')
    
    print("Numpy")
    print(matrix1_np + matrix2_np)

    print("\nПоэлементное умножение матриц:")
    print("Matrix module")
    element_wise_prod = matrix1 * matrix2
    print(element_wise_prod)
    element_wise_prod.write_to_file('hw3/artifacts/3.1/matrix*.txt')
    
    print("Numpy")
    print(matrix1_np * matrix2_np)

    print("\nУмножение матриц:")
    print("Matrix module")
    matrix_prod = matrix1 @ matrix2
    print(matrix_prod)
    matrix_prod.write_to_file('hw3/artifacts/3.1/matrix@.txt')
    
    print("Numpy")
    print(matrix1_np @ matrix2_np)
