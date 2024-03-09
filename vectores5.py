#vectorial product and mixed product
import numpy as np
import math

def productoVectorial(x,y):
    if len(x) == len(y) == 3:
        return np.cross(x,y)
        #return np.array([x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0]])
    else:
        return "Los vectores no tienen la misma longitud"

def productoMixto(x,y,z):
    if len(x) == len(y) == len(z) == 3:
        return np.dot(x,np.cross(y,z))
        #return np.linalg.det(np.array([x,y,z]))
    else:
        return "Los vectores no tienen la misma longitud"
    
print("Vectorial product")
x = np.array([1,2,3])
y = np.array([0,-1,1])
print(x)    
print(y)
print(productoVectorial(x,y))
print("Mixed product")
z = np.array([2,0,-3])
print(x)
print(y)
print(z)
print(productoMixto(x,y,z))