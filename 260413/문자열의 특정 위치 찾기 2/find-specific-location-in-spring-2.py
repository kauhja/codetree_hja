a = input()

Text = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0

for i in range(5):
    if Text[i][2] == a or Text[i][3] == a:
        print(Text[i])
        cnt += 1

print(cnt)