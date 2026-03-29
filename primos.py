"""
Números Primos: módulo de gestión de números primos
Martí Fontseca

>>> import primos
>>> primos.esPrimo(91)
False
"""

from sympy import isprime

def esPrimo(numero):
    """
    Devuelve True si su parámetro es primo, False si no lo es.

    >>> import primos
    >>> primos.esPrimo(97)
    True
    """

    return isprime(numero)

from doctest import testmod
testmod()


def primos(numero):
    """Devuelve una tupla con todos los números primos menores que su argumento."""
    return tuple(n for n in range(2, numero) if esPrimo(n))

def descompon(numero):
    """Devuelve una tupla con la descomposición en factores primos."""
    factores = []
    d = 2
    n = numero
    while n > 1:
        while n % d == 0:
            factores.append(d)
            n //= d
        d += 1
    return tuple(factores)

def mcm(*numeros):
    """Mínimo común múltiplo de un número arbitrario de argumentos."""
    todos = {}
    for n in numeros:
        f_n = descompon(n)
        for f in set(f_n):
            todos[f] = max(todos.get(f, 0), f_n.count(f))
    
    res = 1
    for f, exp in todos.items():
        res *= f**exp
    return res

def mcd(*numeros):
    """Máximo común divisor de un número arbitrario de argumentos."""
    res_factores = None
    for n in numeros:
        f_n = descompon(n)
        conteo = {f: f_n.count(f) for f in set(f_n)}
        if res_factores is None:
            res_factores = conteo
        else:
            res_factores = {f: min(res_factores[f], conteo[f]) 
                            for f in res_factores if f in conteo}
    
    res = 1
    for f, exp in res_factores.items():
        res *= f**exp
    return res

from doctest import testmod
if __name__ == "__main__":
    testmod(verbose=True)