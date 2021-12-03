import math
li=[2,3,5]

for i in range(7,120000,2):
    f=0
    if   i % 5 != 0:
        sq = math.floor(math.sqrt(i))
        for t in range(3, sq + 1, 2):
            if i % t == 0:
                f = 1
                break
        if f == 0:
            li.append(i)
te=int(input())
for i in range(te):
    n=int(input())
    print(li[n-1])


