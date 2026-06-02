n = int(input())
m=n

for i in range(n):
    for j in range(m-i):
        print('*', end=' ')
    print()