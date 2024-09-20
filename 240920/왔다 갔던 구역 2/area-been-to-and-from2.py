n = int(input())

block = []
for i in range(0, 2001):
    block.append(0)

cur = 1000
for _ in range(n):
    x, d = tuple(input().split())
    x = int(x)
    if d == "R":
        end = cur + x
        for j in range(cur, end):
            block[j] += 1      
    else:
        end = cur - x
        for j in range(cur, end, -1):
            block[j] += 1
    cur = end 

sum = 0
for i in range(len(block)):
    if block[i] >= 2:
        sum += 1

print(sum)