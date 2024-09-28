n, m = tuple(map(int, input().split()))
MAX = 1000000
a = [0] * (MAX+1)
b = [0] * (MAX+1)

time_a, time_b = 0, 0

for i in range(1, n+1):
    d, x = tuple(input().split())
    x = int(x)
    if d == "R":
        for j in range(x):
            a[time_a] = a[time_a-1] + 1
            time_a += 1
    else:
        for j in range(x):
            a[time_a] = a[time_a-1] - 1
            time_a += 1

for i in range(1, m+1):
    d, x = tuple(input().split())
    x = int(x)
    if d == "R":
        for j in range(x):
            b[time_b] = b[time_b-1] + 1
            time_b += 1
    else:
        for j in range(x):
            b[time_b] = b[time_b-1] - 1
            time_b += 1

ans = -1
for i in range(1, min(time_a, time_b)):
    if a[i] == b[i] and a[i] != 0:
        ans = i
        print(ans + 1)
        break

if ans == -1: 
    print(-1)