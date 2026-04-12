a, b = input().split(' ')

a=int(a)
b=int(b)

n=0

for i in range(a,b+1):
    if i%2!=0:
        continue
    n+=i

print(n)
