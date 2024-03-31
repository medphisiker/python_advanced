import numpy as np


def write_text_to_file(text, path_to_file):
    """Writes a given text to a text file at the specified path.

    Parameters
    ----------
    text : str
        The text to be written to the file.
    path_to_file : str
        The path to the file where the text will be written.

    Notes
    -----
    This function opens the file in write mode ('w') and writes the provided text to it.
    If the file already exists, its contents will be overwritten.
    """
    with open(path_to_file, "w") as file:
        text_of_matrix = text
        file.write(text_of_matrix)


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
            raise ValueError(message)

        result = []
        for i in range(self.rows):
            result.append([])
            for j in range(self.cols):
                elem = self.matrix[i][j] + other.matrix[i][j]
                result[i].append(elem)

        return type(self)(result)

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

        return type(self)(result)

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
                "The number of columns of the first matrix must match the number of rows"
                " of the second matrix for multiplication"
            )
            raise ValueError(message)

        result = []
        for i in range(self.rows):
            result.append([])
            for j in range(other.cols):
                elem = self.get_matrix_dot_product_elem(self, other, i, j)
                result[i].append(elem)

        return type(self)(result)

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


class StrMixin:
    """
    Mixin class for string representation of matrix-like objects.

    This mixin provides a `__str__` method to convert the matrix into a
    string representation, where each row of the matrix is joined by a newline
    character (`\n`), and each element within a row is joined by a tab character
    (`\t`).

    Attributes
    ----------
    matrix : list of list
        The matrix to be represented as a string. Each inner list represents
        a row of the matrix.

    Methods
    -------
    __str__()
        Returns a string representation of the matrix.
    """

    def __str__(self):
        """
        Returns a string representation of the matrix.

        This method iterates over each row in the matrix, converts each element
        to a string, joins them with a tab character (`\t`), and then joins all
        rows with a newline character (`\n`).

        Returns
        -------
        str
            The string representation of the matrix.
        """
        return "\n".join(["\t".join(map(str, row)) for row in self.matrix])


class ToTxtFileMixin:
    """
    Mixin class for writing the string representation of an object to a text file.

    This class provides a method to write the string representation of an object
    to a specified file path. It is intended to be used as a mixin class,
    allowing other classes to inherit its functionality.

    Methods
    -------
    write_to_file(path_to_file)
        Writes the string representation of the object to a file.
    """

    def write_to_file(self, path_to_file):
        """
        Writes the string representation of the object to a file.

        Parameters
        ----------
        path_to_file : str
            The path to the file where the string representation of the object
            will be written.

        Returns
        -------
        None

        Notes
        -----
        The method opens the file in write mode, converts the object to a string,
        and writes this string to the file.
        """
        text_of_matrix = str(self)
        write_text_to_file(text_of_matrix, path_to_file)


class SubMixin:
    """
    A mixin class for subtraction operation on matrices.

    This class provides a method to perform element-wise subtraction of two matrices.
    The subtraction operation is performed using NumPy arrays for efficient computation.

    Methods
    -------
    __sub__(other)
        Performs element-wise subtraction of the current matrix with another matrix.
    """

    def __sub__(self, other):
        """
        Performs element-wise division of the current matrix with another matrix.

        Parameters
        ----------
        other : Matrix class and any classes that inherit from it.
            The other matrix to subtract the current matrix by.

        Returns
        -------
        Instance of object of Matrix
            A new instance of the class with the result of the matrix subtraction.

        Raises
        ------
        ValueError
            If the shapes of the matrices are not compatible for element-wise subtraction.
        """
        matrix1 = np.array(self.matrix)
        matrix2 = np.array(other.matrix)
        result = matrix1 - matrix2
        result = type(self)(result.tolist())
        return result


class DivMixin:
    """
    A mixin class for division operation on matrices.

    This class provides a method to perform element-wise division of two matrices.
    The division operation is performed using NumPy arrays for efficient computation.

    Methods
    -------
    __truediv__(other)
        Performs element-wise division of the current matrix with another matrix.
    """

    def __truediv__(self, other):
        """
        Performs element-wise division of the current matrix with another matrix.

        Parameters
        ----------
        other : Matrix class and any classes that inherit from it.
            The other matrix to divide the current matrix by.

        Returns
        -------
        Instance of object of Matrix
            A new instance of the class with the result of the matrix division.

        Raises
        ------
        ValueError
            If the shapes of the matrices are not compatible for element-wise division.
        """
        matrix1 = np.array(self.matrix)
        matrix2 = np.array(other.matrix)
        result = matrix1 / matrix2
        result = type(self)(result.tolist())
        return result


