import sys
import time

sys.setrecursionlimit(2000)


def factorial(n):
    respuesta = 1
    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta


def factorial_r(n):
    if n <= 1:  
        return 1
    return n * factorial_r(n - 1)


if __name__ == '__main__':
    n = 1000

    print('--- Versión Iterativa ---')
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(f'Tiempo: {final - comienzo} segundos')

    print('\n--- Versión Recursiva ---')
    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(f'Tiempo: {final - comienzo} segundos')