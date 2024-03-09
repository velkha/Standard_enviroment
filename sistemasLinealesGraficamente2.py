#sistemas compatibles indeterminados
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
x = np.linspace(-10, 10, 100)
plt.axhline(0, color='black')  # Draw horizontal line at y=0
plt.axvline(0, color='black')  # Draw vertical line at x=0

A = np.array([[1, 1, -1], [1,-1, 1], [3,1,-1]])
B = np.array([ [-2], [1], [5]])
AB = np.concatenate((A, B), axis=1)
#print ranks
print(np.linalg.matrix_rank(A))
print(np.linalg.matrix_rank(AB))
#print equal
print(np.linalg.matrix_rank(A) == np.linalg.matrix_rank(AB))

#represent in 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X,Y = np.meshgrid(range(-30,30),range(30))
#get the points from A array and the point from B array
point1 = np.array([0, 0, -2])
normal1 = np.array([1, 1, -1])
point2 = np.array([0, 0, 1])
normal2 = np.array([1, -1, 1])
point3 = np.array([0, 0, 5])
normal3 = np.array([3, 1, -1])
#calculate the z values
d1 = -2
d2 = -1
d3 = -5
Z1 = (-normal1[0]*X - normal1[1]*Y - d1)/normal1[2]
Z2 = (-normal2[0]*X - normal2[1]*Y - d2)/normal2[2]
Z3 = (-normal3[0]*X - normal3[1]*Y - d3)/normal3[2]
#plot the surfaces
ax.plot_surface(X,Y,Z1, color='blue', alpha=0.5)
ax.plot_surface(X,Y,Z2, color='yellow', alpha=0.5)
ax.plot_surface(X,Y,Z3, color='green', alpha=0.5)
plt.show()

