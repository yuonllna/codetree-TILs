n1, n2 = map(int, input().split())

a = input() 
b = input()

def is_con(a, b):
    if b in a:
        return True
    else: return False

if is_con(a, b):
    print("Yes")
else: print("No")