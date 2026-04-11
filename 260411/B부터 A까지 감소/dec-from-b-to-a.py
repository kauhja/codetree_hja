A, B = input().split(" ")
A = int(A)
B = int(B)

n = B

for i in range(B-A+1):
    print(n, end=" ")
    n-=1