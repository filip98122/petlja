s1=int(input())
t1=int(input())
s2=int(input())
t2=int(input())
if (s1+s2)%(t2+t1)==0:
    print(int((s1+s2)/(t2+t1)))
else:
    print((s1+s2)/(t2+t1))