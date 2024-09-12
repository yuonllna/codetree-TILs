i = 1
n = int(input())
for _ in range(n):
    for _ in range(n):
        print(i,end=" ")
        if i+1 > 9:
            i = 1
        else: i += 1
    print()