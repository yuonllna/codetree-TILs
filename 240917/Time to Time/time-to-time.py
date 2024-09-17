a, b, c, d = tuple(map(int, input().split()))

hour = c - a
minute = d - b

while minute < 0:
    hour -= 1
    minute += 60

print(hour*60+minute)