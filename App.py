# REPASO

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

if __name__ == "__main__":
    arreglo=[1,2,3,4,5,6,7,8,9]
    print("La suma del arreglo es: ",sumaArreglo(arreglo))
    print("Estado de búsqueda: ",búsquedaEnArreglo(arreglo,5))
