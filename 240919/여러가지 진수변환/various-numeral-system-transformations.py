n, b = map(int, input().split())

str = []
while n // b > 0:
    tmp = n % b
    n //= b
    str.append(tmp)
str.append(n)

for i in str[::-1]:
    print(i, end="")