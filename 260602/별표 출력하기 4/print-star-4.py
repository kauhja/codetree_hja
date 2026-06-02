n = int(input())
m = n

for i in range(n):
    for j in range(m-i):
        print('*', end=' ')
    print()

for i in range(n-1):
    for j in range(i+2):
        print('*', end=' ')
    print()