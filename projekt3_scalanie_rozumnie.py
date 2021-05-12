#to niby działa, ale recursja za dużo razy i nie może przemielić (overflow się to chyba nazywa)

liczba_testow=int(input())


def scalanie(list_a,list_b,list):
    dlugosc_a=len(list_a)
    dlugosc_b=len(list_b)
    i=j=k=0

    while i<dlugosc_a and j<dlugosc_b:
        if list_a[i]<=list_b[j]:
            list[k]=list_a[i]
            i=i+1
        else:
            list[k]=list_b[j]
            j=j+1
        k=k+1

    while i<dlugosc_a:
        list[k]=list_a[i]
        i=i+1
        k=k+1

    while j<dlugosc_b:
        list[k]=list_b[j]
        j=j+1
        k=k+1

    return list

def merge_sort(list):
    srodek=len(list)//2
    lewa=list[:srodek]
    prawa=list[srodek:]
    lewa=merge_sort(lewa)
    prawa=merge_sort(prawa)
    list=scalanie(lewa,prawa,list)

    return list


for i in range (0,liczba_testow):
    lista=[]
    n_i_lista=[int(item) for item in input().split()]
    n, lista=n_i_lista[0],n_i_lista[1:]
    if len(lista)==n:
        merge_sort(lista)
        for k in range(len(lista)):
            print(lista[k], end=" ")
