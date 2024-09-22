offset = 1000
arr = [[0] * 2001 for _ in range(2001)]

x1, y1, x2, y2 = tuple(map(int,input().split()))
for i in range(x1 + offset, x2 + offset):
    for j in range(y1 + offset, y2 + offset):
        arr[i][j] = 1

x3, y3, x4, y4 = tuple(map(int,input().split()))
for i in range(x3 + offset, x4 + offset):
    for j in range(y3 + offset, y4 + offset):
        if arr[i][j] == 1:
            arr[i][j] = 0

xmin, ymin, xmax, ymax = 1001, 1001, -1001, -1001
for i in range(0, 2001):
    for j in range(0, 2001):
        if arr[i][j] == 1:
            if xmin > i - offset + 1:
                xmin = i - offset + 1
            if xmax < i - offset + 1:
                xmax = i - offset + 1
            if ymin > j - offset + 1:
                ymin = j - offset + 1
            if ymax < j - offset + 1:
                ymax = j - offset + 1
        else: continue

sum = 0
if arr[xmin + offset][ymin + offset] == 0 and arr[xmax + offset][ymax + offset] == 0:
    print(0)
else: 
    for i in range(xmin + offset, xmax + offset):
        for j in range(ymin + offset, ymax + offset):
            sum += 1
    print(sum)