a, b = map(int, input().split())

def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


sum = 0
for i in range(a, b+1):
    if is_prime_num(i):
        sum += i
print(sum)