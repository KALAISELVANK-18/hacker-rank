if __name__ == '__main__':

    li = []
    lim = []
    for _ in range(int(input())):
        li1 = []
        name = input()
        score = float(input())
        lim.append(score)
        li1.append(name)
        li1.append(score)
        li.append(li1)
    lim.sort()
    a = 0
    for i in lim:
        if i != lim[0]:
            a = i
            break
    li2 = []
    for i in range(0, len(li)):
        if li[i][1] == a:
            li2.append(li[i][0])
    li2.sort()
    for i in range(0, len(li2)):
        print(li2[i])