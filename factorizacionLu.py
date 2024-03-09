#factoritation LU 
#el uso de la factorizacionn con lu_factor es mas eficiente que linalg dado que 
#no guarda los datos en 2 matrices sino que guarda los datos en una sola matriz LU, evitando asi carga excesiva
import numpy as np
import scipy
from scipy.linalg import lu

# Your matrix
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Perform LU factorization
P, L, U = lu(A)

# Print the results
print("P:\n", P)
print("L:\n", L)
print("U:\n", U)
# Perform LU factorization using lu_factor()
lu, piv = scipy.linalg.lu_factor(A)

# Extract the permutation matrix P
P = np.eye(len(A))
P = P[piv]

# Extract the lower triangular matrix L
L = np.tril(lu, k=-1) + np.eye(len(A))

# Extract the upper triangular matrix U
U = np.triu(lu)

# Print the results
print("P:\n", P)
print("L:\n", L)
print("U:\n", U)