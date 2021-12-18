import math
import os
import random
import re
import sys
def countApplesAndOranges(s, t, a, b, apples, oranges):
    numApples=0
    numOranges=0
    for i in apples:
        m=a+i
        if m>=s and m<=t:
            numApples=numApples+1
    for i in oranges:
        n=b+i
        if n>=s and n<=t:
            numOranges=numOranges+1
    print("Manzanas= ", numApples)
    print("Naranjas= ", numOranges)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)