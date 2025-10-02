# Lista em Python 
# 🚀 O que é uma lista em Python

# É uma coleção de valores, guardados em uma única variável, em vez de criar várias.

# idades = [15, 20, 18, 22]


# idades[0] → 15 (o primeiro elemento, índice começa em 0)

# idades[1] → 20

# idades[-1] → 22 (último elemento)

# Como criar e preencher uma lista

# Lista vazia + append

# idades = []
# idades.append(15)
# idades.append(20)
# print(idades)  # [15, 20]


# Lista já preenchida

# notas = [7, 8.5, 9]

# Usando com for
# for idade in idades:
#     print(idade)   # percorre e mostra cada idade

# Funções úteis

# len(idades) → quantidade de elementos

# sum(idades) → soma de todos os elementos

# max(idades) → maior valor

# min(idades) → menor valor

# Mini-exemplo
# idades = []
# for i in range(3):
#     idade = int(input("Digite a idade: "))
#     idades.append(idade)

# print("Todas as idades:", idades)
# print("Média:", sum(idades)/len(idades))
# print("Mais velho:", max(idades))
# print("Mais novo:", min(idades))


# Peça 5 números ao usuário, guarde-os em uma lista e depois mostre a lista inteira.
# lista = []
# for i in range(0,5):
#     n = int(input("Digite um numero: "))
#     lista.append(n)
# print(lista)

#Crie um programa que peça para o usuário digitar 5 notas (valores de 0 a 10), 
#guarde todas elas em uma lista, e depois calcule e mostre a média dessas notas.
# lista = []
# for i in range(5):
#     nota = int(input("Digite a Nota: "))
#     lista.append(nota)
# media = sum(lista)/len(lista)
# print("A media das 5 notas é: ", media)

# Faça um programa que peça 7 números inteiros ao usuário, guarde todos em uma lista, e no final:
# Mostre todos os números digitados
# Mostre o maior valor da lista
# Mostre o menor valor da lista
# lista = []
# for i in range(7):
#     n = int(input("Digite um número: "))
#     lista.append(n)
# print("Os números digitaos foram: ",lista)
# print("O maior número é: ",max(lista))
# print("O menor número é: ",min(lista))
# print(f"A lista possui {len(lista)} números")

# Peça para o usuário digitar 4 nomes, guarde todos em uma lista.
# Depois, use um for in para mostrar cada nome com a frase:

# lista = []
# for i in range(4):
#     nome = str(input("Digite um nome: "))
#     lista.append(nome)
# for nome in lista:
#         print(f"Nome {len(lista)}",nome)

# Crie um programa que:
# Peça para o usuário digitar 5 tarefas do dia (ex: "Estudar", "Arrumar o quarto", etc)
# Guarde todas as tarefas em uma lista
# Depois, mostre as tarefas numeradas, assim:

# lista = []
# for i in range(5):
#     tarefas = str(input(f"Digite a tarefa {i+1} do seu dia: "))
#     lista.append(tarefas)
# for i, tarefas in enumerate(lista,start=1):
#     print(i, tarefas)
        
# Crie um programa que:
# Peça para o usuário digitar 3 frutas favoritas
# Guarde as frutas em uma lista
# Mostre a lista completa
# Depois, peça ao usuário qual posição ele quer trocar (0, 1 ou 2)
# Peça a nova fruta e atualize a lista
# Mostre a lista atualizada no final

# lista = []
# for i in range(3):
#     frutas = str(input(f"Digite sua {i+1}ª fruta favorita: "))
#     lista.append(frutas)
# print("Suas frutas favorias favoritas são: ", lista)

# alterar = int(input("Escolha uma fruta para alterar 1,2,3?: "))
# lista[alterar-1] = str(input("Nova fruta: "))
# print(lista)

# Crie um programa que:
# Peça ao usuário para digitar 5 números inteiros
# Guarde todos em uma lista
# Mostre:
# Todos os números digitados
# A soma dos valores
# O maior valor
# O menor valor
# A posição (índice) do maior valor na lista

# lista = []
# print("Digite 5 números inteiros: ")
# for i in range(5):
#     n = int(input(f"Digite N{i+1}: "))
#     lista.append(n)
# print("Os números digitados foram: ",lista)
# print("A soma dos números digitados é: ",sum(lista))
# print("O maior número é: ",max(lista))
# maior = max(lista)
# print("O menor número é: ",min(lista))
# print("O índice do mair número é: ",lista.index(maior))

# Crie uma função chamada mostrar_mensagem() que:
# Mostre a mensagem: "Bem-vindo ao mundo das funções!"

def mostrar_mensagem():
    print("Bem-vindo ao mundo das funções!")

mostrar_mensagem()
