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
"""
n = int(input("Digite um número: "))
soma = 0
while n != 0:
    int(input("Digite outro número: "))
soma = n + n
print(soma)


