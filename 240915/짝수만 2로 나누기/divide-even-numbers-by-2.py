n = input()

inp = input()
_list = inp.split(" ")

for i in _list:
    i = int(i)
    if i % 2 == 0:
        print(i // 2, end=" ")
    else: print(i, end=" ")