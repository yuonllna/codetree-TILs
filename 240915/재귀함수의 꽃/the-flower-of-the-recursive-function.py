n = int(input())

def print_num(n):
    a = n
    if a < 1:
        return
    print(a, end=" ")
    print_num(n-1)
    print(a, end=" ")

print_num(n)