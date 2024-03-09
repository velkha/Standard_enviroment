#use lu_solve to solve the system
# from scipy.linalg import lu_factor, lu_solve
import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Define the matrix A and vector b
A = np.array([[1, 0, -1], [0,1,1,], [-1,-1,2]])
b = np.array([0, 0, 0])

# Perform LU factorization
lu, piv = lu_factor(A)

# Solve the linear system using LU decomposition
x = lu_solve((lu, piv), b)

print("Solution x:", x)