n = int(input())

def func(n):
    first = n // 10
    second = n % 10
    if n % 2 == 0 and (first + second) % 5 == 0:
        print("Yes")
    else: print("No")

func(n)