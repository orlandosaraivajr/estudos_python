def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    meio = len(arr) // 2
    esquerda = arr[:meio]
    direita = arr[meio:]
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

arr = [15, 3, 6, 8, 10, 1, 2, 1]
print("Array não ordenado:", arr)
arr_ordenado = merge_sort(arr)
print("Array ordenado:", arr_ordenado)