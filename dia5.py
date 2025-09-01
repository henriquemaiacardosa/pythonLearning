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

# 3. Peça ao usuário um número inteiro e calcule a soma de todos os números ímpares de 1 até esse número.
numero = int(input("Digite um número: "))
soma = 0
for i in range(1, numero+1):
    if i % 2 != 0:
        soma += i
print(soma)


# 4. Solicite dois números inteiros e exiba todos os números entre eles (inclusive).

# 5. Peça ao usuário um número inteiro e exiba a tabuada desse número de 1 a 10.

# 6. Solicite um número inteiro e conte quantos divisores ele possui.

# 7. Peça ao usuário 5 números e exiba o maior deles.

# 8. Solicite um número inteiro N e exiba a soma dos dígitos desse número.

# 9. Peça ao usuário um número inteiro e verifique se ele é primo.

# 10. Solicite um número inteiro e exiba