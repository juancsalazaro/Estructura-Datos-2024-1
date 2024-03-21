# PILAS

pila=[]

pila.append(1)
pila.append(2)
pila.append(3)
pila.append(4)

print(pila)

pila.pop()

print(pila)

# COLAS
from collections import deque

cola=deque()

cola.append(1)
cola.append(2)
cola.append(3)
cola.append(4)

print(cola)

cola.popleft()

print(cola)

#TABLA HASH

tabla_hash={}

tabla_hash['anios']=21

print(tabla_hash['anios'])

# SET

conjunto= set()

conjunto.add('H')
conjunto.add('O')
conjunto.add('L')
conjunto.add('A')

presente = 'H' in conjunto

print(conjunto)
print(presente)

# PENSAMIENTO RECURSIVO

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

def Fibonacci(n):
    
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
print(Fibonacci(6))