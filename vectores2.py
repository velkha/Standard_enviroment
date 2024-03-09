#create 2 vectors with numpy, choose the numbers and use np.array, then make the scalar product and the norm
import numpy as np
print("Scalar product and norm")
vector7 = np.array([0,3,-1,3,5])
vector8 = np.array([1,2,3,-1,0])
vector9 = np.array([1,2,0,3,-1,1])
print(vector7)
print(vector8)
print(np.dot(vector7,vector8))
print(np.linalg.norm(vector7))

def productoScalar(vector1,vector2):
    if len(vector1) == len(vector2):
        producto = 0
        for i in range(len(vector1)):
            producto += vector1[i] * vector2[i]
        return producto
    else:
        return "Los vectores no tienen la misma longitud"

def norma(vector):
    suma = 0
    for i in range(len(vector)):
        suma += vector[i]**2
    return suma**0.5

print("Scalar product and norm")
print(productoScalar(vector7,vector8))
print(np.linalg.norm(vector7))
print(norma(vector7))
print(np.linalg.norm(vector9))
print(norma(vector9))