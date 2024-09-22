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
        end = cur + x
        for j in range(cur, end):
            black[j] += 1
            flag[j] = True  
    else:
        end = cur - x
        for j in range(cur - 1, end - 1, -1):
            white[j] += 1  
            flag[j] = False
    cur = end 

black_n = 0
white_n = 0
for i in range(0, 10001):
    if flag[i] == True:
        black_n += 1
    elif flag[i] == False:
        white_n += 1
    else: continue

print(white_n, black_n)