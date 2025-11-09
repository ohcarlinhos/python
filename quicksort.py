from random import randint

def meu_quicksort (lista: list[int] = []):
    if(len(lista) <= 1):
        return lista
    
    if(len(lista) == 2):
        a = lista[0]
        b = lista[1]
        return [a, b] if b > a else [b, a]

    pivo = lista.pop(randint(0, len(lista) - 1))
    
    menores_que = []
    maiores_que = []
    
    for i in lista:
        if i > pivo:
            maiores_que.append(i)
        else:
            menores_que.append(i)
    
    return meu_quicksort(menores_que) + [pivo] + meu_quicksort(maiores_que)

# Lista 1: Caso comum com números inteiros
lista1 = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]

# Lista 2: Lista já ordenada (melhor caso para alguns pivôs)
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lista 3: Lista em ordem decrescente (pior caso para alguns pivôs)
lista3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Lista 4: Lista com elementos repetidos
lista4 = [5, 2, 8, 2, 5, 1, 8, 8, 3, 1]

# Lista 5: Bônus - Lista vazia e com um elemento
lista5 = []  # Caso base
lista6 = [42]  # Caso base

# Lista 7: Bônus - Lista com números negativos
lista7 = [3, -1, 4, -2, 0, -5, 7, -3, 2]

print(meu_quicksort(lista1))
print(meu_quicksort(lista2))
print(meu_quicksort(lista3))
print(meu_quicksort(lista4))
print(meu_quicksort(lista5))
print(meu_quicksort(lista6))
print(meu_quicksort(lista7))