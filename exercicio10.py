tempo_composicao = {
    'W' : 1,
    'H' : 1/2,
    'Q' : 1/4,
    'E' : 1/8,
    'S' : 1/16,
    'T' : 1/32,
    'X' : 1/64    
}

composicao = '/HH/QQQQ/XXXTXTEQH/W/HW/'

compassos = composicao.strip('/').split('/')

print(compassos)

for k,v in tempo_composicao.items():
    print(k,v)

