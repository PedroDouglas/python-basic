numero = float(input('Informe o número: '))

if numero <= 0:
    print('Número fora do intervalo')
elif numero > 0 and numero <= 25.0:
    print('[0,25]')
elif numero > 25.0 and numero <= 50:
    print('[25,50]')
elif numero > 50.0 and numero <= 75:
    print('[50,75]')
elif numero > 75.0 and numero <= 100:
    print('[75,100]')
elif numero >= 100.1:
    print('Número fora do intervalo')