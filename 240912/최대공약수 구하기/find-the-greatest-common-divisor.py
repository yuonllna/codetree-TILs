inp = input()
arr = inp.split(" ")
n = int(arr[0])
m = int(arr[1])


def max_num(n, m):
    idx = 1
    if n > m: end = m
    else: end = n
    for i in range(1,end):
        if n % i == 0 and m % i == 0:
            idx = i
        elif n % i == 1 and m % i == 1:
            idx = i
    
    print(idx)

max_num(n,m)