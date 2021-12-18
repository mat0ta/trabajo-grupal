import math
import os
import random
import re
import sys

def staircase(n):
    for i in range(1,n+1):
        fila=''
        for j in range(i):
            fila += '' .join('# ')
            print(fila)


if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)