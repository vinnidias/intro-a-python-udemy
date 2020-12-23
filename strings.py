a = 'Vinicius'
b = 'Dias'
minha_string = 'O rato roeu a roupa do rei de Roma'

concatenado = a + ' ' + b

print(concatenado)

# tamanho da string

tamanho = len(concatenado)

print(tamanho)

# posição da string / string index

print(a[0])
print(a[1])
print(a[2])
print(a[3])

# imprimindo parte de uma string

print(concatenado[0:4])

# métodos para string

print(concatenado.lower())
print(concatenado.upper())

minha_lista = minha_string.split(' ')
print(minha_lista)

busca = minha_string.find('rei')

print(busca)

print(minha_string[busca:])

minha_string = minha_string.replace('rei', 'rainha')
print(minha_string)



