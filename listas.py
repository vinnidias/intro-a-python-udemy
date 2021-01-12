minha_lista = ['abacaxi', 'melancia', 'laranja']
minha_lista2 =  [1,2,3,4,5]
minha_lista3 = ['abacaxi', 2, 9.89, True]

print(minha_lista3)
print(minha_lista[2])

tamanho = len(minha_lista2)

print(tamanho)

for item in minha_lista:
    print(item)

minha_lista.append('tomate')

print(minha_lista)

if 3 in minha_lista2:
    print('o numero 3 esta na lista 2')

del minha_lista[3:]

print(minha_lista)
