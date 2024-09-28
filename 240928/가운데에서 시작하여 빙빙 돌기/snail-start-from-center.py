n = int(input())
x, y = n-1, n-1
arr = [[0] * (n) for _ in range(n)]

dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]
dir_num = 0

arr[x][y] = n*n
for i in range(n * n - 1, 0, -1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
        x, y = x + dxs[dir_num], y + dys[dir_num]
        arr[x][y] = i
    else:
        dir_num = (dir_num + 1) % 4
        x, y = x + dxs[dir_num], y + dys[dir_num]
        arr[x][y] = i

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print("")