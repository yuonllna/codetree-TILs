m, d = map(int, input().split())

def is_2021(m, d):
    if m > 12: return False
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if d <= 31:
            return True
        return False
    elif m == 2:
        if d <= 28:
            return True
        return False
    else: 
        if d <= 30: 
            return True
        return False
    
if is_2021(m, d):
    print("Yes")
else: print("No")