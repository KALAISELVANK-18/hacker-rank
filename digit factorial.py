import sys
import math
ff=int(sys.stdin.readline())
zoo=0
for u in range(10,ff):
    dh=str(u)
    xx=0
    for lo in dh:
        xx+=math.factorial(int(lo))
    if xx%u==0:
        zoo+=u
print(zoo)
