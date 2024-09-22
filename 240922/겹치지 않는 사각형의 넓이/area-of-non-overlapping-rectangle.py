offset = 1000
arr = [[0] * 2001 for _ in range(2001)]
for _ in range(2):
    x1, y1, x2, y2 = tuple(map(int,input().split()))
    for i in range(x1 + offset, x2 + offset):
        for j in range(y1 + offset, y2 + offset):
            arr[i][j] += 1

mx1, my1, mx2, my2 = tuple(map(int,input().split()))
for i in range(mx1 + offset, mx2 + offset):
    for j in range(my1 + offset, my2 + offset):
        arr[i][j] = 0

sum = 0
for i in range(0,2001):
    for j in range(0,2001):
        if arr[i][j] == 1:
            sum += 1

print(sum)