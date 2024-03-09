import numpy as np

M = np.array([[1, 2], [3, 4]])
N = np.array([[5, 6], [7, 8]])
print(M)
print("Sum single matrix")
print(np.sum(M))
print(np.sum(M, axis=0))
print(np.sum(M, axis=1))

print("Sum two matrix")
print(np.sum([M, N]))

print("Sum two matrix by axis")
print(np.sum([M, N], axis=0))
print(np.sum([M, N], axis=1))

print("Sum by pro")
print(np.prod(M))
print(np.prod(M, axis=0))
print(np.prod(M, axis=1))

print("prod with scalar")
print(np.prod(M, 1))
print(5*M)

print("Prod two matrix")
print("M*N")
print(np.prod([M, N]))
print(M.dot(N))
print(np.dot(M, N))
#el siguiente multiplica elemnto a elemento
print(M*N)
print(M@N)
print("N*M")
print(np.prod([N, M]))
print(N.dot(M))
print(np.dot(N, M))
#el siguiente multiplica elemnto a elemento
print(N*M)
print(N@M)

print("Media mean")
print(np.mean(M))
print(np.mean(M, axis=0))
print(np.mean(M, axis=1))

print("transpose")
print(np.transpose(M))

print("trace")
print(np.trace(M))





