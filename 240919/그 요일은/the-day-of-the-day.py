# 변수 선언 및 입력
m1, d1, m2, d2 = tuple(map(int, input().split()))
day = input()
day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def num_of_days(m, d):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    
    for i in range(1, m):
        total_days += days[i]

    total_days += d
    
    return total_days    


diff = num_of_days(m2, d2) - num_of_days(m1, d1) 

cnt = 0
for i in range(0, diff+1):
    if day_of_week[i % 7] == day:
        cnt += 1

print(cnt)