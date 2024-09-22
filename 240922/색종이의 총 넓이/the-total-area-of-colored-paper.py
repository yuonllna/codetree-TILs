n = int(input())

offset = 100
arr = [[0] * 201 for _ in range(201)]
for _ in range(n):
    x, y = tuple(map(int,input().split()))
    for i in range(x + offset, x + offset + 8):
        for j in range(y + offset, y + offset + 8):
            arr[i][j] += 1

sum = 0
for i in range(0,201):
    for j in range(0,201):
        if arr[i][j] >= 1:
            sum += 1

print(sum)