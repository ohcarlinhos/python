# import os
import random

# os.system('cls' if os.name == 'nt' else 'clear')

texto = "abc" # Aspas não fazem diferença entre " ou ' 
numero = 1
numeroDec = 1.4
numeroEmString = "1.5"
booleano = False # Maiúscula: True, False

print(type(texto))
print(type(numero))
print(type(numeroDec))
print(type(booleano))

print(float(numeroEmString))
print(int(float(numeroEmString))) # Assim foi, direto de string não.

if type(texto) == str:
    print("É string")

vaiFuncionar = True

if vaiFuncionar == True:
    print("Funcionou")

vaiFuncionar = False

if vaiFuncionar:
    print("Funcionou")
elif (2 + 2) == 4:
    print("elif é paia haushuashua")
else:
    print("demonstrativo")

# range gera uma sequencia de numeros.
# range(3) de 0 a 2, então se eu passar o tamanho de um array, ele não vai "passar"

print("range(1, 3):")
for item in range(1, 3): # range(1, 3) De 1 ao 2 
    print(item)

print("range com passos range(0, 13, 2):")

# passo do ranger, de 2 em dois range(0, 13, 2)
for item in range(0, 13, 2):
    print(item)

# Listas

nomes = ['Carlos', 'Jep', 'Keke']

print(type(nomes))
print(nomes.index("Keke") == 2)

print(len(nomes[0]))

for l in range(len(nomes[0])):
    print(nomes[0][l])

for i in nomes:
    print(f"O {i} é show!")

for i in range(len(nomes)):
    print(nomes[i])

t = 0
while (t < 3 and True) or False:
    print(t)
    t += 1

numeros = [20, 64, 98]
print(numeros)
numeros.append(55)
print(numeros)
numeros.pop() # passando um indice da pop no indice, ao contrário é o último
print(numeros)

print(random.randint(1, 10))