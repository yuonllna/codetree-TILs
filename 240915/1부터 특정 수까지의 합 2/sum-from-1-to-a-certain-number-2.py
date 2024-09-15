n = int(input())

def sum_(n):
    if n == 1:
        return 1
    return n + sum_(n-1)

print(sum_(n))