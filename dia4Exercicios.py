"""
#Crie um programa que solicita um número ao usuário e verifica se ele é positivo, negativo ou zero
n1 = float(input("Digite um número: "))

if n1 > 0:
    print(f"O número {n1} é maior que 0")
elif n1 == 0:
    print(f"O número {n1} é igual a 0")
else:
    print(f"O número {n1} é menor que 0")

# Crie um programa que pede ao usuário dois números e uma operação (+, -, *, /) e realiza o cálculo correspondente.
n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
operador = input("Digite um operador (+,-,*,/): ")

if operador == "+":
    soma = n1 + n2
    print(f"A soma de {n1:.2f} e {n2:.2f} é: ", soma)
elif operador == "-":
    sub = n1 - n2
    print(f"A subtração de {n1:.2f} e {n2:.2f} é: ", sub)
elif operador == "*":
    mult = n1 * n2
    print(f"A multiplicação de {n1:.2f} e {n2:.2f} é: ", mult)
elif operador == "/":
    if n2 != 0:
        div = n1 / n2
        print(f"A divisão de {n1:.2f} e {n2:.2} é: ", div)
    else:
        print("Erro")
else:
    print("Operador inválido")

# Crie um programa que classifica a idade de uma pessoa em:
# ● Criança: 0 a 12 anos
# ● Adolescente: 13 a 17 anos
# ● Adulto: 18 a 59 anos
# ● Idoso: 60 anos ou mais

idade = int(input("Digite sua idade: "))
if 0 <= idade <= 12: # se a idade for maior ou igual a 0 (não pode ser menor, pois não existe) e se for menor ou igual a 12 (não poode passar de 12 por isso é IGUAL ou MENOR)
    print("Você é criança")
elif 13 <= idade <= 17: # idade for maior ou igual a 13 pois se for menor cai no bloco anterior, e for menor ou IGUAL (igual é restringindo ao valor máximo)
    print("Você é adolescente")
elif 18 <= idade <= 59:
    print("Você é adulto")
else:
    print("Você é idoso")

# Crie um programa que verifica se um ano é bissexto.
# ● Um ano é bissexto se for divisível por 4.
# ● Mas não é bissexto se for divisível por 100, exceto se for divisível por 400

ano = int(input("Digite o ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): # Primeira parte se for div por 4 é bi, se ele for dividido por 100 e der um resto diferente de 0 é por que ele não é divisivel (Mas não é bissexto se for divisível por 100) ou se for div por 400
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")

# Crie um programa que simula um caixa eletrônico. O usuário deve informar o valor do saque
# (apenas valores inteiros) e o programa deve informar quantas cédulas de cada valor serão
# fornecidas.
# ● Considere cédulas de R$100, R$50, R$20, R$10, R$5 e R$2

# valor = int(input("Digite o valor a ser sacado (apenas valores inteiros): R$ "))
# cedula = int(input("Digite em qual cédula você gostaria de sacar (100,50,20,10,5,2) R$: "))

# if cedula == 100:
#     nota100 = valor / 100
#     print(f"{nota100} notas de 100")
# elif cedula == 50:
#     nota50 = valor / 50
#     print(nota50)
# elif cedula == 20:
#     nota20 = valor / 20 
#     print(nota20)
# elif cedula == 10:
#     print(nota10)
#     nota10 = valor / 10
# elif cedula == 5:
#     nota5 = valor / 5
#     print(nota5)
# elif cedula == 2:
#     nota2 = valor / 2
#     print(nota2)
# elif valor == 0:
#     print("Saque inválido")

valor_saque = int(input("Digite o valor do saque: R$"))

if valor_saque <= 0:
    print("Valor inválido.")
else:
    cedulas_100 = valor_saque // 100
    valor_saque %= 100
    cedulas_50 = valor_saque // 50
    valor_saque %= 50
    cedulas_20 = valor_saque // 20
    valor_saque %= 20
    cedulas_10 = valor_saque // 10
    valor_saque %= 10
    cedulas_5 = valor_saque // 5
    valor_saque %= 5
    cedulas_2 = valor_saque // 2
    valor_saque %= 2
if valor_saque != 0:
    print("Não é possível sacar o valor especificado com as cédulas disponíveis.")
else:
    print("Cédulas entregues:")
if cedulas_100 > 0:
    print(f"{cedulas_100} x R$100")
if cedulas_50 > 0:
    print(f"{cedulas_50} x R$50")
if cedulas_20 > 0:
    print(f"{cedulas_20} x R$20")
if cedulas_10 > 0:
    print(f"{cedulas_10} x R$10")
if cedulas_5 > 0:
    print(f"{cedulas_5} x R$5")
if cedulas_2 > 0:
    print(f"{cedulas_2} x R$2")
"""
# Decompondo um número em centenas, dezenas e unidades
# - Peça um número inteiro (0–999) e exiba quantas centenas, dezenas e unidades ele tem.
# - Exemplo: 374 → 3 centenas, 7 dezenas, 4 unidades.

numero = int(input("Digite um número para decompor (0-999): "))


