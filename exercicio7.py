import math


lista = []
def distancia_euclidiana(lista):
    d = math.sqrt(((lista[1]-lista[0])**2)+((lista[3]-lista[2])**2))
    return d


for i in range(4):
    if i < 2:
        x = float(input(f"informe o valor de x{i+1}: "))
        lista.append(x)
    else:
        y = float(input(f"informe o valor de y{i-1}: "))
        lista.append(y)
print(lista)
resultado = distancia_euclidiana(lista)

print("O resultado da distância eu clidiana é: ", resultado)