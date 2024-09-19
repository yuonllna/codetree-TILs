n = int(input())

str = []
while n // 2 > 0:
    tmp = n % 2
    n //= 2
    str.append(tmp)
str.append(n)

for i in range(len(str)-1, -1, -1):
    print(str[i], end="")