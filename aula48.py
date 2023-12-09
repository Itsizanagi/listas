'''

Listas em Python 
Tipo list - Mútavel
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update  Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

append - Adiciona um item ao final 
insert - Adiciona um item no indice escolhido
pop - Remove do final ou do indice escolhido
del - Apaga um indice
clear - limpa a lista
exetend - estende a lista

+ - concatena listas



        01234
        -54321
'''
string = 'ABCDE' # 5 caracteres (len)


  #         0     1      2        3    4
'''lista = [123, True, 'Gustavo', 1.2, []]
print(lista[2].lower())
if lista[3] == 'Gustavo':
    print('Ok, funcionoou')
else:
    print('Foi aqui')'''


'''import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)

if 'Gustavo' in lista:
    print('Foi aqui')'''
#        0   1   2   3   4   5        
lista = [10, 20 ,30, 40]
lista.append('Gustavo') # metodo, add um novo elemento/valor
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 'gustavo')
print(lista[4])


'''lista[2] = 300
del lista[2]
print(lista)
print(lista[2])'''
