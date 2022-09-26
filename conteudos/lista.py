# Listas

## antes
nota1 = 7.9
nota2 = 8.9
nota3 = 9.5

##  Com lista
notas = [7.9, 9.7, 8.5]

## Criando lista
lista = []
lista = list() ##metodo para converter em lista
lista = [9,'b', 7.8 , True] ## aceita varios tipos de variavel
lista = [2,[2,8]] ## lista de lista

## Indexação e Slices (fatiamentos)
lista = [10, 'pedro', 3.1415, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1]) #acessando o último elemento da lista

## Slices
lista = [10,50,20,40,60,30,20]

print(lista[0:3])

print(lista[0:6:2])

## interações com FOR

## 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print (elemento)

## 2. Utilizando os indices

print('Comprimento da lista: ', len(lista))