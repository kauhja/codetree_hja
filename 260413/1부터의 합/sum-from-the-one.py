N = int(input())

n=1
sum = 0

for i in range(100):
    if sum>=N:
        print(n-1)
        break
    else:
        sum+=n
        n+=1
