import numpy

import math
te=int(input())
li=[]
for i in range(te):
    k=int(input())
    li.append(k)
lis=[]
for i in range(1,max(li)+1):
    t=0
    for h in range(1,int(math.sqrt(i))+1):
        if i%h==0:
            if (i/h==h):
                t+=1
            else:
                t+=2

    lis.append(t)

for g in range(te):
    t=0
    s=0
    for f in range(li[g]-1):
        if lis[s]==lis[s+1]:
            t+=1
        s+=1
    print(t-1)
