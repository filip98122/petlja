res=0
for i in range(5):res+=int(input())
res/=5
for i in range(4,-1,-1):
    if res>=i+0.4:
        print(i+1)
        exit()