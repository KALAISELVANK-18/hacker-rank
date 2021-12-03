te = int(input())
for i in range(te):
    t = input()
    tt = t.split(' ')
    li = [(tt[0]), (tt[1])]

    if len(li[0]) >= int(tt[2]):
        print(li[0][int(tt[2]) - 1])
    elif len(li[1]) >= int(tt[2]):
        print(li[1][int(tt[2]) - 1])
    else:
        while True:
            li.append(li[-2] + li[-1])
            if len(li[-1]) >= int(tt[2]):
                print(li[-1][int(tt[2]) - 1])
                break
