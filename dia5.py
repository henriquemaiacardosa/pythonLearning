"""
# Peça ao usuário um número inteiro positivo N e calcule a soma de todos os números de 1 até N.
# No final, exiba o resultado da soma.
 
n = int(input("Digite um número: "))
soma = 0

for i in range(0,n+1):
    soma += i
print("soma",soma)

# Exercício – Produto dos números de 1 até N
# Peça ao usuário um número inteiro positivo N e calcule o 
# produto (multiplicação) de todos os números de 1 até N.
# No final, exiba o resultado.

n = int(input("Digite um número: "))
multiplicacao = 1

for i in range(1,n+1):
    multiplicacao *= i
print("A multiplicação é",multiplicacao)

# Com for, imprima todos os números de 1 até 5.
for i in range (1,6):
    print(i)

#Com while, faça o mesmo, mas sem usar range().
i = 1
while i <= 5:
    print(i)
    i += 1

soma = 0
n = int(input("Digite um número: "))
while n != 0:
    soma += n         
    n = int(input("Digite outro número: "))  S
print("A soma é", soma)

"""

# i = 0
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i+=1

# n = int(input("Digite um número para ver sua tabuada: "))
# for i in range(1,11):
#     tabuada = i * n
#     print(f"{n}x{i}",tabuada)

 # 1. Peça ao usuário um número inteiro e imprima todos os números de 1 até esse número.
# numero = int(input("Digite um número: "))

# for i in range(1, numero+1):
#     print(i)


# 2. Solicite um número inteiro N e exiba todos os números pares de 1 até N.
# numero = int(input("Digite um número: "))

# for i in range(1, numero+1):
#     if i % 2 == 0:
#         print(i)

# # 3. Peça ao usuário um número inteiro e calcule a soma de todos os números ímpares de 1 até esse número.
# numero = int(input("Digite um número: "))
# soma = 0
# for i in range(1, numero+1):
#     if i % 2 != 0:
#         soma += i
# print(soma)

# 4. Solicite dois números inteiros e exiba todos os números entre eles (inclusive).
# n1 = int(input("Digite um número: "))
# n2 = int(input("Digite um número: "))

# n = n1
# if n < n2:
#     while n <= n2:
#         print(n)
#         n += 1

# else:
#     while n >= n2:
#         print(n)
#         n -=1

# Peça ao usuário um número inteiro positivo N 
# e faça uma contagem regressiva até 0, mostrando cada número.
# No final, mostre a mensagem “FIM!”.

#while
# n = int(input("Digite um número: "))

# while n >= 0:   
#     print(n)
#     n -= 1
# print("FIM!")


# #FOR
# n = int(input("Digite um número: "))

# for i in range(n, -1, -1):   
#     print(i)
# print("FIM!")

#Peça ao usuário um número inteiro positivo N e mostre todos os números pares de 1 até N.

#for
# n = int(input("Digite um número inteiro e positivo: "))

# for i in range(2, n+1, 2):
#     print(i)

# # while 
# n = int(input("Type a positive even number:"))
# i = 2
# while i <= n:
#     print(i)
#     i +=2

# Peça ao usuário um número inteiro positivo N e mostre todos os números de 1 até N que são divisíveis por 3 e 5 ao mesmo tempo.

#for
# n = int(input("Type a number: "))

# for i in range(1, n+1):
#     divisor = (i % 3 == 0) and (i % 5 == 0)
#     if divisor:
#         print(i)

# # ou for
# n = int(input("Type a number: "))
# for i in range(15, n+1,15):
#     print(i)

# # while 
# n = int(input("Type a number: "))
# i = 15
# while i <= n:
#     print(i)
#     i += 15
    
# Peça ao usuário um número inteiro positivo N e calcule a soma de 
# todos os números pares de 1 até N.

# n = int(input("Digite um número: "))
# soma = 0

# for i in range(2, n+1, 2):
#     soma +=i
#     print(i)
# print(f"A soma dos pares até {n} é: ",soma)

# n = int(input("Digite um número: "))
# i = 0
# soma = 0

# while i < n:
#     i += 2
#     soma += i
# print(soma)
    
#Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e 
# continue pedindo até que o usuário informe um valor válido.

# nota = float(input("Digite uma nota: "))
# while nota < 0 or nota > 10:
#     nota = int(input("Digite novamente a nota: "))
# print("A nota é:",nota)

# Faça um programa que leia um nome de usuário e a sua senha 
# e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

# nome = str(input("Digite o seu login: "))
# senha = str(input("Digite o sua senha: "))

# while senha == nome:
#     senha = str(input("A senha não pode ser igual ao login, digite outra senha: "))
# print("Login",nome)
# print("Senha",senha)

# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

# nome = str(input("Digite um nome maior que 3 caracteres: "))
# while len(nome) < 3:
#         nome = str(input("Digite um nome maior que 3 caracteres: "))
# print(nome)

# idade = int(input("Digite uma idade: "))
# while (idade > 150) or (idade < 0):
#         idade = int(input("Digite uma idade válida: "))
# print(idade)

# salario = int(input("Digite um salário: "))
# while salario < 0:
#     salario = int(input("Digite um salário válido: "))
# print(salario)

# sexo = str(input("Digite o sexo F/M: "))
# gen = ["F","f","M","m"]
# while sexo not in gen:
#     sexo = str(input("Digite um sexo válido: "))
# print(sexo)

estadoCivil = str(input("Digite o seu estado S/C/V/D: "))
estciv = ["S","s","C","c","V","v","D","d"]
while estadoCivil not in estciv:
    estadoCivil = str(input("Digite um sexo válido: "))
if estadoCivil == "S" or estadoCivil == "s":
    print("Solteiro") 
elif estadoCivil == "C" or estadoCivil == "c":
    print("Casado") 
elif estadoCivil == "V" or estadoCivil == "v":
    print("Viuvo") 
elif estadoCivil == "D" or estadoCivil == "d":
    print("Divorciado") 






    