y = int(input())

def is_four(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return False
        return True
    return False

if is_four(y):
    print("true")
else: print("false")