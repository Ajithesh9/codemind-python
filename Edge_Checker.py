a,b=map(int,input().split())
if a and b >0:
    if b>a:
        a,b=b,a
    if a-b==1 or a-b==9:
    #if a-b==1 or a-b==-1 or a-b==a-1 or a-b==b-1:
        print("Yes")
    else:
        print("No")
else:
    print("No")