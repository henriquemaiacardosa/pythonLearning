# 1. Verificar Par ou Ímpar
# Peça ao usuário um número inteiro e diga se ele é par ou ímpar.
n1 = int(input("Digite um número: "))
if n1 % 2 == 0:
    print("É par")
else:
    print("É ímpar")

# 2. Divisão de Brigadeiros
# Você tem uma quantidade de brigadeiros e vai dividi-los entre 4 amigos.
# Mostre quantos brigadeiros cada amigo recebe e se sobra algum.
brigadeiros = int(input("Há quantos brigadeiros? "))
amigos = 4
divisao = brigadeiros // 4
brigadeiros %= 4
print(f"Cada amigo ficará com {divisao} brigdeiros e sobrará {brigadeiros}")

# 3. Conversão de Minutos para Horas
# Peça ao usuário uma quantidade de minutos.
# Mostre quantas horas completas cabem e quantos minutos sobram.


# 4. Caixa de Maçãs
# Um produtor tem várias maçãs. Cada caixa comporta 10 maçãs.
# Mostre quantas caixas cheias ele consegue montar e quantas maçãs ficam fora das caixas.


# 5. Caixa Eletrônico Simples
# Peça ao usuário um valor inteiro de saque.
# Mostre quantas notas de R$100, R$50, R$20, R$10, R$5 e R$2 serão entregues.
# (Use // e %= para ir decompondo o valor).


# 6. Conversão de Segundos
# Receba uma quantidade de segundos.
# Converta para horas, minutos e segundos.


# 7. Categoria de Idade
# Peça a idade de uma pessoa e diga se ela é:
# Criança (0–12)
# Adolescente (13–17)
# Adulto (18–64)
# Idoso (65+)


# 8. Notas Escolares
# Peça a nota de um aluno:
# Se for maior ou igual a 7 → "Aprovado"
# Entre 5 e 7 → "Recuperação"
# Menor que 5 → "Reprovado"


# 9. Troco em Moedas
# Peça ao usuário um valor em centavos.
# Mostre quantas moedas de 25, 10, 5 e 1 centavo ele deve receber.


# 10. Senha do Cofre
# Peça ao usuário uma senha (ex: 1234).
# Se for correta → "Acesso liberado".
# Se não → "Senha incorreta".