class PropertyMixin:
    """
    A mixin class to add getter and setter to matrix property.
    """

    @property
    def matrix(self):
        """
        Get the matrix property.

        Returns
        -------
        matrix : list of list
            The current matrix a 2D list representing the matrix
            in numpy.array.tolist() style.

        """
        return self._matrix

    @matrix.setter
    def matrix(self, new_matrix):
        """
        Set the matrix property.

        Parameters
        ----------
        new_matrix : list of list
            The new matrix to set a 2D list representing the matrix
            in numpy.array.tolist() style.
        """
        self._matrix = new_matrix


class HashMixin:
    """A mixin class for objects that need a custom hash implementation.

    This class provides a `__hash__` method that computes a hash value
    based on the sum of the elements in the `matrix` attribute, modulo 100000.

    Attributes
    ----------
    matrix : array_like
        The matrix whose elements are used to compute the hash value.

    Methods
    -------
    __hash__()
        Computes and returns the hash value of the object.
    """

    def __hash__(self):
        """
        Computes and returns the hash value of the object.

        The hash value is computed as the sum of the elements in
        the `matrix` attribute, modulo 100000.

        Returns
        -------
        int
            The computed hash value.
        """
        matrix = np.array(self.matrix)
        hash = int(np.sum(matrix) % 100000)
        return hash


class HashMatrix(Matrix, HashMixin):
    """A class representing a matrix with a custom hash implementation.

    This class inherits from both the `Matrix` and `HashMixin` classes,
    providing functionality for matrix operations and a custom hash
    implementation.
    It also includes a caching mechanism for matrix
    multiplication results based on the hash values of the matrices.

    Attributes
    ----------
    _hash : set
        A set used to store the hash values of matrices involved in
        matrix multiplication operations.
    _hash_prod_result : Matrix or None
        A cache for the result of the last matrix multiplication
        operation involving matrices with hash values stored in `_hash`.

    Methods
    -------
    __matmul__(other: Matrix) -> Matrix
        Perform matrix multiplication with caching based on hash values.
    clear_cache()
        Clear the cache for matrix multiplication results.
    """

    _hash = set([])
    _hash_prod_result = None

    def __matmul__(self, other: "Matrix") -> "Matrix":
        """
        Perform matrix multiplication with caching based on hash values.

        This method overrides the `__matmul__` method of the `Matrix` class
        to include caching of matrix multiplication results. If the hash values
        of the two matrices involved in the multiplication are already stored in
        the `_hash` set, and the result of their multiplication is cached in
        `_hash_prod_result`, the cached result is returned instead of
        performing the multiplication again.

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
            If the number of columns of the first matrix does not match
            the number of rows of the second matrix.
        """
        hash1, hash2 = hash(self), hash(other)
        if self._hash_prod_result and hash1 in self._hash and hash2 in self._hash:
            result = HashMatrix._hash_prod_result
        else:
            HashMatrix._hash = set([hash1, hash2])
            result = super().__matmul__(other)
            HashMatrix._hash_prod_result = result

        return result

    @staticmethod
    def clear_cache():
        """Clear the cache for matrix multiplication results.

        This method clears the `_hash_prod_result` attribute, effectively
        removing any cached results of matrix multiplication operations.

        It can be used to avoid hash function collisions.
        """
        HashMatrix._hash_prod_result = None


class ArithmeticMatrix(Matrix, SubMixin, DivMixin):
    """
    A class representing a matrix with arithmetic operations.

    This class inherits from the `Matrix` class and mixes in the `SubMixin` and `DivMixin` classes
    to provide additional functionality for subtraction and division operations.

    Attributes
    ----------
    matrix : list of list
        A 2D list representing the matrix in numpy.array.tolist() style.
    rows : int
        The number of rows in the matrix.
    cols : int
        The number of columns in the matrix.

    Methods
    -------
    __add__(other)
        Add two matrices by element-wise way.
    __mul__(other)
        Multiply two matrices element-wise.
    __matmul__(other)
        Perform matrix multiplication.
    __sub__(other)
        Perform element-wise subtraction of the current matrix with another matrix.
    __truediv__(other)
        Perform element-wise division of the current matrix with another matrix.
    """

    pass


class FunctionalMatrix(Matrix, StrMixin, ToTxtFileMixin):
    """
    A class representing a matrix with functionalities for string representation and file writing.

    This class inherits from the `Matrix` class and mixes in the `StrMixin` and `ToTxtFileMixin` classes
    to provide additional functionality for string representation and writing the matrix to a text file.

    Attributes
    ----------
    matrix : list of list
        A 2D list representing the matrix in numpy.array.tolist() style.
    rows : int
        The number of rows in the matrix.
    cols : int
        The number of columns in the matrix.

    Methods
    -------
    __add__(other)
        Add two matrices by element-wise way.
    __mul__(other)
        Multiply two matrices element-wise.
    __matmul__(other)
        Perform matrix multiplication.
    __str__()
        Returns a string representation of the matrix.
    write_to_file(path_to_file)
        Writes the string representation of the matrix to a file.
    """

    pass


