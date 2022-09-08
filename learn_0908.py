from tkinter import Y


tupla = ()
print("Tupla = ", tupla)
print("id  = ", id(tupla))
print()

tupla = (2, "um", 3, True)
print("Tupla = ", tupla)
print("id = ", id(tupla))
print()

#um unico valor não é uma tupla
t_1 = (1)
print(t_1)
print( type(t_1))
print()

#ao adicionar uma virgula passa a ser uma tupla. ex: t_1 = (1, )
t_1 = (1, )
print(t_1)
print( type(t_1))
print()

t_2 = (1, 2)
print(t_2)
print( type(t_2))
print()

tupla = (1, 'a', 2, 'Brasil', 3.14)

#executa uma varredura nos items do array
for i in tupla:
    print(i)

print()

#executa uma estrutura de array| acesso nome[indice]
for i in range(0, len(tupla)):
    print(tupla[i])

x = 5
y = 10

print()
print("x = ", x)
print("y = ", y)

#trocando valores de variaveis
x, y = y, x
#ou usando uma variavel auxiliar

print()
print("x = ", x)
print("y = ", y)
print()

#retorno multiplos
def divisao(x, y):
    q = x // y
    r = x % y
    return (q, r)

n = 5
d = 3

(rest_int, resto) = divisao(n, d)

print(n, '//',d,'=', rest_int)
print(n, '%',d,'=', resto)
print()

n = 11
d = 4

(rest_int, resto) = divisao(n, d)

print(n, '//',d,'=', rest_int)
print(n, '%',d,'=', resto)
print()