import numpy as np

def add_matrices(matrix1, matrix2):
    """
    Adds two matrices element-wise.
    
    Args:
        matrix1 (np.array): The first input matrix of shape (m, n).
        matrix2 (np.array): The second input matrix of shape (n, m).
    
    Returns:
        np.array: A new matrix that is the result of adding the two given matrices.
    """
    # Ensure the matrices have compatible shapes
    if matrix1.shape != (len(matrix2), len(matrix1[0])):
        raise ValueError("Matrix addition requires compatible shapes. Shape mismatch between matrices.")
    
    # Element-wise summation
    result = np.sum(matrix1, axis=0) + np.sum(matrix2, axis=0)
    return result

# Example usage:
matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
matrix_b = np.array([[7, 8], [9, 10], [11, 12]])

result = add_matrices(matrix_a, matrix_b)
print(result)
