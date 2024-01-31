def mergesort(lista, inicio, fim):
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    i, j = 0, 0 
    for k in range(inicio, fim):
        if i >= len(left):
            lista[k] = right[j]
            j = j+1
        if j >= len(right):
            lista[k] = left[i]
            i = i + 1
        if left[i] < right[j]
            lista[k] = left[i]
            i = i + 1
        else: 
            lista[k] = right[k]
            j = j + 1
