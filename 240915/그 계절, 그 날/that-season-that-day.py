y, m, d = map(int, input().split())

def is_leap_year(y):
    if y % 4 == 0 and y % 100 != 0:
        return True
    elif y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
        return True
    return False

def what_season(y, m, d):
    if m > 12: return False
    if is_leap_year(y):
        if m == 2:
            if d <= 29:
                return True
            return False
        elif m == 4 or m == 6 or m == 9 or m == 11:
            if d <= 30:
                return True
            return False
        else: 
            if d <= 31:
                return True
            return False
    else:
        if m == 2:
            if d <= 28:
                return True
            return False
        elif m == 4 or m == 6 or m == 9 or m == 11:
            if d <= 30:
                return True
            return False
        else: 
            if d <= 31:
                return True
            return False

if what_season(y, m, d):
    if m >= 3 and m <= 5: print("Spring")
    elif m >= 6 and m <= 8: print("Summer")
    elif m >= 9 and m <=11: print("Fall")
    else: print("Winter")
else: print(-1)