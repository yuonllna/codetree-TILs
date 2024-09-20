n = int(input())

block = []
for i in range(0, 201):
    block.append(0)

for _ in range(n):
    x1, x2 = map(int, input().split())
    for j in range(x1 + 100, x2 + 100):
        block[j] += 1


print(max(block))