arquivo = open('meu_arquivo.txt')

linhas = arquivo.readlines()

print(linhas)

for linha in linhas:
    print(linha)

texto = arquivo.read()

print(texto)