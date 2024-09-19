a, b = map(int, input().split())
n = list(map(int, input()))

i = 0
num = 0
for digit in n[::-1]:
    num += int(digit) * a**i
    i += 1

num

str = []
while num // b > 0:
    tmp = num % b
    num //= b
    str.append(tmp)
str.append(num)

for s in str[::-1]:
    print(s, end="")