def divideAndConquer_Max(arr, ind, len):
    maximum = -1

    if (ind >= len - 2):
        if (arr[ind] > arr[ind + 1]):
            return arr[ind]
        else:
            return arr[ind + 1]

    maximum = divideAndConquer_Max(arr, ind + 1, len)

    if (arr[ind] > maximum):
        return arr[ind]
    else:
        return maximum


def divideAndConquer_Min(arr, ind, len):
    minimum = 0
    if (ind >= len - 2):
        if (arr[ind] < arr[ind + 1]):
            return arr[ind]
        else:
            return arr[ind + 1]

    minimum = divideAndConquer_Min(arr, ind + 1, len)

    if (arr[ind] < minimum):
        return arr[ind]
    else:
        return minimum

minimum, maximum = 0, -1

# Inicializamos el arreglo
arr = [6, 4, 8, 90, 12, 56, 7, 1, 63]

maximum = divideAndConquer_Max(arr, 0, 9)
minimum = divideAndConquer_Min(arr, 0, 9)

print("El minimo numero en el arreglo es: ", minimum)
print("El maximo numero en el arreglo es: ", maximum)