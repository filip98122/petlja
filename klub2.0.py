a=int(input())
minvreme=1441
maxvreme=-1
pre12=0
for i in range(a):
    h1,m1,h2,m2=map(int,input().split())
    m1+=h1*60
    m2+=h2*60
    if m1<minvreme:
        minvreme=m1
    if m1<720:
        pre12+=1
    if m2>maxvreme:
        maxvreme=m2
h=(maxvreme-minvreme)//60
m=maxvreme-minvreme
m%=60
print(f"{h} {m}")
print(pre12)