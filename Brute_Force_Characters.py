import random
character = '0123456789abcdefghijklmnopqrstuvwxyz'
character_list = list(character)
password = input('Entre com sua senha:')
adivinhe = ''
while(adivinhe != password):
    adivinhe = random.choices(character_list,k=len(password))
    print(adivinhe)
    adivinhe = ''.join(adivinhe)
    print(adivinhe) #use #print(adivinhe) aqui, linha 10, e na linha 8 para reduzir o tempo de busca drasticamente
print('Sua senha é:' + adivinhe)