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

macas = int(input("Quantas maçãs existem?"))
caixas = 10
caixasMacas = macas // caixas
print(f"São cheias {caixasMacas} caixas com a quantidade de maçãs")
resto = macas % caixas
print("E sobraram ",resto)

pacote = 6
chocolates = int(input("Quantos chocolates você deseja: ")) 
pacotes = chocolates // pacote
resto = chocolates % pacote
print(f"Você precisa comprar {pacotes} pacotes completos de 6 chocolates")
if resto:
    print(f"E sobraram {resto} chocolates")

amigos = 4
brigadeiros = int(input("Digite a quantidade de brigadeiros: "))
divisaoBrigadeiros = brigadeiros // amigos
resto = brigadeiros % amigos
print(f"São {divisaoBrigadeiros} brigadeiros para cada amigo")                  
if resto:
    print(f"E sobram {resto}")
else:
    print("A divisão foi exata! Que sorte!")

minutos = int(input("Digite a quantidade de minutos: "))
horas = minutos // 60
minutos %= 60
print(f"{horas} horas {minutos} minutos:")

# Desafio:
# Crie um programa que receba uma quantidade de segundos e converta para minutos e segundos.
segundos = int(input("Digite os segundos: "))
minutos = segundos // 60
segundos %= 60
print(f"{minutos} minutos {segundos} segundos:")
#Crie um programa que receba uma quantidade de segundos e converta para horas, minutos e segundos.
segundos = int(input("Digite os segundos: "))
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60
print(f"{horas} h {minutos} m {segundos} s")

# 1. Caixas de leite
# Um caminhão está levando leite em litros. Cada caixa comporta 12 litros.
#  Escreva um programa que receba a quantidade total de litros e mostre:
# Quantas caixas completas cabem.
# Quantos litros sobraram fora das caixas.
litros = int(input("Quantos litros de leite será levado? "))
caixa = 12 
leite = litros // caixa
litros %= 12
print(f"{leite} {litros} ")

# 2. Notas escolares
# Um professor tem 127 provas para corrigir. Ele organiza os trabalhos em pilhas de 25 provas.
#  Crie um programa que receba o número total de provas e mostre:
# Quantas pilhas completas ele terá.
# Quantas provas vão sobrar fora das pilhas.

provas = int(input("Digite a quantidade de provas a serem corrigidas: "))
pilha = 25
provasCorrigidas = provas // pilha
provas %= 25
print(f"O professor terá {provasCorrigidas} pilhas para corrigir e {provas} prova(s)")

# 3. Troco em moedas
# Um cliente pagou uma compra e recebeu centavos de troco.
# As moedas disponíveis são de 25, 10, 5 e 1 centavo.
#  Escreva um programa que receba o valor em centavos e mostre quantas moedas de cada tipo ele deve receber.
valorDaCompra = float(input("Valor da compra: R$"))
troco25 = valorDaCompra // 0.25
valorDaCompra %= 0.25
troco10 = valorDaCompra // 0.10
valorDaCompra %= 0.10
troco5 = valorDaCompra // 0.05
valorDaCompra %= 0.02
troco1 = valorDaCompra // 0.01
valorDaCompra %= 0.01
print(f"Troco em moedas de 25 {troco25}, Troco em moedas de 10 {troco10}, Troco em moedas de 5 {troco5}, Troco em moedas de 1 {troco1}")
"""

# Crie um programa que simula um caixa eletrônico. O usuário deve informar o valor do saque
# (apenas valores inteiros) e o programa deve informar quantas cédulas de cada valor serão
# fornecidas.
# ● Considere cédulas de R$100, R$50, R$20, R$10, R$5 e R$2
caixaEletronico = int(input("Digite o valor do saque: "))
if caixaEletronico < 0:
    print("Valor indisponível para saque")
else:
    nota1OO = caixaEletronico // 100
    caixaEletronico %= 100

    nota50 = caixaEletronico // 50
    caixaEletronico %= 50

    nota2O = caixaEletronico // 20
    caixaEletronico %= 20

    nota1O = caixaEletronico // 10
    caixaEletronico %= 10

    nota5 = caixaEletronico // 5
    caixaEletronico %= 5

    nota2 = caixaEletronico // 2
    caixaEletronico %= 2
    
    print(f"Notas de R$100: {nota1OO}")
    print(f"Notas de R$50: {nota50}")
    print(f"Notas de R$20: {nota2O}")
    print(f"Notas de R$10: {nota1O}")
    print(f"Notas de R$5: {nota5}")
    print(f"Notas de R$2: {nota2}")