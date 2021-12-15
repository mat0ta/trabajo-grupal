import math
import os
import random
import re
import sys
def compareTriplets(a, b):
    puntosJugador1=0
    puntosJugador2=0
    marcador=[]
    
    for i,j in zip(a,b):
        print(i,j)
        if i>j:
            puntosJugador1=puntosJugador1+1
            print('Puntua jugador 1', str(puntosJugador1))
        elif i<j:
            puntosJugador2=puntosJugador2+1
            print('Puntua jugador 2', str(puntosJugador2))
    marcador.append(puntosJugador1)
    marcador.append(puntosJugador2)
    print(marcador)
    return marcador


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()