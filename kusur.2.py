a=int(input())
b=int(input())
c=int(input())
a1=min(max(a,b)-min(b,a),c)
c-=min(max(a,b)-min(b,a),c)
a1+=c//2
b1=c//2
if a>b:
    print(a1)
    print(b1)
else:
    print(b1)
    print(a1)