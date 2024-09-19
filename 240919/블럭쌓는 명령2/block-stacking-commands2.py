n, k = map(int, input().split())

block = []
for i in range(n + 1):
    block.append(0)

for _ in range(k):
    start, end = map(int, input().split())
    for j in range(start, end + 1):
        block[j] += 1

print(max(block))