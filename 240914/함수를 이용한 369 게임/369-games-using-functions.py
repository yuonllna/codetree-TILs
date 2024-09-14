a, b = map(int, input().split())

def game(a, b):
    cnt = 0
    for i in range(a, b+1):
        str_n = str(i)
        for j in str_n:
            if j =='3' or j == '6' or j == '9' or int(str_n) % 3 == 0:
                cnt += 1
                break
    return cnt

print(game(a, b))