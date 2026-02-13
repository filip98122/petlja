a=input()
l=[*a]
res=""
if len(l)%3==0:
    pomeri=3
elif len(l)%3==1:
    pomeri=1
else:
    pomeri=2

for i in range(len(l)):
    res=res+l[i]
    pomeri-=1
    if pomeri==0:
        pomeri=3
        res=res+" "
print(res)