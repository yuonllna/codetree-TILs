n, k = map(int, input().split())

block = []
for i in range(n):
    block.append(0)
    
for _ in range(k):
    start, end = map(int, input().split())
    for i in range(start, end + 1):
        block[i] += 1

max = 0
for b in block:
    if max < b:
        max = b

print(max)