lista = [1,2,3,4,5,6,7,8,9,10]
print('Lista inicial: ',lista )

print('1. uma lista com os 4 primeiros números;',lista[:4])
print('2. uma lista com os 5 últimos números;',lista[-5:])
print('3. uma lista contendo apenas os elementos das posições pares;',lista[1::2])
print('4. uma lista contendo apenas os elementos das posições ímpares;',lista[0:-1:2])

lista.sort(reverse=True)
print('5. a lista inversa da lista sorteada',lista)
print('6. uma lista inversa dos 5 primeiros números;',lista[:5])
print('7. uma lista inversa dos 5 últimos números.',lista[-5:])