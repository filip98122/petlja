a = int(input())
b = int(input())
l = []
for i in range(b):
    l.append(i+1)
for i in range(a):
    res = ""
    for  ii in range(b):
        if i!=0:
            if ii == 0:
                l[ii]+=1
        res = res+str(l[ii])
        if ii!=b-1:
            res = res+" "
    print(res)