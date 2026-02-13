a,b = map(int, input().split())
a1,b1 = map(int, input().split())
a2,b2 = map(int, input().split())
a3,b3 = map(int, input().split())
if a==a2+a3 and b == b2+b3 and a1 ==a2+b2 and b1 == a3+b3:
    if a3!=a2  and a3!=b3 and a2!=b2 and b2 != b3:
        if a2<10 and a2 >0:
            if a3<10 and a3 >0:
                if b2<10 and b2 >0:
                    if b3<10 and b3 >0:
                        print("da")
                        exit()

print("ne")