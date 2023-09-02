edades = [25,19,3,11,44]

def promedio_edades (edades) :
    suma = 0
    for n in edades:
        suma = suma + n
    return suma / len(edades)

promedio = promedio_edades(edades)
print(f"El promedio es: {promedio}")