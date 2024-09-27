inp = input()


x, y = 0, 0
dir = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for c in inp:
    if c == "R":
        dir = (dir + 1) % 4
        nx, ny = x, y
    elif c == "L":
        if dir - 1 < 0:
            dir = 4
        dir -= 1
        nx, ny = x, y
    elif c == "F":
        nx, ny = x + dx[dir], y + dy[dir]
    x = nx
    y = ny

    
print(x, y)