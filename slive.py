a = int(input())
pom = (a//5)
e_1 = 2*pom
e_2 = 3*pom
print(e_1)
print(e_2)
print(a%5)
d = 0
if e_1>=1:
    d+=1
if e_2>=1:
    d+=1
if a%5>=1:
    d+=1
print(d)