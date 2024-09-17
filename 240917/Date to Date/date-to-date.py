m1, d1, m2, d2 = tuple(map(int, input().split()))

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = m2 - m1

if month == 0:
    if d1 == d2:
        print(1)
    else: print(d2 - d1)
    
    
else:
    sum = num_of_days[m1-1] - d1 + d2
    for i in range(m1, m2-1):
        sum += num_of_days[i]
    print(sum)