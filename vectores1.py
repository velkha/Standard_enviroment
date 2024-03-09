#create a vector with nuympy from 1 to 10
import numpy as np
print("Vector from 1 to 10")
vector = np.arange(1,11)
print(vector)
#create 2 different vectors with numpy and add them
print("Add 2 vectors")
vector1 = np.arange(1,6)
vector2 = np.arange(6,11)
print(vector1)
print(vector2)
print(vector1 + vector2)
#create 2 different vectors with random numbers and add them
print("Random numbers")
vector3 = np.random.randint(1,10,5)
vector4 = np.random.randint(1,10,5)
print(vector3)
print(vector4)
print(vector3 + vector4)
#create 2 differents vectors with numpy and subtract them, choose the numbers and use np.array
print("Subtract 2 vectors")
vector5 = np.array([1,2,3,4,5])
vector6 = np.array([5,4,3,2,1])
print(vector5)
print(vector6)
print(vector5 - vector6)
