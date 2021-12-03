t = int(input())
for a in range(t):
    n = int(input())
    p=0
    for i in range(1,100000000000):
        p=0
        for t in range(1,n+1):
            if i%t==0:
                p+=1
        if p==n:
            print(i)
            break