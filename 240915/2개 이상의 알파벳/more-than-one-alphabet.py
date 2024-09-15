a = input()
list_ = list(a)

def is_two(list_):
    first = list_[0]
    for i in range(len(list_)):
        if list_[i] != first:
            return True
    return False

if is_two(list_):
    print("Yes")
else: print("No")