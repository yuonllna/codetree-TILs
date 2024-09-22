offset = 1000
arr = [[0] * 2001 for _ in range(2001)]

x1, y1, x2, y2 = tuple(map(int,input().split()))

xmin, ymin, xmax, ymax = x1, y1, x2, y2
for i in range(xmin + offset, xmax + offset + 1):
    for j in range(ymin + offset, ymax + offset + 1):
        arr[i][j] += 1


x3, y3, x4, y4 = tuple(map(int,input().split()))
for i in range(x3 + offset, x4 + offset):
    for j in range(y3 + offset, y4 + offset):
        if arr[i][j] == 1:
            if xmin > i - offset:
                xmin = i
            if xmax < i - offset:
                xmax = i
            if ymin > j - offset:
                ymin = j
            if ymax < j - offset:
                ymax = j
            arr[i][j] = 0

sum = 0
if arr[xmin + offset][ymin + offset] == 0 and arr[xmax + offset][ymax + offset] == 0:
    print(0)
elif arr[xmin + offset][ymin + offset] == 1 and arr[xmax + offset][ymax + offset] == 1:
    for i in range(xmin + offset, xmax + offset):
        for j in range(ymin + offset, ymax + offset):
            sum += 1
    print(sum)
else:
    for i in range(xmin + offset, xmax + offset):
        for j in range(ymin + offset, ymax + offset):
            if arr[i][j] == 1:
                sum += 1   
    print(sum)