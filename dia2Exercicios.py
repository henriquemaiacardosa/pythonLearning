"""""
#Crie uma variável chamada nome e armazene seu nome nela. Exiba com print().
nome = input("Digite seu nome: ")
print("Seu nome",nome)
print("------------------------------------")

# Crie duas variáveis, idade e cidade, e mostre uma frase: "Tenho X anos e moro em Y".
idade = float(input("Digite sua idade: "))
cidade = (input("Digite sua cidade: "))
print("Tenho ", idade," anos e moro em ",cidade, sep="")
print("------------------------------------")

# Crie uma variável altura e mostre no console: "Minha altura é ___ metros".
altura = float(input("Altura: "))
print("Sua altura é:",altura)
print("------------------------------------")

#Crie três variáveis (dia, mes, ano) e exiba a data formatada: "DD/MM/AAAA".
dia = input("Digite um dia:")
mes = input("Digite um mês:")
ano = input("Digite um ano:")
print("A data que você digitou é:")
print(dia,mes,ano,sep="/")
print("------------------------------------")

#Armazene seu sobrenome em uma variável e mostre em letras maiúsculas.
sobrenome = input("Digite o seu sobrenome: ")
print
(sobrenome.upper())
print("------------------------------------")

#Armazene uma frase em mensagem e exiba a quantidade de caracteres usando len().
frase = ("Essa frase tem diversar caracteres")
qtdFrase = len(frase)
print(qtdFrase)
print("------------------------------------")

#Crie uma variável esporte e exiba: "Meu esporte favorito é: ___".
esporte = input("Digite um esporte: ")
print("Seu esporte é: ", esporte)
print("------------------------------------")

#Crie uma variável curso e mostre: "Estou aprendendo Python no curso ___".
curso = input("Digite o nome do seu curso de Python: ")
print("Estou aprendendo Python no curso: ",curso)
print("------------------------------------")

#Crie uma variável pais e exiba: "Eu moro no(a) ___".
pais = input("Em qual país você mora? ")
print("Você mora no",pais)
print("------------------------------------")

#Crie duas variáveis (animal, cor) e exiba: "Meu animal favorito é um ___ da cor ___".
animal = input("Qual o seu animal favorito?")
cor = input("Qual cor desse animal, você prefere?")
print("Meu animal favorito é um",animal,"da cor", cor)
print("------------------------------------")

#Crie duas variáveis inteiras e exiba a soma delas.
n1 = 5
n2 = 3
print(n1+n2)
soma = n2+n1
print(soma)
print("------------------------------------")

#Crie duas variáveis inteiras e exiba a subtração.
n1 = 543
n2= 37
print(n1-n2)
subtracao = n2 - n1
print(subtracao)
print("------------------------------------")

#Crie duas variáveis inteiras e exiba a multiplicação.
n1 = 5436
n2 = 77
print(n1*n2)
multi = n2 *n1
print(multi)
print("------------------------------------")

#Crie duas variáveis inteiras e exiba a divisão.
n1 = 56
n2 = 3
print(n1/n2)
divisao = n2 / n1
print(divisao)
print("------------------------------------")

#Crie duas variáveis inteiras e exiba o resto da divisão (%).
n1 = 7
n2 = 8
print(n1/n2)
divisao = n2/n2
print(divisao)
print("------------------------------------")

#Crie duas variáveis floats e exiba a soma delas.
n1 = 7.568
n2 = 45.63
print(n1+n2)
soma2 = n2+n2
print(soma2)
print("------------------------------------")

#Crie uma variável pi com valor 3.14 e mostre "O valor de pi é: ___".
pi = 3.14
print("O valor de pi é:",pi)
print("------------------------------------")

#Crie uma variável preco (float) e quantidade (int) e exiba o valor total (preço * quantidade).
preco = float(input("Digite o preço do item:"))
quantidade = int(input("Digite a quantidade do item:"))
valor = preco * quantidade
print("O valor do compra é: ",valor)
print("------------------------------------")

#Crie duas variáveis, nota1 e nota2, e exiba a média aritmética.
nota1 = float(input("Digite a N1: ")) 
nota2 = float(input("Digite a N2: "))
media = (nota1 + nota2)/2
print(f"A media do aluno é {media:.2f}")
print("------------------------------------")

#Armazene sua altura em metros (float) e seu peso (float), depois calcule o IMC = peso / altura².
alturaMetros = float(input("Digite sua altura:")) 
pesoKGs = float(input("Digite seu peso:"))
imc = pesoKGs / alturaMetros**2
print(f"Seu IMC é:{imc:.2}")
print("------------------------------------")

#Armazene seu nome em uma variável e exiba apenas a primeira letra.
nome = "Henrique"
print(nome[0])
print("------------------------------------")

#Crie uma string e exiba em letras minúsculas.
string = "BATATA"
print(string.lower)
print("------------------------------------")

#Crie uma string e exiba em letras maiúsculas.
palavra = "abacaxi"
print(palavra.upper()[1])
print("------------------------------------")

#Armazene seu nome e sobrenome em duas variáveis e junte-as em uma só string.
nome = "Henrique"
sobrenome = "Maia Cardosa"
print(nome + " " + sobrenome)
print(f"{nome} {sobrenome}")
print("------------------------------------")

#Armazene uma frase e exiba apenas os 5 primeiros caracteres.
frase = "O carro é rápido"
print(frase[0:5])
print("------------------------------------")

#Crie uma string e exiba apenas os 3 últimos caracteres.
frase = "Essa frase será muito longa para testar o slicing do Python"
print(frase[-3:])
print("------------------------------------")

#Crie uma string e verifique o tamanho dela (len()).
clima = "frio"
print(len(clima))
print("------------------------------------")

#Crie uma string e exiba quantas vezes aparece a letra "a".
clima = "frio"
print(clima.count("a"))
print("------------------------------------")

#Crie uma string e substitua uma palavra por outra (replace).
palavra = "palavra"
print(palavra.replace("palavra","outra"))
print("------------------------------------")

#Armazene uma palavra e exiba-a invertida ([::-1]).
palavra = "Trem"
print(palavra[::-1])
print("------------------------------------")

#Crie uma variável booleana chovendo = True e exiba.
chovendo = True
print(chovendo)
print("------------------------------------")

#Crie uma variável sol = False e mostre no print: "Está ensolarado? ___".
sol = False
print(f"Está ensolarado? {sol}")
print("------------------------------------")

#Crie duas variáveis inteiras e verifique se são iguais.
n1 = 5
n2 = 5
comparacao = n1 == n2
print(comparacao)
n3 = 7
n4 = 8
comparacao2 = n3 == n4
print(comparacao2)
print("------------------------------------")

#Verifique se um número é maior que outro.
maior = 6 > 8
print(maior)
maior2 = 8 > 6
print(maior2)
print("------------------------------------")

#Verifique se um número é menor ou igual a outro.
menorIgual = 3 <= 4
print(menorIgual)
print("------------------------------------")

#Crie duas variáveis booleanas (estudando, cansado) e use and para exibir o resultado.
estudando = True
cansado = False
print(estudando and cansado)
print("------------------------------------")

#Use or entre duas variáveis booleanas e exiba o resultado.
preto = True
branco = False
print(preto or branco)
print("------------------------------------")

#Inverta uma variável booleana com not.
sol = True
print(not sol)
print("------------------------------------")

#Crie uma variável idade = 18 e verifique se ela é maior ou igual a 18.
idade = 17
maiorIdade = 17 >= 18
print(maiorIdade)
print("------------------------------------")

#Crie uma variável nota = 7 e verifique se ela é maior ou igual a 6 (aprovado ou reprovado).
nota = 6
aprovado = nota >6
reprovado = nota <=6
print(aprovado)
print(reprovado)
print("------------------------------------")

#Converta um número inteiro para string e exiba com print().
n1 = 10
print(str(f"{n1}"))
print("------------------------------------")

#Converta uma string "100" para número inteiro e some + 50.
string = "100"
numero  = int(string)
print(numero + 50)
print("------------------------------------")

#Converta uma string "3.5" para float e multiplique por 2.
a1 = "3.5"
n1 = float(a1)
mult = n1 * 2
print(mult)
print("------------------------------------")

#Armazene um número inteiro e converta para float.
n1 = 5
n2 = float(n1)
print(n2)
print("------------------------------------")

#Armazene um número float e converta para inteiro.
n1 = 5.0
n2 =float(n1)
print(n2)
print("------------------------------------")

#Converta uma variável booleana True em inteiro.
booleana = 5 == 5
inteiro = int(booleana)
print(inteiro)
print("------------------------------------")

#Converta um número inteiro 0 em booleano.
n1 = 0
b1 = bool(n1)  
print(b1)
print("------------------------------------")
#Converta uma string "False" para booleano e exiba o tipo.
string = "False"
troca = bool(string)
print(type(troca))

print("------------------------------------")
#Leia uma string "25" e some com outro número inteiro 5 (após conversão).
string = "25"
n = int(string)
n1 = n + 5
print(n1)
print("------------------------------------")

#Crie três variáveis de tipos diferentes (int, float, str), converta todas para string e junte em uma frase.
int = 22
float = 1.65
str = "São meu peso e altura"
print(f"{int} {float} {str}")
"""





