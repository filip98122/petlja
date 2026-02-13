a=input().strip()
dan=int(input().strip())
datum=int(a[0]+a[1])+8-dan
while datum>7:
    datum-=7
print(f"{str(datum).zfill(2)}{a[2:len(a)]}")