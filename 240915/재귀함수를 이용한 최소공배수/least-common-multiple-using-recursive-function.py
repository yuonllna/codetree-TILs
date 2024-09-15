n = int(input())
arr = list(map(int, input().split()))

# 최대공약수 함수
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 두 수의 최소공배수를 구하는 함수
def lcm(a, b):
    return a * b // gcd(a, b)

# 재귀적으로 최소공배수를 구하는 함수
def func(i):
    if i == 0:
        return arr[i]
    return lcm(arr[i], func(i-1))

print(func(n-1))