a, b = input().split(' ')
a = int(a)
b = int(b)

n = a

while n <= b:
    print(n, end=' ')
    
    if n%2==1:
        n=n*2
    else:
        n+=3