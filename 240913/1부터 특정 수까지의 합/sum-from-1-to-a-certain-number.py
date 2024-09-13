n = int(input())

def sum_(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s // 10

print(sum_(n))