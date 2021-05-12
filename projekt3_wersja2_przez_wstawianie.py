liczba_testow=int(input())

def insert_sort(list):
    for i in range (1,len(list)):
        r=list[i]
        j=i-1
        while j>=0 and r<list[j]:
            list[j+1]=list[j]
            j=j-1
        list[j+1]=r
    return list


for i in range (0,liczba_testow):
    lista=[]
    n_i_lista=[int(item) for item in input().split()]
    n, lista=n_i_lista[0],n_i_lista[1:]
    if len(lista)==n:
        insert_sort(lista)
        for k in range(len(lista)):
            print(lista[k], end=" ")
