import random

n, m = map(int, input('Introduce las dimensiones del laberinto (Ej. 2 3): ').split())
k = int(input('Introduce el numero de tuneles que tendra el laberinto: '))
N = n * m
z = [input('Introduce los obstaculos: ').strip() for _ in range(n)]
t = list(range(N + 1))
for _ in range(k):
    a, b, c, d = map(int, input('Introduce las coordenadas de los tuneles. Ej.(2 3): ').split())
    a = (a - 1) * m + b - 1
    b = (c - 1) * m + d - 1
    t[a] = b
    t[b] = a