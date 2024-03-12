import numpy as np

# Create a matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Calculate eigenvalues and eigenvectors, valores propios y vectores propios
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Print the results
print("Eigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)
l1 = eigenvalues[0]
v1 = eigenvectors[:,0]

print(np.isclose(np.dot(matrix,v1), l1*v1))