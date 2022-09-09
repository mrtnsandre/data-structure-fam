from tkinter import Y


tupla = ()
print("Tupla = ", tupla)
print("id  = ", id(tupla))
print()

tupla = (2, "um", 3, True)
print("Tupla = ", tupla)
print("id = ", id(tupla))
print()

#Um unico valor não é uma TUPLA
t_1 = (1)
print(t_1)
print( type(t_1))
print()

#Ao adicionar uma virgula passa a ser uma TUPLA. ex: t_1 = (1, )
t_1 = (1, )
print(t_1)
print( type(t_1))
print()

t_2 = (1, 2)
print(t_2)
print( type(t_2))
print()

tupla = (1, 'a', 2, 'Brasil', 3.14)

#Executa uma varredura nos items do ARRAY
for i in tupla:
    print(i)

print()

#Executa uma estrutura de ARRAY | acesso nome[indice]
for i in range(0, len(tupla)):
    print(tupla[i])

x = 5
y = 10

print()
print("x = ", x)
print("y = ", y)

#Trocando valores de VARIAVEIS
x, y = y, x
#Ou usando uma variavel auxiliar

print()
print("x = ", x)
print("y = ", y)
print()

#Retorno multiplos
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

#Tratamento de ARRAY
def get_Idades(aTupla):
    idades = ()
    nomes = ()

    for t in aTupla:
        idades = idades + (t[0],)
        nomes = nomes + (t[1],)

    mais_jovem = min(idades)
    mais_velho = max(idades)
    num_pessoas = len(nomes)

    return (mais_jovem, mais_velho, num_pessoas)

relacao = ((15, 'Joana'), 
        (35, 'Pedro'), 
        (54, 'Claudiney'), 
        (27, 'Sofia'),
        (10, 'Ana'))

(jovem, idoso, pessoas) = get_Idades(relacao)

print(jovem)
print(idoso)
print(pessoas)