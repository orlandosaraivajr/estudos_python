def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        menores = [x for x in array[1:] if x <= pivot]
        maiores = [x for x in array[1:] if x > pivot]
        return quicksort(menores) + [pivot] + quicksort(maiores)

arr = [15, 3, 6, 8, 10, 1, 2, 1]
print("Array não ordenado:", arr)
arr_ordenado = quicksort(arr)
print("Array ordenado:", arr_ordenado)
