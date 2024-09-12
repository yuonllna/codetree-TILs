i = 1
for _ in range(4):
    for _ in range(4):
        print(i,end=" ")
        if i+1 > 9:
            i = 1
        else: i += 1
    print()