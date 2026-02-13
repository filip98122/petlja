a=input().strip()
b=int(input())

if b==2:
    print("**")
    exit()
else:
    b-=2
l=[*a]
res="*"
breakvar=False
while True:
    for i in range(len(l)):
        res=res+l[i]
        b-=1
        if b==0:
            breakvar=True    
            break
    
    if breakvar:
        break
    
    res=res+" "
    b-=1
    
    if b==0:
        break
res=res+"*"
print(res)