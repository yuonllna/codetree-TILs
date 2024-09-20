n = int(input())

block = []
for i in range(0, 2001):
    block.append(0)

idx = 1000
for _ in range(n):
    x, d = tuple(input().split())
    x = int(x)
    if d == "R":
        for j in range(idx, idx + x + 1):
            block[j] += 1        
    else:
        for j in range(idx, idx - x - 1, -1):
            block[j] += 1
    idx += x
    

sum = 0
for i in range(len(block)):
    if block[i] == 0: continue
    if block[i] >= 2:
        sum += 1

print(sum)