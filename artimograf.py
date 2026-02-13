a,s,b,s,c=map(str,input().split())
a1,s,b1,s,c1=map(str,input().split())
l=[a,b,c]
l1=[a1,b1,c1]
dct={"0":"","1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":""}
d2={}
for i in range(3):
    for j in range(len(l1[i])):
        if dct[l1[i][j]]=="":
            if l1[i][j] in d2:
                print("ne")
                exit()
            dct[l1[i][j]]=l[i][j]
            d2[l[i][j]]=l1[i][j]
        else:
            if l[i][j]!=dct[l1[i][j]]:
                print("ne")
                exit()




print("da")