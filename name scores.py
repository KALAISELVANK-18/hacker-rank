li=[]
n=int(input())
for i in range(n):
    f=input()
    li.append(f)
li.sort()
te=int(input())
st='.ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(te):
    stri=input()
    cou=0
    for h in stri:
        cou+=st.index(h)
    print(cou*(li.index(stri)+1))