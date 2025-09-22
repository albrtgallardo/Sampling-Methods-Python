import matplotlib.pyplot as plt
import numpy as np 
from math import *

from scipy.integrate import simpson

def g(x):
    x_leng = len(x)
    
    exp_arg = 0
    cos_arg = 0
    for i in range(x_leng):
        exp_arg +=  x[i]**2

    for j in range(x_leng - 1):
        cos_arg += x[j] * x[j+1]
  
    cos_arg += x[-1] * x[0]
    
    resultado = np.exp(-exp_arg) * np.cos(cos_arg)**2
    return resultado

#para el simpson de i dimension
def g1d(x):
    return g([x])   


if __name__ == "__main__":
    comb = [1,2,3,5,10]

    # --- Metodo de Simpson ---
    print("Metodo de Simpson")
    x = np.linspace(-1, 1, 101)
    y = g1d(x)

    I = simpson(y, x)
    print("Integral con Simpson compuesto:", I)

    # --- Uniform sampling ---
    print("\nMetodo de Uniform Sampling")
    N_US = int(input("El valor de N: "))
    
    for n in comb:
        valores = 0
        valores2 = 0 

        for k in range(N_US):
            x_rand_list = np.random.uniform(-1.0, 1.0, size=n)
            valores += g(x_rand_list)
            valores2 += g(x_rand_list)**2
            
        solucion_US = valores / N_US * (2**n)
        
        error2_US = valores2 / N_US - (valores / N_US)**2
        error_US = np.sqrt(error2_US / N_US) * (2**n)
        
        print(f"n={n}, Aproximacion={solucion_US:.6f}, Error={error_US:.6f}")


    # --- Hit and miss --- 
    print("\nMetodo de Hit and Miss")
    N_HNM = int(input("El valor de N: "))
    
    for n in comb:
        x_rand_list = []
        contador = 0
        
        for k in range(N_HNM):
            x_rand_list = np.random.uniform(-1.0, 1.0, size=n)
            y = np.random.rand()
            if y <= g(x_rand_list):
                contador += 1 
        
        solucion_HNM = contador / N_HNM * (2**n)
        error_HNM = np.sqrt((contador/N_HNM)*(1 - contador/N_HNM)/N_HNM) * (2**n)

        print(f"n = {n} -> Aproximacion = {solucion_HNM:.6f}. Error = {error_HNM:.6f}")

