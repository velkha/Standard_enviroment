#calculate rank of A and A|B
import numpy as np
A = np.array([[1, 1, 2], [2, 4, -3], [3, 6, -5]])
B = np.array([[9], [1], [0]])
AB = np.concatenate((A, B), axis=1)
print("Rank of A: ", np.linalg.matrix_rank(A))
print("Rank of AB: ", np.linalg.matrix_rank(AB))