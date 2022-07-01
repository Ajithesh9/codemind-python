num=int(input())
while num!=1:
    if num%5==0:
        num=num//5
    elif num%3==0:
        num=num//3
    elif num%2==0:
        num=num//2
    else:
        print('Not Ugly Number')
        break
else:
    print('Ugly Number')
