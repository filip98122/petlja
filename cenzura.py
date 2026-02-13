num1,num2=map(int,input().split())
b=input()
c=input().split()
res=""
for i in range(num1):
    if b[i] in c:
        res=res+"#"
    else:
        res=res+b[i]
print(res)