a=input().strip()
dan=a[0]+a[1]
dan=int(dan)
dun=int(input())
dan-=dun-1
dan%=7
a1=a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]
if dan==0:
    dan+=7
dan=str(dan)
if len(dan)==1:
    dan="0"+dan
print(f"{dan}{a1}")