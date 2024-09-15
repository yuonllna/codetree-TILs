n = int(input())

arr = list(map(int, input().split()))

arr.sort()
max = 0
for i in range(2*n):
    if max < arr[i] + arr[2*n - 1 - i]:
        max = arr[i] + arr[2*n - 1 - i]
    
print(max)