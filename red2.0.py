a=int(input())
b=int(input())
pos=b+1
minus=0
stop=0
for i in range(b):
    c=int(input())
    if stop==0:
        if c<=a:
            stop=1
        else:
            minus+=1
print(pos-minus)