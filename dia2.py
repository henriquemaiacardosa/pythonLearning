"""
print("----------------------------------------")

idade = 22
nome = "Henrique"
altura = 1.65
pesoQuilogramas = 49

print("Seu nome é: ",nome,", tem ",idade," anos, pesa ",pesoQuilogramas,"kgs e mede: ",altura, sep="")
# Usar o sep="" para tirar os espaços, sep é um parâmetro da função print() que define o separador usado entre os argumentos passados no exemplo acima o separador usado foi ter tirao os espaços

print("----------------------------------------")

dia = 21
mes = 8
ano = 2025
print(dia,mes,ano, sep="/")

print("----------------------------------------")

print(type(idade))
print(type(nome))
print(type(altura))
print(type(pesoQuilogramas))
print(type(dia))
print(type(mes))
print(type(ano))

print("----------------------------------------")

bool = True
bool2 = False

print(bool, bool2)

print("----------------------------------------")

print("Operações numéricas")
n1Soma = 4375
n2Soma = 345
print(n1Soma + n2Soma)

print("----------------------------------------")

concatenar = "Oi"
concatenar2 = ",tudo bem?"
print(concatenar + concatenar2)

print("----------------------------------------")

estudante = True

print("Nome:",nome)
print("Idade:",idade)
print("Altura:",altura)
print("Estudante:",estudante)

print("----------------------------------------")

print("Cálculo de Idade")
anoAtual = 2025
anoNascimento = anoAtual - (idade+1)
print("Nasceu em:", anoNascimento)

maiorDeIdade = idade >= 18
print("Maior de idade?",maiorDeIdade)

print("----------------------------------------")


frase = "Olá, meu nome é: " + nome + " e eu tenho " + str(idade) + " anos."

print(frase)

print("----------------------------------------")

print("Calculadora")

n1 = float(input("Digite N1: "))
n2 = float(input("Digite N2: "))

adicao = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2

print("Soma ", adicao)
print("Subtração ", subtracao)
print("Multiplicação ", multiplicacao)
print("Divisão", divisao)
print("----------------------------------------")

print("Conversor de Temperatura")
celsius = float(input("Celsius: "))

conversao = celsius * 9/5 + 32
print("Fahrenheit: ", conversao)

print("----------------------------------------")

raio = float(input("Digite o raio: "))
pi = 3.14159
area = pi * raio ** 2
print("A área do seu circulo é: ", area)
"""


