from random import randint

lista_ordenada = [
    2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78, 89, 91, 95, 102, 115, 128, 134, 147, 156,
    167, 178, 189, 192, 201, 215, 223, 234, 245, 256, 267, 278, 289, 291, 305, 312, 323,
    334, 345, 356, 367, 378, 389, 392, 401, 415, 423, 434, 445, 456, 467, 478, 489, 491,
    502, 515, 523, 534, 545, 556, 567, 578, 589, 592, 601, 615, 623, 634, 645, 656, 667,
    678, 689, 692, 701, 715, 723, 734, 745, 756, 767, 778, 789, 792, 801, 815, 823, 834,
    845, 856, 867, 878, 889, 892, 901, 915, 923, 934, 945, 956, 967, 978, 989, 992, 1001,
    1015, 1023, 1034, 1045, 1056, 1067, 1078, 1089, 1092, 1101, 1115, 1123, 1134, 1145,
    1156, 1167, 1178, 1189, 1192, 1201, 1215, 1223, 1234, 1245, 1256, 1267, 1278, 1289,
    1292, 1301, 1315, 1323, 1334, 1345, 1356, 1367, 1378, 1389, 1392, 1401, 1415, 1423,
    1434, 1445, 1456, 1467, 1478, 1489, 1492, 1501, 1515, 1523, 1534, 1545, 1556, 1567,
    1578, 1589, 1592, 1601, 1615, 1623, 1634, 1645, 1656, 1667, 1678, 1689, 1692, 1701,
    1715, 1723, 1734, 1745, 1756, 1767, 1778, 1789, 1792, 1801, 1815, 1823, 1834, 1845,
    1856, 1867, 1878, 1889, 1892, 1901, 1915, 1923, 1934, 1945, 1956, 1967, 1978, 1989,
    1992, 2000
]

def pesquisa_binaria(lista: list[int] = [], item = 0, ):
    print(f"Entrada: {item}")
    topo = len(lista) - 1
    base = 0

    chute_index = int(topo / 2)
    chute = lista [chute_index]
    
    contador = 0

    while(True):
        contador += 1
        print(f"Contador: {contador}, Chute: {chute}")

        if(topo <= base):
            print(base, topo)
            print(f"O número {item} não está presente na lista.")
            break

        if item == chute:
            print(f"O index de {item} é {chute_index}")
            return chute_index

        elif(item > chute):
            base = chute_index + 1
            
        elif(item < chute):
            topo = chute_index - 1

        chute_index = int((topo - base) / 2) + base 
        chute = lista[chute_index]
    
    return None

print("idx:", pesquisa_binaria(lista_ordenada, 915))
print("idx:", pesquisa_binaria(lista_ordenada, 189))
