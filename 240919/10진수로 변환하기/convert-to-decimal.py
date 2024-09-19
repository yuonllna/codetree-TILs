s = input()
arr = list(s)

i = 0
num = 0
for digit in arr[::-1]:
    num += int(digit) * 2**i
    i += 1

print(num)