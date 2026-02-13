a = input()
b = input()
l = [*a]
l_ = [*b]
res=0
for i in range(len(l_)):
    l_[i] = int(l_[i])
for i in range(len(l)):
    l[i] = int(l[i])
for i in range(4):
    way_minimum = 11
    if l[i] == l_[i]:
        continue
    if l[i]>l_[i]:
        if way_minimum>l[i]-l_[i]:
            way_minimum=l[i]-l_[i]
        if way_minimum>10-l[i]+l_[i]:
            way_minimum = 10-l[i]+l_[i]
        
    if l_[i]>l[i]:
        if way_minimum>l_[i]-l[i]:
            way_minimum=l_[i]-l[i]
        if way_minimum>10-l_[i]+l[i]:
            way_minimum = 10-l_[i]+l[i]
    res+=way_minimum
print(res)
        
    