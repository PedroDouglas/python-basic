print('\n Responda as perguntas com SIM ou NAO')
mora_perto = input('\nMora perto da vítima? ').lower() == 'sim'
ja_trabalhou = input('\nJá trabalhou com a vítima? ').lower() == 'sim'
telefenou = input('\nTelefonou para a vítima? ').lower() == 'sim'
esteve_local_crime = input('\nEsteve no local do crime? ').lower() == 'sim'
devia = input('\nDevia para a vitima? ').lower() == 'sim'

total = mora_perto + ja_trabalhou + telefenou + esteve_local_crime + devia

if total == 5:
    print('\nAssassinoooo! (ง︡\'-\'︠)ง ')
elif total == 4 or total == 3:
    print('\nCúmpliceeee (҂◡̀_◡́)ᕤ')
elif total == 2:
    print('\nSuspeito (≖_≖ )')
else:
    print('\nLiberdade Cantoou ٩(˘◡˘)۶')
