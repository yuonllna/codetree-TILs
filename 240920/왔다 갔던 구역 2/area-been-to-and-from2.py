n = int(input())

block = []
for i in range(0, 101):
    block.append(0)

cur = 0
for _ in range(n):
    x, d = tuple(input().split())
    x = int(x)
    if d == "R":
        for j in range(cur, cur + x + 1):
            block[j] += 1
            cur = x
    elif d == "L":
        for j in range(cur, cur - x, -1):
            block[j] += 1
            cur = x

sum = 0
for i in range(len(block)):
    if block[i] >= 2:
        sum += 1

print(sum)