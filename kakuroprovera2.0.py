kolona1,kolona2=map(int,input().split())
vrsta1,vrsta2=map(int,input().split())
a,b=map(int,input().split())
c,d=map(int,input().split())
if a+c==kolona1 and b+d==kolona2 and a+b==vrsta1 and c+d==vrsta2:
    listprovera=[a,b,c,d]
    listprovera.sort()
    if listprovera[3]<10 and listprovera[0]>-1:
        if a!=b and a!=c and b!=d and d!=c:
            print("da")
            exit()
print("ne")