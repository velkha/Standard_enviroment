#matrix operations
import numpy as np
import matplotlib.pyplot as plt
import math

#matrix addition
def matrix_addition(a, b):
    c = np.add(a, b)
    return c

#matrix subtraction
def matrix_subtraction(a, b):
    c = np.subtract(a, b)
    return c

#matrix multiplication
def matrix_multiplication(a, b):
    c = np.dot(a, b)
    return c


#matrix transpose
def matrix_transpose(a):
    c = np.transpose(a)
    return c

#matrix inverse
def matrix_inverse(a):
    c = np.linalg.inv(a)
    return c

#matrix trace
def matrix_trace(a):
    c = np.trace(a)
    return c

#matrix determinant
def matrix_determinant(a):
    c = np.linalg.det(a)
    return c

#matrix rank
def matrix_rank(a):
    c = np.linalg.matrix_rank(a)
    return c

#matrix power
def matrix_power(a, b):
    c = np.linalg.matrix_power(a, b)
    return c

#matrix eigenvalues
def matrix_eigenvalues(a):
    c = np.linalg.eigvals(a)
    return c

#matrix eigenvectors
def matrix_eigenvectors(a):
    c = np.linalg.eig(a)
    return c

#matrix singular value decomposition
def matrix_svd(a):
    c = np.linalg.svd(a)
    return c

#matrix norm
def matrix_norm(a):
    c = np.linalg.norm(a)
    return c

#generate an exdamp0le matrix in np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

#matrix addition
print("Matrix Addition")
print(matrix_addition(a, b))

#matrix subtraction
print("Matrix Subtraction")
print(matrix_subtraction(a, b))

#matrix multiplication
print("Matrix Multiplication")
print(matrix_multiplication(a, b))

#matrix transpose
print("Matrix Transpose")
print(matrix_transpose(a))

#matrix inverse
print("Matrix Inverse")
print(matrix_inverse(a))

#matrix trace
print("Matrix Trace")
print(matrix_trace(a))

#matrix determinant
print("Matrix Determinant")
print(matrix_determinant(a))

#matrix rank
print("Matrix Rank")
print(matrix_rank(a))

#matrix power
print("Matrix Power")
print(matrix_power(a, 2))

#matrix eigenvalues
print("Matrix Eigenvalues")
print(matrix_eigenvalues(a))

#matrix eigenvectors
print("Matrix Eigenvectors")
print(matrix_eigenvectors(a))

#matrix singular value decomposition
print("Matrix SVD")
print(matrix_svd(a))

#matrix norm
print("Matrix Norm")
print(matrix_norm(a))

#method to save all the method resoults in a file
def save_results():
    f = open("results.txt", "w")
    f.write("Matrix Addition\n")
    f.write(str(matrix_addition(a, b)) + "\n")
    f.write("Matrix Subtraction\n")
    f.write(str(matrix_subtraction(a, b)) + "\n")
    f.write("Matrix Multiplication\n")
    f.write(str(matrix_multiplication(a, b)) + "\n")
    f.write("Matrix Transpose\n")
    f.write(str(matrix_transpose(a)) + "\n")
    f.write("Matrix Inverse\n")
    f.write(str(matrix_inverse(a)) + "\n")
    f.write("Matrix Trace\n")
    f.write(str(matrix_trace(a)) + "\n")
    f.write("Matrix Determinant\n")
    f.write(str(matrix_determinant(a)) + "\n")
    f.write("Matrix Rank\n")
    f.write(str(matrix_rank(a)) + "\n")
    f.write("Matrix Power\n")
    f.write(str(matrix_power(a, 2)) + "\n")
    f.write("Matrix Eigenvalues\n")
    f.write(str(matrix_eigenvalues(a)) + "\n")
    f.write("Matrix Eigenvectors\n")
    f.write(str(matrix_eigenvectors(a)) + "\n")
    f.write("Matrix SVD\n")
    f.write(str(matrix_svd(a)) + "\n")
    f.write("Matrix Norm\n")
    f.write(str(matrix_norm(a)) + "\n")
    f.close()

#save_results()
save_results()