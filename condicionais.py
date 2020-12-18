x = 1 
y = 100000000

# #estrutura condicional utilizando if

if x > y:
    print('x é maior que y')

if y > x:
    print('y é maior q x')

# #estrutura condicional utilizando if e else

if x > y:
    print('x é maior que y')
else:
    print('x é menor que y')


# # indentação:

a = 7
b = 6

if b > a:
    if b > 0:
        print('b é maior que a \nb é positivo')
    else: 
        print('b não é maior que a nem positivo')
else: 
    print('b menor que a')

# condição elif executa a primeira condição verdadeira encontrada

if x == y:
    print('números iguais')
elif x < y:
    print('x menor que y')
elif y > x:
    print('y maior que x')
else: 
    print('números diferentes')