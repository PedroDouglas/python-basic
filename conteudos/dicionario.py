# DICIONARIO 

# Criando dicionarios

dicionario ={}
dicionario = dict()

dicionario ={'nome': 'Pedro', 'idade': 26, 'altura': 1.77}

print(dicionario)
print(dicionario['nome'])

# ADICIONANDO ELEMENTOS NO DICIONARIO

dicionario ['programador'] = True

print(dicionario)

dicionario['altura'] = 2
print(dicionario)


# INTERANDO COM O DICIONARIO

for chave in dicionario:
    print (chave, dicionario[chave])  # por padrao ele retornar as chaves do dicionario


# Testando a existendia de uma chave


print('peso' in dicionario)
print('altura' in dicionario)
