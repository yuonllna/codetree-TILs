y = int(input())

def is_four(y):
    if y % 4 == 0:
        return True

def is_hundred(y):
    if y % 100 == 0 and y % 400 != 0:
        return False
    else: return True

if is_four(y) or is_hundred(y):
    print("true")
else: print("false")