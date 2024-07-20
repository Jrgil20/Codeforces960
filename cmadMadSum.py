def encontrar_mad(arreglo):
    """
    Encuentra el Máximo Duplicado Apareciendo (MAD) en el arreglo.
    Si no existe tal número, devuelve 0.
    """
    frecuencia = {}
    mad = 0
    for num in arreglo:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1
        if frecuencia[num] > 1:
            mad = max(mad, num)
    return mad

def procesar_arreglo(arreglo):
    """
    Procesa el arreglo según las reglas dadas y devuelve la suma final.
    """
    suma_total = 0
    while any(arreglo):  # Continuar hasta que todos los elementos sean 0
        suma_total += sum(arreglo)
        arreglo = [encontrar_mad(arreglo[:i+1]) for i in range(len(arreglo))]
    return suma_total

def resolver():
    t = int(input().strip())  # Número de casos de prueba
    for _ in range(t):
        n = int(input().strip())  # Tamaño del arreglo
        arreglo = list(map(int, input().strip().split()))  # El arreglo en sí
        print(procesar_arreglo(arreglo))


resolver()