n, m = tuple(map(int, input().split()))
x, y = 0, 0
dir_num = 0
arr = [[0] * (m) for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

arr[x][y] = 1
for i in range(2, n * m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
        x, y = x + dxs[dir_num], y + dys[dir_num]
        arr[x][y] = i
    else:
        dir_num = (dir_num + 1) % 4
        x, y = x + dxs[dir_num], y + dys[dir_num]
        arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print("")