ekipa=int(input())
levodesnih=int(input())
goredoleti=int(input())
levodesniti=int(input())
index=(levodesnih)*(goredoleti-1)+levodesniti
index%=ekipa
if index==0:
    index=ekipa
print(index)