import sys

x,y = 0,0
res=1
# Read one character at a time from stdin
while True:
    char = sys.stdin.read(1)  # Reads a single character
    if not char or char =="\n":
        break  # End of input
    if char==">":
        x+=1
    elif char=="<":
        x-=1
    elif char=="^":
        y+=1
    else:
        y-=1
    if x==0 and y==0:
        res+=1
print(res)