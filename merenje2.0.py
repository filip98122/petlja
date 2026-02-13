num = [int(input()),int(input()),int(input())]
num.sort()
najmanji = num[0]
if num[1]-num[0]>0:
    if num[1]-num[0]<najmanji:
        najmanji = num[1]-num[0]

if num[2]-num[1]-num[0]>0:
    if num[2]-num[1]-num[0]<najmanji:
        najmanji = num[2]-num[1]-num[0]

if num[2]-num[1]>0:
    if num[2]-num[1]<najmanji:
        najmanji = num[2]-num[1]


if num[2]-num[0]>0:
    if num[2]-num[0]<najmanji:
        najmanji = num[2]-num[0]

if num[0]+num[1]-num[2]>0:
    if num[0]+num[1]-num[2]<najmanji:
        najmanji = num[0]+num[1]-num[2]
print(najmanji)