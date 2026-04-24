a=int(input())
b=int(input())
for iiii in range(b):
    space=0
    for i in range(a):
        if i==0 or i==a-1:
            print((a//2)*"-"+"*"+(a//2)*"-")
            continue
        if i==1 or i==a-2:
            print(((a-3)//2)*"-"+"***"+((a-3)//2)*"-")
            continue
        if i<=a//2:
            space+=1
        else:
            space-=1
        if i==a//2:
            print("*"*a)
            continue
        print((a-3-space*2)//2*"-"+"*"+"-"*space+"*"+"-"*space+"*"+(a-3-space*2)//2*"-")