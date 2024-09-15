n, m = map(int, input().split())

arr = list(map(int, input().split()))

def mod(n, m, arr):
    sum = arr[m-1]
    while m != 1:
        if m % 2 != 0:
            m -= 1
        else:
            m //= 2
        sum += arr[m-1]
    return sum


print(mod(n, m, arr))