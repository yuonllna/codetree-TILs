n = int(input())

def print_star(n):
    a = n
    if a < 1:
        return
    print_star(n-1)
    print("*"*a)

print_star(n)