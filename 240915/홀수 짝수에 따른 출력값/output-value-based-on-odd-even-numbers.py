n = int(input())

def func(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else: return n + func(n-2)

print(func(n))