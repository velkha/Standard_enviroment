import sympy as sp
from sympy import linsolve
from sympy import Matrix

x, y, z = sp.symbols('x y z')


r = linsolve([x + y - z - 2, x - y + z - 1, 3*x + y - z - 5], (x, y, z))
print(r)
r2 = linsolve(Matrix(([1, 1, -1, 2], [1,-1, 1, 1], [3,1,-1,5])), (x, y, z))
print(r2)

AB = Matrix(([1, 1, -1, 2], [1,-1, 1, 1], [3,1,-1,5]))
A = AB[:, :-1] #todas las filas de todas las columnas menos la ultima
B = AB[:, -1] #todas las filas de la ultima columna
system = A, B
r3 = linsolve(system, x, y, z)
print(r3)