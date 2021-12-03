t=int(input())
f=[]
for i in range(1,t):
    for u in range(1,t):
        st=str(pow(i,u))
        x=0
        for d in st:
            x+=int(d)
        f.append(x)
print(max(f))
