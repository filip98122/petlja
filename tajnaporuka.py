l ="K X R E Z I C U P A M W F G T B Y D V L O H N S J Q".split()
l2="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
a=[*input()]
res=""
for i in range(len(a)):
    res=res+l2[l.index(a[i])]
print(res)