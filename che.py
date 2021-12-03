import itertools
u=list(map(int,input().split(' ')))
li=[]
for i in range(1,u[0]+1):
    li.append(float(pow(i,i)))

y=0
for e in range(1,len(li)+1):
    for t in itertools.combinations(li,e):
        h=list(t)
        if sum(h)%u[1]==0:
            y+=1
print(y)
