# Ejercicio 1: Números Perfectos

def suma_divisores(n):
    """
    Calcula la suma de los divisores propios de un número n.
    Un divisor propio es cualquier número menor a n que divida a n exactamente.
    """
    suma = 0
    # Iteramos desde 1 hasta n-1 (no incluimos a n)
    for i in range(1, n):
        # Si el resto de la división es 0, i es divisor de n
        if n % i == 0:
            suma += i
    return suma

def es_perfecto(n):
    """
    Determina si un número es perfecto.
    Un número es perfecto si la suma de sus divisores propios es igual a sí mismo.
    Utiliza la función suma_divisores definida anteriormente.
    """
    # Verificar si el resultado de suma_divisores es igual al número
    if suma_divisores(n) == n:
        return True
    else:
        return False
    
    # También se puede simplificar en una sola línea:
    # return suma_divisores(n) == n

# --- Pruebas ---
if __name__ == "__main__":
    print("Probando números perfectos:")
    # El 6 es un número perfecto (1 + 2 + 3 = 6)
    print("¿6 es perfecto?", es_perfecto(6))
    
    # El 28 es un número perfecto (1 + 2 + 4 + 7 + 14 = 28)
    print("¿28 es perfecto?", es_perfecto(28))
    
    # El 10 no es perfecto (1 + 2 + 5 = 8)
    print("¿10 es perfecto?", es_perfecto(10))
