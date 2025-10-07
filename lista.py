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

# def mostrar_mensagem():
#     print("Bem-vindo ao mundo das funções!")

# mostrar_mensagem()

#Peça ao usuário dois números inteiros: o início e o fim.
#Depois, faça uma contagem do início até o fim, 
# um número por linha, usando for

# n1 = int(input("Digite o início: "))
# n2 = int(input("Digite o fim: "))
# if n1 < n2:
#     for i in range(n1, n2+1):
#         print(i)
# else:
#     for y in range(n1, n2-1, -1):
#         print(y)

# n1 = int(input("Digite o início: "))
# n2 = int(input("Digite o fim: "))
# i = n1
# if n1 < n2:
#    while i < n2:
#         print(i)
#         i +=1
# else:
#     while i > n2:
#         print(i)
#         i -= 1


# Crie um programa que:
#     Peça números inteiros ao usuário, um por vez
#     Pare quando o usuário digitar 0
#     No final, mostre:
#     A soma apenas dos números pares
#     A quantidade de pares digitados
    
# nP = int(input("Digite um número (Digite 0, para parar): "))
# soma = 0
# i = 0

# while nP != 0:
#     if nP % 2 == 0:
#         soma += nP
#         i += 1
#     nP = int(input("Digite um número (Digite 0, para parar): "))

# if nP == 0:
#     print("A soma dos pares é: ",soma)    
#     print("A quantidade de pares digitados é: ",i)    


# Peça números ao usuário até ele digitar 0
#     Ao final, mostre:
#     O maior número digitado
#     O menor número digitado
#     (Sem contar o 0!)

# numero = float(input("Digite um número (Digite 0 para parar): "))
# lista_numeros = []

# while numero != 0:
#     lista_numeros.append(numero)
#     numero = float(input("Digite um número (Digite 0 para parar): "))
    
# # Se o primeiro número for 0, da erro.
# print("O maior número digitado é: ",max(lista_numeros))
# print("O menor número digitado é: ",min(lista_numeros))


# Peça números inteiros ao usuário até ele digitar 0
#     No final, mostre:
#     Quantos números pares foram digitados
#     Quantos números ímpares foram digitados

# # Entrada
# entrada = float(input("Digite um número (Digita 0 para parar): "))
# listaDosNumerosDigitados = []
# contador_par = 0
# contador_impar = 0

# # Processamento 
# while entrada != 0:
#     if entrada % 2 == 0:
#         contador_par += 1
#         listaDosNumerosDigitados.append(entrada)
#         entrada = float(input("Digite um número (Digita 0 para parar): "))
#     else:
#         contador_impar += 1
#         listaDosNumerosDigitados.append(entrada)
#         entrada = float(input("Digite um número (Digita 0 para parar): "))

# # Saida
# print("A quantidade de pares é: ", contador_par)
# print("A quantidade de impares é: ", contador_impar)
    
# numero = int(input("Digite um número: "))   
# lista = []

# while numero >= 0:
#     numero = int(input("Digite um número: "))           
#     lista.append(numero)
#     if len(lista) == 2:
#         diferenca = lista[0] - lista[1]
#         print(f"A diferença entre {lista[0]} e {lista[1]} é {diferenca}")
#         lista.clear()
    
        
# Você vai simular uma caminhada numa montanha. 
    # O programa começa com um "altitude" igual a 0. 
    # A cada passo, o usuário informa se subiu (S) ou desceu (D) 1 metro. 
        # O programa atualiza a altitude e exibe o valor atual.
            # O programa para quando o usuário digitar P (de "Parar").
    # No final, o programa mostra:
        # A maior altitude atingida
        # A menor altitude atingida        

# altitude = 0
# max = 0
# min = 0

# print("Controle a Montanha Russa (D para descer/ S para subir e P para Parar)")
# passo = ""
# while passo != "P" and passo != "p":
#     passo = str(input("Subir/Descer/Parar: "))

#     if passo == "S" or passo == "s": 
#         altitude += 1
#         if altitude > max:
#             max = altitude
    
#     elif passo == "D" or passo == "d": 
#         altitude -= 1
#         if altitude < min:
#             min = altitude

#     elif passo == "P" or passo == "p":
#         break

#     else:
#         print("Movimento inválido")
#         continue
# print("A maior altitude atingida",max)
# print("A menor altitude atingida",min)

##########################################
        
#Escreva um programa que pede um número n e soma todos os números de 1 até n.

# n = int(input("Digite um número: "))
# soma = 0

# for i in range(1, n+1):
#     print(i, end=" + ")
#     soma += i
# print("=",soma)

# Peça um número n, e mostre todos os números pares de 0 até n.

# n = int(input("Digite um número: "))

# for i in range(0, n, 2):
#     print(i, end=" ")

#O programa pede números até o usuário digitar 0.
#Quando ele digita 0, o programa mostra quantos números foram digitados (sem contar o zero).

# n = int(input("Digite um número: "))
# contador = 0

# while n != 0:
#     n = int(input("Digite um número: "))
#     contador +=1
# print("Foram digitados:",contador,"números")

# O programa pede números ao usuário até ele digitar -1.
#No final, o programa mostra o maior e o menor número que o usuário digitou.

# n = int(input("Digite um número (Para parar, digite -1): "))

# if n == -1:
#     print("Nenhum número válido foi digitado.")
# else:
#     maior = n
#     menor = n

#     while True:
#         n = int(input("Digite um número (Para parar, digite -1): "))
#         if n == -1:
#             break
#         if n > maior:
#             maior = n
#         if n < menor:
#             menor = n

#     print("O maior número digitado foi:", maior)
#     print("O menor número digitado foi:", menor)


# contador = 0
# soma = 0
# ultimo = 0

# while True:
#     numero = int(input("Digite um número: "))
#     contador += 1
#     soma += numero
#     media = soma / contador
#     ultimo = numero
#     if media > 20:
#         print("Último número digitado: ",numero)
#         print("Media: ",media)
#         break
#     else:
#         ultimo = numero



