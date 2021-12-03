import itertools
import string
string.w
li=[1,2,3,4]
for i in range(1,8):
    lis=list(itertools.combinations_with_replacement(li,i))
    lise.append(lis)
for d in range(2):
    g=int(input())
    s=0
    for i in range(len(lise)):
        for t in range(len(lise[i])):
            if sum(lise[i][t]) == g:
                s+=1
    print(s)
print(list(itertools.combinations_with_replacement(li,500)))