class Matrix:
    """
    A class representing a matrix.

    Attributes
    ----------
    matrix : list of list
        A 2D list representing the matrix in numpy.array.tolist() style.
    rows : int
        The number of rows in the matrix.
    cols : int
        The number of columns in the matrix.
    """

    def __init__(self, matrix: list) -> None:
        """
        Initialize a Matrix object.

        Parameters
        ----------
        matrix : list of list
            A 2D list representing the matrix.

        """
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __add__(self, other: "Matrix") -> "Matrix":
        """
        Add two matrices by element-wise way.

        Parameters
        ----------
        other : Matrix
            The matrix to add to the current matrix.

        Returns
        -------
        Matrix
            The result of the addition.

        Raises
        ------
        ValueError
            If the matrices do not have the same number of rows and columns.

        """
        if self.rows != other.rows or self.cols != other.cols:
            message = "The matrices must have the same number of rows and columns for addition"
            raise ValueError()

        result = []
        for i in range(self.rows):
            result.append([])
            for j in range(self.cols):
                elem = self.matrix[i][j] + other.matrix[i][j]
                result[i].append(elem)

        return Matrix(result)

    def __mul__(self, other: "Matrix") -> "Matrix":
        """
        Multiply two matrices element-wise.

        Parameters
        ----------
        other : Matrix
            The matrix to multiply with the current matrix.

        Returns
        -------
        Matrix
            The result of the multiplication.

        Raises
        ------
        ValueError
            If the matrices do not have the same dimensions.

        """
        if self.rows != other.rows or self.cols != other.cols:
            message = "The matrices must have the same number of rows and columns for addition"
            raise ValueError()

        result = []
        for i in range(self.rows):
            result.append([])
            for j in range(self.cols):
                elem = self.matrix[i][j] * other.matrix[i][j]
                result[i].append(elem)

        return Matrix(result)

    def __matmul__(self, other: "Matrix") -> "Matrix":
        """
        Perform matrix multiplication.

        Parameters
        ----------
        other : Matrix
            The matrix to multiply with the current matrix.

        Returns
        -------
        Matrix
            The result of the matrix multiplication.

        Raises
        ------
        ValueError
            If the number of columns of the first matrix does not match the number of rows of the second matrix.

        """
        if self.cols != other.rows:
            message = (
                "The number of columns of the first matrix must match the number of rows",
                "of the second matrix for multiplication",
            )
            raise ValueError()

        result = []
        for i in range(self.rows):
            result.append([])
            for j in range(self.cols):
                elem = self.get_matrix_dot_product_elem(self, other, i, j)
                result[i].append(elem)

        return Matrix(result)

    @staticmethod
    def get_matrix_dot_product_elem(matrix1, matrix2, i, j):
        """
        Calculate the dot product of the i-th row of matrix1 with the j-th column of matrix2.

        Parameters
        ----------
        matrix1 : object
            The first input matrix. It should have a `matrix` attribute that is a 2D list.
        matrix2 : object
            The second input matrix. It should have a `matrix` attribute that is a 2D list.
        i : int
            The index of the row in `matrix1` to be used in the dot product calculation.
        j : int
            The index of the column in `matrix2` to be used in the dot product calculation.

        Returns
        -------
        float
            The dot product of the i-th row of `matrix1` and the j-th column of `matrix2`.

        Examples
        --------
        >>> matrix1 = Matrix([[1, 2], [3, 4]])
        >>> matrix2 = Matrix([[5, 6], [7, 8]])
        >>> Matrix.get_matrix_dot_product_elem(matrix1, matrix2, 0, 0)
        19
        """
        elem_ij = 0
        for k in range(len(matrix1.matrix[i])):
            elem_ij += matrix1.matrix[i][k] * matrix2.matrix[k][j]
        return elem_ij

    def __str__(self):
        """
        Return a string representation of the matrix.

        Returns
        -------
        str
            A string representation of the matrix, with rows separated
            by newlines and elements within each row separated by tabs.
        """
        return "\n".join(["\t".join(map(str, row)) for row in self.matrix])

    def write_to_file(self, path_to_file):
        with open(path_to_file, "w") as file:
            text_of_matrix = str(self)
            file.write(text_of_matrix)
