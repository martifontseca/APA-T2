"""
Tarea 2: APA números primos 
Martí Fontseca

Tests unitarios solicitados:
>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)
>>> mcm(90, 14)
630
>>> mcd(924, 780)
12
>>> mcm(42, 60, 70, 63)
1260
>>> mcd(840, 630, 1050, 1470)
210
"""

def esPrimo(numero):
    """Retorna True si el número es primo, False en caso contrario."""
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El argumento debe ser un número natural mayor que 1.")
    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos(numero):
    """Retorna una tupla con los números primos menores que 'numero'."""
    resultado = []
    for n in range(2, numero):
        if esPrimo(n):
            resultado.append(n)
    return tuple(resultado)

def descompon(numero):
    """Realiza la descomposición en factores primos de un número."""
    factores = []
    divisor = 2
    temp = numero
    while temp > 1:
        if temp % divisor == 0:
            factores.append(divisor)
            temp //= divisor
        else:
            divisor += 1
    return tuple(factores)

def mcd(*numeros):
    """Calcula el Máximo Común Divisor de uno o más números."""
    if not numeros:
        return None
    
    listas_factores = [descompon(n) for n in numeros]
    candidatos = set(listas_factores[0])
    resultado = 1
    
    for f in candidatos:
        conteos = [factores.count(f) for factores in listas_factores]
        min_apariciones = min(conteos)
        resultado *= (f ** min_apariciones)
        
    return resultado

def mcm(*numeros):
    """Calcula el Mínimo Común Múltiple de uno o más números."""
    if not numeros:
        return None
    
    listas_factores = [descompon(n) for n in numeros]
    
    todos_los_factores = set()
    for lista in listas_factores:
        for f in lista:
            todos_los_factores.add(f)
            
    resultado = 1
    for f in todos_los_factores:
        max_apariciones = max(lista.count(f) for lista in listas_factores)
        resultado *= (f ** max_apariciones)
        
    return resultado

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)