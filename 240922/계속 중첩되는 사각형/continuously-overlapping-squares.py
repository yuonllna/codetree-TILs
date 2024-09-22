n = int(input())

offset = 100
red = [[0] * 201 for _ in range(201)]
blue = [[0] * 201 for _ in range(201)]
flag = [[None] * 201 for _ in range(201)]

for i in range(n):
    x1, y1, x2, y2 = tuple(map(int,input().split()))
    if i % 2 == 0:
        for i in range(x1 + offset, x2 + offset):
            for j in range(y1 + offset, y2 + offset):
                red[i][j] += 1
                flag[i][j] = True
    else: 
        for i in range(x1 + offset, x2 + offset):
            for j in range(y1 + offset, y2 + offset):
                blue[i][j] += 1
                flag[i][j] = False

sum = 0
for i in range(0,201):
    for j in range(0,201):
        if flag[i][j] == False:
            sum += 1

print(sum)