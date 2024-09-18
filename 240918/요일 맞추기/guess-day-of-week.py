m1, d1, m2, d2 = tuple(map(int, input().split()))

week_of_days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

tmp = 1
month = m2 - m1
if month == 0:
    if d1 > d2:
        print(week_of_days[tmp - (d1-d2)%7])
    else:
        print(week_of_days[(tmp + (d2-d1))%7])

else:
    if month > 0: 
        sum = num_of_days[m1] - d1 + d2 + 1
        for i in range(m1+1, m2):
            sum += num_of_days[i]
        print(week_of_days[(tmp + sum)%7])
    else: 
        sum = num_of_days[m2] - d1 + d2 + 1
        for i in range(m2+1, m1):
            sum += num_of_days[i]
        print(week_of_days[(tmp - sum)%7])