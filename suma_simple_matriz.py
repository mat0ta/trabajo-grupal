import math
import os
import random
import re
import sys
import pprint

def simpleArraySum(ar):
    suma=0
    for i in ar:
        suma +=1
        print("suma = ", suma)
        return suma


if __name__ == '__main__':
    fptr= open('T3-1.txt', 'w')
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    print(ar)
    result = simpleArraySum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()