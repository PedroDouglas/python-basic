
def adicionar_lista():
    lista = []
    while True:
        condicao = input('0 - para sair: \n1 - para adicionar um valor a lista:\n')
        if condicao == '0':
            break
        elif condicao == '1':
            numero = float(input('\ninforme o numero desejado a adicionar na lista: '))
            lista.append(numero)
    return(lista)

lista = adicionar_lista()

print ("Resultado da soma da lista: ", sum(lista))




