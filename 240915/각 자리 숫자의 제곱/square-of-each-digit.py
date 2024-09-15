n = int(input())

def func(n):
    if n // 10 < 1:
        return (n % 10)*(n % 10)
    return (n % 10)*(n % 10) + func(n//10)

print(func(n))