"""
   no funciona para el caso de prueba
"""


def alice_wins(n, a):
    # Ordenar el arreglo para trabajar con los elementos de manera eficiente
    a.sort()
    # Inicializar mx a 0
    mx = 0
    # Contar el número de movimientos posibles
    moves = 0
    for i in range(n):
        if a[i] >= mx:
            # Actualizar mx y contar el movimiento
            mx = a[i]
            moves += 1
            a[i] = 0  # Simular el movimiento estableciendo el elemento a 0
            # Actualizar mx para reflejar que el elemento más grande ahora es 0
            mx = max(a)
    # Determinar si Alice gana (número impar de movimientos)
    return "YES" if moves % 2 == 1 else "NO"

def main():
    t = int(input().strip())  # Leer el número de casos de prueba
    for _ in range(t):
        n = int(input().strip())  # Leer el tamaño del arreglo
        a = list(map(int, input().strip().split()))  # Leer los elementos del arreglo
        print(alice_wins(n, a))

main()