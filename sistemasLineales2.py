import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,2],[3,0]])
B = np.array([[9,6],[15,0]])

#inverse of A
A_inv = np.linalg.inv(A)
print(A_inv.dot(B))

A = np.array([[1, 2], [0, 3], [ 0, 4]])
B = np.array([[1], [2], [3]])
AB = np.concatenate((A, B), axis=1)
print("Rank of A: ", np.linalg.matrix_rank(A))
print("Rank of AB: ", np.linalg.matrix_rank(AB))