N = int(input("N: "))
M = int(input("M: "))

while N == 0:
    while M == 1:
        print('*', end="")
        M-=1
    print("\n")

    N-=1