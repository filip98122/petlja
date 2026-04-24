zbirgoredole1,zbirgoredole2=map(int,input().split())
zbirlevodesno1,zbirlevodesno2=map(int,input().split())
num1,num2=map(int,input().split())
num3,num4=map(int,input().split())
l=[num1,num2,num3,num4]
if num1+num3==zbirgoredole1 and num2+num4==zbirgoredole2 and num1+num2==zbirlevodesno1 and num3+num4==zbirlevodesno2:
    if num1!=num2 and num1!=num3 and num3!=num4 and num4!=num2:
        if 3<=zbirgoredole1<=17 and 3<=zbirgoredole2<=17 and 3<= zbirlevodesno1<=17 and 3<=zbirlevodesno2<=17:
            if 1<=num1<=9 and 1<=num2<=9 and 1<=num3<=9 and 1<=num4<=9:
                print("da")
                exit()
print("ne")