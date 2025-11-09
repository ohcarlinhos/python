def soma (lista: list[int] = []):
    if len(lista) <= 0:
        return 0

    return lista.pop() + soma(lista)


print(soma([4,5,6,10])) # 25
print(soma([2,4,6])) # 12

def tamanhoLista (lista: list[int] = []):
    try:
        lista.pop()
        return 1 + tamanhoLista(lista)
    except:
        return 0
    
print(tamanhoLista([])) # 0
print(tamanhoLista([4,5,6,10])) # 4
print(tamanhoLista([2,4,6])) # 3

def maiorNumero (lista: list[int] = [], maior = 0):
    if (len(lista) <= 0):
        return maior

    i = lista.pop()   
    if i > maior:
        return maiorNumero(lista, i)
    else:
        return maiorNumero(lista, maior)

print(maiorNumero([])) # 0
print(maiorNumero([4,5, 88, 126, 12,6,10])) # 126
print(maiorNumero([2,4,6])) # 6


def pesquisaBinariaRecursiva (lista: list[int] = [], numero: int = 0, baixo = None, alto = None):
    if baixo == None:
        baixo = 0
    if alto == None:
        alto = alto = len(lista) - 1
    
    if baixo > alto:
        return None

    meio = (baixo + alto) // 2

    if lista[meio] > numero:
        return pesquisaBinariaRecursiva(lista, numero, baixo, meio - 1)
    if lista[meio] < numero:
        return pesquisaBinariaRecursiva(lista, numero, meio + 1, alto)
    
    return meio

lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
         21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
         41, 43, 45, 47, 49, 51, 53, 55, 57, 59,
         61, 63, 65, 67, 69, 71, 73, 75, 77, 79,
         81, 83, 85, 87, 89, 91, 93, 95, 97, 99,
         101, 103, 105, 107, 109, 111, 113, 115, 117, 119,
         121, 123, 125, 127, 129, 131, 133, 135, 137, 139,
         141, 143, 145, 147, 149, 151, 153, 155, 157, 159,
         161, 163, 165, 167, 169, 171, 173, 175, 177, 179,
         181, 183, 185, 187, 189, 191, 193, 195, 197, 199]

print("idx", pesquisaBinariaRecursiva(lista, 95), 95, lista[47])
print("idx", pesquisaBinariaRecursiva(lista, 1), 1, lista[0])
print("idx", pesquisaBinariaRecursiva(lista, 199), 199, lista[99])
print("idx", pesquisaBinariaRecursiva(lista, 200), 200)
print("idx", pesquisaBinariaRecursiva(lista, -10), -10)

def buscaMenor(array: list[int]):
    menor = array[0]
    menor_i = 0

    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
            menor_i = i
    
    return menor_i

print('indice do menor', buscaMenor([2,3,1,4,1]))

def ordenacaoPorSelecao(array: list[int] = []):
    arrayOrdenado = []

    for i in range(len(array)):
        menor_i = buscaMenor(array)
        arrayOrdenado.append(array.pop(menor_i))
    
    return arrayOrdenado

print(ordenacaoPorSelecao([2,3,1,60,4,1]))
print(ordenacaoPorSelecao([42, 7, 19, 3, 56, 23, 11]))