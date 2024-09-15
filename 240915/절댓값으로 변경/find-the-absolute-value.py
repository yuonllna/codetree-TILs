n = int(input())
arr = list(map(int, input().split()))

def change_abs(arr):
    for i in range(0, n):
        if arr[i] < 0:
            arr[i] = abs(arr[i])
        print(arr[i], end=" ")

change_abs(arr)