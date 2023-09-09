class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.top = None

    def apilar(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.top
        self.top = nuevo_nodo

    def desapilar(self):
        if self.top is not None:
            valor = self.top.valor
            self.top = self.top.siguiente
            return valor
        else:
            return None

    def recorrido(self):
        nodo_actual = self.top
        while nodo_actual is not None:
            print(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

if __name__ == "__main__":
    pila = Pila()

    for _ in range(5):
        valor = int(input(f"Ingrese un número: "))
        pila.apilar(valor)

    print("\nPila original:")
    pila.recorrido()

    valor_desapilar = int(input("\nIngrese el número que desea desapilar: "))

    pila_temporal = Pila()
    encontrado = False

    while pila.top is not None:
        valor_actual = pila.desapilar()
        if valor_actual == valor_desapilar:
            encontrado = True
            break
        pila_temporal.apilar(valor_actual)

    while pila_temporal.top is not None:
        pila.apilar(pila_temporal.desapilar())

    if encontrado:
        print(f"Se desapiló el valor {valor_desapilar}")
    else:
        print(f"No se encontró el valor {valor_desapilar} en la pila.")

    print("\nPila actualizada:")
    pila.recorrido()
