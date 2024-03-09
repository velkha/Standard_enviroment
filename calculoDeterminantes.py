#calculo de determinante (como curiosidad esto es una operacion recursiva, por lo que normalmente
# utilizara recursividad por detras entre otras cosas)
import numpy as np
#init np.array
A = np.array([[1, 2, 3], [0, -1, 5], [10, 2, -5]])
print("Determinante de A: ", np.linalg.det(A))