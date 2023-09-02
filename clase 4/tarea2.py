import random

def crear_lista(num_nodos):                                                             # Definir la función
    lista_generada = []                                                                 # Crear la lista vacía
    for _ in range(num_nodos):                                                          
        numero_aleatorio = random.randint(1, 100)                                       # Generar numero un numero aleatorio
        lista_generada.append(numero_aleatorio)                                         
    return lista_generada                                                               # Devuelve la lista completa

num_nodos = int(input("Ingrese el número de nodos a crear: "))                          # Pedír el numero de nodos al usuario
lista_generada = crear_lista(num_nodos)                                                 # Lamar la función
print("Lista generada:", lista_generada)                                                # Imprimir el numero de nodos
