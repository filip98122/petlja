l=[]
for i in range(5):
    l.append(int(input().strip()))
prosek=sum(l)/5
ocena=1
if prosek>=4.4:
    ocena=5
elif prosek>=3.4:
    ocena=4
elif prosek>=2.4:
    ocena=3
elif prosek>=1.4:
    ocena=2
print(ocena)