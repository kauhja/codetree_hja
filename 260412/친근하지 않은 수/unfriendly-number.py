N = int(input())

arr = list(range(1, N+1))

c=0

for i in arr:
    if i%2==0 or i%3==0 or i%5==0:
        continue
    else:
        c+=1

print(c)