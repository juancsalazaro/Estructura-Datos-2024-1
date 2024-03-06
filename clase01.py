def sumaArreglo(arreglo):
    suma=0
    for n in arreglo:
        suma+=n
    return suma

def búsquedaEnArreglo(arreglo,aEncontrar):
    for n in arreglo:
        if n==aEncontrar:
            return True
    return False

def ordenamiento_burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def buscar_maximo(arr):
    maximo = arr[0]
    for num in arr:
        if num > maximo:
            maximo = num
    return maximo

def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a+b
        return b

def ordenamiento_seleccion(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def buscar_elemento(arr, objetivo):
    for num in arr:
        if num == objetivo:
            return True
    return False

def eliminar_duplicados(arr):
    unique_elements = []
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements

def multiplicar_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def buscar_subcadena(cadena, subcadena):
    n = len(cadena)
    m = len(subcadena)
    for i in range(n - m + 1):
        if cadena[i:i+m] == subcadena:
            return i
    return -1

def invertir_arreglo(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr

def contar_ocurrencias(arr):
    ocurrencias = {}
    for num in arr:
        if num in ocurrencias:
            ocurrencias[num] += 1
        else:
            ocurrencias[num] = 1
    return ocurrencias


if __name__ == "__main__":
    arreglo=[1,2,3,4,5,6,7,8,9]
    print("La suma del arreglo es: ",sumaArreglo(arreglo))
    print("Estado de búsqueda: ",búsquedaEnArreglo(arreglo,5))
    print(ordenamiento_burbuja(arreglo))
    print(buscar_maximo(arreglo))
    print(fibonacci(6))