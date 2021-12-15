from fractions import Fraction as F

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

k = 0
g = [[set(), set(), F(0)] for _ in range(N + 1)]
d = set(range(N))
inicio = None

for i in range(n):
    for j in range(m):
        if z[i][j] == 'A':
            d.remove(k)
            inicio = k
        if z[i][j] == '%':
            g[k][1].add(N)
        elif z[i][j] in 'OA':
            if i > 0 and z[i - 1][j] != '#':
                g[k][1].add(t[k - m])
            if i + 1 < n and z[i + 1][j] != '#':
                g[k][1].add(t[k + m])
            if j > 0 and z[i][j - 1] != '#':
                g[k][1].add(t[k - 1])
            if j + 1 < m and z[i][j + 1] != '#':
                g[k][1].add(t[k + 1])
        k += 1

for i, j in enumerate(g):
    if j[1]:
        for k in j[1]:
            g[k][0].add(i)
        k = F(1, len(j[1]))
        j[1] = {l: k for l in j[1]}

while d:
    v = d.pop()
    gv = g[v]
    if all(gv[:2]):
        loop = 1 / (1 - gv[2])
        for u in gv[0]:
            gu = g[u]
            uv = gu[1].pop(v)
            for w, c in gv[1].items():
                if w == u:
                    gu[2] += uv * loop * c
                else:
                    gu[1][w] = uv * loop * c + gu[1].get(w, 0)
                    g[w][0].add(u)
                    g[w][0].discard(v)

a, b, c = g[inicio]
if N in b:
    print('La probabilidad de que Alef salga del laberinto es de: ' + str(float(b[N] / (1 - c))))
else:
    print('La probabilidad de que Alef salga del laberinto es de: 0')