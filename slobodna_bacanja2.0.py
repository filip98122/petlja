a,b = map(int,input().split())
c,d = map(int,input().split())
e,f = map(int,input().split())
a-=c*2
b-=e*2
a-=d*3
b-=f*3

print(f"{a} {b}")
print(a+b)