A = int(input())
B = int(input())
C = int(input())
D = int(input())
if A >B:
    Pobednik1 = "A"
    Pobednik1_rejting = A
if B>A:
    Pobednik1 = "B"
    Pobednik1_rejting = B
if C>D:
    Pobednik2 = "C"
    Pobednik2_rejting = C
if D>C:
    Pobednik2 = "D"
    Pobednik2_rejting = D
if Pobednik1_rejting>Pobednik2_rejting:
    print(Pobednik2)
if Pobednik2_rejting>Pobednik1_rejting:
    print(Pobednik1)