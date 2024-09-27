n = int(input())

dir_num = -1
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
for _ in range(n):
    d, a = tuple(input().split())
    a = int(a)
    if d == "E":
        nx, ny = x + a*dx[0], y + a*dy[0]
    elif d == "S":
        nx, ny = x + a*dx[1], y + a*dy[1]
    elif d == "W":
        nx, ny = x + a*dx[2], y + a*dy[2]
    else:
        nx, ny = x + a*dx[3], y + a*dy[3]
    x = nx
    y = ny

    
print(x, y)