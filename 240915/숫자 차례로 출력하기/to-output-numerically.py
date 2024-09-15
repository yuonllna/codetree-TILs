n = int(input())
  
def first(n):
    a = n
    if a < 1:
        return
    first(n-1)
    print(a, end=" ")
    a -= 1

def second(n):
    b = n
    if b < 1:
        return
    print(b, end=" ")
    second(n-1)
    b -= 1


first(n)
print("")
second(n)