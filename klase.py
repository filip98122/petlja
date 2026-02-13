a = input()
l = [*a]
d = ''
s = ' '
dd = 0
for i in range(len(l)-1,-1,-1):
    dd+=1
    d = d+l[i]
    if dd == 3:
        if i == 0:
            continue
        dd = 0
        d = d+s
l= [*d]
f=''
for i in range(len(l)-1,-1,-1):
    f = f+l[i]
print(f)
        
