offset = 1000
arr = [[0] * 2001 for _ in range(2001)]

x1, y1, x2, y2 = tuple(map(int,input().split()))
for i in range(x1 + offset, x2 + offset):
    for j in range(y1 + offset, y2 + offset):
        arr[i][j] += 1

x3, y3, x4, y4 = tuple(map(int,input().split()))
for i in range(x3 + offset, x4 + offset):
    for j in range(y3 + offset, y4 + offset):
        if arr[i][j] == 1:
            arr[i][j] = 0

xmin, ymin, xmax, ymax = x1, y1, x2, y2
for i in range(0, 2001):
    for j in range(0, 2001):
        if arr[i][j] == 1:
            if xmin > i - offset:
                xmin = i - offset
            if xmax < i - offset:
                xmax = i - offset
            if ymin > j - offset:
                ymin = j - offset
            if ymax < j - offset:
                ymax = j - offset
            
sum = 0
for i in range(xmin + offset, xmax + offset):
    for j in range(ymin + offset, ymax + offset):
        sum += 1   
print(sum)