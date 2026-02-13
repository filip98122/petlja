n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    if l[i]%2==i%2:pass
    else:
        print("ne")
        exit()
        
print("da")