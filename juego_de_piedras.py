import os

def juego(i):
    ganador = ''
    if(jugada(i) != 0):
        ganador = "El jugador 1 es el ganador"
    else:
        ganador = "El jugador 2 es el ganador"
    return ganador

def jugada(i):
    jugada = 0
    modulo = i % 7
    if(modulo >= 2 and modulo <= 3):
        jugada = 2
    elif(modulo == 4):
        jugada = 3
    elif(modulo >= 5 and modulo <= 6):
        jugada = 5
    return jugada