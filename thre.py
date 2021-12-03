import math
import 
def isprime(num):
    f=0
    if num==2:
        return True
    if num>2 and num%2!=0:
        sq=math.floor(math.sqrt(num))
        for i in range(3,sq+1,2):
            if num%i==0:
                f=1
                break
        if f==0:
            return True
        if f==1:
            return False
    if num>2 and num%2==0:
        return False
n=int(input())
xo=3
t=0
i=6
while xo<n:

    f = 0


    if i > 2 and i % 2 != 0 and i%5!=0:
        sq = math.floor(math.sqrt(i))
        for t in range(3, sq + 1, 2):
            if i % t == 0:
                f = 1
                break
        if f == 0:
            xo+=1
            t=i
    i+=1
print(i-1)



