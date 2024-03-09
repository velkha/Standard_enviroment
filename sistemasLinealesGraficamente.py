import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x1 = np.linspace(0, 10, 100)
plt.axhline(0, color='black')  # Draw horizontal line at y=0
plt.axvline(0, color='black')  # Draw vertical line at x=0
plt.plot(x1, (3/2)-2*x1, x1, (x1/2)-1, x1, (1-3*x1)/4)
#plt.show()

point1 = np.array([0, 0, 9/2])
normal1 = np.array([1, 1, 2])

point2 = np.array([0, 0, -1/3])3
normal2 = np.array([2, 4, -3])

point3 = np.array([0, 0, 0])
normal3 = np.array([3, 6, -5])
X,Y = np.meshgrid(range(30), range(30))

z1 = (-normal1[0]*X - normal1[1]*Y - 9/2)/normal1[2]
z2 = (-normal2[0]*X - normal2[1]*Y + 1/3)/normal2[2]
z3 = (-normal3[0]*X - normal3[1]*Y)/normal3[2]

fig = plt.figure()
plot3d = fig.add_subplot(111, projection='3d')
plot3d.plot_surface(X,Y,z1, color='blue', alpha=0.5)
plot3d.plot_surface(X,Y,z2, color='yellow', alpha=0.5)
plot3d.plot_surface(X,Y,z3, color='green', alpha=0.5)
plt.show()