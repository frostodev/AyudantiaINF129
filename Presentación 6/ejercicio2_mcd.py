# Ejercicio 2: MCD Recursivo (Algoritmo de Euclides)

def mcd(a, b):
    """
    Calcula el Máximo Común Divisor entre a y b de forma recursiva,
    usando el algoritmo de Euclides.
    """
    # Caso base: Si b es 0, el MCD es a.
    # En este punto, a contiene el último divisor que no dejó resto.
    if b == 0:
        return a
    
    # Paso recursivo: Llamamos a la función con 'b' y el resto de 'a % b'
    else:
        resto = a % b
        return mcd(b, resto)
        # Nota para los alumnos: Se puede hacer directamente así:
        # return mcd(b, a % b)

# --- Pruebas ---
if __name__ == "__main__":
    print("Calculando el MCD de forma recursiva:")
    
    # El MCD entre 48 y 18 es 6
    print("MCD(48, 18) =", mcd(48, 18))
    
    # El MCD entre 101 y 103 es 1 (son números primos entre sí)
    print("MCD(101, 103) =", mcd(101, 103))
    
    # El MCD entre 56 y 98 es 14
    print("MCD(56, 98) =", mcd(56, 98))
