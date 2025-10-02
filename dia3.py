"""""
senha = "Teste123"
senhaDigitada = "teste123"
verificacaoSenha = senhaDigitada == senha
print("As senhas coincidem?", verificacaoSenha)

pao = 3.50
leite = 4.20
cafe = 2.80
valorPago = 20
valorAreceber = valorPago - (pao+leite+cafe)
print(valorAreceber)

n1 = 8.5
frequencia = 80
aprovadoNota = n1 >= 7
aprovadoFrequancia = frequencia >= 75
aprovado = (n1 >= 7) and (frequencia >= 75)

print(aprovadoNota and aprovadoFrequancia != False)
print("O estudante foi aprovado?", aprovado)

qntItens = int(input("Quantidade: "))
valorTotal = float(input("Valor: "))
desconto = (qntItens > 10) or (valorTotal > 100)
print("Ganhou o desconto?", desconto)

conta = 150
amigos = 3
print("Valor a pagar: ", conta / amigos)
conta = (conta % amigos ) == 0
print("Conta exata? ",conta)

idade = int(input("Qual a sua idade? "))
podeAssitir = idade > 16
print(podeAssitir)

pesoKg = float(input("Digite o seu peso: "))
alturaM = float(input("Digite sua altura: "))
imc = pesoKg / (alturaM ** 2)
resultado = ( 18.5 <= imc <= 24.9) # (imc >= 18.5) and (imc <= 24.9)
print("Peso ideal? ",resultado)   
print(f"Seu imc é: {imc:.2f}")

n1 = int(input("Digite um número inteiro: "))
par = n1 % 2 == 0
impar = n1 % 2 != 0
print("É par: ",par)
print("É impar: ",impar)
"""""