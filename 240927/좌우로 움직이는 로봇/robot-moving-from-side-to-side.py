MAX_T = 1000000

n, m = tuple(map(int, input().split()))
pos_a, pos_b = [0] * (MAX_T + 2), [0] * (MAX_T + 2)

time_a = 1
for _ in range(n):
    t, d = tuple(input().split())
    for _ in range(int(t)):
        pos_a[time_a] = pos_a[time_a - 1] + (1 if d == 'R' else -1)
        time_a += 1

time_b = 1
for _ in range(m):
    t, d = tuple(input().split())
    for _ in range(int(t)):
        pos_b[time_b] = pos_b[time_b - 1] + (1 if d == 'R' else -1)
        time_b += 1

ans = 0

if time_a > time_b:
	for i in range(time_b, time_a + 1):
		pos_b[i] = pos_b[i - 1]
elif time_a < time_b:
	for i in range(time_a, time_b + 1):
		pos_a[i] = pos_a[i - 1]

for i in range(1, max(time_a, time_b)):
    if pos_a[i] == pos_b[i] and pos_a[i-1] < pos_b[i-1]:
        ans += 1
    elif pos_a[i] == pos_b[i] and pos_a[i-1] > pos_b[i-1]:
        ans += 1
        
print(ans)