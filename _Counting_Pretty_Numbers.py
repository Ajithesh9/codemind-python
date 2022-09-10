tc=int(input())
for i in range(tc):
    L,R=map(int,input().split())
    d=0
    for j in range(L,R+1):
        c=j%10
        if c==2 or c==3 or c==9:
            d+=1
    print(d)
        