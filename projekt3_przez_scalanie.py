liczba_testow=int(input())


def scalanie(list,p,q,r):
    n=q-p+1
    m=r-q
    lewa=[0]*n
    prawa=[0]*m

    for i in range(0,n):
        lewa[i]=list[p+i]
    for j in range(0,m):
        prawa[j]=list[q+1+j]

    i=0
    j=0
    k=p
    while i<n and j<m:
        if lewa[i]<=prawa[j]:
            list[k]=lewa[i]
            i=i+1
        else:
            list[k]=prawa[j]
            j=j+1
        k=k+1

    while i<n:
        list[k]=lewa[i]
        i=i+1
        k=k+1
    while j<m:
        list[k]=prawa[j]
        j=j+1
        k=k+1
    return list

def merge_sort(list,p,q):
    if p<q:
        srodek=(p+(q-1))//2
        merge_sort(list,p,srodek)
        merge_sort(list,srodek+1,q)
        scalanie(list,p,srodek,q)
    return list


for i in range (0,liczba_testow):
    lista=[]
    n_i_lista=[int(item) for item in input().split()]
    n, lista=n_i_lista[0],n_i_lista[1:]
    if len(lista)==n:
        merge_sort(lista,0,n-1)
        for k in range(len(lista)):
            print(lista[k], end=" ")
