n = int(input())
arr = [list(input()) for _ in range(n)]
k = int(input())

# 오른쪽, 아래, 왼쪽, 위
# /: 오-위, 아-왼
# \: 왼-위, 오-아
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

if 1 <= k <= n:
    dir_num = 3
    x, y = 0, k - 1
elif n + 1 <= k <= 2*n:
    dir_num = 2
    x, y = 2, k - n - 1
elif 2*n + 1 <= k <= 3*n:
    dir_num = 1
    x, y = 2, k - 3*n
    if k - 3*n < 0:
        y += n
elif 3*n + 1 <= k <= 4*n:
    dir_num = 0
    x, y = k - 4*n, 0
    if k - 4*n < 0:
        x += n

cnt = 0
while True:
    if arr[x][y] == "/":
        if dir_num == 3:
            dir_num = 0
        elif dir_num == 0:
            dir_num = 3
        elif dir_num == 1:
            dir_num = 2
        elif dir_num == 2:
            dir_num = 1
    elif arr[x][y] == "/":
        if dir_num == 1:
            dir_num = 0
        elif dir_num == 0:
            dir_num = 1
        elif dir_num == 3:
            dir_num = 2
        elif dir_num == 2:
            dir_num = 3
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if 0 <= nx < n and 0 <= ny < n:
            x, y = nx, ny
            cnt += 1
    else:
        break

print(cnt)