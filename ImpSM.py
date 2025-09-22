import matplotlib.pyplot as plt 
import numpy as np 
from math import * 


def g(x):
    return np.sqrt(x) * np.cos(x)

if __name__ == "__main__":
    print("-----Metodo de Importance Sampling-----\n")
    N = int(input("Selecciona un valor para N: "))
    sumatorio = 0
    sumatorio2 = 0
    
    for i in range(N):
        x_rand = -np.log(np.random.rand())
        sumatorio += g(x_rand)
        sumatorio2 += g(x_rand)**2

    solucion = sumatorio / N
    error2 = sumatorio2 / N - (sumatorio / N)**2 
    error = np.sqrt(error2 / N)

    print(f"Aproximacion = {solucion:.6f}\nError = {error:.6f}")
