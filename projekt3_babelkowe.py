liczba_testow=int(input())

def bubble_sort(list):
    dlugosc=len(list)
    for i in range (dlugosc-1):
        for j in range(0, dlugosc-i-1):
            if list[j]>list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


for i in range (0,liczba_testow):
    lista=[]
    n_i_lista=[int(item) for item in input().split()]
    n, lista=n_i_lista[0],n_i_lista[1:]
    if len(lista)==n:
        bubble_sort(lista)
        for k in range(len(lista)):
            print(lista[k], end=" ")
