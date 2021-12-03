import sys
iu = str(sys.stdin.readline())
su = 0
for i in range(11, pow(10, int(iu))):
    a = str(i)
    f = a[-1]
    s = a[0:(len(a) - 1)]
    st = f + s
    if int(st)%int(a)==0:
        su += int(a)

sys.stdout.write(str(su))