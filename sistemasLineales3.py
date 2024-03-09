from sympy import symbols
from sympy.solvers.solveset import linsolve
from sympy import Matrix

x, y, z = symbols('x y z')
x1,x2,x3 = symbols('x1 x2 x3')

print(linsolve([2*x1 + 2*x2 - 1, -x1 + x2 - 2], (x1, x2)))
#write with matrix
print(linsolve(Matrix(([2, 2, 1], [-1, 1, 2])), (x1, x2)))