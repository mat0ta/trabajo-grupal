import math
import os
import random
import re
import sys
def aVeryBigSum(ar):



if __name__ == '__main__':
#fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr=open('T3-3.txt', 'w')
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()