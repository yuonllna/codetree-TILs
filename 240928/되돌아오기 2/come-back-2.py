inp = input()

x, y = 0, 0
dir = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

time = 0
flag = False
for c in inp:
    if c == "R":
        dir = (dir + 1) % 4
        time += 1
    elif c == "L":
        if dir - 1 < 0:
            dir = 4
        dir -= 1
        time += 1
    elif c == "F":
        nx, ny = x + dx[dir], y + dy[dir]
        time += 1
        if nx == 0 and ny == 0:
            flag = True
            break
    x = nx
    y = ny

if flag: 
    print(time)
else: print(-1)