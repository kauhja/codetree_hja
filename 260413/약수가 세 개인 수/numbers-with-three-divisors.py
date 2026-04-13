start, end = map(int, input().split(' '))

# Please write your code here.
n=0
sigma = 0

for i in range(start, end+1):
    for j in range(1, i+1):
        if i%j==0:
            n+=1
    if n == 3:
        sigma+=1
    n=0

print(sigma
)

