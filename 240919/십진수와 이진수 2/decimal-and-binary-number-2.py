binary = list(map(int, list(input())))

i = 0
num = 0
for digit in binary[::-1]:
    num += int(digit) * 2**i
    i += 1

num = num *17

str = []
while num // 2 > 0:
    tmp = num % 2
    num //= 2
    str.append(tmp)
str.append(num)

for s in str[::-1]:
    print(s, end="")