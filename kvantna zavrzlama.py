a,b=map(int,(input().strip()).split())
l=list(map(float,(input().strip()).split()))
up=False
zasad=1
res=2
if l[1]>l[0]:
    up=True
for i in range(1,a):
    flip=False
    if up:
        if l[i]>l[i-1]:
            flip=True
    else:
        if l[i]<l[i-1]:
            flip=True
    if flip==True:
        up=not up
        zasad+=1
    else:
        zasad=2
    res=max(res,zasad)
if res>=b:
    print("da")
else:
    print("ne")
print(res)