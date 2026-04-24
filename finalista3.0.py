l=[]
abcd="ABCD"
for i in range(4):
    l.append(int(input().strip()))
tar=min(max(l[0],l[1]),max(l[2],l[3]))
for i in range(4):
    if l[i]==tar:
        print(abcd[i])