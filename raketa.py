a=int(input())
b=int(input())
count=-1
sirina=a*2-1
for i in range(a):
    count+=2
    line="."*((sirina-count)//2)+"*"*count+"."*((sirina-count)//2)
    print(line)
line="*"+"."*((sirina-3)//2)+"o"+"."*((sirina-3)//2)+"*"
for i in range(b):
    print(line)
for i in range(a-1):
    count-=2
    line="."*((sirina-count)//2)+"*"*count+"."*((sirina-count)//2)
    print(line)