a, b = map(int, input().split())

cnt = 0
for i in range(a, b+1):
    if i % 2 == 0 or i % 10 == 5 or (i % 3 == 0 and i % 9 != 0): 
        continue
    else: cnt += 1

print(cnt)