n = int(input())

def func(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return func(n//2) + 1
    else:
        return func(n*3 + 1) + 1

print(func(n))