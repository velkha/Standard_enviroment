#calculate distance of 2 vectors with numpy
import numpy as np
import math
def distance(vector1,vector2):
    if len(vector1) == len(vector2):
        return np.linalg.norm(vector1 - vector2)
    else:
        return "Los vectores no tienen la misma longitud"
def productoScalar(vector1,vector2):
    if len(vector1) == len(vector2):
        producto = 0
        for i in range(len(vector1)):
            producto += vector1[i] * vector2[i]
        return producto
    else:
        return "Los vectores no tienen la misma longitud"

print("Distance")
vector10 = np.array([0,3,-1,3,5])
vector11 = np.array([1,2,3,-1,0])
print(vector10)
print(vector11)
print(distance(vector10,vector11))

#anglerad between 2 vectors
def angleRad(vector1,vector2):
    if len(vector1) == len(vector2):
        return math.acos(productoScalar(vector1,vector2)/(np.linalg.norm(vector1)*np.linalg.norm(vector2)))
    else:
        return "Los vectores no tienen la misma longitud"

def radiansToDegrees(radians):
    return radians*180/math.pi

print("Angle in radians")
print(vector10)
print(vector11)
print(angleRad(vector10,vector11))
print("Angle in degrees")
print(radiansToDegrees(angleRad(vector10,vector11)))