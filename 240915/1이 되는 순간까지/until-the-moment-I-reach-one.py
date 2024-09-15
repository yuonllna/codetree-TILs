n = int(input())

cnt = 0
def func(n):
    global cnt
    if n == 1:
        return cnt
    if n % 2 == 0:
        cnt += 1
        return func(n//2)
    if n % 2 != 0:
        cnt +=1
        return func(n//3)

print(func(n))