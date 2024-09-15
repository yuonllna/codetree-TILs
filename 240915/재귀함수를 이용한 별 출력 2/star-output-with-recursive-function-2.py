n = int(input())

def print_star(n):
    if n < 1:
        return 
    print("*"*n, end=" ")
    print("")
    print_star(n-1)
    print("*"*n, end=" ")
    print("")

print_star(n)