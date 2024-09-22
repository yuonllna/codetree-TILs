n = int(input())

offset = 100
arr = [[0] * 201 for _ in range(201)]
for _ in range(n):
    x1, y1, x2, y2 = tuple(map(int,input().split()))
    for i in range(x1 + offset, x2 + offset):
        for j in range(y1 + offset, y2 + offset):
            arr[i][j] += 1

sum = 0
for i in range(0,201):
    for j in range(0,201):
        if arr[i][j] >= 1:
            sum += 1

print(sum)