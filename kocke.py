a=int(input())
l=list(map(int,input().split()))
b=int(input())
for iii in range(b):
    s=input()
    s=s.replace("#","")
    a1,b1,c1=map(str,(s.strip()).split())
    b1=int(b1)
    c1=int(c1)
    if a1=="m":
        ostatak=1
    else:
        ostatak=0
    offset1=0
    offset2=0
    while True:
        if b1+offset1>=c1-offset2:
            break
        if l[b1+offset1]%2==ostatak and l[c1-offset2]%2==ostatak:
            h=l[b1+offset1]
            l[offset1+b1]=l[c1-offset2]
            l[c1-offset2]=h
            offset1+=1
            offset2+=1
            continue
        if l[b1+offset1]%2!=ostatak:
            offset1+=1
        if l[c1-offset2]%2!=ostatak:
            offset2+=1
    print(*l)
najduzi=1
res=0
streak=1
najmanji=l[0]
for i in range(1,len(l)):
    if l[i]<najmanji:
        if streak>najduzi:
            najduzi=streak
        streak=0
        res+=1
    streak+=1
    najmanji=l[i]
if streak>najduzi:
    najduzi=streak
res+=1
print(res,najduzi)