soma = 0

for variavel in range(1, 5):
    nota = float(input(f'Informe sua nota {variavel}: '))
    soma = soma + nota 

soma = soma / variavel
print(f'Sua nota final é: {soma}')


