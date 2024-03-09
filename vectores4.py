#octogonal proyedction in py
import numpy as np
import math
def productoScalar(vector1,vector2):
    if len(vector1) == len(vector2):
        producto = 0
        for i in range(len(vector1)):
            producto += vector1[i] * vector2[i]
        return producto
    else:
        return "Los vectores no tienen la misma longitud"
def octProyection(vector1,vector2):
    if len(vector1) == len(vector2):
        #pow is the power function, potencia
        return (productoScalar(u,v)/pow(np.linalg.norm(u),2))*u
    else:
        return "Los vectores no tienen la misma longitud"
    
u = np.array([3,1])
v = np.array([1,2])

print("Octogonal proyection")
print(u)
print(v)
print(octProyection(u,v))