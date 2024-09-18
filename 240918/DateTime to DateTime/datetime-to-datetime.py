a, b, c = tuple(map(int, input().split()))

if a < 11 or (a >= 11 and b < 11) or (b >= 11 and c < 11):
    print(-1)
else: 
    day = a - 11
    hour = b - 11
    minute = c - 11

    if hour < 0:
        day -= 1
        hour += 24
    if minute < 0:
        hour -= 1
        minute += 60

    ans = day * 24 * 60 + hour * 60 + minute
    print(ans)