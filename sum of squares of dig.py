import math
iu=int(input())
nee=0
for i in range(1,iu+1):
    dd=str(i)
    zoo=0
    for u in dd:
        zoo+=int(u)**2
    ss=str(math.sqrt(zoo))
    if ss[-1]=='0'and ss[-2]=='.':
        nee+=i
print(nee)  