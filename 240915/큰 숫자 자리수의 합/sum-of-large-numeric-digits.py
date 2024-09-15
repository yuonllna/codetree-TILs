a, b, c = map(int, input().split())

tmp = a * b * c

def func(n):
    if n // 10 < 1:
        return (n % 10)
    else: 
        return (n % 10) + func(n//10)

print(func(tmp))