n = int(input())

def func(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    else:
        return func(n-1)*func(n-2)% 100

print(func(5))