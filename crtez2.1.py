a=int(input())
spaces=a//2
def spcchange(i,spaces):
    if i>=a//2:
        return spaces+1
    else:
        return spaces-1
for i in range(a):
    if i==0 or i==a-1:
        print("-"*spaces+"*"+"-"*spaces)
        spaces=spcchange(i,spaces)
        continue
    if i==1 or i==a-2:
        print("-"*spaces+"*"*3+"-"*spaces)
        spaces=spcchange(i,spaces)
        continue
    if i==a//2:
        print("*"*a)
        spaces=spcchange(i,spaces)
        continue
    print("-"*spaces+"*"+"-"*((a-spaces*2-3)//2)+"*"+"-"*((a-spaces*2-3)//2)+"*"+"-"*spaces)
    spaces=spcchange(i,spaces)