a, b = map(int, input().split())

def sum_num(n):
    sum = 0
    while n / 10 > 0:
        sum += (n % 10)
        n = n // 10
    if sum % 2 == 0:
        return True
    return False

def is_prime(n):
    if n == 1: return False
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

cnt = 0
for i in range(a, b+1):
    if sum_num(i) and is_prime(i):
        cnt += 1

print(cnt)