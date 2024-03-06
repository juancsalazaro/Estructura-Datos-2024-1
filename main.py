# LISTAS

def addToList():
    lista=[]
    estado=True
    while estado:
        opcion=input("Desea ingresar un dato: 1, salir: 0: ")
        if opcion == "1":
            dato=input("Dato a ingresar: ")
            lista.append(dato)
            print(lista)
        else:
            print(lista)
            estado=False

def removeDuplicate():
    arreglo=[1,2,3,4,5,6,54,3,2,6,7,8,3,21]
    arregloSinDuplicado=[]
    for n in arreglo:
        if n not in arregloSinDuplicado:
            arregloSinDuplicado.append(n)
    return arregloSinDuplicado

def sumToLisr():
    arreglo=[1,2,3,4,5,6,54,3,2,6,7,8,3,21]
    suma=0
    for n in arreglo:
        suma += n
    return suma

def compareTwoList():
    arregloOne=[1,2,3,4,5,6,7,8,9,0]
    arregloTwo=[10,11,12,13,14,0]
    for n in arregloOne:
        if n  in arregloTwo:
            return True
    return False

def sumCircularList():
    matriz=[
          [1,2,3],
          [4,5,6],
          [7,8,9]
          ]
    total_resta=matriz[0][0]
    filas = len(matriz)
    columnas = len(matriz[0])

    print("Filas: ",filas)
    print("Columnas: ",columnas)

    limite_superior = 0
    limite_inferior = filas - 1
    limite_izquierdo = 0
    limite_derecho = columnas - 1

    print(limite_superior)
    print(limite_inferior)
    print(limite_izquierdo)
    print(limite_derecho)

    while limite_superior <= limite_inferior and limite_izquierdo <= limite_derecho:
        # Recorrido de arriba hacia abajo
        print("rango ↑ ↓:", limite_superior, limite_inferior+1)
        for i in range(limite_superior, limite_inferior + 1):
            total_resta -= matriz[i][limite_izquierdo]
        limite_izquierdo += 1

        # Recorrido de izquierda a derecha
        print("rango ← →:", limite_izquierdo, limite_derecho+1)
        for i in range(limite_izquierdo, limite_derecho + 1):
            total_resta -= matriz[limite_inferior][i]
        limite_inferior -= 1

        # Recorrido de abajo hacia arriba (si es necesario)
        if limite_superior <= limite_inferior:
            print("rango ↓ ↑:", limite_superior, limite_inferior)
            for i in range(limite_inferior, limite_superior - 1, -1):
                total_resta -= matriz[i][limite_derecho]
            limite_derecho -= 1

        # Recorrido de derecha a izquierda (si es necesario)
        if limite_izquierdo <= limite_derecho:
            print("rango → ←:", limite_izquierdo, limite_derecho)
            for i in range(limite_derecho, limite_izquierdo - 1, -1):
                total_resta -= matriz[limite_superior][i]
            limite_superior += 1

    return total_resta

if __name__ == '__main__':
    # addToList()
    # print("--------------------------")
    # print(removeDuplicate())
    # print("--------------------------")
    # print(sumToLisr())
    # print("--------------------------")
    # print(compareTwoList())
    print(sumCircularList())