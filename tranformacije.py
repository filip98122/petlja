a = int(input())
b = int(input())
for i in range(b):
    a*=a
    a+=1
    a = a%1000
print(f"{(a%1000):03}")