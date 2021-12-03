te = int(input())
for i in range(te):
    g = input()
    co = 0
    for t in range(1, int(g)):
        lo = str(t)
        if t % 10 != 0 and ((int(lo[0])%2!=0 and int(lo[-1])!=0) or (int(lo[-1])%2!=0 and int(lo[0])!=0)):

            re = lo[::-1]
            d = int(re) + t

            ne = 0
            for n in str(d):
                if n in ['1', '3', '5', '7', '9']:
                    ne += 1

            if ne == len(str(d)):
                co += 1
    print(co)

