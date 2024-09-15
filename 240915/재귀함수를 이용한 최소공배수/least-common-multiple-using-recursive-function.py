n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def func(i):
    if i == 0:
        return arr[i]
    if gcd(arr[i], arr[i-1]) != 1:
        if i == 1:
            return gcd(arr[i], arr[i-1])
        return gcd(arr[i], arr[i-1]) * func(i-2)
    return arr[i] * func(i-1)

print(func(n-1))