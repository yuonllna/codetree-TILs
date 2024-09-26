MAX_T = 1000000

n, m = tuple(map(int, input().split()))
pos_a, pos_b = [0] * (MAX_T + 1), [0] * (MAX_T + 1)

time_a = 1
for _ in range(n):
    v, t = tuple(map(int, input().split()))
    for i in range(t):
        pos_a[time_a] = pos_a[time_a - 1] + v
        time_a += 1

time_b = 1
for _ in range(m):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        pos_b[time_b] = pos_b[time_b - 1] + v
        time_b += 1

# winner 설정
winner = 0
if pos_a[1] > pos_b[1]:
    winner = 1
elif pos_a[1] < pos_b[1]:
    winner = 2

# 선두 변경 횟수
sum = 0

for i in range(2, min(time_a, time_b)):  
    if pos_a[i] > pos_b[i] and pos_a[i-1] <= pos_b[i-1]:  
        if winner != 1:
            sum += 1
        winner = 1  
    elif pos_a[i] < pos_b[i] and pos_a[i-1] >= pos_b[i-1]: 
        if winner != 2: 
            sum += 1
        winner = 2 

print(sum)