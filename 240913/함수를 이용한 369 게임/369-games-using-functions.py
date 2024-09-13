a, b = map(int, input().split(" "))

def game(a, b):
    cnt = 0
    for i in range(a, b+1):
        n = i // 10
        m = i % 10
        if n == 3 or n == 6 or n == 9 or m == 3 or m == 6 or m == 9 or i % 3 ==0:
            cnt += 1
    return cnt

print(game(a, b))