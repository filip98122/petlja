a,b,c,d=map(int,input().split())
suma=a+b+c+d
labcd=[a,b,c,d]
lstr={"a":0,"b":1,"c":2,"d":3}
lstr1=["a","b","c","d"]
for i in range(4):
    if labcd[i]>=51:
        print(lstr1[i])
        exit()
index1,index2=map(str,input().split())
index11=lstr[index1]
index21=lstr[index2]
if labcd[index11]-labcd[index21]>=20:
    print(index1)
    exit()
if labcd[index21]-labcd[index11]>=20:
    print(index2)
    exit()
print(input())