class FunctionalArithmeticMatrix(
    ArithmeticMatrix, StrMixin, ToTxtFileMixin, PropertyMixin
):
    """
    A class representing a matrix with functionalities for arithmetic operations, string representation, file writing
    and for getting and setting `matrix` property.

    This class inherits from the `ArithmeticMatrix` class and mixes in the `StrMixin`, `ToTxtFileMixin` and
    `PropertyMixin` classes to provide additional functionality for arithmetic operations
    (addition, multiplication, subtraction, division), string representation, writing the matrix to a text file and
    getting and setting `matrix` property.

    Attributes
    ----------
    matrix : list of list
        A 2D list representing the matrix in numpy.array.tolist() style.
    rows : int
        The number of rows in the matrix.
    cols : int
        The number of columns in the matrix.

    Methods
    -------
    __add__(other)
        Add two matrices by element-wise way.
    __mul__(other)
        Multiply two matrices element-wise.
    __matmul__(other)
        Perform matrix multiplication.
    __sub__(other)
        Perform element-wise subtraction of the current matrix with another matrix.
    __truediv__(other)
        Perform element-wise division of the current matrix with another matrix.
    __str__()
        Returns a string representation of the matrix.
    write_to_file(path_to_file)
        Writes the string representation of the matrix to a file.
    """

    pass


class ArithmeticHashMatrix(HashMatrix, SubMixin, DivMixin):
    """
    A class representing a matrix with arithmetic operations and a custom hash implementation.

    This class inherits from both the `HashMatrix` and `SubMixin` and `DivMixin` classes,
    providing functionality for matrix operations, subtraction, division, and a custom hash
    implementation. It also includes a caching mechanism for matrix multiplication results
    based on the hash values of the matrices.

    Attributes
    ----------
    matrix : list of list
        A 2D list representing the matrix in numpy.array.tolist() style.
    rows : int
        The number of rows in the matrix.
    cols : int
        The number of columns in the matrix.
    _hash : set
        A set used to store the hash values of matrices involved in
        matrix multiplication operations.
    _hash_prod_result : Matrix or None
        A cache for the result of the last matrix multiplication
        operation involving matrices with hash values stored in `_hash`.

    Methods
    -------
    __add__(other)
        Add two matrices by element-wise way.
    __mul__(other)
        Multiply two matrices element-wise.
    __matmul__(other)
        Perform matrix multiplication with caching based on hash values.
    __sub__(other)
        Perform element-wise subtraction of the current matrix with another matrix.
    __truediv__(other)
        Perform element-wise division of the current matrix with another matrix.
    clear_cache()
        Clear the cache for matrix multiplication results.
    """

    pass


class FunctionalArithmeticHashMatrix(
    ArithmeticHashMatrix, StrMixin, ToTxtFileMixin, PropertyMixin
):
    """
    A class representing a matrix with functionalities for arithmetic operations, string representation, file writing,
    and for getting and setting `matrix` property, along with a custom hash implementation.

    This class inherits from the `ArithmeticHashMatrix` class and mixes in the `StrMixin`, `ToTxtFileMixin`, and
    `PropertyMixin` classes to provide additional functionality for arithmetic operations (addition, multiplication,
    subtraction, division), string representation, writing the matrix to a text file, and getting and setting `matrix`
    property. It also includes a caching mechanism for matrix multiplication results based on the hash values of
    the matrices.

    Attributes
    ----------
    matrix : list of list
        A 2D list representing the matrix in numpy.array.tolist() style.
    rows : int
        The number of rows in the matrix.
    cols : int
        The number of columns in the matrix.
    _hash : set
        A set used to store the hash values of matrices involved in
        matrix multiplication operations.
    _hash_prod_result : Matrix or None
        A cache for the result of the last matrix multiplication
        operation involving matrices with hash values stored in `_hash`.

    Methods
    -------
    __add__(other)
        Add two matrices by element-wise way.
    __mul__(other)
        Multiply two matrices element-wise.
    __matmul__(other)
        Perform matrix multiplication with caching based on hash values.
    __sub__(other)
        Perform element-wise subtraction of the current matrix with another matrix.
    __truediv__(other)
        Perform element-wise division of the current matrix with another matrix.
    clear_cache()
        Clear the cache for matrix multiplication results.
    __str__()
        Returns a string representation of the matrix.
    write_to_file(path_to_file)
        Writes the string representation of the matrix to a file.
    """

    pass
