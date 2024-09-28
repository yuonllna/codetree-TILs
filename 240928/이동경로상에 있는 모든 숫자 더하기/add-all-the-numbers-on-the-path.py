n, t = tuple(map(int, input().split()))
cmd = input()
arr = [list(map(int, input().split())) for _ in range(n)]

# 오른쪽, 아래, 왼쪽, 위
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 3

x = n // 2
y = n // 2

sum = arr[x][y]

for c in cmd:
    if c == "R":
        dir_num = (dir_num + 1) % 4
    elif c == "L":
        if dir_num - 1 < 0:
            dir_num = 4
        dir_num -= 1
    elif c == "F":
        nx, ny = x + dx[dir_num], y + dy[dir_num]
        if 0 <= nx < n and 0 <= ny < n:
            x, y = x + dx[dir_num], y + dy[dir_num]
            sum += arr[x][y]
        else:
            continue

print(sum)