liczba_testow=int(input())

def select_sort(list):
    for i in range(len(list)):
        najmniejsza=i
        for j in range (i+1,len(list)):
            if list[najmniejsza]>list[j]:
                najmniejsza=j
        list[i], list[najmniejsza]=list[najmniejsza], list[i]
    return list


for i in range (0,liczba_testow):
    lista=[]
    n_i_lista=[int(item) for item in input().split()]
    n, lista=n_i_lista[0],n_i_lista[1:]
    if len(lista)==n:
        select_sort(lista)
        for k in range(len(lista)):
            print(lista[k], end=" ")
