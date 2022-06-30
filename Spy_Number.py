n=int(input())
add=0
pro=1
while n>0:
    s=n%10
    add=add+s
    pro=s*pro
    n=n//10
if add==pro:
    print("Spy Number")
else:
    print("Not Spy Number")