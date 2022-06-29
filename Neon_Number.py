n=int(input())
p=n*n
s=0
l=len(str(p))
for i in range(1,l+1):
    r=p%10
    s=s+r
    p=p//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")