import os

import numpy as np
from matrix import FunctionalArithmeticHashMatrix, write_text_to_file

if __name__ == "__main__":
    # Set path to store artifacts
    artifacts_folder_path = "hw3/artifacts/3.3"

    # Создаем матрицы
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    C = [[2, 1], [4, 3]]
    D = [[5, 6], [7, 8]]

    A = FunctionalArithmeticHashMatrix(A)
    B = FunctionalArithmeticHashMatrix(B)
    C = FunctionalArithmeticHashMatrix(C)
    D = FunctionalArithmeticHashMatrix(D)

    # Записываем матрицы в файлы
    file_path = os.path.join(artifacts_folder_path, "A.txt")
    A.write_to_file(file_path)

    file_path = os.path.join(artifacts_folder_path, "B.txt")
    B.write_to_file(file_path)

    file_path = os.path.join(artifacts_folder_path, "C.txt")
    C.write_to_file(file_path)

    file_path = os.path.join(artifacts_folder_path, "D.txt")
    D.write_to_file(file_path)

    print("\nУмножение матриц A и B:")
    AB = A @ B
    print(AB)
    file_path = os.path.join(artifacts_folder_path, "AB.txt")
    AB.write_to_file(file_path)

    print("\nУмножение матриц C и D без кэширования:")
    # Сбросим cache, чтобы вынудить произвести честный расчет произведения
    # матриц C и D несмотря на коллизию хэшей матриц.
    # Иначе получим cache в виде матрицы AB
    FunctionalArithmeticHashMatrix.clear_cache()

    CD = C @ D
    print(CD)
    file_path = os.path.join(artifacts_folder_path, "CD.txt")
    CD.write_to_file(file_path)

    print("\nХэш матриц AB и CD")
    # для нашей hash функции hash(AB) == hash(CD)
    CD_hash = hash(AB)
    print(CD_hash)
    file_path = os.path.join(artifacts_folder_path, "hash.txt")
    write_text_to_file(str(CD_hash), file_path)
