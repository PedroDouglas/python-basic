# METODOS DE LISTA

lista = [1, 3, 12, 8, 2]

## append

print('Antes do append',lista)

lista.append(3)

print('Depois do append',lista)

## insert

lista.insert(0 , -1)

print('Depois do insert', lista)

##  extend (juntar duas listas)

lista2= [1,2,3,4]

lista.extend(lista2)

print('Depois do extend',lista)

## pop

lista.pop()

print('Depois do pop ', lista)

lista.pop(0)
print('Depois do pop ', lista)


## remove

lista.remove(3) ## ele remove o primeiro elemento que ele encontra
print('Depois do remove ', lista)

## count
print ('Quantidade de números dois na lista: ',lista.count(2))

## index
print('Qual o index do elemento 8', lista.index(8))

## sort
lista.sort()
print('Lista após o sort',lista)

lista.sort(reverse=True) # ordem decrescente

print('Lista após o sort descrecente',lista)

## FUNÇÕES PARA LISTAS

#len(tamanho)
print('tamanho da lista',len(lista))

#sum
print('soma total dos elementos da lista', sum(lista))

#min
print('menor valor da lista', min(lista))

#max
print('maior valor da lista', max(lista))
