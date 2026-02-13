a=input()



def count_control_chars(s):
    return sum(1 for c in s if ord(c) < ord(' '))


l=[*a]
b=int(input())
print(count_control_chars(a))



if b==2:
    print("**")
    exit()
else:
    b-=2
res="*"

schedule=False
while True:
    for i in range(len(l)):
        res=res+l[i]
        b-=1
        if b==0:
            schedule=True    
            break
    if schedule:
        break
    res=res+" "
    b-=1
    if b==0:
        break
res=res+"*"
print(res)

print(count_control_chars(res))
print(count_control_chars(res))
