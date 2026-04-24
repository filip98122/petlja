a=input().strip()
dan=int(a[0]+a[1])
ostalo=a[2:-1]+a[-1]
b=int(input())
dan-=b-1
dan%=7
if dan==0:
    dan+=7
print(f"0{dan}{ostalo}")