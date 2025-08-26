"""
# estrutura  de repetição
# repetir N vezes
# onde N, a gente pode definir
# ou N é uma condição

frutas = ["maçã","banana","laranja"]

for fruta in frutas:
    print("Eu gosto de", fruta)

for i in range(5):
    print("Número:", i)

contador = 0
while contador < 5:
    print("Contagem: ", contador)
    contador += 1
    
for numero in range(10):
    if numero == 5:
         break
    print("Número: ",numero)
    
for numero in range(5):
    if numero == 2:
        continue
    print("Numero",numero)

for numero in range (1, 11):
    print(numero)
"""
n = int(input("Digite um número inteiro positivo: "))
soma = 0
for soma in range(1, n):
    soma += 1
print(f"A soma de 1 até {n} é: ",soma)
