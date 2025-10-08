tupla_semaforo = ("vermelho","amarelo","verde")

print("Primeira cor",tupla_semaforo[0])
print("Última cor",tupla_semaforo[-1])
print("azul" in tupla_semaforo)

for i in range (0,3):
    print(tupla_semaforo[i])

print(tupla_semaforo.count("vermelho"))