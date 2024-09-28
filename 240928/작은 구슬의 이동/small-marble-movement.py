n, t = tuple(map(int, input().split()))
r, c, d = tuple(input().split())
x = int(r)
y = int(c)
arr = [[0] * (n+1) for _ in range(n+1)]

dxs = [1, 0,  0, -1]
dys = [0, 1, -1, 0]

if d == "U":
    dir_num = 0
elif d == "R":
    dir_num = 1
elif d == "L":
    dir_num = 2
else: dir_num = 3

for _ in range(t):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if 1 <= nx <= n and 1 <= ny <= n:
        x, y = x + dxs[dir_num], y + dys[dir_num]
    else:
        dir_num = 3 - dir_num 

print(x, y)