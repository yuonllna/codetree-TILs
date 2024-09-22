offset = 1000
arr = [[0] * 2001 for _ in range(2001)]

xmin, ymin, xmax, ymax = 0, 0, 0, 0

x1, y1, x2, y2 = tuple(map(int,input().split()))
for i in range(x1 + offset, x2 + offset):
    for j in range(y1 + offset, y2 + offset):
        arr[i][j] += 1
xmin, ymin, xmax, ymax = x1, y1, x2, y2

x3, y3, x4, y4 = tuple(map(int,input().split()))
for i in range(x3 + offset, x4 + offset):
    for j in range(y3 + offset, y4 + offset):
        if arr[i][j] == 1:
            if xmin > i - offset:
                xmin = i
            elif xmax < i - offset:
                xmax = i
            elif ymin > j - offset:
                xmin = j
            elif ymax < j - offset:
                xmax = j
            arr[i][j] = 0

sum = 0
for i in range(xmin + offset, xmax + offset):
    for j in range(ymin + offset, ymax + offset):
        sum += 1

print(sum)