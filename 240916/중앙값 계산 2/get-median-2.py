n = int(input())

arr = list(map(int, input().split()))

for i in range(n):
    if (i+1) % 2 != 0:
        print(arr[i//2], end=" ")