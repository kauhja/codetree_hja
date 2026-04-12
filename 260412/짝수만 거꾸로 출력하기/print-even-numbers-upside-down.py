n = int(input())

arr = list(input().split())
for i in range(n):
    arr[i] = int(arr[i])

for i in range(n-1, -1, -1):
    if arr[i] % 2 == 0:
        print(arr[i], end=" ")
