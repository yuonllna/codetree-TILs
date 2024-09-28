n = int(input())
x_init, y_init = 0, 0
x, y = 0, 0

dx, dy = [0,1,-1,0], [1,0,0,-1]

time = 1
flag = False

for _ in range(n):
    d, a = tuple(input().split())
    a = int(a)
    if d == "N":
        dir_num = 0
    elif d == "E":
        dir_num = 1
    elif d == "W":
        dir_num = 2
    else: dir_num = 3

    for i in range(a):
        x += dx[dir_num]
        y += dy[dir_num]
        if x == x_init and y == y_init:
            flag = True
            break
        time += 1
    if flag:
        break
    
if flag:
    print(time)
else: print(-1)