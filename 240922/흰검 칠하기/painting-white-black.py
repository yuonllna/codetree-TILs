n = int(input())

black = []
white = []
flag = []
for _ in range(0, 10001):
    black.append(0)

for _ in range(0, 10001):
    white.append(0)

for _ in range(0, 10001):
    flag.append(None)

cur = 5000
for _ in range(n):
    x, d = tuple(input().split())
    x = int(x)
    if d == "R":
        for j in range(cur, cur + x):
            black[j] += 1
            flag[j] = True
        cur = cur + x - 1
    else:
        for j in range(cur, cur - x, -1):
            white[j] += 1  
            flag[j] = False
        cur = cur - x + 1

black_n = 0
white_n = 0
grey_n = 0
for i in range(0, 10001):
    if black[i] >= 2 and white[i] >= 2:
        grey_n += 1
    elif flag[i] == True:
        black_n += 1
    elif flag[i] == False:
        white_n += 1
    else: continue

print(white_n, black_n, grey_n)