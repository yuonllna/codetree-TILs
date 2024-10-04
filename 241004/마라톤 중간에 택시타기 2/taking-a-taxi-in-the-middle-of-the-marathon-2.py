n = int(input())

x = [0]*101
y = [0]*101

for i in range(n):
    x[i], y[i] = tuple(map(int, input().split()))

min_distance = 100000
for i in range(1, n-1):
    distance = 0
    for j in range(1, n):
        if j == i:
            continue
        if j == i+1:
            distance += abs(x[j] - x[j-2]) + abs(y[j] - y[j-2])
        else: 
            distance += abs(x[j] - x[j-1]) + abs(y[j] - y[j-1])
    min_distance = min(min_distance, distance)
    

print(min_distance)