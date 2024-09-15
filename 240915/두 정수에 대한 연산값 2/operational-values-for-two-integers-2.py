a, b = map(int, input().split())

def modify(a, b):
    if a > b:
        a *= 2
        b += 10
    else:
        a += 10
        b *= 2
    print(a, b)

modify(a, b)