n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0
for i in range(n):
    row_sum = 0
    for j in range(n):
        if arr[i][j] == 1:
            row_sum += 1
    max_sum = max(max_sum, row_sum)

print(max_sum)