import matplotlib.pyplot as plt
import numpy as np 
from math import *


def f(x):
    return(sqrt(1 - x**2))

if __name__ == "__main__":

    print("Método de Hit and Miss")
    max_rang = int(input("Hasta qué número de iteración 10^x: "))
    N = 1
    valor_exacto = pi / 4

    valores_N = []
    errores_N = []

    for i in range(max_rang):  
        N *= 10
        contador = 0
        for _ in range(N):
            x = np.random.rand()
            y = np.random.rand()
            if y <= f(x):
                contador += 1
        aproximacion = contador / N
        error = abs(aproximacion - valor_exacto)
        print(f"N = {N} -> Aproximación = {aproximacion:.6f}, Error = {error:.6f}")
        
        valores_N.append(N)
        errores_N.append(error)

    

    plt.plot(valores_N, errores_N, marker ='o')

    # Escalas logarítmicas
    plt.xscale("log")   # eje X log
    plt.yscale("log")   # eje Y log

    # Etiquetas y título
    plt.xlabel('Numero de iteraciones (log)')
    plt.ylabel('Error absoluto (log)')
    plt.title('Errores del metodo hit and miss en funcion del numero de iteraciones')
    #plt.grid(True, which="both")  # grid también en la escala log
    plt.show()


