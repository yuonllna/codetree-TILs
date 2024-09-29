n = int(input())

arr = list(map(int, input().split()))

min_sum = 100000000
for i in range(n):
    loc = i
    sum_diff = 0
    for j in range(n):
        sum_diff += arr[j] * abs(j - loc)
    min_sum = min(min_sum, sum_diff)

print(min_sum)