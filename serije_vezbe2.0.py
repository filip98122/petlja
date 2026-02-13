string=" "
a=int(input())
b=int(input())
for i in range(b):
    if i==0:
        continue
    string=string+str(i+1)
    string=string+" "
for i in range(a):
    print(f"{i+1}{string}")