male_i_srednje = int(input())
srednje_i_velike = int(input())
male = int(input())
srednje = int(input())
velike = int(input())
res = 0
male_i_srednje-=male
if male_i_srednje<=0:
    pass
else:
    if male_i_srednje<srednje:
        srednje-=male_i_srednje
        male_i_srednje = 0
    elif male_i_srednje==srednje:
        srednje=0
        male_i_srednje = 0
    elif male_i_srednje>srednje:
        res+=male_i_srednje-srednje
        srednje = 0
srednje_i_velike-=srednje+velike
if srednje_i_velike<=0:
    pass
else:
    res+=srednje_i_velike
print(res)