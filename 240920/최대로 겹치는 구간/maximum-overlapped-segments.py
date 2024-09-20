n = int(input())

block = []
for i in range(0, 201):
    block.append(0)

for _ in range(n):
    x1, x2 = map(int, input().split())
    for j in range(x1 + 100, x2 + 100 + 1):
        block[j] += 1

max = 0
for i in range(0, n+100+1):
    if block[i] > max and block[i+1] > max:
        max = block[i]
print(max)