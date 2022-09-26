#  FUNÇÕES

# 1. O que são e para que utilizá-las?

# Funções já utilizadas anteriormente:

"""print() # imprimi uma mensagem no console
max() # retornar o maior valor
min() # retornar o menor valor
input() # retornar o dado informar pelo usuario via console
len() # recebe a lista e retornar o tamanha desta lista"""

# 2. Criação de funções:

# Funcao inicial

def saudacao():
    print('Seja bem vindo(a)!')
    print('Olá, é um prazer ter você fazendo parte desse curso')

saudacao()



# Função com parametro
def saudacao(nome):
    print(f'Seja bem vindo(a)! {nome}')
    print('Olá, é um prazer ter você fazendo parte desse curso')

saudacao('Pedro')

# Funcao com parametro default
def saudacao(nome, curso='Python'): ## NÃO É OBRIGATORIO PASSAR O PARAMETRO QUE TEM VALOR DEFAULT
    print(f'Seja bem vindo(a)! {nome}')
    print(f'Olá, é um prazer ter você fazendo parte desse curso {curso}')

saudacao('Pedro', 'C++')


# Função com retorno
def soma(num1, num2):
    return num1+num2

resultado = soma(1,2)

print('O resultado da soma é: ',resultado)

def calculadora( num1, num2, operador='+'):
    if operador == '+':
        return num1 + num2 
    elif operador == '-':
        return num1 - num2

resultado = calculadora(2,3,'-')
print('O resultado da soma é: ',resultado)
