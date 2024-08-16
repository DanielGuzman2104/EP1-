import numpy as np


matriz_1 = np.array([[22, 12], [22, 11]])
matriz_2 = np.array([[34, 4], [12, 9]])

print("")
suma = matriz_1 + matriz_2
print("Suma: ")
print(suma)

print("")
resta = matriz_1 - matriz_2
print("Resta:")
print(resta)

print("")
multiplicacion = np.dot(matriz_1, matriz_2)
print("Multiplicacion:") 
print(multiplicacion)

print("")
division = matriz_1 / matriz_2
print("División (elemento a elemento):")
print(division)
