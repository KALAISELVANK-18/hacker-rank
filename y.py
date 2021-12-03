ro = input()
roo = ro.split(' ')
fab = [int(roo[0]), int(roo[1]), int(roo[2])]
for i in range(1000):
    q = len(fab)

    zoo = (int(fab[q - 3]) + int(fab[q - 2]) + int(fab[q - 1]))
    fab.append(zoo)
a = 0
print(fab)
w = 3
while a < int(roo[3]):

    k = 0
    for i in range(len(fab)):
        if fab[i] % w != 0:
            k += 1

    w += 2
    if k == len(fab):
        a += 1

print(w-2)