a=input().strip()
l=[*a]
l2=[]
l2.append(int(f"{l[0]}{l[1]}"))
l2.append(int(f"{l[0]}{l[2]}"))
l2.append(int(f"{l[1]}{l[2]}"))
l2.sort()
print(l2[2])