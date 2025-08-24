"""
# Condicionais  ->estruturas if, else

idade = 16

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

# meia entrada => menor de 18 ou esteja estudando em escola pública/faculdade

estudante = input("Você estuda? (1 para sim / 0 para não): ")
converte= int(estudante)
idade = int(input("Digite sua idade: "))

if (converte == 1) or (idade <= 18):
    print("Você paga meia entrada")
else:
    print("Você paga Inteira")

# nota: A, B, C
# > 9 = A, > 8 = B e > 6 = C

nota = float(input("Digite sua nota: "))
if (nota > 9):
    print("Sua nota é: A")
elif (nota > 8):
    print("Sua nota é: B")
elif (nota > 6):
    print("Sua nota é: C")
else:
    print("F")

# Climas: ensolarado, chuvoso, nublado

clima = input("Escolha o clima atual (1:Ensolarado/2:Nublado/3:Chuvoso): ")
converteClima = int(clima)

if converteClima == 1:
    print("O dia está ensolarado")
elif converteClima == 2:
    print("Clima Nublado")
elif converteClima == 3:
    print("Clima Chuvoso")
else:
    print("Clima inválido")

# Comissão de vendas
# > 1000 = 5%
# > 500 = 2%
# = 1%

comissao = float(input("Quanto foi vendido: "))
if comissao > 1000:
    parte   = comissao * 0.05
    print("A comissão do vendedor é:",round(parte,2))
elif comissao > 500:
    parte   = comissao * 0.02
    print("A comissão do vendedor é:",round(parte,2))
else:
    parte   = comissao * 0.01
    print("A comissão do vendedor é:",round(parte,2))


# Baseado na entrada no usuario se o numero é maior ou menor que 0

numero = float(input("Digite um número: "))
if numero > 0:
    print("É maior que 0")
else:
    print("É menor que 0")
"""