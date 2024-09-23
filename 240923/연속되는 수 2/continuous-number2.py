n = int(input())

a = [0] * n
cnt = [0] * n
idx = 0
for i in range(n):
    a[i] = int(input())
    if i == 0:
        cnt[idx] += 1 
    elif a[i] != a[i-1]:
        idx += 1
        cnt[idx] += 1
    elif a[i] == a[i-1]: 
        cnt[idx] += 1

max = 0
for c in cnt:
    if max < c:
        max = c

print(max)