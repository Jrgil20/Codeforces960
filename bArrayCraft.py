def construct_array(n, x, y):
    a = [0] * n  # Inicializar el arreglo con ceros
    # Paso 1: Llenar con 1 hasta x
    for i in range(x):
        a[i] = 1
    # Paso 2: Llenar con -1 desde x hasta y-1 (si es necesario)
    for i in range(x, y):
        a[i] = -1
    # Paso 3: Llenar con 1 desde y hasta el final
    for i in range(y, n):
        a[i] = 1
    return a

def main():
    t = int(input().strip())  # Leer el número de casos de prueba
    for _ in range(t):
        n, x, y = map(int, input().strip().split())  # Leer n, x, y
        a = construct_array(n, x, y)  # Construir el arreglo
        print(' '.join(map(str, a)))  # Imprimir el arreglo

main()