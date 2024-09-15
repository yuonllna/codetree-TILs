n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    if a == 1 or b == 1:
        return 1
    for i in range(2, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            return i
    return 1

def func(i):
    if i == 1:
        return arr[i] * gcd(arr[i], arr[i-1])
    if gcd(arr[i], arr[i-1]) != 1:
        return gcd(arr[i], arr[i-1]) * func(i-2)
    return arr[i] * func(i-1)

print(func(n-1))